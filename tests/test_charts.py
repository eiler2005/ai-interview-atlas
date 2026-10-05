"""The generated figures: valid SVG, a palette selected per surface, and nothing active."""

import re
from datetime import date
from pathlib import Path
from xml.etree import ElementTree

import pytest

from atlas.charts import MODES, Figures, ramp_step, tone, wrap_text
from atlas.content import load
from atlas.render import render

FIXTURE = Path(__file__).parent / "fixtures" / "content"
TODAY = date(2026, 9, 27)
LANGS = ("en", "ru")
FIGURES = ("banner", "evidence", "coverage", "roadmap", "postings")
# Everything the privacy checker's SVG allowlist admits that a figure actually uses.
ALLOWED_ELEMENTS = {"svg", "title", "desc", "rect", "path", "circle", "line", "text", "g"}


@pytest.fixture(scope="module")
def figures():
    return Figures(load(FIXTURE, today=TODAY))


def document(figures, name: str, lang: str, mode: str = "light") -> str:
    return getattr(figures, name)(lang, mode)


@pytest.mark.parametrize("name", FIGURES)
@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("mode", MODES)
def test_every_figure_is_well_formed_svg_with_a_title_and_description(figures, name, lang, mode):
    svg = document(figures, name, lang, mode)
    root = ElementTree.fromstring(svg)
    assert root.tag == "{http://www.w3.org/2000/svg}svg"
    assert root.get("role") == "img"
    tags = {child.tag.rsplit("}", 1)[-1] for child in root}
    assert {"title", "desc"} <= tags, "a figure must name itself for a reader who cannot see it"


@pytest.mark.parametrize("name", FIGURES)
@pytest.mark.parametrize("lang", LANGS)
@pytest.mark.parametrize("mode", MODES)
def test_a_figure_carries_nothing_the_privacy_checker_forbids(figures, name, lang, mode):
    """The checker's SVG allowlist has no `style` element and no active attributes.

    It also refuses an escaped attribute, an external reference and any `url()`, so a figure
    that reaches for a stylesheet or a web font could not be committed at all. That is why
    dark mode lives in a `<picture>` outside the image rather than in a media query inside
    it, and why the PDF rasteriser still sees a correct light figure.
    """
    svg = document(figures, name, lang, mode)
    assert "<style" not in svg and "class=" not in svg
    for node in ElementTree.fromstring(svg).iter():
        assert node.tag.rsplit("}", 1)[-1] in ALLOWED_ELEMENTS, node.tag
        for key, value in node.attrib.items():
            name_of = key.rsplit("}", 1)[-1].lower()
            assert not name_of.startswith("on")
            assert name_of not in {"src", "base", "style"}
            assert "\\" not in value
            assert not re.search(r"url\s*\(|https?\s*:|file\s*:|@import|javascript\s*:", value)


@pytest.mark.parametrize("name", FIGURES)
@pytest.mark.parametrize("lang", LANGS)
def test_each_surface_gets_its_own_steps(figures, name, lang):
    """Dark mode is selected, not an inversion: the two files differ in their colours."""
    light, dark = document(figures, name, lang, "light"), document(figures, name, lang, "dark")
    assert light != dark
    assert tone("surface", "light") in light
    assert tone("surface", "dark") in dark
    assert tone("surface", "dark") not in light


@pytest.mark.parametrize("name", FIGURES)
@pytest.mark.parametrize("mode", MODES)
def test_a_figure_is_deterministic(figures, name, mode):
    assert document(figures, name, "en", mode) == document(figures, name, "en", mode)


def test_the_two_languages_differ_only_in_their_text(figures):
    english = figures.coverage("en", "light")
    russian = figures.coverage("ru", "light")
    assert english != russian

    def without_text(svg: str) -> str:
        return re.sub(r">[^<]*<", "><", svg)

    assert without_text(english).count("<rect") == without_text(russian).count("<rect")


def test_the_evidence_figure_counts_every_question_exactly_once(figures):
    counts = figures.question_evidence()
    assert sum(counts.values()) == len(figures.content.questions)
    # A generated question is practice, never evidence that an employer asked it.
    generated = [q for q in figures.content.questions if q["provenance"] == "generated"]
    assert counts["generated"] == len(generated)


def test_the_evidence_figure_counts_every_loop_stage_exactly_once(figures):
    stages = sum(len(company["loop"]) for company in figures.content.companies.values())
    assert sum(figures.stage_claims().values()) == stages


def test_coverage_counts_match_the_question_bank(figures):
    rows = figures.theme_counts()
    assert {theme["id"] for theme, _ in rows} == {
        theme["id"] for theme in figures.content.taxonomy["themes"]
    }
    for track in ("engineering", "leadership"):
        total = sum(counts[track] for _, counts in rows)
        assert total == sum(1 for q in figures.content.questions if track in q["tracks"])


def test_the_roadmap_figure_draws_every_item_and_marks_its_status(figures):
    svg = figures.roadmap("en", "light")
    items = [item for stage in figures.content.roadmap["stages"] for item in stage["items"]]
    for item in items:
        for line in wrap_text(item["text"]["en"], 86):
            assert line in svg
    # Every status is a shape, so the status never rests on colour alone. The legend draws
    # one of each in addition to the items.
    ruled_out = sum(1 for item in items if item["status"] == "declined")
    assert svg.count("l7.2 7.2m0-7.2l-7.2 7.2") == ruled_out + 1


@pytest.mark.parametrize(("share", "expected"), [(0, 0), (0.01, 0), (0.5, 3), (0.99, 5), (1, 5)])
def test_a_magnitude_lands_on_a_ramp_step_inside_the_ramp(share, expected):
    assert ramp_step(share) == expected


def test_wrapping_keeps_every_word_and_respects_the_limit():
    body = "one two three four five six seven eight nine ten"
    lines = wrap_text(body, 12)
    assert " ".join(lines).split() == body.split()
    assert all(len(line) <= 12 for line in lines)


def test_the_build_writes_both_surfaces_of_every_figure_in_both_languages():
    pages = render(load(FIXTURE, today=TODAY))
    for name in ("banner", "evidence", "coverage", "roadmap", "radar"):
        for lang in LANGS:
            for suffix in ("", ".dark"):
                path = f"docs/assets/{name}.{lang}{suffix}.svg"
                assert path in pages, path
                assert pages[path].startswith("<svg")


def test_a_page_offers_the_dark_figure_before_falling_back_to_the_light_one():
    readme = render(load(FIXTURE, today=TODAY))["README.md"]
    assert '<source media="(prefers-color-scheme: dark)"' in readme
    # The fallback is the light file, which is what a renderer without `<picture>` shows.
    assert 'srcset="docs/assets/banner.en.dark.svg"' in readme
    assert 'src="docs/assets/banner.en.svg"' in readme
