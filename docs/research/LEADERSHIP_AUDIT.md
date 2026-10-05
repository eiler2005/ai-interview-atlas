# AI Leadership: coverage and evidence audit

[English](LEADERSHIP_AUDIT.md) · [Русский](../ru/research/LEADERSHIP_AUDIT.md) · [Practice cases](../learning/AI_LEADERSHIP.md) · [Learning path](../LEARNING_PATH.md)

Audit date: **2026-10-05**. **Baseline before content corrections:** bank snapshot `6648af25ee5f04f1141b96a81900032af06a460d`, 294 questions overall. The baseline findings and 20 checks below describe that snapshot; links navigate to the current questions. The current-content addendum records subsequent corrections and additions. This is a curriculum audit, not a claim that the collection covers every leadership interview.

All **155 Leadership-tagged questions** were reviewed individually for the meaning of their prompt, tested competence and outline, role/level fit, evidence metadata and availability of reading and answers. There are **70 Leadership priority questions** and **89 answer-bearing Leadership questions**: the latter includes questions prioritised only for Engineering. All 155 have outlines; 37 have no reading. The per-question working record separates editorial branch assignment from the role actually named by evidence. This semantic review is not a fresh factual verification of all 155 source claims. The separate source check below covers **20 different questions**.

## What the baseline bank supports

Product discovery, AI suitability, metrics, launch judgement and first-line engineering management have usable learning material. Technical design questions also support a leader's design review, provided the exercise asks for a decision, operating owner and evidence. A technically demanding prompt does not establish managerial seniority.

Head/Director preparation is materially thinner. Feature prioritisation, cost per task, a large-team retrospective and stakeholder influence are useful precursors; none alone tests a portfolio under a cash and staffing constraint. The new cases add portfolio allocation, build/buy, management through managers and executive decisions as **editorial practice**. They do not create evidence that employers ask those cases.

TPM practice has useful dependency, uncertainty and readiness scenarios. Several of the clearest ones are generated, and sourced delivery prompts mostly come from PM or EM material. Their educational relevance is stronger than their evidence of specialist AI TPM interviewing.

### Baseline evidence composition

Count questions once by their combination of evidence kinds, not once per company attribution:

| Evidence combination | Questions | What it establishes |
| --- | ---: | --- |
| Preparation guide only | 31 | Secondary preparation material |
| Compilation only | 84 | Unverified question attribution from a compilation |
| Preparation guide plus compilation | 1 | Two kinds of secondary support, not first-hand confirmation |
| Participant report | 23 | Public candidate/interviewer account within its stated role and date |
| Official source | 2 | Employer-published general PM or Senior Staff+ material |
| Generated; no interview evidence | 14 | Editorial practice only |

The compilation appears on 85 distinct questions, including the mixed row. Many guides and reports share one publisher; source count is not independent corroboration. Primary technical reading improves an answer's learning support without upgrading interview attribution. A job posting describes responsibilities, never a question or interview stage. See the [methodology](../METHODOLOGY.md).

## Baseline P0 competence matrix

These are editorial preparation priorities, selected by responsibility rather than title or market-frequency claims. **Covered** means the present bank has a usable prompt, outline and learning support for the stated scope; **partial** means an important decision/output is absent; **missing** means no direct current question covers the scope. These are material-coverage judgments, not learner scores. Evidence strength is a separate column. **A** = written answer; **O** = outline only. Each linked question contains its precise reading list; named readings below are useful starting points, not new interview sources. Case IDs refer to the [supplement](../learning/AI_LEADERSHIP.md).

| P0 competence | Role and scope | Exact current anchors; answer/reading support | Educational coverage before supplement | Interview-evidence limit | Practice |
| --- | --- | --- | --- | --- | --- |
| Discovery and AI/no-AI decision | Product, senior IC/lead | [prod-enterprise-discovery](../themes/ai-product-strategy.md#prod-enterprise-discovery), [prod-ai-suitability](../themes/ai-product-strategy.md#prod-ai-suitability), [prod-expensive-mvp](../themes/ai-product-strategy.md#prod-expensive-mvp): A; research recruiting, Rules of ML | Covered for a bounded opportunity | Interviewer account plus prep guide; level is editorial | P1 |
| Metrics and experiments | Product, senior IC/lead | [prod-ai-feature-metrics](../themes/ai-product-strategy.md#prod-ai-feature-metrics): A; HEART. [eval-online](../themes/evals-observability.md#eval-online): O; evaluation reading | Partial: experiment validity needs an executed analysis | Guide/compilation; eval-engineer practice tag is not PM evidence | P2 |
| Economics, trust, launch/stop | Product, senior IC/lead | [prod-enterprise-ai-pricing](../themes/ai-product-strategy.md#prod-enterprise-ai-pricing), [prod-confident-errors](../themes/ai-product-strategy.md#prod-confident-errors), [prog-prelaunch-hallucinations](../themes/program-delivery.md#prog-prelaunch-hallucinations): A; cost essay, NIST, agent evals | Covered at one-product scope; combine decisions in practice | Interviewer account and secondary samples; no universal loop | P3 |
| Architecture and reliability | EM/Platform, team/service owner | [sd-gateway](../themes/ai-system-design.md#sd-gateway), [eval-release-gate](../themes/evals-observability.md#eval-release-gate), [inf-cost-reduction](../themes/inference-economics.md#inf-cost-reduction): A; idempotency, evals, SRE | Covered for technical review; partial operational authority | Compilation and engineering practice tags | E1 |
| AI-assisted SDLC and hiring signal | EM/Platform, people manager | [lead-ai-review-skills](../themes/engineering-leadership.md#lead-ai-review-skills): A; [lead-ai-interview-redesign](../themes/engineering-leadership.md#lead-ai-interview-redesign): O; AI-resistant evaluations | Partial: no observed review/calibration output yet | Generated; official blog is reading, not evidence these questions were asked | E2 |
| Staffing and platform ownership | EM/Platform, team lead/manager | [lead-platform-team-charter](../themes/engineering-leadership.md#lead-platform-team-charter), [ops-platform-ownership](../themes/ai-operating-model.md#ops-platform-ownership), [lead-strategic-hiring](../themes/engineering-leadership.md#lead-strategic-hiring): A; Team Topologies, SRE, manager training | Covered for a team charter; add explicit capacity arithmetic | Generated plus general secondary management material | E3 |
| Coaching, performance, team health | EM, first-line manager | [lead-low-performance](../themes/engineering-leadership.md#lead-low-performance), [lead-mentee-growth](../themes/engineering-leadership.md#lead-mentee-growth), [lead-team-after-change](../themes/engineering-leadership.md#lead-team-after-change): A; manager training, organisational change | Covered at team scope; source adaptations noted below | General EM reports; not proof of an AI-specific loop | E4 |
| Portfolio and budget allocation | Head/Director, delegated portfolio authority | [prod-roadmap](../themes/ai-product-strategy.md#prod-roadmap): O, no reading; [prod-product-cannibalisation](../themes/ai-product-strategy.md#prod-product-cannibalisation): O, no reading; [inf-cost-reduction](../themes/inference-economics.md#inf-cost-reduction): A | **Missing direct multi-initiative budget case**; anchors are precursors | PM/technical material; insufficient director interview evidence | H1 |
| Build/buy and resource allocation | Head/Director, investment owner | [app-open-model-engagement](../themes/applied-scenarios.md#app-open-model-engagement): O; evals, serving docs. [lead-platform-team-charter](../themes/engineering-leadership.md#lead-platform-team-charter): A | Partial: vendor exit, staffing, opportunity cost and cash envelope absent together | Compilation/generated; insufficient director interview evidence | H2 |
| Organisation change and executive stakeholders | Head/Director, several teams/managers | [lead-team-scale](../themes/engineering-leadership.md#lead-team-scale), [lead-reorganisation-retention](../themes/engineering-leadership.md#lead-reorganisation-retention), [beh-stakeholder-priorities](../themes/behavioral-values.md#beh-stakeholder-priorities): A; manager training, organisational change | Partial: team-level material needs a manager-of-managers decision | EM report/compilation; no verified director-level loop | H3 |
| Research uncertainty and milestones | TPM/Delivery, programme owner | [prog-research-milestones](../themes/program-delivery.md#prog-research-milestones), [lead-research-product-boundary](../themes/engineering-leadership.md#lead-research-product-boundary): A; design docs, Rules of ML | Covered conceptually; needs a falsifiable milestone plan | Generated; no reported TPM question | T1 |
| Dependencies and schedule recovery | TPM/Delivery, multi-team programme | [prog-dependency-slip](../themes/program-delivery.md#prog-dependency-slip), [prog-cross-team-delivery](../themes/program-delivery.md#prog-cross-team-delivery): A; dependency mapping, design docs | Covered for replanning | Generated and EM report; report unavailable in current check | T2 |
| Readiness, rollout and incidents | TPM/Delivery, release coordination | [prog-multi-owner-readiness](../themes/program-delivery.md#prog-multi-owner-readiness), [prog-device-update](../themes/program-delivery.md#prog-device-update), [app-pilot-rescue](../themes/applied-scenarios.md#app-pilot-rescue): A; NIST, SRE, evals | Covered in separate prompts; rehearse one connected incident | Generated/PM guide/compilation; not direct TPM evidence | T3 |
| Technical literacy, evaluation and action authority | All four, depth follows remit | [pt-method-choice](../themes/post-training.md#pt-method-choice), [eval-benchmark-mismatch](../themes/evals-observability.md#eval-benchmark-mismatch), [sec-action-authorisation](../themes/safety-security-governance.md#sec-action-authorisation), [sec-safe-deployment](../themes/safety-security-governance.md#sec-safe-deployment): A; RAG/LoRA, Rules of ML, NIST | Covered for decisions; not a substitute for engineering implementation | Mostly compilation; learning support is stronger than interview attribution | S1 |
| Truthful behavioural evidence | All four, actual authority and contribution | [beh-mistake-learning](../themes/behavioral-values.md#beh-mistake-learning), [prog-initiative-retrospective](../themes/program-delivery.md#prog-initiative-retrospective): A; postmortem culture | Covered as an account-building method | Compilation/EM account; learner's experience must be real | S2 |

## Baseline twenty-question source check

All checks below were made **2026-10-05** on public page content. This is a purposive sample, five practice anchors per branch, not a random estimate of accuracy. The Head/Director rows deliberately inspect transferable precursors because direct director evidence is insufficient. The TPM rows likewise do not relabel PM/EM reports as TPM reports. “Match” means the opened source supports the question's core, not its editorial answer or every follow-up. No source was upgraded because it called itself verified.

| Branch | Canonical question | Exact source and opened scope | Finding |
| --- | --- | --- | --- |
| Product | [prod-enterprise-ai-pricing](../themes/ai-product-strategy.md#prod-enterprise-ai-pricing) | [Habr interviewer account][HABR], economics section | Match: pricing, costs and customisation; participant, no named employer |
| Product | [prod-enterprise-discovery](../themes/ai-product-strategy.md#prod-enterprise-discovery) | [Habr][HABR], discovery section | Match: enterprise persona, recruitment and problem value |
| Product | [prod-expensive-mvp](../themes/ai-product-strategy.md#prod-expensive-mvp) | [Habr][HABR], prototyping section | Match: expensive/slow MVP; outline is editorial |
| Product | [prod-notification-paradox](../themes/ai-product-strategy.md#prod-notification-paradox) | [Meta AI PM participant][META-PM], analytical screen | Match; general analytics prompt within reported AI-PM interview |
| Product | [prod-impactful-product](../themes/ai-product-strategy.md#prod-impactful-product) | [Monzo PM guide][MONZO-PM], project walkthrough | Match; official **general PM**, dated 2022 |
| EM/Platform | [lead-low-performance](../themes/engineering-leadership.md#lead-low-performance) | [Google L6 EM participant][GOOGLE-EM], people-management round | **Adapted:** source hypothetical; bank asks past experience |
| EM/Platform | [lead-disruptive-star](../themes/engineering-leadership.md#lead-disruptive-star) | [Google L6 EM][GOOGLE-EM], people-management round | **Adapted:** source hypothetical; bank asks past experience |
| EM/Platform | [lead-mentee-growth](../themes/engineering-leadership.md#lead-mentee-growth) | [Anthropic EM participant][ANTHROPIC-EM], management questions | Match; EM account, not director confirmation |
| EM/Platform | [lead-team-disagrees](../themes/engineering-leadership.md#lead-team-disagrees) | [Anthropic EM][ANTHROPIC-EM], management questions | Match; response method remains editorial |
| EM/Platform | [lead-team-after-change](../themes/engineering-leadership.md#lead-team-after-change) | [Google L6 EM][GOOGLE-EM], new-team morale scenario | Match in core; bank generalises the scenario |
| Head/Director precursor | [lead-team-scale](../themes/engineering-leadership.md#lead-team-scale) | [Anthropic EM][ANTHROPIC-EM], process and management questions | Match to EM scope; managers-of-managers not established |
| Head/Director precursor | [lead-reorganisation-retention](../themes/engineering-leadership.md#lead-reorganisation-retention) | [Google L6 EM][GOOGLE-EM], difficult-change discussion | **Adapted:** actual attrition in source; threatened departure in bank |
| Head/Director precursor | [lead-opportunity-coalition](../themes/engineering-leadership.md#lead-opportunity-coalition) | [Monzo Senior Staff+][MONZO-STAFF], impact and leadership section | Match; official **IC** leadership, not director/EM interview |
| Head/Director precursor | [prod-product-cannibalisation](../themes/ai-product-strategy.md#prod-product-cannibalisation) | [Meta AI PM][META-PM], marketplace follow-up | Match; L5 PM report, not portfolio-owner interview |
| Head/Director precursor | [lead-strategic-hiring](../themes/engineering-leadership.md#lead-strategic-hiring) | [Stripe preparation guide][STRIPE], people/organisation screen | Partial match: strategic hiring topic; bank reframes it; secondary |
| TPM/Delivery transfer | [prog-difficult-launch](../themes/program-delivery.md#prog-difficult-launch) | [OpenAI PM guide][OPENAI-PM], recently asked launch questions | Match in secondary guide; PM scope |
| TPM/Delivery transfer | [prog-prelaunch-hallucinations](../themes/program-delivery.md#prog-prelaunch-hallucinations) | [Amazon AI PM guide][AMAZON-PM], generative-AI samples | Match to **practice sample**, not first-hand interview proof |
| TPM/Delivery transfer | [prog-device-update](../themes/program-delivery.md#prog-device-update) | [Amazon AI PM guide][AMAZON-PM], product-thinking samples | Match; secondary PM guide |
| TPM/Delivery transfer | [prog-cross-team-delivery](../themes/program-delivery.md#prog-cross-team-delivery) | [Meta EM report][META-EM], attempted original and redirect URLs | **Unavailable:** public fetch failed; no pass or new corroboration |
| TPM/Delivery transfer | [prog-initiative-retrospective](../themes/program-delivery.md#prog-initiative-retrospective) | [Anthropic EM][ANTHROPIC-EM], initiative presentation | Match; reported EM presentation, not TPM loop |

The adapted and partial findings above are historical findings against the baseline wording, not descriptions of the corrected prompts now reached by the links. The first audit pass did not change the bank. The authorised content pass below subsequently aligned four prompts while retaining their IDs and evidence kinds. Hypothetical practice and truthful past experience remain distinct formats.

## Current-content addendum — 2026-10-05

The content pass now has **160 Leadership questions, 76 Leadership priorities and 97 answer-bearing Leadership questions**, including shared Engineering priorities. Across both tracks there are **299 questions, 158 answer-bearing priority questions, 247 sources and reading on all 299 questions**. Counts establish available material, not competence mastery or factual verification. The original 155-question semantic record remains a dated baseline; new and reworded questions received the separate semantic checks described here. The 20 baseline source checks do not verify every new answer or all current employer attributions.

### Source-faithful corrections

| Stable ID | Current wording/type and follow-through | Current source verdict |
| --- | --- | --- |
| [lead-low-performance](../themes/engineering-leadership.md#lead-low-performance) | Hypothetical performance problem; changed to applied scenario with prospective support and follow-up | Google L6 EM participant report reopened; hypothetical core matches |
| [lead-disruptive-star](../themes/engineering-leadership.md#lead-disruptive-star) | Hypothetical collaboration problem; changed to applied scenario, with observable behaviour and fair process | Same report reopened; hypothetical core matches |
| [lead-reorganisation-retention](../themes/engineering-leadership.md#lead-reorganisation-retention) | Actual difficult change involving departures; changed to behavioural, with truthful experience and remaining-team consequences | Same report reopened; actual attrition core matches |
| [lead-strategic-hiring](../themes/engineering-leadership.md#lead-strategic-hiring) | Most recent strategic engineering hire; behavioural answer distinguishes personal authority, hiring bar and observed results | Stripe guide reopened; last strategic hire and hiring-bar scope now aligned; still secondary preparation material |

Each correction includes EN/RU tests, outline and answer changes. The explanatory follow-ups are editorial, not a transcript. Google remains a general EM participant report; Stripe remains a general management preparation guide. The original URLs redirected to the same Aced material. Relative update labels do not establish publication or interview dates. [Meta EM][META-EM] was attempted again on 2026-10-05 and remained unavailable: `prog-cross-team-delivery` is **not freshly verified**, and the source retains its last successful retrieval date.

### Added learning coverage and semantic checks

| Question and priority | Role/authority and distinct decision | Educational coverage now | Interview evidence |
| --- | --- | --- | --- |
| [ops-ai-portfolio-allocation](../themes/ai-operating-model.md#ops-ai-portfolio-allocation), L71 | Head/Director with delegated portfolio authority; allocate cash and people after a cut across dependent initiatives | Direct bounded question, EN/RU answer, checklist and appraisal reading; extends feature-roadmap precursors | Generated from eligible operating-model radar theme; no employer attribution |
| [ops-ai-build-buy-exit](../themes/ai-operating-model.md#ops-ai-build-buy-exit), L72 | Investment owner; approve renewal or replacement with contract timing and a funded, tested exit | Direct question with organisational capacity and continuity, beyond model selection | Generated; cloud guidance supports learning only |
| [lead-managers-accountability](../themes/engineering-leadership.md#lead-managers-accountability), L73 | Manager of managers; resolve interfaces and executive commitments while retaining managers' authority | Direct question, answer and decision-rights checks, beyond a single platform charter | Generated; GitLab role/process reading is not question evidence |
| [prod-ai-stop-investment](../themes/ai-product-strategy.md#prod-ai-stop-investment), L74 | Product investment owner; stop or narrow an existing product and support its users | Direct question joining incremental value, remaining uncertainty and withdrawal, beyond initial launch | Generated; experiment/metrics reading is not interview corroboration |
| [prog-incident-without-rollback](../themes/program-delivery.md#prog-incident-without-rollback), L75 | TPM/programme coordination; contain harm and establish restart evidence when rollback is unavailable | Direct question connecting incident authority, customer response and recovery | Generated; not reported as an AI TPM question |
| [lead-ai-interview-redesign](../themes/engineering-leadership.md#lead-ai-interview-redesign), L76 | EM/hiring owner; choose disclosed tool policies and assess individual judgement | Existing generated question gains EN/RU answer and revised checklist; avoids prescribing one universal AI policy | Generated status retained; official engineering blogs are reading |

All six have three-point checklists, primary reading and answers of 100–180 words in each language. Priorities 1–70 retain their order. The five new questions use qualifying Leadership radar themes and make their role authority explicit in the scenario; they do not invent employer levels. Conceptual comparison checked the additional decision dimension against roadmap, platform-charter, model-selection, launch and readiness predecessors. Similar wording checks alone would not establish distinct coverage.

Thirty reading gaps in the seven Leadership-owned themes were filled with topic-specific primary material; the parallel Engineering pass closed the remaining gaps. Reading fit was checked against each prompt: for example offline synchronisation for the field catalogue, marketplace matching for cold start, FINRA's detection discussion for financial-crime decomposition, and compensation components for the mission-without-upside question. Sources describe methods or domains, not new interview occurrences. Research uncertainty and multi-owner readiness already have direct questions; the guide now routes to their answers instead of duplicating them.

### Stronger process sources, with limits

All three pages below were opened on 2026-10-05. [Amazon's TPM preparation page](https://amazon.jobs/content/en/how-we-hire/tpm-interview-prep) is undated and describes a general TPM phone screen, writing assessment and five-interview loop, including systems design. The Amazon company page now separates those official stages from its existing secondary AI-PM path.

[GitLab's Engineering Director page](https://handbook.gitlab.com/job-description-library/engineering/development/management/director/) contains an actual hiring-process section and shows a 2026-03-12 modification date. [Product Management Leadership](https://handbook.gitlab.com/job-description-library/product/product-management-leadership/) also describes Director hiring stages; no publication date was established here. These support scoped general Director process and responsibility claims. They do not supply the new AI cases, independent corroboration from a second publisher, or evidence that all Director roles have identical authority. No GitLab company page was added solely from these same-publisher documents.

Direct first-hand Head/Director and specialist AI TPM question evidence remains a sourcing gap. The source corrections, educational additions and official process research improve different things; none justifies calling the entire current bank freshly source-verified. The question-led guide keeps changed conditions and a shared oral-answer rubric, without requiring code exercises, labs, projects or an automated evaluator.

## Ambiguous assignments and remaining gaps

Role tags are editorial. The bank includes FDE, evaluation-engineer, inference-engineer and research-engineer prompts in Leadership. `sd-model-api`, `agt-erp-writes`, `inf-runtime-choice`, `llm-compute-optimal` and `code-refactoring` are technical review or elective depth; they cannot substitute for hiring, coaching or resource allocation. `lead-engineering-persuasion` is product partnership, not people management. `prod-handyman-marketplace` and `prod-volunteer-cold-start` are general PM transfer exercises even though their account describes an AI-PM track.

Domain prompts about payments, clinical notes, legal authority, age assurance or robotics are conditional on the role's remit. Their short outlines and generic references do not establish legal, medical or physical-safety sufficiency. The supplement does not promote them to universal P0. Unspecified levels stay unspecified; a `senior` practice label is not evidence of a company's level calibration. Real budget authority, direct reports, managers led and decisions owned must be stated independently.

The remaining sourcing priority is direct public Head/Director and AI TPM interviewing evidence from additional independent publishers. The remaining learning priority is learner-produced evidence: decisions, arithmetic, release criteria and delayed retries. Completing a case adds a practice result, not a reported interview question or professional achievement.

## Current role research and source boundaries

The following official pages were opened on **2026-10-05**. Dates are publication dates when known; otherwise undated/live. These are scoped employer examples, not a representative labour-market survey.

| Source | Date | Exact use and limit |
| --- | --- | --- |
| [Anthropic PM, Claude Science](https://job-boards.greenhouse.io/anthropic/jobs/5394887008) | Undated/live | This posting links researcher discovery, roadmap ownership and evaluation fluency. It does not describe an interview |
| [Anthropic EM, Data Infrastructure](https://job-boards.greenhouse.io/anthropic/jobs/5426135008) | Undated/live | This role combines people development, platform reliability/cost and staffing. Platform employment at an AI company does not establish an AI-specialist interview |
| [Anthropic TPM, Research](https://job-boards.greenhouse.io/anthropic/jobs/5203545008) | Undated/live | This role includes research/engineering coordination, changing priorities and operational ownership; no interview questions are supplied |
| [Pfizer AI Oncology Portfolio Lead, Director](https://www.pfizer.com/about/careers/job/4964531?langcode=en) | Undated/live | Explicitly an individual-contributor role: a Director title alone cannot establish people or budget authority |
| [Anthropic, AI-resistant technical evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) | 2026-01-21 | A performance-engineering hiring-task redesign example; motivates calibration practice, not a universal policy permitting AI in interviews |
| [Monzo PM][MONZO-PM] / [Senior Staff+][MONZO-STAFF] | 2022-10-04 / 2025-05-02 | Official interview baselines; general PM and senior IC scopes, respectively |
| [Habr interviewer][HABR] | Date not established in this check | First-hand account of the author's enterprise AI PM interviewing; not a company-wide process |
| Participant and prep pages linked in the 20-row table | Undated/dynamic | Relative page timestamps are not exact interview dates; guides remain secondary, reports remain individual accounts |

An additional Sony Pictures Director posting appeared in search, but opening it returned no readable body; it was not used to establish director requirements. An Anthropic Business Technology PM posting redirected to a jobs listing and was excluded. Unavailable pages and search snippets were not silently counted as successful verification.

[HABR]: https://habr.com/ru/articles/1038482/
[META-PM]: https://www.tryexponent.com/experiences/meta-facebook-product-manager-interview-618bfd
[GOOGLE-EM]: https://www.tryexponent.com/experiences/google-staff-engineering-manager-interview-fd33b1
[ANTHROPIC-EM]: https://www.tryexponent.com/experiences/anthropic-engineering-manager-interview-170078
[META-EM]: https://www.tryexponent.com/experiences/meta-facebook-engineering-manager-interview-916dc8
[MONZO-PM]: https://monzo.com/blog/2022/10/04/product-management-at-monzo-the-interview-process
[MONZO-STAFF]: https://monzo.com/blog/demystifying-the-senior-staff-engineering-interview-process
[STRIPE]: https://www.tryexponent.com/blog/stripe-interview-process
[OPENAI-PM]: https://www.tryexponent.com/guides/openai-product-manager-interview
[AMAZON-PM]: https://www.tryexponent.com/guides/amazon-ai-product-manager-interview
