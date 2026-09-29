"""Load atlas content and reject anything that is unsourced, inconsistent or private."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

SCHEMA = Path(__file__).resolve().parents[1] / "content" / "schema" / "atlas.schema.json"
TRACKS = ("engineering", "leadership")
# Source kinds that may back each loop claim; an assumption cites nothing.
CLAIM_SOURCES = {
    "confirmed": {"official"},
    "participant_report": {"participant_report"},
    "secondary": {"prep_guide", "secondary_compilation"},
    "assumption": set(),
}
# Lower is stronger. References explain topics; they never show where a question was asked.
STRENGTH = {"official": 0, "participant_report": 1, "prep_guide": 2, "secondary_compilation": 2}
READING_KINDS = {"official", "reference", "prep_guide"}
FORBIDDEN = {
    "private-path": re.compile(r"/(?:Users|home)/[A-Za-z]"),
    "private-telegram-link": re.compile(r"t\.me/c/"),
    "journal-id": re.compile(
        r"\b(?:linkedinsalaries|telegram|jobicy|hh|li)-\d{3,}"
        r"|\btrudvsem-[0-9a-f]{8}-|\bact-[0-9a-f]{32}\b"
    ),
}
EMAIL = re.compile(r"[\w.+-]+@([\w.-]+\.[A-Za-z]{2,})")
EXAMPLE_DOMAINS = {"example.com", "example.org", "example.net", "example.invalid"}
# Section anchors on generated pages; a question id is an anchor too and must not collide.
RESERVED_IDS = {
    "contents",
    "tracks",
    "themes",
    "companies",
    "reference",
    "loop",
    "prep",
    "questions",
}


class ContentError(ValueError):
    """Every problem found in one pass, so an author can fix them together."""

    def __init__(self, problems: list[str]):
        super().__init__("\n".join(problems))
        self.problems = problems


class _Loader(yaml.SafeLoader):
    """Safe YAML that keeps ISO dates as strings, as the schema expects."""


_Loader.yaml_implicit_resolvers = {
    first: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for first, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


@dataclass
class Content:
    taxonomy: dict
    sources: dict[str, dict]
    companies: dict[str, dict]
    questions: list[dict]
    radar: dict | None

    @property
    def themes(self) -> dict[str, dict]:
        return {theme["id"]: theme for theme in self.taxonomy["themes"]}

    @property
    def roles(self) -> dict[str, dict]:
        return {role["id"]: role for role in self.taxonomy["roles"]}

    def asked_at(self, question: dict) -> dict[str, str]:
        """Company -> strongest source kind among the question's evidence."""
        result: dict[str, str] = {}
        for item in question.get("evidence", []):
            company = item.get("company")
            if not company:
                continue
            kind = self.sources[item["source"]]["kind"]
            if company not in result or STRENGTH[kind] < STRENGTH[result[company]]:
                result[company] = kind
        return result


def read_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.load(handle, Loader=_Loader)


def _validator(definition: str) -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator({**schema, "$ref": f"#/$defs/{definition}"})


def _schema_problems(name: str, value, definition: str) -> list[str]:
    problems = []
    for error in sorted(_validator(definition).iter_errors(value), key=lambda e: list(e.path)):
        where = "/".join(str(part) for part in error.path) or "(root)"
        problems.append(f"{name}: {where}: {error.message}")
    return problems


def _scan_text(name: str, text: str) -> list[str]:
    problems = [f"{name}: forbidden {rule}" for rule, rx in FORBIDDEN.items() if rx.search(text)]
    if any(m.group(1).lower() not in EXAMPLE_DOMAINS for m in EMAIL.finditer(text)):
        problems.append(f"{name}: forbidden contact-email")
    return problems


def load(content_dir: Path, *, today: date | None = None) -> Content:
    """Read `content_dir` and validate it completely, or raise ContentError."""
    today = today or datetime.now(UTC).date()
    problems: list[str] = []
    raw: dict[str, str] = {}

    def document(path: Path, definition: str):
        name = str(path.relative_to(content_dir))
        raw[name] = path.read_text(encoding="utf-8")
        value = read_yaml(path)
        problems.extend(_schema_problems(name, value, definition))
        return value

    taxonomy = document(content_dir / "taxonomy.yaml", "taxonomy")
    source_list = document(content_dir / "sources.yaml", "sources")
    companies = {
        path.stem: document(path, "company")
        for path in sorted((content_dir / "companies").glob("*.yaml"))
    }
    question_files = {
        path.stem: document(path, "questionsFile")
        for path in sorted((content_dir / "questions").glob("*.yaml"))
    }
    radar_path = content_dir / "radar.yaml"
    radar = document(radar_path, "radar") if radar_path.is_file() else None
    for name, text in raw.items():
        problems.extend(_scan_text(name, text))
    if problems:
        raise ContentError(problems)

    sources = _unique("sources.yaml", source_list, problems)
    questions = []
    for stem, data in question_files.items():
        if data["theme"] != stem:
            problems.append(f"questions/{stem}.yaml: theme must match the file name")
        questions += [{**question, "theme": data["theme"]} for question in data["questions"]]
    content = Content(taxonomy, sources, companies, questions, radar)
    problems += _check_taxonomy(content)
    problems += _check_sources(content, today)
    problems += _check_companies(content, today)
    problems += _check_questions(content, today)
    if radar:
        problems += _check_radar(content)
    if problems:
        raise ContentError(problems)
    return content


def _unique(name: str, items: list[dict], problems: list[str]) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for item in items:
        if item["id"] in result:
            problems.append(f"{name}: duplicate id {item['id']}")
        result[item["id"]] = item
    return result


def _not_future(name: str, value: str | None, today: date) -> list[str]:
    if not value:
        return []
    parts = [int(part) for part in value.split("-")] + [1, 1]
    try:
        parsed = date(*parts[:3])
    except ValueError:
        return [f"{name}: invalid date {value}"]
    return [f"{name}: date {value} is in the future"] if parsed > today else []


def _check_taxonomy(content: Content) -> list[str]:
    problems: list[str] = []
    for key in ("tracks", "roles", "themes"):
        _unique(f"taxonomy.yaml {key}", content.taxonomy[key], problems)
    if sorted(track["id"] for track in content.taxonomy["tracks"]) != sorted(TRACKS):
        problems.append("taxonomy.yaml: tracks must be exactly engineering and leadership")
    return problems


def _check_sources(content: Content, today: date) -> list[str]:
    problems = []
    for source in content.sources.values():
        name = f"sources.yaml {source['id']}"
        problems += _not_future(name, source.get("published"), today)
        problems += _not_future(name, source["retrieved"], today)
        if source["kind"] == "secondary_compilation" and not source.get("license"):
            problems.append(f"{name}: a reused compilation must state its license")
    return problems


def _check_companies(content: Content, today: date) -> list[str]:
    problems = []
    roles = content.roles
    for stem, company in content.companies.items():
        name = f"companies/{stem}.yaml"
        if company["id"] != stem:
            problems.append(f"{name}: id must match the file name")
        for track, ids in company["roles"].items():
            for role in ids:
                if roles.get(role, {}).get("track") != track:
                    problems.append(f"{name}: role {role} is not a {track} role")
        for index, stage in enumerate(company["loop"]):
            cited = stage.get("sources", [])
            allowed = CLAIM_SOURCES[stage["claim"]]
            if stage["claim"] == "assumption":
                if cited:
                    problems.append(f"{name}: loop/{index}: an assumption cites no sources")
                continue
            if not cited:
                problems.append(f"{name}: loop/{index}: {stage['claim']} needs a source")
            for source in cited:
                kind = content.sources.get(source, {}).get("kind")
                if kind is None:
                    problems.append(f"{name}: loop/{index}: unknown source {source}")
                elif kind not in allowed:
                    problems.append(f"{name}: loop/{index}: {stage['claim']} cannot rest on {kind}")
        coding = company["coding"]
        if coding["value"] != "unknown" and not coding.get("sources"):
            problems.append(f"{name}: coding requirement needs a basis source")
        if coding["value"] != "unknown" and not any(
            content.sources.get(source, {}).get("kind") in {"official", "participant_report"}
            for source in coding.get("sources", [])
        ):
            problems.append(f"{name}: known coding requirement needs a company or candidate source")
        for source in coding.get("sources", []):
            if source not in content.sources:
                problems.append(f"{name}: coding: unknown source {source}")
        for source in company.get("prep", []):
            if content.sources.get(source, {}).get("kind") != "official":
                problems.append(f"{name}: prep material must be an official source: {source}")
        problems += _not_future(name, company["reviewed"], today)
    return problems


def _check_questions(content: Content, today: date) -> list[str]:
    problems = []
    seen: set[str] = set()
    themes, roles = content.themes, content.roles
    radar_themes = {row["theme"] for row in (content.radar or {}).get("rows", [])}
    for question in content.questions:
        name = f"questions/{question['theme']}.yaml {question['id']}"
        if question["id"] in seen:
            problems.append(f"{name}: duplicate question id")
        if question["id"] in RESERVED_IDS or question["id"].startswith("track-"):
            problems.append(f"{name}: id is reserved for a page section anchor")
        seen.add(question["id"])
        if question["theme"] not in themes:
            problems.append(f"{name}: unknown theme")
        for role in question.get("roles", []):
            if role not in roles:
                problems.append(f"{name}: unknown role {role}")
            elif roles[role]["track"] not in question["tracks"]:
                problems.append(f"{name}: role {role} is outside the question's tracks")
        if not set(question.get("start_here", [])) <= set(question["tracks"]):
            problems.append(f"{name}: start_here must name the question's own tracks")
        if "priority" in question and not question.get("start_here"):
            problems.append(f"{name}: priority applies to start_here questions only")
        if question.get("start_here") and not (question.get("outline") and question.get("reading")):
            problems.append(f"{name}: start_here questions need an outline and reading")
        outline = question.get("outline")
        if outline and len(outline["en"]) != len(outline["ru"]):
            problems.append(f"{name}: English and Russian outlines differ in length")
        answer = question.get("answer")
        if answer and not question.get("start_here"):
            problems.append(f"{name}: answers belong to start_here questions")
        for language, text in (answer or {}).items():
            if "\n" in text or text != text.strip():
                problems.append(f"{name}: the {language} answer must be one clean paragraph")
        for source in question.get("reading", []):
            kind = content.sources.get(source, {}).get("kind")
            if kind not in READING_KINDS:
                problems.append(f"{name}: reading must be an official, reference or guide source")
        evidence, basis = question.get("evidence", []), question.get("basis", [])
        if question["provenance"] == "published":
            if not evidence or basis:
                problems.append(f"{name}: published needs evidence and no generated basis")
            for item in evidence:
                kind = content.sources.get(item["source"], {}).get("kind")
                if kind is None or kind == "reference":
                    problems.append(f"{name}: evidence must be an interview source")
                if item.get("company") and item["company"] not in content.companies:
                    problems.append(f"{name}: unknown company {item['company']}")
                problems += _not_future(name, item.get("observed"), today)
        else:
            if evidence or not basis:
                problems.append(f"{name}: generated needs a basis and no interview evidence")
            for item in basis:
                if item.removeprefix("radar:") not in radar_themes:
                    problems.append(f"{name}: basis {item} has no published radar row")
        problems += _not_future(name, question["added"], today)
    return problems


def _check_radar(content: Content) -> list[str]:
    radar, problems = content.radar, []
    sample = radar["sample"]
    if sum(sample["tracks"].values()) != sample["postings"]:
        problems.append("radar.yaml: track counts must add up to the sample")
    if sum(sample["markets"].values()) != sample["postings"]:
        problems.append("radar.yaml: market counts must add up to the sample")
    if radar["period"]["from"] > radar["period"]["to"]:
        problems.append("radar.yaml: period is reversed")
    for theme in radar.get("criteria", {}):
        if theme not in content.themes:
            problems.append(f"radar.yaml: criteria for unknown theme {theme}")
    for track, count in radar.get("ai_mentions", {}).items():
        total = sample["tracks"].get(track, 0)
        if total < radar["min_track"] or not radar["min_cell"] <= count <= total:
            problems.append(
                f"radar.yaml: ai_mentions for {track} is suppressed or exceeds its sample"
            )
    seen = set()
    for row in radar["rows"]:
        key = (row["track"], row["theme"])
        total = sample["tracks"].get(row["track"], 0)
        if key in seen:
            problems.append(f"radar.yaml: duplicate row {key}")
        seen.add(key)
        if row["theme"] not in content.themes:
            problems.append(f"radar.yaml: unknown theme {row['theme']}")
        if total < radar["min_track"]:
            problems.append(f"radar.yaml: {row['track']} sample is below min_track")
        if not radar["min_cell"] <= row["postings"] <= total:
            problems.append(f"radar.yaml: {key} is suppressed or exceeds its sample")
    return problems
