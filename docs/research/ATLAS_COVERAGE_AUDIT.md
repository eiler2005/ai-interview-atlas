# Atlas coverage audit

[English](ATLAS_COVERAGE_AUDIT.md) · [Русский](../ru/research/ATLAS_COVERAGE_AUDIT.md) · [Learning roadmap](../LEARNING_ROADMAP.md) · [Expansion plan](../plans/ATLAS_EXPANSION.md)

Audit date: **2026-10-05**. Initial P0 question-bank snapshot: `6648af25ee5f04f1141b96a81900032af06a460d`. The Atlas has a broad technical and product preparation base. Its main learning gap is a sequence of observable work; its main evidence gap is independent, role-specific interview support, especially for Head/Director and AI TPM responsibilities. More questions alone would not resolve either gap.

The initial P0 phase added research and practice guidance inside the **two existing tracks**. Engineering gains two routes; Leadership gains four responsibility branches within one route. The existing [eight-week learning path](../LEARNING_PATH.md) is preserved. New curriculum drills are editorial exercises, separate from the published and radar-generated question bank. Adding those documents alone did not change the bank. The subsequent content phase is counted separately in the current addendum below.

## Scope and method

The initial audit combines a mechanical inventory of the YAML bank, source-bounded Engineering research and an individual semantic review of all Leadership-tagged questions. It distinguishes four questions: does relevant material exist; what work should a learner produce; what evidence supports the interview attribution; and what was freshly verified? A useful practice topic can have weak interview evidence, and a well-sourced question can still be insufficient preparation for a responsibility.

| Component | Work performed | Boundary |
| --- | --- | --- |
| Repository inventory | Counts, track overlap, answers, reading, evidence metadata and duplicate checks | Structural checks do not verify source claims or detect every semantic duplicate |
| Engineering | Existing route/theme/anchor review; Hello Interview inventory; competence-roadmap comparison; primary checks on contracts, evals and security | Not a fresh semantic or source audit of every Engineering question; Premium and unavailable bodies excluded |
| Leadership | All 155 prompts, tested competences and outlines reviewed for role/scope, evidence and learning support; 20-question source check | The 20 are a targeted diagnostic set, not a random accuracy sample; no claim that all 155 source attributions were freshly verified |
| Curriculum | Original drills, deliverables, failure cases, delayed retries and 0–3 gates | Workload and thresholds are editorial; no study validates interview outcomes or automated scores |

Detailed boundaries and direct citations are in [Engineering research](ENGINEERING_RESEARCH.md) and [Leadership audit](LEADERSHIP_AUDIT.md).

## Baseline counts and what they mean

| Measure at the snapshot | Count | Interpretation |
| --- | ---: | --- |
| Unique bank questions | 294 | 278 published-source entries and 16 radar-generated entries |
| Engineering / Leadership membership | 225 / 155 | 86 belong to both; track counts must not be added as unique questions |
| Themes / companies / role-family pages | 17 / 29 / 6 | Navigation and scope, not coverage or quality scores |
| Priority questions / written answers | 140 | 70 priorities per track; answers in both languages |
| Core source registry | 207 | YAML entries; document bibliographies are separate and do not inflate this total |
| Published questions with only secondary support | 230 of 278 | Attribution relies on preparation guides or compilations |
| Questions citing one shared compilation | 194 | Concentration limits independent corroboration |
| Leadership questions with answers | 89 | Includes 19 shared questions prioritised only for Engineering; not 89 Leadership priorities |
| Leadership with / without reading | 118 / 37 | All 155 have outlines; an outline is not a substitute for primary reading |

Within Leadership, 141 entries cite published sources and 14 are generated. Counting each question once by its evidence combination gives **116 supported only by secondary material, 23 by participant reports and 2 by official material**. The official examples concern general PM and Senior Staff+ IC interviews; they do not establish direct Head/Director interview coverage. The shared compilation appears on 85 Leadership questions. Separate pages from one publisher and translated copies are not independent corroboration. See the [methodology](../METHODOLOGY.md).

Normalised question-text and source-URL checks found no exact duplicate groups in the audit, and the configured text-similarity scan found no candidate pairs above its 0.82 threshold in the Leadership review set. This narrow result does not rule out conceptual overlap.

## Coverage decisions

“Usable” here means material supports a preparation task, not that a learner has mastered it or that a company asks it. The matrices in the linked reports identify exact anchors and evidence limits.

| Area | Existing strengths | Gap and decision |
| --- | --- | --- |
| AI-assisted coding | [Build](../themes/coding-practical.md#code-ai-assisted-build), [review](../themes/coding-practical.md#code-agent-pr-review), [session choices](../themes/coding-practical.md#code-agent-session-choices), [ownership](../themes/coding-practical.md#code-ai-assisted-ownership) and restricted [product-structure work](../themes/coding-practical.md#code-product-structure) | Add a four-week sequence with bounded changes, independent probes and defence; do not universalise AI permission |
| Algorithm judgement | Existing practical coding, cache and performance questions | Add seven-family applicability/limit/counterexample guidance with original examples and public reading; no paid-problem reconstruction |
| Applied AI service lifecycle | Strong breadth across fundamentals, retrieval, evals, agents, cost and security | Add an eight-week route that keeps one small service, baseline and failure contract throughout; preserve broader foundations |
| Product leadership | Discovery, AI/no-AI choice, metrics, trust and economics | Require a decision memo, experiment analysis and launch/stop criteria; titles alone do not define scope |
| EM / Platform | Technical review, reliability and first-line people-management material | Add observable review/calibration, capacity and ownership work; generated SDLC/hiring prompts remain generated |
| Head / Director | Useful precursors in prioritisation, cost and organisation questions | Direct multi-initiative budget practice is missing; add explicitly editorial portfolio, build/buy and management-through-managers cases; seek direct interview evidence later |
| TPM / Delivery | Dependency, uncertainty and readiness scenarios | Practise re-planning and operational ownership; distinguish generated work and PM/EM transfer from specialist AI TPM evidence |

## Findings that remain open

The [Leadership source check](LEADERSHIP_AUDIT.md) found three Google EM prompts whose bank versions adapt the source scenario or response mode. A hypothetical case should not silently become a demand for a real past example. The initial audit recorded the difference; the subsequent content phase corrected the YAML while preserving IDs. One Meta EM account was unavailable during the check and received no new verification. The official Senior Staff+ source is IC evidence even when its practice topic helps managers.

Engineering research inventoried 30 Hello Interview entries, inspected accessible material on 28, and excluded two unavailable article bodies. Seven pattern pages and thirteen problem breakdowns expose a Premium continuation; full paid content was not analysed. The unsourced competence-map PDF is one overlapping map, not an independent confirming source. Technical checks informed the route's distinctions between schema and meaning, deterministic checks and variable outcomes, input filtering and authorisation, and protocol and trust. See the [source register](ENGINEERING_RESEARCH.md#source-register-for-this-report).

The radar is also limited: its 79-posting sample contains only 17 Engineering postings, below the publication minimum of 20, and the Leadership sample is concentrated in particular sectors. It should not determine universal study-time weights or substitute for direct role evidence. No private research identifiers or source material are added to this audit.

## Current content addendum — 2026-10-05

The authorised content phase is implemented in the working tree after the initial P0 snapshot. The historical counts and the original 155-question/20-source-check scope above are retained; they are not claims about a fresh audit of every current attribution.

| Current measure | Count | Change from initial snapshot |
| --- | ---: | --- |
| Unique questions | 299 | +5 radar-generated Leadership questions; 278 published and 21 generated overall |
| Engineering / Leadership membership | 225 / 160 | Still 86 shared; no new formal Engineering question |
| Engineering / Leadership priorities | 82 / 76 | +12 / +6; original IDs and priorities preserved |
| Unique questions with EN/RU answers | 158 | +18; 110 Engineering and 97 Leadership answer-bearing entries overlap |
| Questions with reading | 299 | Every current question has reading; source fit matters more than link count |
| Core source registry | 247 | +40 registered sources; bibliography links alone still do not count |

Engineering strengthened the five existing AI-assisted coding entries, filled 30 missing-reading entries across its ten technical themes and added 12 answers on coding ownership, bounded context, contracts, evaluation, recovery and retrieval. Its two routes now require explanations, counterexamples and checklists, with seven algorithm families and eight production modules. Leadership corrected the three source adaptations, added five explicitly generated questions and six answers, filled its remaining reading gaps and expanded the four-branch case guidance. See the [Leadership content addendum](LEADERSHIP_AUDIT.md) for its evidence checks and limits.

Technical references improve learning support; they do not upgrade published interview evidence. Editorial case questions remain outside the bank unless they separately satisfy its provenance rules. The Meta report remains unavailable, direct Head/Director and AI TPM corroboration remains limited, and the Engineering radar still cannot support generated questions under the publication threshold.

Python exercises, executable labs, production-project implementation and an AI evaluator are deferred by the maintainer. The content is implemented locally; independent final review, repository validation and any publication decision are separate statuses. These counts describe the content update, not a release or an empirical validation of learner proficiency.

## What this iteration delivers

The [learning roadmap](../LEARNING_ROADMAP.md) directs readers to the existing baseline or one of three focused routes. The route documents specify prerequisites, weekly outputs, independent checks, delayed retries and failure conditions. The [expansion plan](../plans/ATLAS_EXPANSION.md) records implemented content, unresolved interview evidence and implementation deferred by the maintainer.

A draft, a passing site build and an independent content review are different statuses. Repository validation checks structure; independent review checks the new prose and decisions; publication remains a separate maintainer decision. This report does not retroactively extend earlier answer reviews to the new documents or claim that future work has shipped.
