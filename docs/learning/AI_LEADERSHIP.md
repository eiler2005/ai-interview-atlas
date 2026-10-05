# AI Leadership: questions, explanations and answer checks

[English](AI_LEADERSHIP.md) · [Русский](../ru/learning/AI_LEADERSHIP.md) · [Eight-week learning path](../LEARNING_PATH.md) · [Coverage audit](../research/LEADERSHIP_AUDIT.md)

Use this supplement alongside the existing eight-week plan. Choose **Product**, **EM/Platform**, **Head/Director**, or **TPM/Delivery** by the decisions the role owns. A senior product IC need not manage people; a Director title need not carry budget authority. The audit separates educational coverage from interview evidence.

Start with the linked bank question, explain your reasoning aloud, then read its answer, checklist and primary reading. Use the short case prompts below as follow-ups. They are **editorial practice**, not reported employer questions; any supplied numbers are fictional. A practice answer never becomes a professional achievement. These pages provide questions and reading, with no automated scoring or required project submission.

## Route through the questions

| Branch | Start with | Explanation to check | Follow-up cases |
| --- | --- | --- | --- |
| Product | [Discovery](../themes/ai-product-strategy.md#prod-enterprise-discovery), [AI suitability](../themes/ai-product-strategy.md#prod-ai-suitability), [metrics](../themes/ai-product-strategy.md#prod-ai-feature-metrics), [stopping investment](../themes/ai-product-strategy.md#prod-ai-stop-investment) | User problem, credible baseline, incremental value, economics and a decision to launch, narrow or stop | P1–P3 |
| EM/Platform | [AI code review](../themes/engineering-leadership.md#lead-ai-review-skills), [hiring redesign](../themes/engineering-leadership.md#lead-ai-interview-redesign), [platform charter](../themes/engineering-leadership.md#lead-platform-team-charter), [performance](../themes/engineering-leadership.md#lead-low-performance) | Technical judgement, operating ownership, staffing and fair people management | E1–E4 |
| Head/Director | [Portfolio allocation](../themes/ai-operating-model.md#ops-ai-portfolio-allocation), [build/buy and exit](../themes/ai-operating-model.md#ops-ai-build-buy-exit), [management through managers](../themes/engineering-leadership.md#lead-managers-accountability) | Authority over money, capacity and several managers; explicit executive tradeoffs | H1–H3 |
| TPM/Delivery | [Research milestones](../themes/program-delivery.md#prog-research-milestones), [dependency slip](../themes/program-delivery.md#prog-dependency-slip), [readiness](../themes/program-delivery.md#prog-multi-owner-readiness), [incident without rollback](../themes/program-delivery.md#prog-incident-without-rollback) | Uncertainty, dependencies, decision rights, containment and restart evidence | T1–T3 |

Leadership priorities **71–76** append five new generated questions and an answer to the existing hiring-redesign question; priorities 1–70 retain their order. Each has EN/RU explanations, a three-point checklist and reading. The Head/Director questions explicitly assume delegated authority; candidates without it should explain recommendations and escalation at their actual scope.

The eight-week baseline remains unchanged: use P1–P2 in weeks 1–2, S1/P3/E1 in weeks 3–4, operating-model cases in week 5, T1–T3 in week 6, role depth in week 7 and a mixed discussion with delayed retries in week 8. Select relevant questions rather than adding another workload.

## Shared answer rubric

| Score | What is observable in the answer |
| --- | --- |
| 0 | No coherent decision, or a critical misconception |
| 1 | Plausible terminology, but missing evidence, mechanism, owner or a useful check |
| 2 | Independent recommendation with assumptions, a rejected alternative, mechanism, tradeoff, owner and relevant evidence |
| 3 | Also handles changed conditions, exposes a failure case and says when to stop or reverse |

Use the rubric for self-review or a discussion with a peer. Note the question, specific feedback and what to revisit; retry weak answers after a delay without reading the example first. A suggested learning gate is 2 or more on the first explanation and delayed retry, with no critical failure hidden in an average. It is an editorial aid, not a validated hiring assessment. An unobserved skill stays unassessed.

## Product

### P1 — Discover the problem and earn the AI choice

**Question:** Who has the problem, who pays, what happens today, and why might AI improve the outcome? **Check:** separate observed needs from assumptions, name a non-AI option and choose evidence that could reject AI. **Changed condition:** half the requests have structured answers that ordinary search can retrieve. Re-scope the recommendation. Read the discovery and AI-suitability anchors above; Google PAIR and Rules of ML supply useful starting points.

### P2 — Measure value and design the comparison

**Question:** What outcome would demonstrate improvement over the existing workflow? **Check:** define the denominator, comparison population, randomisation unit, contamination risk, review labels and guardrails. Explain why rising acceptance or engagement need not mean better outcomes. **Changed condition:** most adoption comes from one enthusiastic team while rare-case quality deteriorates. The [metrics question](../themes/ai-product-strategy.md#prod-ai-feature-metrics) and [cannibalisation question](../themes/ai-product-strategy.md#prod-product-cannibalisation) link HEART and Microsoft's experiment-design guidance.

### P3 — Explain economics and the stop decision

**Question:** Is the product worth continued investment? For illustration, an old process costs $6 per case; a pilot adds $2 of review, $0.20 of model/retrieval cost and $3,000 of monthly operations across 10,000 eligible cases. **Check:** the apparent $3.50 difference is not established savings: remaining work, failures, escalations and realised use of capacity are unknown. At half volume, the fixed allocation rises from $0.30 to $0.60 per case. **Changed condition:** a severe subgroup failure appears before launch. Use [pricing](../themes/ai-product-strategy.md#prod-enterprise-ai-pricing) and [stop investment](../themes/ai-product-strategy.md#prod-ai-stop-investment) to explain narrowing, delay or withdrawal and the consequences for users.

## EM/Platform

### E1 — Review architecture and operating ownership

**Question:** Who owns quality, reliability, permissions and recovery across the application, platform and provider? **Check:** trace one request and one ambiguous action timeout; identify a control independent of model output. **Changed condition:** a provider update improves average quality but breaks a critical slice. Use [gateway design](../themes/ai-system-design.md#sd-gateway), [release gates](../themes/evals-observability.md#eval-release-gate) and [action authority](../themes/safety-security-governance.md#sec-action-authorisation), with their SRE, evaluation and security reading.

### E2 — Improve AI-assisted development and hiring

**Question:** What must an engineer personally explain and verify when AI produces the change, and how will the hiring loop assess that work? **Check:** distinguish tool access from capability; state a clear stage-specific tool policy, comparable candidate conditions and observable scoring criteria. Discuss interviewer disagreement and the limits of a small calibration sample. **Changed condition:** code production speeds up while review queues and escaped defects worsen. Use [review skills](../themes/engineering-leadership.md#lead-ai-review-skills) and [hiring redesign](../themes/engineering-leadership.md#lead-ai-interview-redesign). The Anthropic and Canva readings describe their own approaches, not a universal permission to use AI.

### E3 — Staff the work and define the platform boundary

**Question:** Which capability is missing, and should you hire, train, borrow expertise or stop work? **Check:** include time for operations and learning, define what the platform owns and keep customer outcomes with an accountable product owner. **Changed condition:** the hiring allocation disappears. Use [platform charter](../themes/engineering-leadership.md#lead-platform-team-charter) for the scenario; [strategic hiring](../themes/engineering-leadership.md#lead-strategic-hiring) now asks for a real past hire and must be answered from actual experience.

### E4 — Coach and address performance

**Question:** How would you address an observable performance or collaboration gap? **Check:** hear the employee's perspective, separate unclear expectations from capability and conduct, agree support and follow-up. Strong individual output does not excuse harmful behaviour. **Changed condition:** a reorganisation creates uncertainty. [Low performance](../themes/engineering-leadership.md#lead-low-performance) and [disruptive star](../themes/engineering-leadership.md#lead-disruptive-star) are hypothetical; [reorganisation and attrition](../themes/engineering-leadership.md#lead-reorganisation-retention) requires a real account of departures. Do not substitute a fictional retention success.

## Head/Director

### H1 — Allocate a constrained portfolio

**Question:** Which initiatives retain funding after a budget cut, and which commitments change? **Check:** compare money and people capacity, distinguish mandatory work from discretionary scope, expose shared dependencies and avoid counting benefits twice. **Changed condition:** cut the cash envelope by 30% while one scarce specialist is unavailable. Start with [portfolio allocation](../themes/ai-operating-model.md#ops-ai-portfolio-allocation). The Green Book supplies appraisal questions; its public-sector valuation assumptions are not corporate finance defaults.

### H2 — Decide build/buy with an executable exit

**Question:** What would you approve when vendor economics change and replacement is costly? **Check:** compare common time horizons, staff opportunity cost, operations, contract notice dates, portability tests and continuity. An exit needs funded capacity and demonstrated replacement quality. **Changed condition:** the vendor withdraws the old model before migration is ready. Use [build/buy and exit](../themes/ai-operating-model.md#ops-ai-build-buy-exit), with cloud lock-in and cost-framework reading.

### H3 — Lead through managers and executives

**Question:** How do you resolve cross-team ownership without becoming every team's delivery manager? **Check:** assign decision rights, keep execution with managers, coach privately and take evidenced options to the sponsor. **Changed condition:** two managers dispute an evaluation obligation after an executive has promised launch. Use [management through managers](../themes/engineering-leadership.md#lead-managers-accountability). GitLab describes one general Director scope and communication practice; the editorial AI scenario is not a reported GitLab question.

## TPM/Delivery

### T1 — Plan research uncertainty

**Question:** Which result would disprove the central hypothesis, and when would it change the programme? **Check:** make milestones retire named uncertainties, agree decision thresholds and consider the affordability of a fallback. Calendar progress does not prove technical feasibility. **Changed condition:** the first result is inconclusive and the next experiment needs unavailable customer data. Use [research milestones](../themes/program-delivery.md#prog-research-milestones).

### T2 — Recover a dependency slip

**Question:** Which downstream gate changes when data access or labelling slips? **Check:** show the dependency, owner, confidence range and decision deadline; compare reordering, scope reduction and renegotiation. **Changed condition:** a two-week delay conflicts with a contractual date. Synthetic examples cannot silently replace customer validation. Use [dependency slip](../themes/program-delivery.md#prog-dependency-slip); the Meta report behind [cross-team delivery](../themes/program-delivery.md#prog-cross-team-delivery) remained unavailable on the latest check.

### T3 — Decide readiness and coordinate an incident

**Question:** Who can release, stop and restart the service, and on what evidence? **Check:** distinguish containment from recovery, assign incident and customer owners, preserve traces and require representative checks before restoring autonomy. **Changed condition:** a model regression causes harmful actions and rollback is unavailable. Use [readiness](../themes/program-delivery.md#prog-multi-owner-readiness) and [incident without rollback](../themes/program-delivery.md#prog-incident-without-rollback). Amazon's official TPM process supports a general interview baseline, not these editorial AI questions.

## Shared questions

### S1 — Explain technical tradeoffs at the right depth

Explain an evaluation or architecture choice, its failure mode and what you would ask an engineer to demonstrate. Use [method choice](../themes/post-training.md#pt-method-choice), [benchmark mismatch](../themes/evals-observability.md#eval-benchmark-mismatch) and [safe deployment](../themes/safety-security-governance.md#sec-safe-deployment). Change the data-access or latency constraint. Check that the recommendation changes for a reason, with responsibility and evidence attached.

### S2 — Give truthful behavioural evidence

Choose a real decision and a real mistake or disagreement. State context, your authority, your action, alternatives, observed outcome and uncertainty. Separate team results from personal contribution. Use [mistake and learning](../themes/behavioral-values.md#beh-mistake-learning) and [initiative retrospective](../themes/program-delivery.md#prog-initiative-retrospective). If you lack the requested experience, say so and explain the closest real example; label any hypothetical reasoning separately.

The [audit](../research/LEADERSHIP_AUDIT.md) records what changed in the bank and where direct Head/Director or AI TPM interview evidence is still missing. Reading, a good answer and a practice score do not strengthen an employer attribution.
