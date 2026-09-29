## Summary

<!-- What does this PR change, and why? Link the issue it addresses, if any. -->

## Checklist

- [ ] Sources are public and dated in `src/content/sources.yaml`.
- [ ] Both `en` and `ru` are filled in, or the answer-language exception is noted (see CONTRIBUTING.md).
- [ ] Ran `uv run python scripts/build.py` and did not hand-edit generated files.
- [ ] Checks pass locally: `ruff check`, `ruff format --check`, `pytest`, `scripts/build.py --check`, and, when `docs/`, `scripts/` or `src/atlas` change, the strict site build (see CONTRIBUTING.md).
- [ ] No personal data, NDA material or login-walled content is included.
- [ ] Markers (`published`/`generated`; `confirmed`/`participant_report`/`secondary`/`assumption`) reflect the real source kind.
