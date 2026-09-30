"""Synthetic contracts: provenance, anonymity, private-content rejection and determinism."""

import shutil
from datetime import date
from pathlib import Path

import pytest
import yaml

from atlas import cli, links
from atlas.content import ContentError, load, read_yaml
from atlas.render import render, ru_count

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
        "docs/ROADMAP.md",
        "docs/ru/ROADMAP.md",
        "docs/LEARNING_PATH.md",
        "docs/ru/LEARNING_PATH.md",
        "docs/AI_ROLES.md",
        "docs/ru/AI_ROLES.md",
        "docs/REASONING_MODELS.md",
        "docs/ru/REASONING_MODELS.md",
        "CHANGELOG.md",
        "docs/ru/CHANGELOG.md",
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


def test_source_disclosure_counts_questions_and_ignores_reading():
    content = load(FIXTURE, today=TODAY)
    question = next(q for q in content.questions if q["theme"] == "agents-tools")
    # The same compilation attached to two employers still backs one question.
    question["evidence"].append({"source": "big-compilation", "company": "sample-bank"})
    for question in content.questions:
        question["reading"] = ["eval-paper", "example-labs-careers"]
    pages = render(content)
    for path in ("README.md", "docs/README.md"):
        assert "Of 3 questions attributed to published sources, 1 rely only" in pages[path]
        assert "Another 1 are generated practice questions" in pages[path]
        assert "2 questions cite the same compilation" in pages[path]
    for path in ("README.ru.md", "docs/ru/README.md"):
        assert "Из 3 вопросов с опубликованными источниками 1 опираются только" in pages[path]
        assert "Число вопросов, ссылающихся на одну подборку: 2 — " in pages[path]
    # Technical reading above did not strengthen the weak question; interview evidence does.
    weak = next(q for q in content.questions if q["theme"] == "behavioral-values")
    weak["evidence"].append({"source": "example-labs-careers"})
    assert (
        "3 questions attributed to published sources, 0 rely only" in render(content)["README.md"]
    )
    for question in content.questions:
        question["evidence"] = [
            e for e in question.get("evidence", []) if e["source"] != "big-compilation"
        ]
    assert "questions cite the same compilation" not in render(content)["README.md"]


def test_published_question_needs_interview_evidence(content_dir):
    path = content_dir / "questions" / "agents-tools.yaml"
    edit(path, lambda data: data["questions"][0].update(evidence=[]))
    assert "published needs evidence" in problems(content_dir)
    edit(path, lambda data: data["questions"][0].update(evidence=[{"source": "eval-paper"}]))
    assert "evidence must be an interview source" in problems(content_dir)


def test_source_url_reuse_is_required_even_with_a_trailing_slash(content_dir):
    def duplicate(data):
        data.append({**data[0], "id": "duplicate-source", "url": data[0]["url"] + "/"})

    edit(content_dir / "sources.yaml", duplicate)
    assert "duplicate source URL; reuse example-labs-careers" in problems(content_dir)


@pytest.mark.parametrize("language", ["en", "ru"])
def test_repeated_question_text_is_rejected_across_themes(content_dir, language):
    original = read_yaml(content_dir / "questions" / "agents-tools.yaml")["questions"][0]

    def duplicate(data):
        data["questions"][0]["text"][language] = (
            "  " + "   ".join(original["text"][language].upper().split()) + "  "
        )

    edit(content_dir / "questions" / "evals-observability.yaml", duplicate)
    assert f"duplicate {language} question text; reuse {original['id']}" in problems(content_dir)


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
    assert '### <a id="regression-gate"></a>1. Спроектируйте гейт' in page
    assert "Ответы готовы: 1 из 1." in page
    assert "answers/leadership.md)" not in page.split("\n")[3]
    # The answers are reached from the track's start page, not from the README.
    assert (
        "[Ответы на эти вопросы](../answers/leadership.md)" in pages["docs/ru/start/leadership.md"]
    )
    assert "answers/" not in pages["docs/start/leadership.md"]
    assert "**80 written answers**" not in pages["README.md"]
    assert "**1 написанный ответ**" in pages["README.ru.md"]


def test_adding_english_answer_preserves_russian_and_links_both_editions(content_dir):
    before = render(load(content_dir, today=TODAY))
    path = content_dir / "questions" / "evals-observability.yaml"
    edit(path, lambda data: data["questions"][0]["answer"].update(en="A synthetic answer."))
    pages = render(load(content_dir, today=TODAY))
    english = pages["docs/answers/leadership.md"]
    russian = pages["docs/ru/answers/leadership.md"]
    assert "A synthetic answer." in english and "A synthetic answer." not in russian
    assert "../ru/answers/leadership.md" in english
    assert "../../answers/leadership.md" in russian
    # Adding a translation changes navigation, not the original answer body.
    assert before["docs/ru/answers/leadership.md"].split("###", 1)[1] == russian.split("###", 1)[1]
    assert "../answers/leadership.md" in pages["docs/start/leadership.md"]


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


def test_every_question_has_one_anchor_on_its_theme_page_and_links_to_it_elsewhere():
    pages = render(load(FIXTURE, today=TODAY))
    theme = pages["docs/themes/evals-observability.md"]
    assert theme.count('<a id="regression-gate"></a>') == 1
    assert "question=regression-gate" in theme  # a correction form with the id filled in
    # Other pages point at the canonical entry instead of repeating the anchor.
    common = pages["docs/common.md"]
    assert "(themes/evals-observability.md#regression-gate)" in common
    assert '<a id="regression-gate">' not in common
    start = pages["docs/ru/start/leadership.md"]
    assert "(../themes/evals-observability.md#regression-gate)" in start
    assert "✍ [Ответ](../answers/leadership.md#regression-gate)" in start
    # The answer links back to the checklist and to the contents of its page.
    answers = pages["docs/ru/answers/leadership.md"]
    assert "[Чек-лист](../themes/evals-observability.md#regression-gate)" in answers
    assert "[1. Спроектируйте гейт, который решает, выпускать ли изменение промпта.]" in answers
    assert "[↑ К содержанию](#contents)" in answers


def test_answer_links_appear_only_in_the_language_that_has_the_answer():
    pages = render(load(FIXTURE, today=TODAY))
    assert "✍" not in pages["docs/themes/evals-observability.md"]
    assert (
        "✍ [Ответ](../answers/leadership.md#regression-gate)"
        in (pages["docs/ru/themes/evals-observability.md"])
    )


def test_company_page_does_not_link_to_itself_and_pages_through_companies():
    pages = render(load(FIXTURE, today=TODAY))
    labs = pages["docs/companies/example-labs.md"]
    assert "Asked at: Example Labs ✅" in labs
    assert "(example-labs.md)" not in labs
    assert "[Sample Bank](sample-bank.md) →" in labs
    assert "← [Example Labs](example-labs.md)" in pages["docs/companies/sample-bank.md"]
    assert "On this page: [Interview loop](#loop)" in labs


def test_themes_page_forward_and_back_in_taxonomy_order():
    pages = render(load(FIXTURE, today=TODAY))
    first = pages["docs/themes/evals-observability.md"]
    assert "← [" not in first
    assert "[Agents and tools](agents-tools.md) →" in first
    middle = pages["docs/themes/agents-tools.md"]
    assert "← [Evaluation and observability](evals-observability.md)" in middle
    assert "[Behavioral and values](behavioral-values.md) →" in middle
    assert "[AI Interview Atlas](../../README.md) › [Themes](../README.md#themes)" in middle


def test_map_of_the_atlas_links_every_section_in_both_languages():
    pages = render(load(FIXTURE, today=TODAY))
    hub, russian = pages["docs/README.md"], pages["docs/ru/README.md"]
    for anchor in ("tracks", "themes", "companies", "reference"):
        assert f'<a id="{anchor}"></a>' in hub and f'<a id="{anchor}"></a>' in russian
    assert "[Start here](start/leadership.md)" in hub
    assert "[Ответы](answers/leadership.md): готово 1 из 1" in russian
    assert "answers/" not in hub  # English has no answers in the fixture yet
    assert "[Changelog](../CHANGELOG.md)" in hub and "[Журнал изменений](CHANGELOG.md)" in russian
    readme = pages["README.md"]
    assert "**Navigate:** [Map of the atlas](docs/README.md)" in readme
    assert "[Themes](#themes) · [Companies](#companies)" in pages["README.md"]
    assert "[Темы](#темы) · [Компании](#компании)" in pages["README.ru.md"]


def test_generated_navigation_passes_the_link_and_anchor_check(tmp_path):
    root = repository(tmp_path)
    assert cli.main(["--root", str(root)]) == 0
    assert links.check(root) == []


@pytest.mark.parametrize("reserved", ["contents", "questions", "track-both"])
def test_question_ids_cannot_take_a_section_anchor(content_dir, reserved):
    path = content_dir / "questions" / "agents-tools.yaml"
    edit(path, lambda data: data["questions"][0].update(id=reserved))
    assert "id is reserved for a page section anchor" in problems(content_dir)


def test_role_pages_separate_reported_questions_from_practice():
    pages = render(load(FIXTURE, today=TODAY))
    builders, leaders = pages["docs/roles/builders.md"], pages["docs/roles/leaders.md"]
    # The candidate report names the AI engineer role, so the question counts as reported.
    reported = builders.split("### Reported for these roles", 1)[1]
    assert "(../themes/evals-observability.md#regression-gate)" in reported
    # For the product manager it is only tagged, so it is practice, not a reported question.
    assert "### Reported for these roles" not in leaders
    assert "### Also practise" in leaders and "#regression-gate)" in leaders
    # Symbolic links in the guide resolve relative to each page.
    assert "[the gate](../themes/evals-observability.md#regression-gate)" in builders
    assert "[learning path](../LEARNING_PATH.md)" in leaders
    assert "**Practice deliverable:** build a demo." in builders
    assert "**Practice deliverable:**" not in leaders


def test_role_page_shows_stages_reported_for_its_roles_or_says_there_are_none():
    pages = render(load(FIXTURE, today=TODAY))
    builders = pages["docs/roles/builders.md"]
    assert "| [Example Labs](../companies/example-labs.md) | Practical coding<br>*Applied AI" in (
        builders
    )
    assert "🗣 candidate report" in builders
    assert "Recruiter screen" not in builders  # untagged stages stay on the company page only
    leaders = pages["docs/ru/roles/leaders.md"]
    assert "Публичных данных о собеседованиях на эти роли пока нет." in leaders
    overview = pages["docs/AI_ROLES.md"]
    assert "| [Builders](roles/builders.md) | Build AI features. | 1 | 1 | 1 | 0 |" in overview
    assert "| [Leaders](roles/leaders.md) | Lead AI products. | 0 | 0 | 0 | 1 |" in overview
    company = pages["docs/companies/example-labs.md"]
    assert "| Practical coding<br>*Applied AI engineer* |" in company


def test_a_job_posting_never_counts_as_interview_evidence(content_dir):
    path = content_dir / "questions" / "agents-tools.yaml"
    edit(path, lambda data: data["questions"][0].update(evidence=[{"source": "example-posting"}]))
    assert "evidence must be an interview source" in problems(content_dir)
    path = content_dir / "companies" / "example-labs.yaml"
    edit(path, lambda data: data["loop"][0].update(sources=["example-posting"]))
    assert "confirmed cannot rest on posting" in problems(content_dir)


def test_roles_guide_links_and_role_ownership_are_checked(content_dir):
    path = content_dir / "roles.yaml"

    def break_guide(data):
        data["families"][1]["roles"].append("ai-engineer")
        data["families"][0]["prep"]["en"] = "see [a gap](question:no-such-question)"
        data["families"][0]["sections"][0]["text"]["ru"] = "см. [внешнюю](https://example.com)"

    edit(path, break_guide)
    found = problems(content_dir)
    assert "role ai-engineer already belongs to builders" in found
    assert "en link to unknown question no-such-question" in found
    assert "ru text has a link that is not kind:id" in found


def test_evidence_role_must_exist_and_fit_the_question(content_dir):
    path = content_dir / "questions" / "evals-observability.yaml"
    edit(path, lambda data: data["questions"][0]["evidence"][1].update(role="no-such-role"))
    assert "evidence names unknown role no-such-role" in problems(content_dir)
    edit(path, lambda data: data["questions"][0].update(tracks=["leadership"], roles=["ai-pm"]))
    edit(path, lambda data: data["questions"][0]["evidence"][1].update(role="ai-engineer"))
    assert "evidence role ai-engineer is outside the question's tracks" in problems(content_dir)


def test_compilation_is_named_but_linked_to_its_attribution_not_the_external_repository():
    pages = render(load(FIXTURE, today=TODAY))
    readme = pages["README.md"]
    assert "[Interview question compilation](docs/sources.md#kind-secondary-compilation)" in readme
    assert "https://example.com/compilation" not in readme
    assert '<a id="kind-secondary-compilation"></a>' in pages["docs/sources.md"]


def test_role_guide_rejects_future_dates_and_unrepresented_primary_track(content_dir):
    edit(content_dir / "roles.yaml", lambda data: data.update(checked="2026-10-01"))
    assert "roles.yaml: date 2026-10-01 is in the future" in problems(content_dir)
    edit(content_dir / "roles.yaml", lambda data: data["families"][0].update(track="leadership"))
    assert "primary track must be represented by a family role" in problems(content_dir)


def test_company_stage_role_must_be_covered_by_company(content_dir):
    path = content_dir / "companies" / "example-labs.yaml"
    edit(path, lambda data: data["roles"]["engineering"].remove("applied-ai-engineer"))
    assert "role applied-ai-engineer is outside company roles" in problems(content_dir)


def test_role_assumptions_stay_on_company_page_and_do_not_count_as_reported():
    content = load(FIXTURE, today=TODAY)
    stage = content.companies["example-labs"]["loop"][1]
    stage.update(claim="assumption", sources=[])
    pages = render(content)
    assert "Practical coding" not in pages["docs/roles/builders.md"]
    assert "Practical coding" in pages["docs/companies/example-labs.md"]
    assert (
        "| [Builders](roles/builders.md) | Build AI features. | 0 | 0 | 1 | 0 |"
        in (pages["docs/AI_ROLES.md"])
    )


def test_mixed_role_family_is_reachable_from_both_tracks_in_both_languages():
    content = load(FIXTURE, today=TODAY)
    content.families[0]["roles"].append("ai-pm")
    content.guide["families"].pop()
    pages = render(content)
    for lang, root, prefix, names in (
        ("en", "README.md", "docs", "AI Engineering / AI Leadership"),
        ("ru", "README.ru.md", "docs/ru", "AI-инженерия / AI-лидерство"),
    ):
        assert names in pages[f"{prefix}/roles/builders.md"]
        assert pages[root].count(f"({prefix}/roles/builders.md)") == 2
        assert pages[f"{prefix}/README.md"].count("(roles/builders.md)") == 2


def test_role_reported_question_shows_matching_evidence_not_unrelated_companies():
    pages = render(load(FIXTURE, today=TODAY))
    section = pages["docs/roles/builders.md"].split("### Reported for these roles", 1)[1]
    assert "https://example.org/blog/interview" in section
    assert "Sample Bank" in section
    assert "Example Labs" not in section
    assert "https://example.com/compilation" not in section
    assert '<a id="role-questions"></a>Questions' in pages["docs/roles/builders.md"]
    assert '<a id="questions"></a>Questions' not in pages["docs/roles/builders.md"]


@pytest.mark.parametrize(
    ("count", "expected"),
    [
        (1, "источник"),
        (2, "источника"),
        (4, "источника"),
        (5, "источников"),
        (11, "источников"),
        (14, "источников"),
        (21, "источник"),
        (22, "источника"),
        (100, "источников"),
        (111, "источников"),
        (162, "источника"),
        (294, "источника"),
    ],
)
def test_russian_counts_agree_with_the_numeral(count, expected):
    assert ru_count(count, "источник", "источника", "источников") == expected
