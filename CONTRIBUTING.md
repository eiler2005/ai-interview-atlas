# Contributing

[English](CONTRIBUTING.md) · [Русский](CONTRIBUTING.ru.md)

Corrections and new questions are welcome when they come with a dated public source. Read the [methodology](docs/METHODOLOGY.md) first.

## Report something

You do not need to edit YAML to help. Open an issue with one of the forms:

- **Propose a question**: the question, what it tests, and the dated public source that reports it.
- **Report a correction**: every question on a theme page has a *Suggest a fix* link that opens this form with the question's id filled in.
- **Report an outdated or broken source**: a dead link, or a page whose content or process has changed.

Personal data or confidential material that reached the repository is a privacy issue, not a normal bug: follow [SECURITY.md](SECURITY.md) and do not repeat it in a public issue.

## Add or correct content

1. Add the source to `src/content/sources.yaml`: `id`, `kind`, `title`, `publisher`, `url`, `retrieved` (the date you read it), `lang`, plus `published` when known and `license` for a reused compilation.
2. Add a question to `src/content/questions/<theme>.yaml`, or a loop stage to `src/content/companies/<company>.yaml`. Write in your own words and fill both `en` and `ru`.
3. Mark provenance honestly. A `published` question cites the source that reports it, with `company` when the report names one. A `generated` question cites only `radar:<theme>`. A loop stage is `confirmed` only by a company source, `participant_report` only by a first-hand account, `secondary` by a guide or compilation, and `assumption` when there is no source.
4. Run `uv run python scripts/build.py` to regenerate the README and pages. Do not edit generated files by hand.

Quote every YAML string and use block style for long text. Dates are ISO strings (`"2026-09-27"`, `"2026-09"` or `"2026"`).

## What we cannot accept

- Material behind a login, paywall bypass or CAPTCHA, or content scraped against a site's terms.
- Questions from anyone who says they were under a non-disclosure agreement.
- Personal data: contact details, private paths, private channel links, CV text or anything that identifies a candidate.
- Answers that only link to a paid course.

## Checks

```sh
uv sync
uv run ruff check . && uv run ruff format --check .
uv run pytest -q
uv run python scripts/build.py --check
# when docs/, scripts/ or src/atlas change:
uv run --group site mkdocs build --strict -f scripts/mkdocs.yml
```

Maintainers also run a publication check: the path allowlist, content rules and [Gitleaks](https://github.com/gitleaks/gitleaks), plus a private dictionary of strings that must never appear here. The checker is the [Career Copilot](https://github.com/eiler2005/career-copilot) CLI, used from this repository without checking that project out:

```sh
git config --local core.hooksPath .githooks
git config --local ajh.privateDictionary /absolute/path/to/privacy-dictionary.json
uvx --from "git+https://github.com/eiler2005/career-copilot@fac2dd3c3545c97b07fdb47fddb717f7db732a60" \
  ajh privacy check --root . --scope worktree --gitleaks
```

Set `ATLAS_PRIVACY_APP` to a local checkout of that project to use it instead. The hooks repeat the check for the exact staged files and for the full history before a push. Stage explicit paths and never bypass the hooks.

## Answers

A `start_here` question may carry a written answer:

```yaml
    answer:
      ru: "One paragraph of 100-150 words."
```

Write one paragraph a candidate could say aloud: the point first, then the mechanism and what it costs, then what you would do or measure, then where the answer stops holding. It must agree with that question's `tests` line and its three-bullet `outline`, which it turns into speech. Ground it in the cited `reading`; use no invented numbers, benchmarks or company facts. Standard formulas are fine.

For `behavioral` and `self_presentation` questions, never write a story. Describe how the candidate builds their own answer, what the interviewer is actually listening for, the usual mistake and how to close. An answer that reads like a ready-made anecdote will be rejected.

A language may be added first and the other later: `answers` pages and the answers book for a language appear only once that language has answers. Keep the text plain, without Markdown or line breaks.

## Preview the site

The same pages can be published as a searchable site with an English and a Russian menu; deployment to GitHub Pages stays off until the maintainer enables it. MkDocs builds it from `docs/` with the configuration in `scripts/mkdocs.yml`; `scripts/mkdocs_hooks.py` builds the menu from `src/content` and points links that leave `docs/` at the map of the atlas or at GitHub, so there is no menu to maintain by hand.

```sh
uv sync --group site
uv run --group site mkdocs serve -f scripts/mkdocs.yml            # http://127.0.0.1:8000/ai-interview-atlas/
uv run --group site mkdocs build --strict -f scripts/mkdocs.yml   # into build/site, as CI runs it
```

## Printable PDF books

The same content can be printed as one book per language. The books use the [Career Copilot](https://github.com/eiler2005/career-copilot) document renderer pinned in `pyproject.toml` and its standard layout: A4 pages, 12 pt body text, a contents page, PDF bookmarks and clickable source links.

```sh
uv sync --group pdf
uv run --group pdf python scripts/build_pdf.py
```

The books, their Markdown sources and hash manifests are written to `dist/pdf/`. The build needs a Unicode TTF font: Arial on macOS, DejaVu Sans on Linux, or `--font PATH`. It stops if the font lacks any character. The radar chart is included when `rsvg-convert` is installed. Before sharing a book, check its extracted text and look at every page (`pdftotext`, `pdftoppm`). PDFs are release files: never commit them.
