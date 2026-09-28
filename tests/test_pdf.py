"""Printable books: literal Markdown, font-safe markers, contents and (with the renderer) a PDF."""

import shutil
from datetime import date
from pathlib import Path

import pytest

from atlas.content import load
from atlas.pdf import PLACEHOLDER, Book, pdf_text

FIXTURE = Path(__file__).parent / "fixtures" / "content"
TODAY = date(2026, 9, 27)


def book(lang: str = "en") -> Book:
    return Book(load(FIXTURE, today=TODAY), FIXTURE, lang)


def test_text_stays_literal_and_markers_use_font_glyphs():
    assert pdf_text("a_b *c* [d](e) <f> | g") == r"a\_b \*c\* \[d\](e) \<f\> \| g"
    assert pdf_text("✅ 🗣 🧪 ❔") == "● ○ ‡ ?"
    assert pdf_text("Q&A &amp;") == r"Q&A \&amp;"


def test_book_has_contents_every_part_and_every_question():
    english = book()
    markdown = english.markdown()
    titles = [title for title, _ in english.parts()]
    assert markdown.count(f" — {PLACEHOLDER}") == len(titles)
    headings = [line[2:] for line in markdown.splitlines() if line.startswith("# ")]
    assert headings == ["AI Interview Atlas", "Contents", *titles]
    for question in english.content.questions:
        assert pdf_text(question["text"]["en"]) in markdown
    assert "Example Labs ●" in markdown
    assert "Sample Bank ○" in markdown
    assert "‡ generated from job-posting themes" in markdown
    assert not set("✅🗣🧪❔") & set(markdown)
    numbered = english.markdown(list(range(3, 3 + len(titles))))
    assert f"- {titles[0]} — 3" in numbered and PLACEHOLDER not in numbered


def test_start_here_checklists_print_once_and_themes_point_to_them():
    markdown = book().markdown()
    assert markdown.count("A golden set from real traffic.") == 1
    assert "Answer checklist: *Start here: AI Leadership*, question 1." in markdown
    russian = book("ru").markdown()
    assert "# Содержание" in russian
    assert "Спроектируйте гейт" in russian
    assert "Чек-лист ответа — в части «С чего начать: AI-лидерство», вопрос 1." in russian


def test_rendered_pdf_matches_its_contents(tmp_path):
    pytest.importorskip("job_search_agent.pdf_documents")
    from pypdf import PdfReader

    from atlas import pdf

    try:
        pdf.font_files(None)
    except SystemExit:
        pytest.skip("no Unicode TTF font available")
    root = tmp_path / "repo"
    shutil.copytree(FIXTURE, root / "src" / "content")
    [manifest] = pdf.build(root, root / "dist", ["en"])
    reader = PdfReader(root / "dist" / manifest["output"])
    assert len(reader.pages) == manifest["pages"]
    assert manifest["font_size"] == 12
    for entry in manifest["contents"]:
        assert entry["part"] in reader.pages[entry["page"] - 1].extract_text()
    text = " ".join(" ".join(page.extract_text() for page in reader.pages).split())
    assert "Design the gate that decides whether a prompt change ships." in text
    assert (root / "dist" / f"{manifest['output']}.manifest.json").is_file()
