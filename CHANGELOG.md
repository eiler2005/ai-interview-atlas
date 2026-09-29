# Changelog

[English](CHANGELOG.md) · [Русский](docs/ru/CHANGELOG.md)

## Unreleased — 2026-09-29 navigation, site and repository

### Added
- Every question has a stable anchor on its theme page. Start pages, answers, company pages and *Asked across companies* link each question to that entry, and a priority question also to its written answer.
- A generated map of the atlas (`docs/README.md`, `docs/ru/README.md`): tracks, themes, companies by segment and reference pages in one place. The README opens with a one-line menu.
- Answers pages open with contents grouped by theme; each answer links back to its checklist and to the contents. Theme and company pages have a breadcrumb to their section of the map and links to the previous and next page; company pages, and theme pages with more than one track section, have an *On this page* line.
- A searchable site built with MkDocs Material from the same pages, with an English menu and a Russian tab. The menu is built from the content, and the strict build fails if a page is missing from it. Deployment to GitHub Pages stays off until the maintainer enables it.
- Issue forms for proposing a question, reporting a correction and reporting an outdated source; every question on a theme page links to the correction form with its id filled in. A pull request template, code owners, a security policy and a code of conduct.
- A weekly source-freshness job that checks that cited URLs still resolve (sites that block automated checks are skipped) and keeps one issue listing the failures, and a release workflow that builds the PDF books into a draft release for the maintainer to inspect and publish.

### Changed
- CI runs on pull requests and on pushes to `main` rather than on every push, so a pull-request branch is no longer checked twice; superseded pull-request runs are cancelled and every action is pinned to a commit. Dependabot proposes monthly updates for actions and Python dependencies.
- A company page no longer links to itself in *Asked at*.

## Unreleased — 2026-09-28 continuation

### Changed
- Added the project title and descriptive text to the README banner; updated its alt text and image attribution.
- Added a bilingual learning path with role-specific priorities, eight-week practice plans, diagnostic checks and evidence-based completion gates; the project roadmap remains separate.
- Added a bilingual repository roadmap, separate from a personal preparation plan, with explicit limits on company evidence and source freshness.
- Completed 80 English written answers alongside 80 Russian answers and corrected technical and translation issues. All 160 texts passed independent content review; all four local PDF books passed text and visual production checks. Local files do not establish a new release or maintainer approval.
- Added a primary Faiss reference for the comparison of exact search, HNSW and IVF-PQ; the catalogue now contains 108 sources.
- Automated checks complement factual review; worktree, index and history privacy checks have distinct scopes.

## 2026-09-28 — A README that explains itself

### Changed
- The README is a landing page: what this is, who it is for, what is inside, why it differs from the usual question lists, and how to start in three steps. It is 103 lines instead of 322.
- The priority questions of each track moved to `docs/{lang}/start/{track}.md`, and the questions asked at two or more companies to `docs/{lang}/common.md`. Both are linked from the README, and a track's start page links its answers.
- Both PDF books open with the same summary as the README.

## 2026-09-28 — Written answers, in Russian first

### Added
- Written answers for 80 priority questions, 40 per track: one paragraph of 100-150 words that a candidate could say aloud — the point, the mechanism and its trade-off, what to do or measure, and where the answer stops holding. Each answer is presented as one good answer, not the reference answer.
- For `behavioral` and `self_presentation` questions an answer describes how to build your own account and what the interviewer is listening for; no invented stories, companies or numbers.
- Answers live in the `answer` field of the same content files and are rendered to separate pages (`docs/ru/answers/`) and a separate PDF edition, so the question pages and the main book stay unchanged for a first pass at answering yourself. PDF pagination depends on the build; local editions are not necessarily released assets.
- Answers start in one language: pages and the answers book for a language appear only once that language has answers. English answers follow in a later wave.

## 2026-09-28 — Printable PDF books

### Added
- `scripts/build_pdf.py` builds one PDF book per language from the same content with the Career Copilot document renderer: A4 pages, 12 pt body text, a contents page whose page numbers are checked against the rendered bookmarks, and clickable source links. The parts are the *Start here* questions for each track, every theme, company loops, the requirements radar with its chart, the methodology, attribution and sources.
- Answer checklists are printed once, in *Start here*; theme parts point to them by number. Emoji markers are printed as font glyphs (● confirmed by the company, ○ candidate report, † secondary, ‡ generated, ? assumption), and the build stops if the font lacks any character. Books, their Markdown sources and hash manifests are written to the ignored `dist/pdf/`.

## 2026-09-27 — First edition

### Added
- 255 bilingual questions across 17 themes: 191 in AI Engineering and 146 in AI Leadership, with overlap between tracks. Each track has 40 starting questions with answer outlines and reading.
- 20 company pages with sourced interview-loop claims, coding requirements and clearly labelled general-role baselines where specialist AI evidence is unavailable.
- 107 source records: 21 official sources, 9 participant reports, 17 preparation guides, 1 secondary compilation and 59 references. Of the questions, 245 cite interview sources and 10 are labelled as practice generated from published radar themes. References support reading, not claims that a question was asked.
- An aggregate requirements radar from 79 postings collected in September 2026: 62 leadership and 17 engineering. Only leadership theme counts are published; engineering is below the minimum track size of 20, and cells below five postings are suppressed.
- Content schema for tracks, roles, themes, sources, companies, questions and the requirements radar, with provenance rules enforced at build time.
- Generator for bilingual README, theme, company, radar and source pages plus a static radar SVG; `--check` fails on stale pages, broken local links and missing Russian pages.
- Methodology, attribution and contribution guides in English and Russian; privacy hooks and CI that reuse the Career Copilot checker and Gitleaks.

### Limits
- Preparation guides and compilation tags remain secondary evidence, not first-hand confirmation. General software or product interview guides do not establish an AI-specific loop; source-check dates do not guarantee a current process for every team.
- The radar is a small, nonrepresentative sample weighted towards international fintech and business software. It measures requirements in retained postings, not current hiring availability or the whole market. Only anonymised aggregates are published.
