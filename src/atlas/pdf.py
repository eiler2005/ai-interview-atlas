"""Printable PDF books rendered with the Career Copilot document renderer.

The Markdown built here uses only what that renderer supports: headings, paragraphs,
emphasis, lists, tables, http(s) links, page-break markers and one local PNG chart.
Emoji markers are replaced by glyphs the document font has; any other character the
font lacks stops the build instead of printing an empty box. The contents page is
filled from the rendered PDF outline, so its page numbers match the delivered bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
from contextlib import contextmanager
from importlib import metadata
from itertools import pairwise
from pathlib import Path

from .content import STRENGTH, TRACKS, Content, ContentError, load
from .render import LABELS, LANGS, Renderer, percent

FONT_SIZE = 12
PAGEBREAK = "<!-- pagebreak -->"
PLACEHOLDER = "000"
MARKERS = {
    "official": "●",
    "participant_report": "○",
    "prep_guide": "†",
    "secondary_compilation": "†",
}
GENERATED = "‡"
EMOJI = {"✅": "●", "🗣": "○", "🧪": "‡", "❔": "?", "⚠️": "(!)", "⚠": "(!)", "️": ""}
SOURCE_KINDS = (
    "official",
    "participant_report",
    "prep_guide",
    "secondary_compilation",
    "reference",
    "posting",
)
BOOK = {
    "en": {
        "subtitle": (
            "Questions and interview loops for AI leadership and AI engineering · edition {edition}"
        ),
        "how": "How to use this book",
        "how_items": [
            (
                "Pick your track: **{engineering}** or **{leadership}**. Each has a *Start here* "
                "part with its priority questions, what they test, what a strong answer covers "
                "and what to read."
            ),
            (
                "Then work through the themes your interviews will cover. The requirements radar "
                "shows what the job postings in its sample ask for."
            ),
            (
                "Before an interview, read the company pages: loop stages with their basis, the "
                "coding requirement and the questions reported for that company."
            ),
            (
                "Practise aloud. Use the checklists as prompts for your own reasoning and real "
                "examples, not as scripts."
            ),
        ],
        "legend": (
            "Markers: ● confirmed by the company · ○ candidate report · † prep guide or "
            "compilation without a first-hand source · ‡ generated from job-posting themes · "
            "? assumption. Interview loops change often, so check the dates."
        ),
        "contents": "Contents",
        "start_intro": (
            "Priority questions for this track in study order. Each one lists what it tests, "
            "what a strong answer covers and what to read."
        ),
        "tracks_label": {
            "engineering": "AI Engineering",
            "leadership": "AI Leadership",
            "both": "both tracks",
        },
        "see_start": "Answer checklist: *Start here: {track}*, question {number}.",
        "companies": "Companies",
        "companies_intro": (
            "Interview loops by company. Each stage shows its basis; the questions reported "
            "for a company are listed briefly, with full details in the theme parts."
        ),
        "loop": "Interview loop",
        "basis": "Basis",
        "coding": "Coding",
        "prep": "Official preparation material",
        "reported": "Questions reported for {company}",
        "none_reported": "No company-specific questions are recorded yet.",
        "question_count": "{count} questions",
        "methodology": "Methodology",
        "attribution": "Attribution",
        "sources": "Sources",
        "chart_note": "Chart and table show the same shares.",
        "answers_elsewhere": (
            "Written answers to these questions are in the companion book "
            "“AI Interview Atlas — Answers”."
        ),
        "answers_title": "AI Interview Atlas — Answers",
        "answers_subtitle": (
            "Written answers to the priority questions of both tracks · edition {edition}"
        ),
        "answers_how": [
            "Answer the question yourself first, aloud and from memory. Only then read on.",
            (
                "Each answer here is one good answer, not the only correct one. An interviewer "
                "listens to your reasoning and your real examples, so take the structure and replace "
                "the examples with your own."
            ),
            (
                "Questions are numbered as in *Start here* in the main book, where each one also has "
                "its checklist and reading."
            ),
        ],
    },
    "ru": {
        "subtitle": "Вопросы и этапы интервью для AI-лидерства и AI-инженерии · выпуск {edition}",
        "how": "Как пользоваться книгой",
        "how_items": [
            (
                "Выберите трек: **{engineering}** или **{leadership}**. У каждого есть часть "
                "«С чего начать» с приоритетными вопросами: что они проверяют, что покрывает "
                "сильный ответ и что почитать."
            ),
            (
                "Затем пройдите темы, которые ждёте на интервью. Радар требований показывает, "
                "что требуют вакансии из его выборки."
            ),
            (
                "Перед интервью прочитайте страницы компаний: этапы с основаниями, требование "
                "к кодингу и вопросы, о которых сообщали для этой компании."
            ),
            (
                "Отвечайте вслух. Чек-листы — подсказки для собственных рассуждений и реальных "
                "примеров, а не текст для заучивания."
            ),
        ],
        "legend": (
            "Метки: ● подтверждено компанией · ○ отчёт кандидата · † гайд или подборка без "
            "первоисточника · ‡ сгенерировано по темам вакансий · ? предположение. Этапы "
            "интервью часто меняются — смотрите даты."
        ),
        "contents": "Содержание",
        "start_intro": (
            "Приоритетные вопросы трека в порядке изучения. У каждого указано, что он "
            "проверяет, что покрывает сильный ответ и что почитать."
        ),
        "tracks_label": {
            "engineering": "AI-инженерия",
            "leadership": "AI-лидерство",
            "both": "оба трека",
        },
        "see_start": "Чек-лист ответа — в части «С чего начать: {track}», вопрос {number}.",
        "companies": "Компании",
        "companies_intro": (
            "Этапы интервью по компаниям. У каждого этапа указано основание; вопросы, о "
            "которых сообщали для компании, перечислены кратко, подробности — в частях "
            "по темам."
        ),
        "loop": "Этапы интервью",
        "basis": "Основание",
        "coding": "Кодинг",
        "prep": "Официальные материалы для подготовки",
        "reported": "Вопросы, о которых сообщали для {company}",
        "none_reported": "Вопросов по этой компании пока нет.",
        "question_count": "Вопросов: {count}",
        "methodology": "Методика",
        "attribution": "Атрибуция",
        "sources": "Источники",
        "chart_note": "График и таблица показывают одни и те же доли.",
        "answers_elsewhere": (
            "Письменные ответы на эти вопросы собраны в отдельной книге "
            "«AI Interview Atlas — Ответы»."
        ),
        "answers_title": "AI Interview Atlas — Ответы",
        "answers_subtitle": (
            "Письменные ответы на приоритетные вопросы обоих треков · выпуск {edition}"
        ),
        "answers_how": [
            "Сначала ответьте сами, вслух и по памяти. Читайте дальше только после этого.",
            (
                "Каждый ответ здесь — один из хороших, а не единственно верный. Интервьюер слушает "
                "ваши рассуждения и ваши примеры, поэтому берите структуру, а примеры подставляйте "
                "свои."
            ),
            (
                "Нумерация совпадает с разделом «С чего начать» в основной книге, где у каждого "
                "вопроса есть чек-лист и материалы для чтения."
            ),
        ],
    },
}


def pdf_text(text: str) -> str:
    """Content as literal Markdown text, with emoji markers swapped for font glyphs."""
    for emoji, glyph in EMOJI.items():
        text = text.replace(emoji, glyph)
    text = re.sub(r"([\\`*_\[\]<>|])", r"\\\1", text.strip())
    # Only an entity-like ampersand would be decoded; escape just those.
    return re.sub(r"&(?=#|[A-Za-z][A-Za-z0-9]*;)", r"\\&", text)


def link(label: str, url: str) -> str:
    target = f"<{url}>" if re.search(r"[\s()]", url) else url
    return f"[{pdf_text(label)}]({target})"


def _doc(path: Path) -> str:
    """A hand-written doc without its title and language switch; headings kept."""
    lines = path.read_text(encoding="utf-8").splitlines()
    body = [line for line in lines if not line.startswith(("# ", "[English]"))]
    text = "\n".join(body).strip()
    # Relative links cannot work in a PDF; keep only their labels.
    text = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\)", r"\1", text)
    for emoji, glyph in EMOJI.items():
        text = text.replace(emoji, glyph)
    return text


class Book:
    def __init__(self, content: Content, root: Path, lang: str, chart: Path | None = None):
        self.content, self.root, self.lang, self.chart = content, root, lang, chart
        self.renderer = Renderer(content)
        self.labels, self.book = LABELS[lang], BOOK[lang]
        self.numbers: dict[str, tuple[str, int]] = {}
        for track in TRACKS:
            for number, question in enumerate(self.renderer.start_here(track), 1):
                self.numbers.setdefault(question["id"], (track, number))

    # Shared pieces

    def track_name(self, track: str) -> str:
        return pdf_text(self.renderer.track_names[track][self.lang])

    def company_name(self, company: str) -> str:
        return self.content.companies[company]["name"][self.lang]

    def asked_at(self, question: dict) -> str:
        found = self.content.asked_at(question)
        ordered = sorted(
            found.items(), key=lambda item: (STRENGTH[item[1]], self.company_name(item[0]))
        )
        # A no-break space keeps each marker on the line of its company.
        return ", ".join(
            f"{pdf_text(self.company_name(company))} {MARKERS[kind]}" for company, kind in ordered
        )

    def tracks(self, question: dict) -> str:
        names = self.book["tracks_label"]
        if set(question["tracks"]) == set(TRACKS):
            return names["both"]
        return names[question["tracks"][0]]

    def meta(self, question: dict, *, theme: bool = False) -> str:
        labels = self.labels
        parts = [labels["types"][question["type"]]]
        if question.get("level"):
            parts.append(labels["levels"][question["level"]])
        parts.append(self.tracks(question))
        if theme:
            parts.append(pdf_text(self.content.themes[question["theme"]]["name"][self.lang]))
        asked = self.asked_at(question)
        if asked:
            parts.append(f"{labels['asked_at']}: {asked}")
        if question["provenance"] == "generated":
            parts.append(f"{GENERATED} {labels['generated']}")
        return "*" + " · ".join(parts) + "*"

    def reading(self, source_id: str) -> str:
        source = self.content.sources[source_id]
        year = f" ({source['published'][:4]})" if source.get("published") else ""
        return f"{link(source['title'], source['url'])} — {pdf_text(source['publisher'])}{year}"

    def source_line(self, source_id: str) -> str:
        source, labels = self.content.sources[source_id], self.labels
        parts = [link(source["title"], source["url"]), pdf_text(source["publisher"])]
        if source.get("published"):
            parts.append(f"{labels['published']} {source['published']}")
        parts.append(f"{labels['retrieved']} {source['retrieved']}")
        if source.get("license"):
            parts.append(f"{labels['license']} {pdf_text(source['license'])}")
        return ", ".join(parts)

    def question(
        self, question: dict, heading: str, *, full: bool, theme: bool = False
    ) -> list[str]:
        labels, lang = self.labels, self.lang
        lines = [
            f"### {heading} {pdf_text(question['text'][lang])}",
            "",
            self.meta(question, theme=theme),
            "",
            f"**{labels['tests']}:** {pdf_text(question['tests'][lang])}",
            "",
        ]
        if not full:
            track, number = self.numbers[question["id"]]
            reference = self.book["see_start"].format(track=self.track_name(track), number=number)
            return lines + [reference, ""]
        if question.get("outline"):
            lines += [f"**{labels['covers']}:**", ""]
            lines += [f"- {pdf_text(point)}" for point in question["outline"][lang]]
            lines.append("")
        if question.get("reading"):
            lines += [f"**{labels['read']}:**", ""]
            lines += [f"- {self.reading(source)}" for source in question["reading"]]
            lines.append("")
        return lines

    # Parts

    def intro(self) -> list[str]:
        content, book, lang = self.content, self.book, self.lang
        names = {track: self.track_name(track) for track in TRACKS}
        counts = {track: sum(track in q["tracks"] for q in content.questions) for track in TRACKS}
        stats = self.labels["stats"].format(
            questions=len(content.questions),
            companies=len(content.companies),
            sources=len(content.sources),
            updated=self.renderer.updated(),
            **counts,
        )
        lines = [
            "# AI Interview Atlas",
            "",
            f"*{pdf_text(book['subtitle'].format(edition=self.renderer.updated()))}*",
            "",
            f"**{pdf_text(self.labels['hero'])}**",
            "",
            pdf_text(self.labels["intro"]),
            "",
            f"**{pdf_text(stats)}**",
            "",
            f"## {book['how']}",
            "",
        ]
        for index, item in enumerate(book["how_items"], 1):
            lines.append(f"{index}. {item.format(**names)}")
        lines += ["", book["legend"], "", f"## {self.labels['tracks']}", ""]
        for track in content.taxonomy["tracks"]:
            roles = [
                pdf_text(role["name"][lang])
                for role in content.taxonomy["roles"]
                if role["track"] == track["id"]
            ]
            lines.append(
                f"- **{pdf_text(track['name'][lang])}.** {pdf_text(track['summary'][lang])}"
            )
            lines.append(f"  - {', '.join(roles)}")
        return lines

    def contents(self, titles: list[str], pages: list[int] | None) -> list[str]:
        # A list keeps the contents on one page; table rows are taller.
        lines = [f"# {self.book['contents']}", ""]
        for index, title in enumerate(titles):
            lines.append(f"- {title} — {pages[index] if pages else PLACEHOLDER}")
        return lines

    def start_here(self, track: str) -> tuple[str, list[str]]:
        title = self.labels["start"].format(track=self.track_name(track))
        lines = [f"# {title}", "", self.book["start_intro"], ""]
        if self.renderer.answered(self.lang, track):
            lines += [f"*{self.book['answers_elsewhere']}*", ""]
        for number, question in enumerate(self.renderer.start_here(track), 1):
            lines += self.question(question, f"{number}.", full=True, theme=True)
        return title, lines

    def theme(self, theme: dict) -> tuple[str, list[str]]:
        lang, labels = self.lang, self.labels
        title = pdf_text(theme["name"][lang])
        questions = [q for q in self.content.questions if q["theme"] == theme["id"]]
        lines = [
            f"# {title}",
            "",
            pdf_text(theme["summary"][lang]),
            "",
            f"*{self.book['question_count'].format(count=len(questions))}*",
        ]
        groups = [
            (labels["both"], lambda q: set(q["tracks"]) == set(TRACKS)),
            (self.track_name("engineering"), lambda q: q["tracks"] == ["engineering"]),
            (self.track_name("leadership"), lambda q: q["tracks"] == ["leadership"]),
        ]
        number = 0
        for group, belongs in groups:
            chosen = [q for q in questions if belongs(q)]
            if not chosen:
                continue
            lines += ["", f"## {group}", ""]
            for question in chosen:
                number += 1
                full = question["id"] not in self.numbers
                lines += self.question(question, f"{number}.", full=full)
        return title, lines

    def companies(self) -> tuple[str, list[str]]:
        lang, labels, book = self.lang, self.labels, self.book
        lines = [
            f"# {book['companies']}",
            "",
            book["companies_intro"],
            "",
            (
                f"| {labels['company']} | {labels['segment']} | {labels['coding']} "
                f"| {labels['reviewed']} |"
            ),
            "| --- | --- | --- | --- |",
        ]
        ordered = self.renderer.companies_in_order(lang)
        for company in ordered:
            lines.append(
                f"| {pdf_text(company['name'][lang])} | {labels['segments'][company['segment']]} "
                f"| {labels['coding_values'][company['coding']['value']]} "
                f"| {pdf_text(self.renderer.reviewed(company, lang))} |"
            )
        for index, company in enumerate(ordered):
            lines += ["", "---", ""] if index else [""]
            lines += self.company(company)
        return book["companies"], lines

    def company(self, company: dict) -> list[str]:
        lang, labels, book, content = self.lang, self.labels, self.book, self.content
        name = pdf_text(company["name"][lang])
        markets = ", ".join(labels["market_names"][m] for m in company["markets"])
        reviewed = labels["last_reviewed"].format(date=self.renderer.reviewed(company, lang))
        lines = [
            f"## {name}",
            "",
            f"*{labels['segments'][company['segment']]} · {markets} · {pdf_text(reviewed)}*",
            "",
        ]
        if company.get("summary"):
            lines += [pdf_text(company["summary"][lang]), ""]
        for track in TRACKS:
            roles = [
                pdf_text(content.roles[role]["name"][lang])
                for role in company["roles"].get(track, [])
            ]
            if roles:
                lines.append(f"- **{self.track_name(track)}:** {', '.join(roles)}")
        lines += ["", f"### {book['loop']}", ""]
        for stage in company["loop"]:
            detail = f" {pdf_text(stage['detail'][lang])}" if stage.get("detail") else ""
            title = pdf_text(stage["stage"][lang])
            if stage.get("roles"):
                title += (
                    " ("
                    + ", ".join(pdf_text(content.roles[r]["name"][lang]) for r in stage["roles"])
                    + ")"
                )
            lines += [f"**{title}.**{detail}", ""]
            lines += [f"*{book['basis']}: {pdf_text(labels['claims'][stage['claim']])}*", ""]
            if stage.get("sources"):
                lines += [f"- {self.source_line(source)}" for source in stage["sources"]]
                lines.append("")
        coding = company["coding"]
        coding_line = f"**{book['coding']}:** {labels['coding_values'][coding['value']]}"
        if coding.get("note"):
            coding_line += f". {pdf_text(coding['note'][lang])}"
        lines += [coding_line, ""]
        if coding.get("sources"):
            lines += [f"- {self.source_line(source)}" for source in coding["sources"]] + [""]
        if company.get("prep"):
            lines += [f"### {book['prep']}", ""]
            lines += [f"- {self.source_line(source)}" for source in company["prep"]] + [""]
        reported = [q for q in content.questions if company["id"] in content.asked_at(q)]
        lines += [f"### {book['reported'].format(company=name)}", ""]
        if not reported:
            return lines + [book["none_reported"], ""]
        for theme in content.taxonomy["themes"]:
            for question in (q for q in reported if q["theme"] == theme["id"]):
                kind = content.asked_at(question)[company["id"]]
                lines.append(
                    f"- {pdf_text(question['text'][lang])} "
                    f"*({pdf_text(theme['name'][lang])} {MARKERS[kind]})*"
                )
        return lines + [""]

    def radar(self) -> tuple[str, list[str]]:
        radar, labels, lang = self.content.radar, self.labels, self.lang
        sample = radar["sample"]
        title = labels["radar_title"]
        lines = [
            f"# {title}",
            "",
            f"- **{labels['period']}:** {radar['period']['from']} — {radar['period']['to']}",
            f"- **{labels['sample']}:** "
            + labels["sample_value"].format(
                postings=sample["postings"],
                engineering=sample["tracks"].get("engineering", 0),
                leadership=sample["tracks"].get("leadership", 0),
            )
            + "; "
            + labels["market_value"].format(
                intl=sample["markets"].get("intl", 0),
                ru=sample["markets"].get("ru", 0),
                unknown=sample["markets"].get("unknown", 0),
            ),
            "",
        ]
        if self.chart:
            lines += [f"![{self.book['chart_note']}]({self.chart.name})", ""]
        lines += [
            (
                f"| {labels['theme']} | {self.track_name('engineering')} "
                f"| {self.track_name('leadership')} |"
            ),
            "| --- | --- | --- |",
        ]
        for theme, cells in self.renderer.radar_cells():
            values = []
            for track in TRACKS:
                row, total = cells[track], sample["tracks"].get(track, 0)
                share = percent(row["postings"], total) if row else None
                values.append(
                    labels["share"].format(share=share, postings=row["postings"]) if row else "—"
                )
            lines.append(f"| {pdf_text(theme['name'][lang])} | {values[0]} | {values[1]} |")
        lines += [""] + [pdf_text(line) for line in self.renderer.ai_share(lang)]
        lines += [
            "",
            labels["suppressed"].format(min_cell=radar["min_cell"], min_track=radar["min_track"]),
            "",
            f"## {labels['method']}",
            "",
            pdf_text(radar["method"][lang]),
        ]
        if radar.get("criteria"):
            lines += ["", f"### {labels['criteria']}", ""]
            for theme in self.content.taxonomy["themes"]:
                criterion = radar["criteria"].get(theme["id"])
                if criterion:
                    name = pdf_text(theme["name"][lang])
                    lines.append(f"- **{name}:** {pdf_text(criterion[lang])}")
        return title, lines

    def document(self, name: str, key: str) -> tuple[str, list[str]] | None:
        path = self.root / "docs" / ("" if self.lang == "en" else "ru") / name
        if not path.is_file():
            return None
        title = self.book[key]
        return title, [f"# {title}", "", _doc(path)]

    def sources(self) -> tuple[str, list[str]]:
        labels = self.labels
        title = self.book["sources"]
        lines = [f"# {title}", ""]
        by_kind: dict[str, list[dict]] = {}
        for source in self.content.sources.values():
            by_kind.setdefault(source["kind"], []).append(source)
        for kind in SOURCE_KINDS:
            chosen = sorted(
                by_kind.get(kind, []),
                key=lambda s: (s["publisher"].casefold(), s["title"].casefold()),
            )
            if chosen:
                lines += [f"## {labels['kinds'][kind]}", ""]
                lines += [f"- {self.source_line(source['id'])}" for source in chosen] + [""]
        return title, lines

    def parts(self) -> list[tuple[str, list[str]]]:
        parts = [self.start_here(track) for track in TRACKS if self.renderer.start_here(track)]
        parts += [self.theme(theme) for theme in self.content.taxonomy["themes"]]
        if self.content.companies:
            parts.append(self.companies())
        if self.content.radar:
            parts.append(self.radar())
        for name, key in (("METHODOLOGY.md", "methodology"), ("ATTRIBUTION.md", "attribution")):
            part = self.document(name, key)
            if part:
                parts.append(part)
        parts.append(self.sources())
        return parts

    @property
    def has_contents(self) -> bool:
        """A contents page earns its own page only once there are several parts."""
        return len(self.parts()) >= 3

    def markdown(self, pages: list[int] | None = None) -> str:
        """The whole book; `pages` fills the contents, or placeholders on the first pass."""
        parts = self.parts()
        blocks = [self.intro()]
        if self.has_contents:
            blocks.append(self.contents([title for title, _ in parts], pages))
        blocks += [lines for _, lines in parts]
        return f"\n\n{PAGEBREAK}\n\n".join("\n".join(b).strip() for b in blocks) + "\n"


class AnswersBook(Book):
    """The same content, printed as answers only: one part per track."""

    def intro(self) -> list[str]:
        book = self.book
        lines = [
            f"# {book['answers_title']}",
            "",
            f"*{pdf_text(book['answers_subtitle'].format(edition=self.renderer.updated()))}*",
            "",
        ]
        for index, item in enumerate(book["answers_how"], 1):
            lines.append(f"{index}. {item}")
        return lines

    def track_answers(self, track: str) -> tuple[str, list[str]]:
        labels, lang = self.labels, self.lang
        title = labels["answers"].format(track=self.track_name(track))
        priority = self.renderer.start_here(track)
        numbers = {q["id"]: number for number, q in enumerate(priority, 1)}
        answered = self.renderer.answered(lang, track)
        lines = [
            f"# {title}",
            "",
            pdf_text(labels["answers_intro"]),
            "",
            f"*{labels['answers_progress'].format(done=len(answered), total=len(priority))}*",
        ]
        for question in answered:
            theme = self.content.themes[question["theme"]]
            lines += [
                "",
                f"### {numbers[question['id']]}. {pdf_text(question['text'][lang])}",
                "",
                f"*{labels['types'][question['type']]} · {pdf_text(theme['name'][lang])}*",
                "",
                pdf_text(question["answer"][lang]),
            ]
            if question.get("reading"):
                lines += [
                    "",
                    f"**{labels['read']}:** "
                    + " · ".join(self.reading(source) for source in question["reading"]),
                ]
        return title, lines

    def parts(self) -> list[tuple[str, list[str]]]:
        return [
            self.track_answers(track)
            for track in TRACKS
            if self.renderer.answered(self.lang, track)
        ]


def missing_glyphs(markdown: str, font_path: Path) -> list[str]:
    from reportlab.pdfbase.ttfonts import TTFont

    cmap = TTFont("AtlasProbe", str(font_path)).face.charToGlyph
    return sorted({char for char in markdown if not char.isspace() and ord(char) not in cmap})


def font_files(font: str | None) -> tuple[Path, Path]:
    """Regular and bold faces exactly as the Career Copilot renderer resolves them."""
    from job_search_agent.pdf_documents import FONT_CANDIDATES

    for value, bold_name in [(font, None)] if font else FONT_CANDIDATES:
        if value and Path(value).is_file():
            path = Path(value)
            bold = path.with_name(bold_name) if bold_name else path
            return path, bold if bold.is_file() else path
    raise SystemExit("A Unicode TTF font is required; pass --font PATH")


def chart_png(root: Path, lang: str, target: Path) -> Path | None:
    """Rasterise the generated radar SVG at twice its size, or leave the chart out."""
    svg = root / "docs" / "assets" / f"radar.{lang}.svg"
    tool = shutil.which("rsvg-convert")
    if not svg.is_file() or not tool:
        return None
    target.parent.mkdir(parents=True, exist_ok=True)
    command = [tool, "--zoom", "2", "--format", "png", "--output", str(target), str(svg)]
    subprocess.run(command, check=True)
    return target


def part_pages(data: bytes) -> list[int]:
    """1-based pages of the top-level outline entries: one per H1 heading."""
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    return [
        reader.get_destination_page_number(item) + 1
        for item in reader.outline
        if not isinstance(item, list)
    ]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def renderer_version() -> dict:
    """Name, version and pinned commit of the installed Career Copilot renderer."""
    dist = metadata.distribution("job-search-agent")
    origin = dist.read_text("direct_url.json")
    commit = json.loads(origin).get("vcs_info", {}).get("commit_id") if origin else None
    return {"package": "job-search-agent", "version": dist.version, "commit": commit}


@contextmanager
def introductions_kept_with_content():
    """Keep a paragraph that introduces what follows on the same page as it.

    The pinned renderer keeps only headings with the next block. For one render, wrap
    its Markdown converter so body paragraphs that open with bold or italic text (the
    marker line, "Tests:", list labels, company stages) do the same, but never across
    a heading: a chain that ran into the next question could outgrow a page. Styles,
    page furniture and bookmarks stay the renderer's own.
    """
    from job_search_agent import pdf_documents

    original = pdf_documents.markdown_flowables

    def style(flowable) -> str:
        return getattr(getattr(flowable, "style", None), "name", "")

    def flowables(*args, **kwargs):
        story = original(*args, **kwargs)
        for flowable, following in pairwise(story):
            opens = getattr(flowable, "text", "").startswith(("<b>", "<i>"))
            before_heading = style(following).startswith("DocumentHeading")
            if style(flowable) == "DocumentBody" and opens and not before_heading:
                flowable.keepWithNext = 1
        return story

    pdf_documents.markdown_flowables = flowables
    try:
        yield
    finally:
        pdf_documents.markdown_flowables = original


def render_book(book: Book, font: str | None) -> tuple[bytes, str, dict[str, str], list[int]]:
    """Render until the contents page numbers match the outline of the rendered bytes."""
    from job_search_agent.pdf_documents import render_markdown

    chart = book.chart
    pages: list[int] | None = None
    for _ in range(4):
        markdown = book.markdown(pages)
        resources: dict[str, str] = {}
        with introductions_kept_with_content():
            data = render_markdown(
                markdown,
                font_path=font,
                font_size=FONT_SIZE,
                source_dir=chart.parent if chart else None,
                resource_root=chart.parent if chart else None,
                resources=resources,
            )
        found = part_pages(data)
        # The intro, and the contents when present, come before the parts.
        before = 2 if book.has_contents else 1
        if len(found) != len(book.parts()) + before:
            raise SystemExit("Every book part needs exactly one top-level heading")
        if found[before:] == pages:
            return data, markdown, resources, pages
        pages = found[before:]
    raise SystemExit("Contents page numbers did not settle")


def write_book(book: Book, name: str, out: Path, root: Path, font: str | None) -> dict:
    """Render one book, write it with its Markdown source, and return its manifest."""
    from job_search_agent.pdf_documents import inspect_pdf

    font_path, bold_path = font_files(font)
    data, markdown, resources, pages = render_book(book, font)
    (out / name).write_bytes(data)
    (out / f"{name}.md").write_text(markdown, encoding="utf-8")
    inputs = {
        path.relative_to(root).as_posix(): sha(path.read_bytes())
        for path in sorted((root / "src" / "content").rglob("*.yaml"))
    }
    for doc in ("METHODOLOGY.md", "ATTRIBUTION.md"):
        path = root / "docs" / ("" if book.lang == "en" else "ru") / doc
        if path.is_file():
            inputs[path.relative_to(root).as_posix()] = sha(path.read_bytes())
    manifest = {
        "output": name,
        "language": book.lang,
        "edition": book.renderer.updated(),
        "font_size": FONT_SIZE,
        "fonts": {
            "regular": {"path": str(font_path), "sha256": sha(font_path.read_bytes())},
            "bold": {"path": str(bold_path), "sha256": sha(bold_path.read_bytes())},
        },
        "renderer": renderer_version(),
        "markdown_sha256": sha(markdown.encode("utf-8")),
        "resources": resources,
        "contents": [
            {"part": re.sub(r"\\(.)", r"\1", title), "page": page}
            for (title, _), page in zip(book.parts(), pages, strict=True)
        ],
        "inputs": inputs,
        **inspect_pdf(data),
    }
    (out / f"{name}.manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def build(root: Path, out: Path, langs: list[str], font: str | None = None) -> list[dict]:
    """The questions book for each language, plus an answers book where answers exist."""
    try:
        import job_search_agent.pdf_documents  # noqa: F401
    except ImportError as error:  # pragma: no cover - depends on the optional group
        raise SystemExit("Install the PDF renderer first: uv sync --group pdf") from error
    content = load(root / "src" / "content")
    font_path, bold_path = font_files(font)
    out.mkdir(parents=True, exist_ok=True)
    renderer = Renderer(content)
    edition = renderer.updated()
    results = []
    for lang in langs:
        png = out / "assets" / f"radar.{lang}.png"
        chart = chart_png(root, lang, png) if content.radar else None
        editions = [(Book(content, root, lang, chart), f"ai-interview-atlas-{edition}-{lang}.pdf")]
        if any(renderer.answered(lang, track) for track in TRACKS):
            editions.append(
                (
                    AnswersBook(content, root, lang),
                    f"ai-interview-atlas-answers-{edition}-{lang}.pdf",
                )
            )
        for book, name in editions:
            markdown = book.markdown()
            missing = set(missing_glyphs(markdown, font_path))
            missing |= set(missing_glyphs(markdown, bold_path))
            if missing:
                raise SystemExit(f"The PDF font lacks glyphs for: {' '.join(sorted(missing))}")
            results.append(write_book(book, name, out, root, font))
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the printable PDF books (12 pt text).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--out", type=Path, default=None, help="default: ROOT/dist/pdf")
    parser.add_argument("--lang", nargs="+", choices=LANGS, default=list(LANGS))
    parser.add_argument("--font", help="Unicode TTF font; defaults to the renderer's choice")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    out = (args.out or root / "dist" / "pdf").resolve()
    try:
        results = build(root, out, args.lang, args.font)
    except ContentError as error:
        print(f"Content errors ({len(error.problems)}):", file=sys.stderr)
        for problem in error.problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    for result in results:
        print(f"{out / result['output']}: {result['pages']} pages, sha256 {result['sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
