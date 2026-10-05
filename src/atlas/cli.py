"""Build the generated pages, or check that content, pages and links are consistent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import export, links
from .content import ContentError, load
from .render import render

# Folders the build owns entirely, and the files it owns in each. Anything matching that
# is on disk but not in the current output is left over from older content: a removed
# company, a theme that lost its last question, or a figure whose source file is gone.
GENERATED_DIRS = (
    ("docs/themes", "*.md"),
    ("docs/companies", "*.md"),
    ("docs/answers", "*.md"),
    ("docs/start", "*.md"),
    ("docs/roles", "*.md"),
    ("docs/assets", "*.svg"),
    ("docs/ru/themes", "*.md"),
    ("docs/ru/companies", "*.md"),
    ("docs/ru/answers", "*.md"),
    ("docs/ru/start", "*.md"),
    ("docs/ru/roles", "*.md"),
)


def stale_files(root: Path, pages: dict[str, str]) -> list[str]:
    """Generated files on disk that the current content no longer produces."""
    found = []
    for folder, pattern in GENERATED_DIRS:
        for path in sorted((root / folder).glob(pattern)):
            name = path.relative_to(root).as_posix()
            if name not in pages:
                found.append(name)
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--check", action="store_true", help="fail instead of writing")
    parser.add_argument(
        "--export",
        type=Path,
        metavar="PATH",
        help="also write the question bank as JSON, for practice tools",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        content = load(root / "src" / "content")
    except ContentError as error:
        print(f"Content errors ({len(error.problems)}):", file=sys.stderr)
        for problem in error.problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    if args.export:
        args.export.parent.mkdir(parents=True, exist_ok=True)
        args.export.write_text(export.dumps(content), encoding="utf-8")
        print(f"Exported {len(content.questions)} questions to {args.export}")
    pages = render(content)
    if args.check:
        problems = [
            f"out of date: {name}"
            for name, text in pages.items()
            if not (root / name).is_file() or (root / name).read_text(encoding="utf-8") != text
        ]
        problems += [f"stale generated page: {name}" for name in stale_files(root, pages)]
        problems += links.check(root, pages)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        print(f"Atlas check: {'failed' if problems else 'passed'} ({len(problems)} problems)")
        return 1 if problems else 0
    for name, text in pages.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
    for name in stale_files(root, pages):
        (root / name).unlink()
    problems = links.check(root)
    for problem in problems:
        print(f"- {problem}", file=sys.stderr)
    tracks = {
        t: sum(t in q["tracks"] for q in content.questions) for t in ("engineering", "leadership")
    }
    print(
        f"Built {len(pages)} files: {len(content.questions)} questions {tracks}, "
        f"{len(content.companies)} companies, {len(content.sources)} sources"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
