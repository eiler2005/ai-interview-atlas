"""The documentation site: navigation built from the content, and links kept inside the site.

The site is built by MkDocs from `docs/`. Its menu comes from the taxonomy and the company
files, so it never drifts from the generated pages. Links that leave `docs/` (the README,
CONTRIBUTING, the changelog, the licence) point at GitHub, except the two READMEs, whose
place on the site is taken by the map of the atlas.
"""

from __future__ import annotations

import posixpath
import re
from urllib.parse import urlsplit

from .content import TRACKS, Content
from .render import (
    LABELS,
    LANGS,
    REPO,
    SEGMENTS,
    Renderer,
    answers_page,
    base,
    common_page,
    company_page,
    hub_page,
    methodology_page,
    radar_page,
    reference_name,
    sources_page,
    start_page,
    theme_page,
)

DOCS = "docs"
BRANCH = "main"
TAB = {"en": None, "ru": "Русский"}
LINK = re.compile(r"(\]\()([^)\s]+)((?:\s+\"[^\"]*\")?\))")
NESTED = re.compile(r"^((?:  )+)(?=(?:[-*+]|\d+\.) )")
FENCE = re.compile(r"^\s*(```|~~~)")


def in_docs(path: str) -> str:
    """A repository path as MkDocs sees it, relative to `docs/`."""
    return posixpath.relpath(path, DOCS)


def section(lang: str, renderer: Renderer) -> list[dict]:
    """The menu for one language: map, tracks, answers, themes, companies, reference."""
    labels, content = LABELS[lang], renderer.content
    names = {track: renderer.track_names[track][lang] for track in TRACKS}
    menu: list[dict] = [{labels["map"]: in_docs(hub_page(lang))}]
    start = [{names[t]: in_docs(start_page(lang, t))} for t in TRACKS]
    start.append({reference_name(lang, "learning_path"): in_docs(f"{base(lang)}/LEARNING_PATH.md")})
    menu.append({labels["start_name"]: start})
    answered = [t for t in TRACKS if renderer.answered(lang, t)]
    if answered:
        menu.append(
            {labels["answers_name"]: [{names[t]: in_docs(answers_page(lang, t))} for t in answered]}
        )
    menu.append(
        {
            labels["themes"]: [
                {theme["name"][lang]: in_docs(theme_page(lang, theme["id"]))}
                for theme in content.taxonomy["themes"]
            ]
        }
    )
    if content.companies:
        companies = []
        for segment in SEGMENTS:
            chosen = [c for c in renderer.companies_in_order(lang) if c["segment"] == segment]
            if chosen:
                companies.append(
                    {
                        labels["segments"][segment]: [
                            {c["name"][lang]: in_docs(company_page(lang, c["id"]))} for c in chosen
                        ]
                    }
                )
        menu.append({labels["companies"]: companies})
    reference = []
    if renderer.common():
        reference.append({labels["common"]: in_docs(common_page(lang))})
    if content.radar:
        reference.append({labels["radar_title"]: in_docs(radar_page(lang))})
    reference += [
        {reference_name(lang, "methodology"): in_docs(methodology_page(lang))},
        {reference_name(lang, "sources"): in_docs(sources_page(lang))},
        {reference_name(lang, "attribution"): in_docs(f"{base(lang)}/ATTRIBUTION.md")},
        {reference_name(lang, "roadmap"): in_docs(f"{base(lang)}/ROADMAP.md")},
    ]
    if lang == "ru":
        # English keeps its changelog at the repository root, outside the site.
        reference.append({reference_name(lang, "changelog"): "ru/CHANGELOG.md"})
    menu.append({labels["reference"]: reference})
    return menu


def nav(content: Content) -> list[dict]:
    """English at the top level; every other language in its own tab."""
    renderer = Renderer(content)
    menu = section("en", renderer)
    for lang in LANGS:
        if TAB[lang]:
            menu.append({TAB[lang]: section(lang, renderer)})
    return menu


def rewrite_links(markdown: str, page: str) -> str:
    """Point links that leave `docs/` at the map of the atlas or at GitHub.

    `page` is the page's path relative to `docs/`, as MkDocs reports it.
    """
    folder = posixpath.dirname(posixpath.join(DOCS, page))

    def replace(match: re.Match) -> str:
        opening, target, closing = match.groups()
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            return match.group(0)
        resolved = posixpath.normpath(posixpath.join(folder, parts.path))
        if resolved == DOCS or resolved.startswith(DOCS + "/"):
            return match.group(0)
        fragment = f"#{parts.fragment}" if parts.fragment else ""
        home = {"README.md": hub_page("en"), "README.ru.md": hub_page("ru")}.get(resolved)
        if home:
            new = posixpath.relpath(home, folder) + fragment
        else:
            new = f"{REPO}/blob/{BRANCH}/{resolved}{fragment}"
        return f"{opening}{new}{closing}"

    return LINK.sub(replace, markdown)


def nest_lists(markdown: str) -> str:
    """Indent nested list items by four spaces per level instead of two.

    The pages use two spaces, which GitHub renders as nesting; Python-Markdown needs four.
    """
    lines, fenced = [], False
    for line in markdown.split("\n"):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced:
            line = NESTED.sub(lambda m: m.group(1) * 2, line)
        lines.append(line)
    return "\n".join(lines)
