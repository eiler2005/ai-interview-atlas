"""A machine-readable snapshot of the atlas, for practice tools outside a Markdown page.

The Markdown pages are for reading; this is the same content as data, so a drill app, a
flashcard deck or an analysis can use it without parsing prose. Three rules shape it:

* **Provenance travels with the claim.** Every question carries the kind of each source
  behind it and the marker a reader would see on the page, so a consumer cannot quietly
  present a compilation as a first-hand report.
* **Nothing is invented at export time.** Fields are copied from validated content; the only
  derived values are the per-company source kind, which already drives the pages, and counts.
* **The shape is versioned.** `schema_version` follows semantic versioning: a new optional
  field is a minor bump, a removed or re-typed field a major one.

The result is deterministic, so two builds of the same content produce identical bytes.
"""

from __future__ import annotations

import json
from typing import Any

from .content import TRACKS, Content

SCHEMA_VERSION = "1.0"
# What a reader sees on the page for a source of each kind, so an export consumer can show
# the same thing. A generated question carries the flask instead.
MARKERS = {
    "official": "✅",
    "participant_report": "🗣",
    "prep_guide": "†",
    "secondary_compilation": "†",
}
GENERATED_MARKER = "🧪"


def _source(content: Content, source_id: str) -> dict[str, Any]:
    source = content.sources[source_id]
    return {
        "id": source["id"],
        "kind": source["kind"],
        "title": source["title"],
        "publisher": source["publisher"],
        "url": source["url"],
        "retrieved": source["retrieved"],
        "published": source.get("published"),
        "lang": source.get("lang"),
        "license": source.get("license"),
    }


def _question(content: Content, question: dict) -> dict[str, Any]:
    generated = question["provenance"] == "generated"
    evidence = [
        {
            "source": item["source"],
            "kind": content.sources[item["source"]]["kind"],
            "marker": MARKERS[content.sources[item["source"]]["kind"]],
            "company": item.get("company"),
            "role": item.get("role"),
            "observed": item.get("observed"),
        }
        for item in question.get("evidence", [])
    ]
    return {
        "id": question["id"],
        "theme": question["theme"],
        "tracks": [track for track in TRACKS if track in question["tracks"]],
        "type": question["type"],
        "level": question.get("level"),
        "roles": question.get("roles", []),
        "text": question["text"],
        "tests": question["tests"],
        "outline": question.get("outline"),
        "answer": question.get("answer"),
        "start_here": question.get("start_here", []),
        "priority": question.get("priority"),
        "provenance": question["provenance"],
        "marker": GENERATED_MARKER
        if generated
        else min((item["marker"] for item in evidence), key=lambda mark: "✅🗣†".index(mark)),
        "evidence": evidence,
        "basis": question.get("basis", []),
        "asked_at": content.asked_at(question),
        "reading": question.get("reading", []),
        "added": question.get("added"),
    }


def _company(content: Content, company: dict) -> dict[str, Any]:
    asked = [q["id"] for q in content.questions if company["id"] in content.asked_at(q)]
    return {
        "id": company["id"],
        "name": company["name"],
        "segment": company["segment"],
        "markets": company["markets"],
        "roles": company["roles"],
        "summary": company.get("summary"),
        "coding": company["coding"],
        "reviewed": company["reviewed"],
        "loop": [
            {
                "stage": stage["stage"],
                "detail": stage.get("detail"),
                "claim": stage["claim"],
                "sources": stage.get("sources", []),
                "roles": stage.get("roles", []),
            }
            for stage in company["loop"]
        ],
        "questions": sorted(asked),
    }


def document(content: Content) -> dict[str, Any]:
    """The whole atlas as one JSON-ready document."""
    questions = [_question(content, question) for question in content.questions]
    return {
        "schema_version": SCHEMA_VERSION,
        "license": "Apache-2.0",
        "repository": "https://github.com/eiler2005/ai-interview-atlas",
        "markers": {
            "official": "✅ confirmed by the company",
            "participant_report": "🗣 first-hand candidate report",
            "secondary": "† prep guide or compilation without a first-hand source",
            "generated": "🧪 generated from published radar themes, not a reported question",
        },
        "counts": {
            "questions": len(questions),
            "answers": sum(1 for question in questions if question["answer"]),
            "themes": len(content.taxonomy["themes"]),
            "companies": len(content.companies),
            "sources": len(content.sources),
            "tracks": {
                track: sum(1 for question in questions if track in question["tracks"])
                for track in TRACKS
            },
        },
        "tracks": content.taxonomy["tracks"],
        "themes": content.taxonomy["themes"],
        "roles": content.taxonomy["roles"],
        "questions": sorted(questions, key=lambda question: question["id"]),
        "companies": [_company(content, company) for company in content.companies.values()],
        "sources": [_source(content, source) for source in sorted(content.sources)],
    }


def dumps(content: Content) -> str:
    """The export as text: stable key order, real Unicode, one trailing newline."""
    return json.dumps(document(content), ensure_ascii=False, indent=2, sort_keys=False) + "\n"
