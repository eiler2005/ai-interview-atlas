"""The machine-readable export: a stable shape, and provenance that travels with the claim."""

import json
from datetime import date
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from atlas import cli, export
from atlas.content import load

FIXTURE = Path(__file__).parent / "fixtures" / "content"
SCHEMA = Path(__file__).parents[1] / "src" / "content" / "schema" / "export.schema.json"
TODAY = date(2026, 9, 27)


@pytest.fixture(scope="module")
def document():
    return export.document(load(FIXTURE, today=TODAY))


def test_the_export_matches_its_published_schema(document):
    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    assert sorted(validator.iter_errors(document), key=str) == []


def test_the_export_is_deterministic_and_round_trips_through_json():
    content = load(FIXTURE, today=TODAY)
    first = export.dumps(content)
    assert first == export.dumps(load(FIXTURE, today=TODAY))
    assert json.loads(first) == export.document(content)
    assert first.endswith("}\n")


def test_counts_agree_with_the_exported_collections(document):
    assert document["counts"]["questions"] == len(document["questions"])
    assert document["counts"]["companies"] == len(document["companies"])
    assert document["counts"]["sources"] == len(document["sources"])
    assert document["counts"]["answers"] == sum(1 for q in document["questions"] if q["answer"])


def test_a_question_carries_the_marker_a_reader_would_see(document):
    for question in document["questions"]:
        if question["provenance"] == "generated":
            assert question["marker"] == "🧪"
            assert question["evidence"] == []
            assert question["basis"], "a generated question must name its radar basis"
            continue
        assert question["evidence"], "a published question must carry its evidence"
        kinds = {item["kind"] for item in question["evidence"]}
        if "official" in kinds:
            assert question["marker"] == "✅"
        elif "participant_report" in kinds:
            assert question["marker"] == "🗣"
        else:
            assert question["marker"] == "†"


def test_a_compilation_is_never_exported_as_a_first_hand_report(document):
    for question in document["questions"]:
        for item in question["evidence"]:
            if item["kind"] in ("prep_guide", "secondary_compilation"):
                assert item["marker"] == "†"


def test_every_referenced_id_resolves_inside_the_export(document):
    sources = {source["id"] for source in document["sources"]}
    themes = {theme["id"] for theme in document["themes"]}
    questions = {question["id"] for question in document["questions"]}
    for question in document["questions"]:
        assert question["theme"] in themes
        assert {item["source"] for item in question["evidence"]} <= sources
        assert set(question["reading"]) <= sources
    for company in document["companies"]:
        assert set(company["questions"]) <= questions
        for stage in company["loop"]:
            assert set(stage["sources"]) <= sources


def test_a_company_lists_exactly_the_questions_reported_for_it(document):
    for company in document["companies"]:
        expected = sorted(
            question["id"]
            for question in document["questions"]
            if company["id"] in question["asked_at"]
        )
        assert company["questions"] == expected


def test_the_cli_writes_the_export_where_it_is_asked_to(tmp_path, monkeypatch):
    root = tmp_path / "repo"
    (root / "src").mkdir(parents=True)
    import shutil

    shutil.copytree(FIXTURE, root / "src" / "content")
    target = tmp_path / "out" / "atlas.json"
    monkeypatch.chdir(tmp_path)
    cli.main(["--root", str(root), "--check", "--export", str(target)])
    written = json.loads(target.read_text(encoding="utf-8"))
    assert written["schema_version"] == export.SCHEMA_VERSION
    assert written["counts"]["questions"] == len(written["questions"])
