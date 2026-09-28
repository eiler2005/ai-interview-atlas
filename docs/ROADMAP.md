# Roadmap

[English](ROADMAP.md) · [Русский](ru/ROADMAP.md) · [AI Interview Atlas](../README.md)

What this repository plans to improve next, and what it will not do. This is the project's development roadmap, not a personal interview-preparation schedule; for practice, start with either track's *Start here* page. There are no delivery dates here on purpose: an item moves when the evidence for it exists, not when a calendar says it should.

## Where the atlas is today

As of 2026-09-28:

- 255 questions across 17 themes, each saying what it tests, split between the engineering and the leadership track.
- 80 priority questions — 40 per track — each with an answer checklist, reading and a written answer in English and Russian. All 160 answer texts have passed independent content review.
- 20 company pages showing sourced loop stages, coding requirements and reported questions where evidence exists. Some describe general software or product roles rather than specialist AI roles; secondary evidence and assumptions remain visible.
- 108 sources, recording when each was read and its publication date when known.
- A requirements radar over 79 job postings from September 2026.
- A PDF builder for the main books and separate answers editions. New local builds are not released assets: the [releases page](https://github.com/eiler2005/ai-interview-atlas/releases/latest) lists what has actually been published.

The contribution workflow requires schema and provenance validation, language and link checks, and privacy checks with distinct worktree, index and history scopes. These checks do not establish factual accuracy or publication approval. The written answers have passed independent content review, and the four local PDF books have completed production checks of extracted text and every rendered page. Publication remains a separate decision.

## Next

- **Independent content review and PDF production checks.** *Done for this edition.* A separate session reviewed all 80 answers in each language for factual accuracy, agreement with the checklists and language quality. All four local books also passed text and visual production checks. These are distinct checks; neither publishes a release. Answers remain examples of good reasoning, not reference answers.
- **Checklists beyond the priority set.** *Planned.* Today only the priority questions say what a strong answer covers. The rest give the question and what it tests, which is enough to practise with but less than the project should offer.
- **Better company evidence and more companies.** *Planned.* Seek independent corroboration and specialist AI evidence where current pages have only general-role baselines or limited public evidence. The current 20 are not a ranking and have not all cleared a two-independent-source threshold. As the [methodology](METHODOLOGY.md) explains, each claim carries its own evidence marker; two documents from one publisher do not count as independent corroboration.
- **Source freshness.** *Planned.* A scheduled job that checks every cited URL still resolves, and a visible mark on company pages whose review date is more than twelve months old. Interview loops change, and a page that quietly ages is worse than one that admits it.

## After that

- **Written answers beyond the priority set**, starting with the themes the radar shows employers ask for most.
- **A refreshed radar** on a newer and larger sample. The engineering track is suppressed today because 17 postings is below the minimum of 20 the method requires; a larger sample would publish it.
- **Filtering by level and role** — junior, senior, staff, manager, director — but only where the sources actually say which level a question was asked at. Guessing would defeat the point of the provenance model.

## Later, if there is demand

- A third language, with the necessary schema, renderer and validation changes as well as translation.
- A machine-readable export of the question bank for practice tools, so the questions can be drilled somewhere other than a Markdown page.

## What this project will not do

- **No confidential or NDA material, and nothing described as leaked.** Everything here comes from public sources, and a report from someone who says they were under an agreement is not used.
- **No unattributed interview claims.** A question is either backed by a public source with a recorded reading date and publication date when known, or marked as generated from published radar themes. The marker is visible on the page; a reading date does not establish when an interview happened.
- **No answers that are a link to a paid course.** The answer is on the page.
- **No scraping behind login walls, CAPTCHA or against a site's terms.**
- **No personal data.** No candidate facts, CVs, private notes or company-attributed data from anyone's private job search. The radar is an anonymised aggregate with a minimum cell size, and it is the only private input.

## How to help

[CONTRIBUTING](../CONTRIBUTING.md) has the full process. The three most useful contributions right now:

1. A dated first-hand account of a loop stage that a company page currently marks as an assumption.
2. A correction to an answer or a checklist, with the source that shows it.
3. Wording fixes in either language — the English and the Russian are meant to say the same thing, and where they do not, that is a bug.
