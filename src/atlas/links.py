"""Check local Markdown links, anchors and English/Russian page pairs offline."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\n]*?)\)")


def without_fences(text: str) -> str:
    return re.sub(r"(?ms)^\s*(```|~~~).*?^\s*\1\s*$", "", text)


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<(?:a|[a-z][\w]*)[^>]+(?:id|name)=["\']([^"\']+)', text))
    seen: dict[str, int] = {}
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", without_fences(text)):
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        occurrence = seen.get(slug, 0)
        seen[slug] = occurrence + 1
        result.add(slug + (f"-{occurrence}" if occurrence else ""))
    return result


def check(root: Path, pages: dict[str, str] | None = None) -> list[str]:
    """Links in `pages` (path -> text) and in hand-written Markdown under `root`."""
    texts = dict(pages or {})
    for path in sorted(root.glob("*.md")) + sorted((root / "docs").rglob("*.md")):
        texts.setdefault(str(path.relative_to(root)), path.read_text(encoding="utf-8"))
    errors = []
    for name, text in sorted(texts.items()):
        if not name.endswith(".md"):
            continue
        source = root / name
        for raw in LINK.findall(without_fences(text)):
            target = raw.strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not (parsed.path or parsed.fragment):
                continue
            destination = (source.parent / unquote(parsed.path)) if parsed.path else source
            relative = (
                destination.resolve().relative_to(root.resolve()).as_posix()
                if (destination.resolve().is_relative_to(root.resolve()))
                else None
            )
            if relative is None:
                errors.append(f"{name}: link leaves the repository: {target}")
                continue
            exists = relative in texts or destination.exists()
            if not exists:
                errors.append(f"{name}: missing {target}")
            elif parsed.fragment and relative.endswith(".md"):
                body = texts.get(relative) or destination.read_text(encoding="utf-8")
                if unquote(parsed.fragment) not in anchors(body):
                    errors.append(f"{name}: missing anchor {target}")
    names = {name for name in texts if name.endswith(".md")}
    names |= {str(p.relative_to(root)) for p in (root / "docs").rglob("*.md")}
    for name in sorted(names):
        english = name.startswith("docs/") and not name.startswith("docs/ru/")
        if english and "docs/ru/" + name.removeprefix("docs/") not in names:
            errors.append(f"Missing Russian page for {name}")
    for name in ("README.ru.md", "CONTRIBUTING.ru.md"):
        if name not in names and not (root / name).is_file():
            errors.append(f"Missing Russian page {name}")
    return errors
