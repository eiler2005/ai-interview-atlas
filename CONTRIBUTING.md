# Contributing

[English](CONTRIBUTING.md) · [Русский](CONTRIBUTING.ru.md)

Corrections and new questions are welcome when they come with a dated public source. Read the [methodology](docs/METHODOLOGY.md) first.

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
```

Maintainers also run the [Career Copilot](https://github.com/eiler2005/career-copilot) privacy checker with a private dictionary and Gitleaks. With both projects checked out side by side:

```sh
git config --local core.hooksPath .githooks
git config --local ajh.privateDictionary /absolute/private/privacy-dictionary.json
uv run --project ../app ajh privacy check --root . --scope worktree --gitleaks
```

The hooks repeat the check for the exact staged files and for the full history before a push. Stage explicit paths and never bypass the hooks.
