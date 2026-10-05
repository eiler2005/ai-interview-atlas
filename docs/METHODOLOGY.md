# Methodology

[English](METHODOLOGY.md) · [Русский](ru/METHODOLOGY.md) · [AI Interview Atlas](../README.md)

The atlas collects what is publicly known about interviews for AI engineering and AI leadership roles and shows how well each claim is supported. It does not contain leaked or confidential material.

## Tracks and roles

- **AI Engineering:** AI/LLM engineers, applied AI engineers, forward deployed engineers, AI solutions architects, agent engineers, AI evaluation engineers, AI platform and MLOps engineers, inference and performance engineers, research engineers, and ML engineers and data scientists where a company's evidence concerns them.
- **AI Leadership:** AI product managers, directors and heads of product, engineering managers, directors and heads of engineering, technical program managers, AI platform leads, heads of AI adoption, deployment strategists, forward-deployed and solutions leaders.

A question can belong to both tracks. The same topic is asked differently: an engineer implements an evaluation harness, a leader designs the release policy that uses it.

The [AI roles guide](AI_ROLES.md) groups these roles into six families, each with a page. A question appears there as *reported for these roles* only when its source names the role; a role tag without such a source is an editorial choice for practice. Likewise a company loop stage is shown on a role page only when its source reports it for that role.

Company pages may also include general software-engineering, product-management, Director or TPM interview baselines, explicitly labelled as such. A general-role guide does not establish a specialist AI loop. Separate documents from one publisher count as separate sources, not independent corroboration; translated copies and mirrors do not add another source.

## Sources

Every source records the page, its publisher, the publication date when known and the date it was read (`retrieved`).

Most reported questions currently rely on secondary preparation material, with many drawn from one compilation. The home page shows these counts separately from generated practice questions. This is a preparation collection with visible evidence limits, not a verified inventory of questions used by employers. Adding a paper or technical document to a question's reading improves its learning support; it does not upgrade the interview-evidence marker or corroborate a company attribution.

| Kind | What it is | How it is used |
| --- | --- | --- |
| Company source | The employer's own careers pages, interview guides, engineering blogs and official talks | Confirms loop stages and coding requirements; strongest evidence for a question |
| Candidate report | A first-hand account by someone who interviewed, or by an interviewer or hiring manager describing their own interviews: blog post, public forum post, talk | Supports loop stages and questions, with the date the interview took place when reported |
| Preparation guide | A third-party guide describing a company's process | Shown as secondary; never presented as first-hand |
| Compilation | A list of questions compiled by others without a source per question | Paraphrased with attribution and shown as secondary (†) |
| Reference | Papers, documentation and standards | Reading material for answers only; never evidence that a question was asked |
| Job posting | An employer's description of an open role | Describes what a role involves on a role page; never evidence of an interview stage or question |

We read sources without logging in, bypassing a CAPTCHA or scraping against a site's terms. We skip accounts from people who say they were under a non-disclosure agreement, including the rest of an account whose author withholds questions for that reason. We do not use programmatically generated "interview guide" sites that repeat one template across many employers and give statistics without a source. An official page from an archived or long-unchanged repository keeps its original date, and the page notes its age. Questions and loop descriptions are paraphrased; a source is quoted by at most one short sentence.

## Markers

- ✅ confirmed by the company;
- 🗣 candidate report;
- † preparation guide or compilation without a first-hand source;
- 🧪 generated: a practice question written from a theme that job postings demand, not a question anyone reported;
- ❔ assumption: a loop stage we expect but could not source; it is shown so that the gap is visible.

"Asked at" lists every company with evidence for a question and uses the strongest marker available for that company. A compilation tag alone is weak evidence: treat † as a hint to verify, not as a fact.

## Questions and answers

Each question states what it tests, lists what a strong answer covers and provides reading. Priority questions have a written answer. These outlines are checklists grounded in primary material where reading is listed, not scripts; interviewers reward your own reasoning and your real examples. Numbers in outlines come from the cited reading or are marked as estimates.

Coding appears only where a company source or candidate reports show that the loop includes it. Leadership candidates should read the practical coding questions anyway: many loops ask them to review or reason about such code.

## Requirements radar

The radar counts how many job postings in a sample ask for each theme. The sample consists of public, full-text postings for senior product, engineering and programme roles, collected from employer career boards and job boards during one job search and deduplicated by employer and title. The track comes from the job title, with content checks to exclude functions outside scope. A leadership title includes senior product individual contributors and does not by itself establish people management. Design, marketing, sales and similar functions are excluded. It is not a representative market survey: it leans towards international fintech and business software. Collection dates are not proof that a vacancy remains open.

A model reads responsibilities and requirements against written theme criteria and retains a short evidence phrase for each marked theme. In this edition, Claude Sonnet 5 classified the first 60 postings; GPT Astra completed the remaining batch and checked a reproducible random sample of eight retained postings plus flagged ambiguous cases against full text. The final sample contains 79 postings. Original classifications, corrections, source hashes and actual author/reviewer identities are retained privately. Author checks and independent review are recorded separately; self-checking is not independent review.

A posting counts once per theme, including explicitly requested optional experience. Theme demand and current AI ownership are different measures: a role may request prior AI experience without explicitly owning AI work. The ownership count requires an explicit remit for AI/ML products, features, models, teams or infrastructure; personal AI-tool use and company boilerplate do not qualify. Conservative exclusions resolve ambiguous ownership. These judgments remain subject to sampling and classification error.

Only aggregates are published: no employer names, job titles, quotes, links or identifiers. A theme is shown for a track only when at least five postings mention it and the track has at least twenty postings, so a track with a thin sample is left out rather than guessed.

## Content expansion of 2026-10-05

The current edition contains 299 questions with EN/RU checklists and reading, and 158 priority questions with EN/RU answers: 82 Engineering and 76 Leadership priorities. Five new Leadership scenarios are explicitly generated from eligible radar themes, with editorial role authority and no employer attribution. The original priorities retain their order. New and revised public content in this iteration was authored by actual GPT-6 Astra; the radar's earlier author history above is unchanged.

Coverage audits retain their baseline counts and source-check results separately from current-content addenda. A semantic review checks whether the prompt, type, outline, answer and role scope agree. A source check separately compares the prompt with readable source content. Adding reading, an explanation or an official general-role process cannot upgrade an unrelated question's evidence. Official role-family pages support interview stages only where an actual hiring-process section says so; responsibilities alone remain role information. Behavioural answers coach truthful experience, while hypothetical answers explain a proposed decision.

A failed access attempt is recorded as unavailable and does not advance the last successful retrieval date. A redirect to the same readable document may support a new retrieval date without changing its kind or treating the mirror as independent corroboration. Publication dates, page updates, interview dates and retrieval dates are distinct.

## Freshness and review

Interview loops change. Each company page records the date of its source check, not a guarantee that every team follows that process today. Historical evidence stays labelled with its period. The publication workflow requires frontier-model authorship, an independent review in a separate session from every author/editor, and a maintainer publication decision. A local draft or recorded check does not establish approval or publication. If something is wrong or outdated, open an issue with a dated public source. See [attribution](ATTRIBUTION.md) for upstream material and licensing.
