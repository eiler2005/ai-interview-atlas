"""The site menu covers every generated page, and links that leave docs/ stay usable."""

import posixpath
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from atlas import links, site
from atlas.content import load
from atlas.render import render

FIXTURE = Path(__file__).parent / "fixtures" / "content"
TODAY = date(2026, 9, 27)
GUIDES = (
    "LEARNING_ROADMAP.md",
    "learning/AI_ASSISTED_CODING.md",
    "learning/PRODUCTION_AI_ENGINEERING.md",
    "learning/AI_LEADERSHIP.md",
    "research/ATLAS_COVERAGE_AUDIT.md",
    "research/ENGINEERING_RESEARCH.md",
    "research/LEADERSHIP_AUDIT.md",
    "plans/ATLAS_EXPANSION.md",
)


def paths(menu) -> list[str]:
    found = []
    for entry in menu:
        for value in entry.values():
            found += paths(value) if isinstance(value, list) else [value]
    return found


def test_menu_lists_every_generated_page_in_both_languages_once():
    content = load(FIXTURE, today=TODAY)
    menu = site.nav(content)
    listed = paths(menu)
    assert len(listed) == len(set(listed))
    generated = {
        name.removeprefix("docs/")
        for name in render(content)
        if name.startswith("docs/") and name.endswith(".md")
    }
    assert generated <= set(listed)
    assert listed[0] == "README.md"
    russian = next(entry["Русский"] for entry in menu if "Русский" in entry)
    assert paths(russian)[0] == "ru/README.md"
    assert all(path.startswith("ru/") for path in paths(russian))
    for guide in ("AI_ROLES.md", "REASONING_MODELS.md", "LEARNING_PATH.md", *GUIDES):
        assert guide in listed
        assert f"ru/{guide}" in listed


def test_curriculum_guides_are_discoverable_without_replacing_track_question_links():
    pages = render(load(FIXTURE, today=TODAY))
    for prefix, readme in (
        ("docs", "README.md"),
        ("docs/ru", "README.ru.md"),
    ):
        entries = [readme, f"{prefix}/README.md"]
        entries += [f"{prefix}/start/{track}.md" for track in ("engineering", "leadership")]
        for page in entries:
            targets = {
                posixpath.normpath(posixpath.join(posixpath.dirname(page), urlsplit(raw).path))
                for raw in links.LINK.findall(pages[page])
                if not urlsplit(raw).scheme and urlsplit(raw).path
            }
            assert {f"{prefix}/{guide}" for guide in GUIDES} <= targets
        hub = pages[f"{prefix}/README.md"]
        for section in ("tracks", "themes", "companies", "reference"):
            assert hub.count(f'<a id="{section}"></a>') == 1
        for track in ("engineering", "leadership"):
            assert f"(start/{track}.md)" in hub
            assert f"({prefix}/start/{track}.md)" in pages[readme]
        start = pages[f"{prefix}/start/leadership.md"]
        assert "(../themes/evals-observability.md#regression-gate)" in start
        assert '<a id="regression-gate"></a>' not in start


def test_links_outside_docs_go_to_the_map_or_to_github():
    text = (
        "[Atlas](../../README.md) [RU](../../README.ru.md#top) [Guide](../../CONTRIBUTING.md) "
        '[Theme](../themes/x.md#q) [Web](https://example.org/a_(b)) [Here](#local "title")'
    )
    result = site.rewrite_links(text, "themes/agents-tools.md")
    assert "[Atlas](../README.md)" in result
    assert "[RU](../ru/README.md#top)" in result
    assert "[Guide](https://github.com/eiler2005/ai-interview-atlas/blob/main/CONTRIBUTING.md)" in (
        result
    )
    assert "[Theme](../themes/x.md#q)" in result
    assert "[Web](https://example.org/a_(b))" in result
    assert '[Here](#local "title")' in result
    assert site.rewrite_links("[Map](../README.md)", "ru/common.md") == "[Map](../README.md)"


def test_nested_lists_get_four_spaces_per_level_outside_code():
    text = "- a\n  - b\n    - c\n```\n  - kept\n```\n  continuation"
    assert site.nest_lists(text) == (
        "- a\n    - b\n        - c\n```\n  - kept\n```\n  continuation"
    )
