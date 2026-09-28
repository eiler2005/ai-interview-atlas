"""Synthetic contracts: provenance, anonymity, private-content rejection and determinism."""

import shutil
from datetime import date
from pathlib import Path

import pytest
import yaml

from atlas import cli, links
from atlas.content import ContentError, load, read_yaml
from atlas.render import render

FIXTURE = Path(__file__).parent / "fixtures" / "content"
TODAY = date(2026, 9, 27)


@pytest.fixture
def content_dir(tmp_path):
    target = tmp_path / "content"
    shutil.copytree(FIXTURE, target)
    return target


def edit(path: Path, change) -> None:
    data = read_yaml(path)
    change(data)
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def problems(content_dir: Path) -> str:
    with pytest.raises(ContentError) as error:
        load(content_dir, today=TODAY)
    return str(error.value)


def repository(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    shutil.copytree(FIXTURE, root / "src" / "content")
    for name in (
        "CONTRIBUTING.md",
        "CONTRIBUTING.ru.md",
        "docs/METHODOLOGY.md",
        "docs/ru/METHODOLOGY.md",
        "docs/ATTRIBUTION.md",
        "docs/ru/ATTRIBUTION.md",
    ):
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text("# Synthetic\n", encoding="utf-8")
    return root


def test_fixture_renders_deterministically_with_markers():
    content = load(FIXTURE, today=TODAY)
    pages = render(content)
    assert pages == render(load(FIXTURE, today=TODAY))
    readme = pages["README.md"]
    assert "**4 questions** across 3 themes: 3 for engineering, 3 for leadership" in readme
    assert "[Asked across companies](docs/common.md)" in readme
    # Asked at two companies: listed on its own page, strongest basis first.
    common = pages["docs/common.md"]
    assert "[Sample Bank](companies/sample-bank.md) 🗣" in common
    assert "[Example Labs](companies/example-labs.md) †" in common
    agents = pages["docs/themes/agents-tools.md"]
    assert "[Example Labs](../companies/example-labs.md) ✅" in agents
    evals = pages["docs/themes/evals-observability.md"]
    assert "🧪 generated from job-posting themes" in evals
    assert "Спроектируйте гейт" in pages["docs/ru/themes/evals-observability.md"]
    assert pages["docs/assets/radar.en.svg"].startswith("<svg")


def test_dates_stay_strings_and_future_dates_are_rejected(content_dir):
    content = load(content_dir, today=TODAY)
    assert content.sources["example-labs-careers"]["retrieved"] == "2026-09-20"
    edit(content_dir / "sources.yaml", lambda data: data[0].update(retrieved="2026-10-01"))
    assert "in the future" in problems(content_dir)


def test_published_question_needs_interview_evidence(content_dir):
    path = content_dir / "questions" / "agents-tools.yaml"
    edit(path, lambda data: data["questions"][0].update(evidence=[]))
    assert "published needs evidence" in problems(content_dir)
    edit(path, lambda data: data["questions"][0].update(evidence=[{"source": "eval-paper"}]))
    assert "evidence must be an interview source" in problems(content_dir)


def test_generated_question_needs_published_radar_theme(content_dir):
    path = content_dir / "questions" / "evals-observability.yaml"
    edit(path, lambda data: data["questions"][1].update(basis=["radar:behavioral-values"]))
    assert "has no published radar row" in problems(content_dir)
    edit(
        path,
        lambda data: data["questions"][1].update(
            basis=["radar:evals-observability"], evidence=[{"source": "prep-guide"}]
        ),
    )
    assert "generated needs a basis and no interview evidence" in problems(content_dir)


def test_loop_claim_must_match_source_kind(content_dir):
    path = content_dir / "companies" / "example-labs.yaml"
    edit(path, lambda data: data["loop"][0].update(sources=["big-compilation"]))
    assert "confirmed cannot rest on secondary_compilation" in problems(content_dir)
    edit(path, lambda data: data["loop"][0].update(claim="assumption"))
    assert "an assumption cites no sources" in problems(content_dir)


@pytest.mark.parametrize("value", ["required", "not_required", "varies"])
def test_coding_requirement_cannot_be_established_by_a_guide(content_dir, value):
    path = content_dir / "companies" / "example-labs.yaml"
    edit(path, lambda data: data.update(coding={"value": value, "sources": ["prep-guide"]}))
    assert "known coding requirement needs a company or candidate source" in problems(content_dir)
    edit(path, lambda data: data["coding"].update(value="unknown"))
    assert load(content_dir, today=TODAY).companies["example-labs"]["coding"]["value"] == "unknown"
    edit(path, lambda data: data["coding"].update(value=value, sources=["candidate-blog"]))
    assert load(content_dir, today=TODAY).companies["example-labs"]["coding"]["value"] == value


def test_radar_suppresses_small_cells_and_thin_tracks(content_dir):
    path = content_dir / "radar.yaml"
    edit(path, lambda data: data["rows"][1].update(postings=4))
    assert "suppressed or exceeds its sample" in problems(content_dir)
    shutil.copy(FIXTURE / "radar.yaml", path)

    def thin(data):
        data["sample"]["tracks"] = {"engineering": 10, "leadership": 50}

    edit(path, thin)
    assert "engineering sample is below min_track" in problems(content_dir)


@pytest.mark.parametrize(
    ("text", "rule"),
    [
        ("see /" + "Users/synthetic/notes", "private-path"),
        ("https://t.me/c/123/456", "private-telegram-link"),
        ("from telegram-1234567-89", "journal-id"),
        ("write to synthetic" + "@" + "mail.invalid", "contact-email"),
    ],
)
def test_private_content_is_rejected(content_dir, text, rule):
    path = content_dir / "questions" / "behavioral-values.yaml"
    edit(path, lambda data: data["questions"][0]["tests"].update(en=text))
    assert f"forbidden {rule}" in problems(content_dir)


def test_start_here_needs_outline_and_matching_translations(content_dir):
    path = content_dir / "questions" / "evals-observability.yaml"
    edit(path, lambda data: data["questions"][0]["outline"]["ru"].pop())
    assert "outlines differ in length" in problems(content_dir)
    edit(path, lambda data: data["questions"][0].pop("outline"))
    assert "start_here questions need an outline and reading" in problems(content_dir)


def test_answers_render_only_for_the_language_that_has_them(content_dir):
    pages = render(load(content_dir, today=TODAY))
    assert "docs/ru/answers/leadership.md" in pages
    assert "docs/answers/leadership.md" not in pages
    page = pages["docs/ru/answers/leadership.md"]
    # Numbered like Start here, and no link to a counterpart that does not exist yet.
    assert "### 1. Спроектируйте гейт" in page
    assert "Ответы готовы: 1 из 1." in page
    assert "answers/leadership.md)" not in page.split("\n")[3]
    # The answers are reached from the track's start page, not from the README.
    assert (
        "[Ответы на эти вопросы](../answers/leadership.md)" in pages["docs/ru/start/leadership.md"]
    )
    assert "answers/" not in pages["docs/start/leadership.md"]
    assert "**80 written answers**" not in pages["README.md"]
    assert "**1 написанных ответов**" in pages["README.ru.md"]


def test_an_answer_needs_a_priority_question_and_one_paragraph(content_dir):
    path = content_dir / "questions" / "agents-tools.yaml"
    edit(path, lambda data: data["questions"][0].update(answer={"ru": "Ответ."}))
    assert "answers belong to start_here questions" in problems(content_dir)
    path = content_dir / "questions" / "evals-observability.yaml"
    edit(path, lambda data: data["questions"][0].update(answer={"ru": "Первый.\nВторой."}))
    assert "the ru answer must be one clean paragraph" in problems(content_dir)


def test_build_then_check_detects_drift_stale_pages_and_links(tmp_path):
    root = repository(tmp_path)
    assert cli.main(["--root", str(root)]) == 0
    assert cli.main(["--root", str(root), "--check"]) == 0
    readme = root / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8") + "manual edit\n", encoding="utf-8")
    assert cli.main(["--root", str(root), "--check"]) == 1
    assert cli.main(["--root", str(root)]) == 0
    stale = root / "docs" / "companies" / "gone.md"
    stale.write_text("old\n", encoding="utf-8")
    assert cli.main(["--root", str(root), "--check"]) == 1
    assert cli.main(["--root", str(root)]) == 0 and not stale.exists()
    (root / "docs" / "ru" / "METHODOLOGY.md").unlink()
    errors = links.check(root)
    assert any("missing METHODOLOGY.md" in e or "Missing Russian page" in e for e in errors)
