"""SVG figures built from the same validated content as the Markdown pages.

Two constraints shape how these are drawn.

The privacy checker that guards this repository accepts only a small list of SVG elements,
and `<style>` is not among them: a stylesheet can carry `@import` and `url()`, so the rule
refuses it outright rather than trying to tell a safe one from an unsafe one. Every colour
therefore sits on the element as a presentation attribute, and there is no CSS anywhere.

Dark mode is handled a level up instead. Each figure is rendered twice -- once for a light
surface, once for a dark one -- and the Markdown wraps the pair in a `<picture>` element
whose `prefers-color-scheme` source picks between them. The dark figure is a separate set of
steps chosen for a dark surface, not an inverted light one. A renderer that ignores
`<picture>`, such as the `rsvg-convert` pass that puts the chart into the PDF books, falls
back to the light file and gets a correct figure.

The palette is the validated default data-visualisation palette: categorical slots 1 and 2
(blue, orange) for the two tracks, and one blue ramp wherever the value is a magnitude or an
ordered strength. Colour never carries meaning alone -- every bar, cell and segment is
directly labelled, and every status is drawn as a shape.
"""

from __future__ import annotations

from xml.sax.saxutils import escape

from .content import STRENGTH, TRACKS, Content

FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

# role -> (light surface value, dark surface value). Both columns are selected for their own
# surface; the dark column is not a flip of the light one.
PALETTE: dict[str, tuple[str, str]] = {
    "surface": ("#fcfcfb", "#1a1a19"),
    "ink": ("#0b0b0b", "#ffffff"),
    "ink2": ("#52514e", "#c3c2b7"),
    "muted": ("#898781", "#898781"),
    "grid": ("#e1e0d9", "#2c2c2a"),
    "axis": ("#c3c2b7", "#383835"),
    "ring": ("rgba(11,11,11,0.10)", "rgba(255,255,255,0.10)"),
    "engineering": ("#2a78d6", "#3987e5"),
    "leadership": ("#eb6834", "#d95926"),
    "good": ("#0ca30c", "#0ca30c"),
    "warning": ("#fab219", "#fab219"),
    "critical": ("#d03b3b", "#d03b3b"),
    # Ink for a label sitting on a saturated mark, where the usual ink would disappear.
    "oncell": ("#ffffff", "#0b0b0b"),
}
# One blue hue for magnitude. On a light surface a darker step means "more"; on a dark
# surface a lighter step does, so the dark column runs the other way.
RAMP = (
    ("#cde2fb", "#184f95"),
    ("#9ec5f4", "#1c5cab"),
    ("#5598e7", "#256abf"),
    ("#2a78d6", "#3987e5"),
    ("#1c5cab", "#6da7ec"),
    ("#104281", "#b7d3f6"),
)
# Ordered evidence strength, strongest first; validated as an ordinal ramp in both modes.
EVIDENCE = (("#1c5cab", "#b7d3f6"), ("#2a78d6", "#6da7ec"), ("#5598e7", "#2a78d6"))
# From this ramp step on, a cell is saturated enough that its label needs the contrast ink.
INVERT_FROM = 3

PALETTE |= {f"ramp-{index}": pair for index, pair in enumerate(RAMP)}
PALETTE |= {f"evidence-{index}": pair for index, pair in enumerate(EVIDENCE)}

LABELS = {
    "en": {
        "postings_title": "Share of postings that mention each theme",
        "postings_desc": (
            "Grouped bars: for each theme, the share of job postings in the sample that "
            "mention it, by track."
        ),
        "suppressed": "— = suppressed, not zero (track n < {min_track} or theme n < {min_cell})",
        "coverage_title": "Questions and written answers by theme",
        "coverage_desc": (
            "A table of counts: for each theme, the questions on the engineering track, on "
            "the leadership track, and the number with a written answer."
        ),
        "coverage_cols": ("AI Engineering", "AI Leadership", "Answers"),
        "coverage_note": "A question can belong to both tracks, so the columns overlap.",
        "evidence_title": "What backs the atlas",
        "evidence_desc": (
            "Two stacked bars: the question bank by its strongest evidence, and company "
            "interview-loop stages by the strength of their claim."
        ),
        "evidence_rows": ("{total} questions", "{total} company loop stages"),
        "evidence_kinds": {
            "official": "Company-confirmed",
            "participant_report": "First-hand report",
            "secondary": "Prep guide or compilation",
            "generated": "Generated practice",
            "assumption": "Assumption",
        },
        "evidence_note": (
            "First-hand evidence concentrates in loop stages; most questions are "
            "paraphrased from secondary compilations."
        ),
        "roadmap_title": "Project roadmap",
        "roadmap_desc": (
            "Stages of work, each listing its items with a status: done, in progress, "
            "planned, or ruled out."
        ),
        "roadmap_status": {
            "done": "Done",
            "progress": "In progress",
            "planned": "Planned",
            "declined": "Ruled out",
        },
        "roadmap_note": "An item moves when the evidence for it exists, not on a date.",
        "banner_tagline": "Interview questions, answers and learning paths — every claim dated",
        "banner_stats": (
            ("questions", "questions"),
            ("answers", "written answers"),
            ("companies", "company loops"),
            ("sources", "dated sources"),
        ),
        "banner_footer": "Apache-2.0 · English and Russian · nothing behind a paywall",
    },
    "ru": {
        "postings_title": "Доля вакансий, где упоминается тема",
        "postings_desc": (
            "Сгруппированные полосы: для каждой темы — доля вакансий выборки, где она "
            "упоминается, по трекам."
        ),
        "suppressed": "— = скрыто, не ноль (трек n < {min_track} или тема n < {min_cell})",
        "coverage_title": "Вопросы и написанные ответы по темам",
        "coverage_desc": (
            "Таблица значений: для каждой темы — вопросы инженерного трека, трека "
            "лидерства и число вопросов с написанным ответом."
        ),
        "coverage_cols": ("AI-инженерия", "AI-лидерство", "Ответы"),
        "coverage_note": "Вопрос может относиться к двум трекам, поэтому столбцы пересекаются.",
        "evidence_title": "На чём держится атлас",
        "evidence_desc": (
            "Две составные полосы: банк вопросов по сильнейшему свидетельству и этапы "
            "интервью компаний по силе утверждения."
        ),
        "evidence_rows": ("{total} вопросов", "{total} этапов интервью"),
        "evidence_kinds": {
            "official": "Подтверждено компанией",
            "participant_report": "Рассказ участника",
            "secondary": "Подборка или гайд",
            "generated": "Учебная практика",
            "assumption": "Предположение",
        },
        "evidence_note": (
            "Свидетельства из первых рук сосредоточены в этапах интервью; большинство "
            "вопросов пересказано из вторичных подборок."
        ),
        "roadmap_title": "План развития проекта",
        "roadmap_desc": (
            "Этапы работы: у каждого пункта статус — сделано, в работе, запланировано "
            "или отклонено."
        ),
        "roadmap_status": {
            "done": "Сделано",
            "progress": "В работе",
            "planned": "Запланировано",
            "declined": "Отклонено",
        },
        "roadmap_note": "Пункт двигается, когда появляется основание, а не по дате.",
        "banner_tagline": "Вопросы, ответы и маршруты подготовки — каждое утверждение с датой",
        "banner_stats": (
            ("questions", "вопросов"),
            ("answers", "написанных ответов"),
            ("companies", "процессов интервью"),
            ("sources", "источников с датами"),
        ),
        "banner_footer": "Apache-2.0 · английский и русский · ничего за платной стеной",
    },
}


MODES = ("light", "dark")
# Index into every PALETTE pair.
TONE = {"light": 0, "dark": 1}


def num(value: float) -> str:
    """A short, stable number: integers without a trailing decimal point."""
    rounded = round(value, 2)
    return str(int(rounded)) if rounded == int(rounded) else str(rounded)


def tone(role: str, mode: str) -> str:
    """The value of one palette role on one surface."""
    return PALETTE[role][TONE[mode]]


def entry_width(name: str) -> float:
    """Room one legend entry needs: swatch, gap, text at 11px, and a separation."""
    return 17 + 6.3 * len(name) + 22


def wrap_text(body: str, limit: int) -> list[str]:
    """Greedy wrap on spaces: SVG has no text flow, so the lines are decided here."""
    lines, current = [], ""
    for word in body.split():
        candidate = f"{current} {word}".strip()
        if len(candidate) > limit and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def ramp_step(share: float, steps: int = len(RAMP)) -> int:
    """Which ramp step a magnitude between 0 and 1 falls in."""
    if share <= 0:
        return 0
    return min(steps - 1, int(share * steps))


class Paint:
    """Draws the primitives for one surface: every colour resolved to a literal value."""

    def __init__(self, mode: str):
        self.mode = mode

    def fill(self, role: str) -> str:
        return f'fill="{tone(role, self.mode)}"'

    def stroke(self, role: str) -> str:
        return f'stroke="{tone(role, self.mode)}"'

    def both(self, fill_role: str, stroke_role: str) -> str:
        return f'fill="{tone(fill_role, self.mode)}" stroke="{tone(stroke_role, self.mode)}"'

    def label(
        self,
        x: float,
        y: float,
        body: str,
        *,
        role: str = "ink",
        size: int = 13,
        weight: int | None = None,
        anchor: str | None = None,
    ) -> str:
        bold = f' font-weight="{weight}"' if weight else ""
        place = f' text-anchor="{anchor}"' if anchor else ""
        return (
            f'<text x="{num(x)}" y="{num(y)}" font-size="{size}" {self.fill(role)}{bold}{place}>'
            f"{escape(body)}</text>"
        )

    def bar(
        self, x: float, y: float, width: float, height: float, role: str, radius: float = 4
    ) -> str:
        """A horizontal bar anchored to the baseline at `x`, rounded only at the value end."""
        if width <= 0:
            return ""
        radius = min(radius, width, height / 2)
        return (
            f'<path {self.fill(role)} d="M{num(x)} {num(y)}h{num(width - radius)}'
            f"a{num(radius)} {num(radius)} 0 0 1 {num(radius)} {num(radius)}"
            f"v{num(height - 2 * radius)}"
            f"a{num(radius)} {num(radius)} 0 0 1 {num(-radius)} {num(radius)}"
            f'H{num(x)}z"/>'
        )

    def swatch(self, x: float, y: float, role: str, size: int = 11) -> str:
        return f'<rect x="{num(x)}" y="{num(y)}" width="{size}" height="{size}" rx="2" {self.fill(role)}/>'

    def legend(self, x: float, y: float, items: list[tuple[str, str]]) -> list[str]:
        """A swatch and a name per series, left to right."""
        parts: list[str] = []
        for name, role in items:
            parts.append(self.swatch(x, y, role))
            parts.append(self.label(x + 17, y + 10, name, role="ink2", size=11))
            x += entry_width(name)
        return parts

    def flowing_legend(
        self, x: float, y: float, limit: float, items: list[tuple[str, str]], line_height: int = 17
    ) -> tuple[list[str], int]:
        """A legend that wraps inside `limit`; returns the marks and the number of lines used."""
        parts: list[str] = []
        left, lines = x, 1
        for name, role in items:
            width = entry_width(name)
            if left > x and left + width - 22 > x + limit:
                left, lines = x, lines + 1
                y += line_height
            parts.append(self.swatch(left, y, role, 9))
            parts.append(self.label(left + 15, y + 9, name, role="ink2", size=11))
            left += width
        return parts, lines

    def frame(self, width: int, height: int, title: str, desc: str, body: list[str]) -> str:
        """One finished figure: a labelled card drawn for this surface."""
        return "\n".join(
            [
                (
                    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
                    f'viewBox="0 0 {width} {height}" role="img" '
                    f'aria-labelledby="figure-title figure-desc" font-family="{FONT}">'
                ),
                f'<title id="figure-title">{escape(title)}</title>',
                f'<desc id="figure-desc">{escape(desc)}</desc>',
                (
                    f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" '
                    f"{self.both('surface', 'ring')}/>"
                ),
                *[line for line in body if line],
                "</svg>",
            ]
        )

    def status_mark(self, x: float, y: float, status: str) -> list[str]:
        """A status drawn as a shape, so the status never rests on colour alone."""
        if status == "done":
            return [
                f'<circle cx="{num(x)}" cy="{num(y - 4)}" r="5.5" {self.fill("good")}/>',
                (
                    f'<path d="M{num(x - 2.6)} {num(y - 4.2)}l1.8 1.9 3.2-3.5" fill="none" '
                    f'{self.stroke("surface")} stroke-width="1.6" stroke-linecap="round" '
                    'stroke-linejoin="round"/>'
                ),
            ]
        if status == "progress":
            return [
                (
                    f'<circle cx="{num(x)}" cy="{num(y - 4)}" r="4.6" fill="none" '
                    f'{self.stroke("warning")} stroke-width="2.2"/>'
                ),
                (
                    f'<path d="M{num(x)} {num(y - 8.6)}A4.6 4.6 0 0 1 {num(x)} {num(y + 0.6)}z" '
                    f"{self.fill('warning')}/>"
                ),
            ]
        if status == "declined":
            return [
                (
                    f'<path d="M{num(x - 3.6)} {num(y - 7.6)}l7.2 7.2m0-7.2l-7.2 7.2" fill="none" '
                    f'{self.stroke("critical")} stroke-width="2" stroke-linecap="round"/>'
                )
            ]
        return [
            (
                f'<circle cx="{num(x)}" cy="{num(y - 4)}" r="4.4" fill="none" '
                f'{self.stroke("muted")} stroke-width="1.6"/>'
            )
        ]


class Figures:
    """Every generated figure for one content set, in both languages."""

    def __init__(self, content: Content):
        self.content = content

    # The numbers behind the figures

    def answered(self) -> int:
        return sum(1 for question in self.content.questions if question.get("answer"))

    def question_evidence(self) -> dict[str, int]:
        """Each question counted once, under its strongest evidence."""
        counts = dict.fromkeys(("official", "participant_report", "secondary", "generated"), 0)
        for question in self.content.questions:
            if question["provenance"] == "generated":
                counts["generated"] += 1
                continue
            kinds = [self.content.sources[item["source"]]["kind"] for item in question["evidence"]]
            best = min(kinds, key=lambda kind: STRENGTH[kind])
            # A prep guide and a compilation make the same claim to a reader: † with no
            # first-hand source behind it.
            counts[best if best in counts else "secondary"] += 1
        return counts

    def stage_claims(self) -> dict[str, int]:
        """Company interview-loop stages by how strongly each one is claimed."""
        counts = dict.fromkeys(("official", "participant_report", "secondary", "assumption"), 0)
        for company in self.content.companies.values():
            for stage in company["loop"]:
                claim = stage["claim"]
                counts["official" if claim == "confirmed" else claim] += 1
        return counts

    def theme_counts(self) -> list[tuple[dict, dict[str, int]]]:
        rows = []
        for theme in self.content.taxonomy["themes"]:
            questions = [q for q in self.content.questions if q["theme"] == theme["id"]]
            counts = {track: sum(1 for q in questions if track in q["tracks"]) for track in TRACKS}
            counts["answers"] = sum(1 for q in questions if q.get("answer"))
            rows.append((theme, counts))
        return rows

    def published_cells(self) -> list[tuple[dict, dict[str, dict | None]]]:
        """Themes with at least one publishable radar cell, in taxonomy order."""
        radar = self.content.radar
        rows = {(row["track"], row["theme"]): row for row in radar["rows"]}
        cells = []
        for theme in self.content.taxonomy["themes"]:
            row: dict[str, dict | None] = {}
            for track in TRACKS:
                cell = rows.get((track, theme["id"]))
                publishable = (
                    cell
                    and cell["postings"] >= radar["min_cell"]
                    and radar["sample"]["tracks"].get(track, 0) >= radar["min_track"]
                )
                row[track] = cell if publishable else None
            if any(row.values()):
                cells.append((theme, row))
        return cells

    # The figures

    def postings(self, lang: str, mode: str) -> str:
        """Demand: the share of postings in the sample that mention each theme."""
        paint = Paint(mode)
        labels, radar = LABELS[lang], self.content.radar
        sample, cells = radar["sample"], self.published_cells()
        names = {t["id"]: t["name"][lang] for t in self.content.taxonomy["tracks"]}
        pad, label_width, plot = 20, 300, 330
        top, row_height, thickness = 100, 36, 12
        width = pad + label_width + plot + 60
        height = top + row_height * len(cells) + 60
        axis_x = pad + label_width
        bottom = top + row_height * len(cells) - 10
        body = [
            paint.label(pad, 32, labels["postings_title"], size=16, weight=600),
            *paint.legend(pad, 50, [(names[track], track) for track in TRACKS]),
        ]
        for share in (0, 25, 50, 75, 100):
            x = axis_x + plot * share / 100
            body.append(
                f'<line x1="{num(x)}" y1="{top - 14}" x2="{num(x)}" y2="{num(bottom)}" '
                f'{paint.stroke("grid")} stroke-width="1"/>'
            )
            body.append(
                paint.label(x, top - 20, f"{share}%", role="muted", size=11, anchor="middle")
            )
        for index, (theme, row) in enumerate(cells):
            y = top + index * row_height
            body.append(paint.label(axis_x - 12, y + 16, theme["name"][lang], anchor="end"))
            for offset, track in enumerate(TRACKS):
                cell = row[track]
                bar_y = y + 1 + offset * (thickness + 2)
                if not cell:
                    body.append(
                        paint.label(axis_x + 4, bar_y + thickness - 2, "—", role="muted", size=11)
                    )
                    continue
                share = round(100 * cell["postings"] / sample["tracks"][track])
                length = max(3.0, plot * share / 100)
                body.append(paint.bar(axis_x, bar_y, length, thickness, track))
                body.append(
                    paint.label(
                        axis_x + length + 6,
                        bar_y + thickness - 2,
                        f"{share}%",
                        role="ink2",
                        size=11,
                    )
                )
        body.append(
            f'<line x1="{num(axis_x)}" y1="{top - 14}" x2="{num(axis_x)}" y2="{num(bottom)}" '
            f'{paint.stroke("axis")} stroke-width="1"/>'
        )
        footer = [
            "; ".join(f"{names[track]} n={sample['tracks'][track]}" for track in TRACKS),
            labels["suppressed"].format(min_track=radar["min_track"], min_cell=radar["min_cell"]),
            f"{radar['period']['from']} — {radar['period']['to']}",
        ]
        for index, line in enumerate(footer):
            body.append(paint.label(pad, bottom + 24 + index * 16, line, role="muted", size=11))
        return paint.frame(width, height, labels["postings_title"], labels["postings_desc"], body)

    def coverage(self, lang: str, mode: str) -> str:
        """Supply: how many questions and written answers each theme holds."""
        paint = Paint(mode)
        labels = LABELS[lang]
        rows = self.theme_counts()
        columns = list(TRACKS) + ["answers"]
        peak = max(max(counts[column] for column in columns) for _, counts in rows) or 1
        pad, label_width, cell_width, gap = 20, 300, 110, 6
        top, row_height = 78, 26
        width = pad * 2 + label_width + len(columns) * (cell_width + gap)
        height = top + row_height * len(rows) + 40
        body = [paint.label(pad, 32, labels["coverage_title"], size=16, weight=600)]
        for index, name in enumerate(labels["coverage_cols"]):
            x = pad + label_width + index * (cell_width + gap) + cell_width / 2
            body.append(paint.label(x, top - 12, name, size=12, weight=600, anchor="middle"))
        for index, (theme, counts) in enumerate(rows):
            y = top + index * row_height
            body.append(
                paint.label(pad + label_width - 12, y + 17, theme["name"][lang], anchor="end")
            )
            for column_index, column in enumerate(columns):
                value = counts[column]
                x = pad + label_width + column_index * (cell_width + gap)
                step = ramp_step(value / peak)
                body.append(
                    f'<rect x="{num(x)}" y="{num(y)}" width="{cell_width}" '
                    f'height="{row_height - 4}" rx="4" {paint.fill(f"ramp-{step}")}/>'
                )
                body.append(
                    paint.label(
                        x + cell_width / 2,
                        y + 16,
                        str(value),
                        role="oncell" if step >= INVERT_FROM else "ink",
                        size=12,
                        anchor="middle",
                    )
                )
        body.append(paint.label(pad, height - 16, labels["coverage_note"], role="muted", size=11))
        return paint.frame(width, height, labels["coverage_title"], labels["coverage_desc"], body)

    def evidence(self, lang: str, mode: str) -> str:
        """Provenance: what kind of source stands behind each claim in the atlas."""
        paint = Paint(mode)
        labels = LABELS[lang]
        names = labels["evidence_kinds"]
        series = [
            (
                labels["evidence_rows"][0],
                self.question_evidence(),
                ("official", "participant_report", "secondary", "generated"),
            ),
            (
                labels["evidence_rows"][1],
                self.stage_claims(),
                ("official", "participant_report", "secondary", "assumption"),
            ),
        ]
        roles = {
            "official": "evidence-0",
            "participant_report": "evidence-1",
            "secondary": "evidence-2",
            "generated": "muted",
            "assumption": "muted",
        }
        pad, plot, thickness = 20, 700, 30
        width, top = pad * 2 + plot, 62
        body = [paint.label(pad, 32, labels["evidence_title"], size=16, weight=600)]
        y = top
        for row_name, counts, order in series:
            total = sum(counts.values()) or 1
            body.append(paint.label(pad, y, row_name.format(total=total), size=13, weight=600))
            x, entries = pad, []
            for key in order:
                value = counts.get(key, 0)
                if not value:
                    continue
                span = plot * value / total
                share = round(100 * value / total)
                # A 2px gap of surface keeps neighbouring segments from reading as one block.
                body.append(
                    f'<rect x="{num(x)}" y="{num(y + 12)}" width="{num(max(span - 2, 1))}" '
                    f'height="{thickness}" rx="3" {paint.fill(roles[key])}/>'
                )
                entries.append((f"{names[key]} {value} ({share}%)", roles[key]))
                x += span
            # Segments are often too narrow for a label of their own, so the numbers travel
            # with the legend instead of sitting on the bar.
            marks, lines = paint.flowing_legend(pad, y + 52, plot, entries)
            body += marks
            y += 68 + 17 * lines
        height = int(y + 26)
        body.append(paint.label(pad, height - 14, labels["evidence_note"], role="muted", size=11))
        return paint.frame(width, height, labels["evidence_title"], labels["evidence_desc"], body)

    def roadmap(self, lang: str, mode: str) -> str:
        """The roadmap as a spine of stages, every item marked with its status."""
        paint = Paint(mode)
        labels = LABELS[lang]
        status_names = labels["roadmap_status"]
        pad, spine, wrap = 20, 48, 86
        top, line_height, stage_gap = 96, 21, 20
        width = 820
        body = [paint.label(pad, 32, labels["roadmap_title"], size=16, weight=600)]
        legend_x = pad
        for key in ("done", "progress", "planned", "declined"):
            body += paint.status_mark(legend_x + 5, 56, key)
            body.append(paint.label(legend_x + 17, 56, status_names[key], role="ink2", size=11))
            legend_x += 32 + 6.6 * len(status_names[key])
        y, rows = top, []
        for stage in self.content.roadmap["stages"]:
            rows.append(
                f'<circle cx="{num(pad + 6)}" cy="{num(y - 5)}" r="5" {paint.fill("engineering")}/>'
            )
            rows.append(paint.label(spine, y, stage["name"][lang], size=13, weight=600))
            y += 10
            for item in stage["items"]:
                lines = wrap_text(item["text"][lang], wrap)
                rows += paint.status_mark(spine + 5, y + 11, item["status"])
                for offset, chunk in enumerate(lines):
                    rows.append(
                        paint.label(spine + 18, y + 11 + offset * line_height, chunk, size=12)
                    )
                y += line_height * len(lines) + 4
            y += stage_gap
        bottom = y - stage_gap - 6
        body.append(
            f'<line x1="{num(pad + 6)}" y1="{top - 14}" x2="{num(pad + 6)}" y2="{num(bottom)}" '
            f'{paint.stroke("axis")} stroke-width="1"/>'
        )
        body += rows
        height = int(bottom + 32)
        body.append(paint.label(pad, height - 14, labels["roadmap_note"], role="muted", size=11))
        return paint.frame(width, height, labels["roadmap_title"], labels["roadmap_desc"], body)

    def banner(self, lang: str, mode: str) -> str:
        """The title card: what the atlas is, and how much of it there is."""
        paint = Paint(mode)
        labels = LABELS[lang]
        names = {t["id"]: t["name"][lang] for t in self.content.taxonomy["tracks"]}
        values = {
            "questions": len(self.content.questions),
            "answers": self.answered(),
            "companies": len(self.content.companies),
            "sources": len(self.content.sources),
        }
        width, height, pad = 820, 264, 32
        body = [
            paint.label(pad, 74, "AI Interview Atlas", size=38, weight=700),
            paint.label(pad, 104, labels["banner_tagline"], size=14, role="ink2"),
        ]
        x = pad
        for track in TRACKS:
            name = names[track]
            chip = 24 + 7.4 * len(name)
            body.append(
                f'<rect x="{num(x)}" y="126" width="{num(chip)}" height="26" rx="13" '
                f"{paint.fill(track)}/>"
            )
            body.append(
                paint.label(
                    x + chip / 2, 144, name, role="oncell", size=12, weight=600, anchor="middle"
                )
            )
            x += chip + 10
        tile = (width - pad * 2 - 3 * 12) / 4
        for index, (key, caption) in enumerate(labels["banner_stats"]):
            left = pad + index * (tile + 12)
            body.append(
                f'<rect x="{num(left)}" y="172" width="{num(tile)}" height="58" rx="8" '
                f'fill="none" {paint.stroke("grid")}/>'
            )
            body.append(paint.label(left + 14, 202, str(values[key]), size=25, weight=700))
            body.append(paint.label(left + 14, 220, caption, role="muted", size=11))
        body.append(paint.label(pad, height - 18, labels["banner_footer"], role="muted", size=11))
        alt = f"AI Interview Atlas — {labels['banner_tagline']}"
        return paint.frame(width, height, "AI Interview Atlas", alt, body)
