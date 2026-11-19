# Forward Deployed Engineer: from customer problem to production

[English](fde.md) · [Русский](../ru/careers/fde.md) · [Careers ahead](README.md) · [Atlas map](../README.md)

An FDE turns an ambiguous customer workflow into a working system and stays close enough to learn whether it helps. Preparation therefore needs a continuous argument: **why this workflow → what to build → how to prove it works → who can operate it**.

Sources checked: **19 November 2026**. The cases, diagrams, rubric and schedule below are editorial preparation tools, not a disclosed interview loop or employer scoring system. For attributed interview evidence, use the existing [FDE role guide](../roles/fde.md).

## Why this role now

Lenny Rachitsky's report of 10 November 2026 describes **4.6× growth in FDE openings over the preceding year and roughly 1,500 open roles**. Its openings data comes from TrueUp's coverage of tech companies. The report itself warns that some growth may reflect renaming adjacent jobs, such as sales engineering. These are reported openings, not completed hires, and they do not establish low competition or an individual's hiring chances. [Market report](https://www.lennysnewsletter.com/p/state-of-the-tech-job-market-late).

OpenAI's public FDE description assigns discovery, technical scoping, system design, building and production rollout to the role. It measures success through adoption, workflow impact and evaluation feedback into product development. This establishes a delivery remit at one employer, not a universal definition or interview specification. [OpenAI FDE role](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/).

## What the role owns

Read each vacancy by responsibility. Similar titles can hide different work. These distinctions are a comparison aid, not universal employer boundaries.

| Role orientation | Main question | Evidence to prepare |
| --- | --- | --- |
| FDE / customer-embedded engineering | Can this customer use and operate the system? | Working integration, evaluation, rollout and handoff |
| Solutions / sales engineering | Does the solution fit the buyer's needs? | Discovery, feasibility and clear demonstration |
| Core product engineering | Can the product serve many users reliably? | Maintainable services, interfaces and operational decisions |
| AI product / deployment leadership | Is the investment worthwhile and can delivery succeed? | Scope, outcome baseline, ownership and decision gates |

The useful FDE preparation model is a complete delivery loop:

```text
Observe workflow → Define outcome → Build smallest useful slice
       ↑                                      ↓
Product feedback ← Operate ← Evaluate + launch decision
                      ↓
           Customer ownership and handoff
```

At each transition, bring evidence: workflow map; baseline and acceptance criteria; functioning integration; representative failure cases; operating instructions. A demo alone covers only one transition.

## Practice cases

**Original exercises, not reported interview questions.** All quantities and deadlines below are synthetic constraints. Work through each aloud, then produce a one-page decision note. Related Atlas questions have their own provenance; linking them here does not establish that an FDE employer asks them.

### Case 1 — A useful support assistant in two weeks

**Brief.** A support team wants an assistant over 20,000 internal documents. Access differs by team, documents conflict, and reviewers have little spare time. The sponsor asks for a two-week pilot.

**Your task.** Ask five discovery questions, choose one workflow, draw the data path and propose a pilot decision. State what you would defer.

**A strong answer covers:** the existing task and time/error baseline; permissions enforced before evidence reaches the model; document freshness and citations; a representative evaluation set with answerable, unanswerable and forbidden-access cases; a human fallback; a named pilot owner. Separate retrieval failures from generation failures before changing models.

**A useful opening:** “I would pick one support workflow and agree what a correct, usable result means with its operators. Before expanding access, I would verify permissions and measure whether the assistant reduces work after review and correction.” Continue with architecture and tests; do not claim the exercise as past experience.

**Pressure test.** The demo looks good and the sponsor wants company-wide launch tomorrow. Name the missing evidence and propose the smallest safe next step.

Related: [enterprise retrieval design](../themes/ai-system-design.md#sd-enterprise-rag), [constrained enterprise pilot](../themes/applied-scenarios.md#app-vpc-pilot), [retrieval failures](../themes/applied-scenarios.md#app-rag-account-triage).

### Case 2 — The agent timed out after creating a work order

**Brief.** An assistant creates ERP work orders. A request times out, the operator retries, and two orders appear. The customer wants the model prompt fixed.

**Your task.** Explain the failure, sketch recovery and define what a human approves.

```text
Draft → Validate + authorise → Approve exact action → Execute
                                                       ↓
                                  Record outcome / reconcile timeout
                                                       ↓
                                    Retry only after state is known
```

**A strong answer covers:** unknown outcome versus failed operation; stable operation identifiers and downstream deduplication where available; reconciliation where it is not; approval bound to exact arguments and current permissions; audit records; compensation or escalation for irreversible effects. The executor enforces controls independently of model instructions.

**Pressure test.** The ERP has no idempotency API. Describe a lookup/reconciliation strategy and the remaining race. Explain when you stop automation for operator resolution instead of promising exactly-once execution.

Related: [ERP writes](../themes/agents-tools.md#agt-erp-writes), [timeouts and retries](../themes/agents-tools.md#agt-retries), [approval binding](../themes/agents-tools.md#agt-approval).

### Case 3 — The pilot passed its benchmark but nobody uses it

**Brief.** A pilot answers 90% of a small test set correctly. Weekly usage is declining, users still copy results into another tool, and the sponsor wants a rollout decision in five days.

**Your task.** Separate quality, workflow fit and adoption; propose an investigation and a decision with an owner.

**A strong answer covers:** test-set selection and hidden errors; observing actual users; total task time including review and re-entry; integration friction; relevant user segments; cost per completed useful task; criteria to continue, narrow or stop. Do not equate usage with benefit or a test score with production readiness.

**Pressure test.** One team loves the tool while another rejects it. Segment evidence instead of averaging away the difference.

Related: [rescuing a pilot](../themes/applied-scenarios.md#app-pilot-rescue), [AI suitability](../themes/ai-product-strategy.md#prod-ai-suitability), [AI feature metrics](../themes/ai-product-strategy.md#prod-ai-feature-metrics).

## Assess your answer

This editorial rubric diagnoses preparation gaps; it does not predict hiring. Score each dimension **0** when absent, **1** when named, **2** when connected to a concrete decision, artifact and trade-off.

| Dimension | What makes the answer inspectable |
| --- | --- |
| Discovery | User task, baseline, constraints and outcome owner |
| Engineering | Data flow, trust boundaries, integrations and recovery |
| Evaluation | Representative cases, failure analysis and justified release gate |
| Delivery | Scope, dependencies, staged exposure, rollback and handoff |
| Communication | Plain assumptions; decisions explained to operator and sponsor |

Rehearse any dimension below 2. A high total does not compensate for missing permissions or uncontrolled writes. Engineers should implement and test a narrow slice; leaders should explain architecture, delivery and accountability while being precise about their own contribution.

## Two-week preparation plan

| Sessions | Work | Completion evidence |
| --- | --- | --- |
| 1–2 | Compare two target role descriptions | Role map and three recruiter questions |
| 3–4 | Complete case 1 and its linked questions | Workflow, architecture and evaluation table |
| 5–6 | Build a demo with synthetic data | Reproducible run, failures and limitations |
| 7–8 | Complete case 2; inject timeouts and duplicates | Recovery behavior and approval checklist |
| 9–10 | Complete case 3; explain rollout aloud | Decision note, owner, stop criteria and handoff |
| 11–14 | Run two practice interviews; revise weak dimensions | Improved second attempt and what changed |

Prepare one truthful example of ambiguity, one difficult failure and one handoff. Distinguish personal decisions from team achievements. If your example is a practice project, say so.

## Further learning and source limits

- [Anthropic Partner Academy: Claude FDE](https://anthropic-partners.skilljar.com/path/claude-fde): the public outline lists 11 courses, about 9.5 hours; nine overlap Claude Developer, with Delivery Methodology and Driving enterprise adoption of Claude added. One outcome is a written pilot plan with a baseline, success measures agreed before building, a first shippable slice and initial users. This describes training, not interviews; check access conditions directly. Publication date not shown; checked 19 November 2026.
- [OpenAI FDE role](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/): supports the responsibilities above; it does not verify coding-round format or interview questions.
- [Lenny's late-2026 report](https://www.lennysnewsletter.com/p/state-of-the-tech-job-market-late): supports the dated market signal. Only the publicly accessible excerpt was used.
- Continue with the [sourced FDE role guide](../roles/fde.md), [learning path](../LEARNING_PATH.md), [engineering](../start/engineering.md) and [leadership](../start/leadership.md) start pages. Confirm the actual interview format with the employer.
