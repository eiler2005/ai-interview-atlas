# Learning path

[English](LEARNING_PATH.md) · [Русский](ru/LEARNING_PATH.md) · [AI Interview Atlas](../README.md)

Use this curriculum to turn reading into explanations, working examples and defensible decisions. Choose **AI Engineering** or **AI Leadership**; leadership has product, engineering/platform and programme emphases. The separate [project roadmap](ROADMAP.md) describes repository development.

The baseline is **eight weeks at 6–8 hours a week**, an editorial estimate for experienced software or product practitioners who meet the entry checks below. It is not a beginner-to-expert promise or a research-validated preparation time. Remediation and the advanced branch need additional time. Move on when the evidence meets a gate, not when the week ends.

The atlas has 70 priority questions per track, with checklists, reading and example answers. Every question in the wider 294-question bank says what a strong answer covers, but only the priority questions have written answers. Here **E12** means question 12 on [Engineering: Start here](start/engineering.md), and **L12** means question 12 on [Leadership: Start here](start/leadership.md). These numbers select practice material; they do not establish what a particular employer will ask. This curriculum and its exercises are editorial recommendations, not company interview evidence.

## 1. Check your starting point

Spend one 60–90-minute session without notes. Explain a familiar system, identify a failure and propose a measurement. Then attempt the relevant checks below. Record what you actually produced, not just confidence.

| Check | Engineering evidence | Leadership evidence | If missing |
| --- | --- | --- | --- |
| Programming and data | Write a small Python function with tests, read JSON, explain array shapes and an HTTP timeout | Trace a request across client, service, model and data store; identify ownership and failure handling | Engineering: practise Python, tests and small array operations before model code. Leadership: draw and explain a basic service with an engineer |
| Quantitative reasoning | Explain matrix multiplication, probabilities, derivatives and train/validation separation | Calculate a cost-per-success example; distinguish a rate, a count and a causal claim | Work through small numerical examples; engineering adds linear algebra, calculus and introductory ML before advanced training |
| ML understanding | Explain training versus inference, overfitting and a held-out evaluation | Explain why a plausible output can be wrong and why a demo is not a release decision | Read the introduction and transformer overview in [Hugging Face, chapters 1–4][S2]; fill introductory deep-learning gaps first |
| Decisions and experience | Explain one real design trade-off and how you checked it | Explain one real decision, your authority, alternatives and observed result | Gather a real example and identify missing evidence; never manufacture a behavioural story |

Score each attempt using the rubric below. If a prerequisite scores 0 or 1, use a remediation week and retry a different example. Leadership does not require implementing a transformer; engineering cannot substitute a fluent explanation for running and testing code. A new field may require several remediation weeks. Follow the slower route when that happens.

## 2. Decide what deserves depth

**P0:** establish a usable baseline before the final mock. **P1:** add depth after P0, especially when role responsibilities support it. **P2:** optional specialism unless the target role makes it central. These are curriculum priorities, not market-frequency rankings. Even P2 topics get a brief recognition check; you need not complete their advanced exercises in eight weeks.

| Atlas theme | Engineering | Leadership | Why this order; when to change it |
| --- | --- | --- | --- |
| [LLM fundamentals](themes/llm-fundamentals.md) | P0 | P0 | Mechanisms constrain designs; leadership needs conceptual depth, engineering also shapes and arithmetic |
| [Inference, serving and cost](themes/inference-economics.md) | P0 | P1 | Latency, capacity and cost bound a solution; platform leaders move it to P0 |
| [RAG and retrieval](themes/rag-retrieval.md) | P0 | P1 | A concrete way to study data quality, access and evaluation; knowledge-product PMs move it to P0 |
| [Agents, tools and protocols](themes/agents-tools.md) | P0 | P0 | Actions require explicit state, authority, failure handling and stopping rules |
| [Fine-tuning and post-training](themes/post-training.md) | P1 | P2 | Learn evaluation and simpler alternatives first; model-training roles move it to P0 |
| [Evaluation and observability](themes/evals-observability.md) | P0 | P0 | Needed to decide whether any intervention helped |
| [Safety, security and governance](themes/safety-security-governance.md) | P0 | P0 | Defines permitted behaviour and who accepts residual risk |
| [Multimodal and voice](themes/multimodal-voice.md) | P2 | P2 | Adds modality-specific data and failure modes; move to P0 for a voice or vision remit |
| [AI system design](themes/ai-system-design.md) | P0 | P0 | Integrates quality, dependencies, operations and constraints |
| [Practical coding](themes/coding-practical.md) | P0 | P1 | Tests whether a design survives execution; EMs practise review/debugging, PMs and TPMs may trace behaviour |
| [AI product strategy and metrics](themes/ai-product-strategy.md) | P1 | P0 | Establishes user value and the alternative to building AI |
| [AI platform and operating model](themes/ai-operating-model.md) | P1 | P1 | Clarifies shared services and ownership; EM/platform leaders move it to P0 |
| [Leading engineering teams](themes/engineering-leadership.md) | P2 | P1 | People-management judgement requires its own practice; EMs move it to P0 |
| [Programmes and delivery](themes/program-delivery.md) | P1 | P0 | Makes uncertain work, dependencies and launch decisions explicit |
| [Applied and customer scenarios](themes/applied-scenarios.md) | P0 | P0 | Checks transfer from definitions to an unfamiliar problem |
| [Payments and regulated domains](themes/domain-payments-fintech.md) | P2 | P2 | Needs domain-specific failure and authority models; promote only for a relevant remit |
| [Behavioural and values](themes/behavioral-values.md) | P0 | P0 | Real examples reveal judgement, accountability and learning |

Choose one role emphasis. **PM/product:** deepen discovery, value metrics, UX and experimentation. **EM/platform:** deepen architecture, reliability, cost, team development and operating ownership. **TPM/programme:** deepen dependency maps, decision records, readiness and rollout coordination. These are emphases, not exemptions from shared P0 work. Use the actual role description and dated company evidence to choose electives; a title alone is insufficient.

Do not copy radar percentages into your timetable. The [radar](radar.md) has 79 postings: 17 engineering and 62 leadership. Engineering is suppressed below the minimum of 20; the published leadership sample leans towards fintech and business software. Its 40% domain figure does not make payments a universal prerequisite. The [methodology](METHODOLOGY.md) explains these limits.

## 3. Use a practice loop with evidence

Before reading, answer aloud or sketch a solution from memory. Read the relevant source section and the atlas checklist, then correct the explanation or implementation. Obtain feedback from a peer, tests or comparison with the cited material. Log the mistake and its cause. Retry without notes after a delay, using a changed constraint; mix in older questions each week.

Retrieval and spacing have support in learning research ([vocabulary experiment][S8], [science-text experiment][S9], [research review][S10]), but these studies do not establish AI-interview outcomes or this timetable. A retry after roughly two days and again the following week is a practical scheduling choice, not a scientifically optimal interval. Example answers are feedback material, not scripts to memorise. If using an AI critic, verify its objections against sources or tests; its score is not evidence by itself.

| Score | Observable evidence |
| --- | --- |
| 0 | Cannot produce a coherent answer or working approach; critical misconception remains |
| 1 | Recalls terminology but needs prompts, misses a key mechanism or cannot check the result |
| 2 | Independently explains or implements the mechanism, states assumptions and a trade-off, and supplies a relevant check |
| 3 | Also handles a changed constraint, finds a failure case and explains when the approach should not be used |

Apply the rubric to each weekly output and question attempt. A weekly gate needs **at least 2 on its output and on a delayed attempt**, plus the row's concrete check. Do not average away a permission leak, an invented behavioural claim or a broken correctness test: fix it and retry. Record date, question/topic, output, score, feedback and next retry. The threshold is an editorial learning rule, not a hiring predictor.

Budget a typical week as 1½ hours reading, 2½–3½ building or analysing, 1 hour closed-book explanation and 1–2 hours feedback and delayed retries. Select about five new priority questions each week, starting with numbers 1–40, and revisit older weak ones. Listed ranges are candidate pools, not extra assignments: choose relevant anchors from them and carry unused questions into lighter or final weeks. Cross-track questions are optional substitutes, not additional quota. By the final mock, attempt questions 1–40 of your own track once, plus the ones from 41–70 that your target role needs; for P2 this may be only a brief recognition check. Unresolved weak areas remain visible rather than being declared complete.

## 4. Engineering: eight-week baseline

Build one small document assistant over public or invented documents. Keep its scope narrow enough to test. Introduce access rules and a failure list from the first week; week 6 deepens them rather than introducing safety late. Each week's source selection is a reading slice, not an instruction to finish the entire course.

| Week | Read and practise | Deliverable and acceptance gate |
| --- | --- | --- |
| 1 — foundations | [Hugging Face][S2], chapters 1–4 transformer/model/tokenizer sections; E1–3, attention and KV cache; E38, causal attention; E41–42 and E57, experts, latent attention and fast exact attention | Small CPU attention calculation with a causal mask; a shape and memory worksheet. Tests show that future tokens cannot affect earlier outputs; explain the memory assumptions without notes |
| 2 — evaluation first | [FSDL bootcamp][S3], LLMOps; E14, retrieval versus generation evaluation; E27–29, judges and release gates; E51–52 and E68–69, grounding and reasoning evaluation; E59, a reported regression | An error taxonomy and 30–50 public or synthetic cases, with expected evidence and separate development/check subsets. Manually inspect disagreements; distinguish retrieval failure from answer failure and state sampling limits |
| 3 — retrieval | [FSDL bootcamp][S3], augmented language models; E12–16, E46–47 and E66, and the readings linked from [RAG](themes/rag-retrieval.md); E58, questions over a warehouse | Compare a lexical baseline with one retrieval change. Record relevance, answer support and latency on the same cases. Demonstrate a denied-access and a stale-document case; keep evaluation cases separate from tuning |
| 4 — actions | [Building effective agents][S5], workflows versus agents, tool interfaces and stopping; E18–21; E40, asynchronous batches; E48–50, MCP, memory and multi-agent work; E55 and E60, the agent loop and reversible actions | A bounded tool workflow with a stubbed external service. Tests cover malformed arguments, timeout, retry and stop conditions; show that retries do not silently repeat a consequential action |
| 5 — serving and architecture | [FSDL bootcamp][S3], deployment/LLMOps; E6–11 and E34–37, system design; E43–45, E53–54, E56 and E70, caching, reasoning budgets, a model API, latency; follow the questions' primary reading | Capacity/cost worksheet and architecture diagram. Label measured versus assumed inputs, trace a request and diagnose an injected delay; compare two designs under the same quality requirement |
| 6 — risk and release | [NIST profile][S7], overview and relevant actions under Govern/Map/Measure/Manage; E28, E30–31; L1–4, trust boundaries | Threat model, minimal trace record, rollback plan and release checklist. Demonstrate denied tool access and one failed release check; identify who can stop deployment and what traces must not retain |
| 7 — adaptation or specialism | [Hugging Face][S2], relevant chapters 10–12; E22–26 and E61–65, adaptation, training memory and reinforcement learning. For voice/vision, use E32–33 and [multimodal readings](themes/multimodal-voice.md) instead of a training implementation | A decision memo comparing prompting, retrieval and adaptation, or a modality-specific test plan. Tie the choice to an observed failure; include a cheaper alternative and a regression check. A training run is optional |
| 8 — transfer and mock | Remaining engineering priorities, including E67, owning AI-assisted code; [applied scenarios](themes/applied-scenarios.md); [behavioural questions](themes/behavioral-values.md) | Demonstrate the assistant, defend an unfamiliar design constraint and explain a real past mistake. Peer/test feedback identifies remaining gaps; delayed retry meets the rubric without reading an example answer |

The 30–50 cases are a small learning exercise, not statistical proof of quality, safety or deployment readiness. A production claim needs a suitable sampling design, larger evidence where needed and domain-specific review.

**No GPU option:** use tiny arrays and CPU tests, lexical retrieval, static documents, recorded sample outputs and deterministic tool stubs. A permitted hosted model is optional; set a spending limit. Stubs test orchestration, not model quality. A worksheet is an estimate, not a serving benchmark. State which capabilities you have not exercised.

**Advanced branch:** after the prerequisites, use [Stanford CS336][S1] assignments on basics, systems, scaling, data and alignment. Choose the assignment matching a real gap; the full course sits outside this eight-week budget. Systems and training work may require compute and stronger PyTorch/mathematical preparation. Reading solutions is not equivalent to completing assignments.

## 5. Leadership: eight-week baseline

Use one fictional or public product case throughout. Produce decision documents that another person could challenge. Keep actual career examples separate and truthful; a simulated product case cannot become a claimed professional achievement.

| Week | Read and practise | Deliverable and acceptance gate |
| --- | --- | --- |
| 1 — problem and baseline | [PAIR][S6], user needs and success; [FSDL teams/PM][S4], product design; L6–9; L65–66, an expensive MVP and enterprise discovery | One-page opportunity brief: user, task, current workaround, outcome and non-AI alternative. Explain what observation would make you stop; distinguish evidence from assumptions |
| 2 — metrics and evaluation | [PAIR][S6], evaluating success and feedback; L10–15; L44–45, an answer engine's metric and evaluation without customer data; E14, stage evaluation | Metric tree and a 30–50-case exercise set with failure labels. Separate adoption, task success, quality and harm; explain why an engagement increase might be misleading |
| 3 — technical judgement | [Hugging Face][S2], chapter 1 concepts; [FSDL bootcamp][S3], augmentation; L29–34; L41–43, model choice, agent use cases and pricing; L52, L64 and L70, customer engagements | Options memo for a customer pilot: retrieval, prompting, adaptation or no AI. Include data access, integration, latency and cost assumptions; defend one rejected option under a changed constraint |
| 4 — safety and authority | [NIST profile][S7], relevant risk categories and proposed actions; [PAIR][S6], control and failure; L1–5; L53 and L67–68, control exceptions, moderation and interpretability | Risk register with owners, controls and residual-risk decisions. Tabletop a wrong answer and an unauthorised action; identify a stop condition and an escalation path. This is not legal certification |
| 5 — operating model | [FSDL teams/PM][S4], roles and team structure; L16–24; L46–49 and L59–61, review, hiring, quality, team scale and shared platforms; L69, shared data access | PM: product/platform ownership map. EM/platform: team charter and a real coaching example. TPM: dependency and decision-owner map. Each must resolve an ambiguous responsibility and explain how an unresolved dispute escalates |
| 6 — delivery under uncertainty | [FSDL teams/PM][S4], ML project planning; [Building effective agents][S5], simplest justified design; L25–28; L50–51 and L57–58, research milestones, readiness, a misjudgement and a slipped dependency | Phased pilot and launch plan with exit criteria, rollback and named decision roles. Replan after a dependency slips or quality regresses; preserve the user outcome instead of defending only the date |
| 7 — role-specific depth | PM: [PAIR][S6], trust/mental models and L13–14. EM/platform: L17–23 and L63 plus E9–11. TPM: L26–28 plus [programme scenarios](themes/program-delivery.md). Relevant domain roles add L35–37 and L62 | A challenged decision: PM tests a UX/metric hypothesis; EM/platform resolves cost/reliability/ownership; TPM runs a readiness tabletop. Show evidence, alternative, owner and reversal condition; use the domain branch only when relevant |
| 8 — leadership mock | L38–40, L54–56 and remaining leadership priorities; [behavioural questions](themes/behavioral-values.md) | Present a five-minute recommendation, answer follow-ups and discuss two real examples. Separate your actions from the team's and observed results from guesses. Retry the weakest case after feedback; leave unmet gates recorded |

## 6. Adjust the pace

**Two-week triage:** this is gap selection, not the eight-week curriculum compressed. Week 1: run the entry check, select two P0 weaknesses using the target role, attempt 8–10 questions and build one small diagnostic output. Week 2: correct it, practise two real behavioural examples, run one mock and retry the weakest answers. Defer electives and advanced training. Record what remains untested; do not claim mastery because an interview is near.

**Twelve weeks or longer:** reserve weeks 1–2 for prerequisites, spread baseline weeks 1–6 across weeks 3–10, and use weeks 11–12 for an elective and the final mock. Keep delayed retrieval each week. Add more time if the prerequisite or output gates fail; beginners may need a separate introductory course before starting this route.

Completion means a record of attempts, corrected outputs and successful delayed retries for the chosen P0 scope. It does not mean a course certificate, guaranteed interview success or readiness to deploy the practice system.

## Research notes and limits

Sources checked **2026-09-28**. The priorities, weekly workload, exercise sizes, retry intervals and rubric thresholds are this atlas's editorial design. Course providers inform subject coverage; they do not endorse this plan. Older material is useful for concepts, not current API instructions. Follow current documentation before running examples.

| Source | Date/version | What informed the plan; limitation |
| --- | --- | --- |
| [S1: Stanford CS336][S1] | Spring 2026 | Prerequisite depth and optional assignment sequence; an advanced course, not a universal entry requirement |
| [S2: Hugging Face LLM course][S2] | Live, undated | Foundation, data/tokenizer and advanced reading slices; requires Python, recommends prior introductory deep learning |
| [S3: FSDL LLM bootcamp][S3] | Spring 2023 | System lifecycle and augmentation coverage; historical tooling |
| [S4: FSDL teams and PM][S4] | 2022-09-26 | Roles, uncertain delivery and product decisions; not evidence of current hiring practice |
| [S5: Building effective agents][S5] | 2024-12-19 | Baselines before added autonomy; provider guidance, tooling has evolved |
| [S6: Google PAIR Guidebook][S6] | Published 2019-05-08; updated 2021-05-18 | Human-centred questions about needs, trust and failure; linked for reading, worksheets are not reproduced |
| [S7: NIST AI 600-1][S7] | 2024-07-26 | Voluntary generative-AI risk profile; not a compliance certificate or legal advice; [full text](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) |
| [S8: Karpicke & Roediger][S8] | 2008 | Retrieval experiment with vocabulary learning; does not test technical interviews |
| [S9: Karpicke & Blunt][S9] | 2011 | Retrieval experiment using science texts; does not validate this curriculum's transfer or timing |
| [S10: Dunlosky et al.][S10] | 2013 | Research synthesis supporting practice testing and distributed practice; not a primary experiment or a guarantee for every task |

[S1]: https://cs336.stanford.edu/
[S2]: https://huggingface.co/learn/llm-course/chapter1/1
[S3]: https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/
[S4]: https://fullstackdeeplearning.com/course/2022/lecture-8-teams-and-pm/
[S5]: https://www.anthropic.com/engineering/building-effective-agents
[S6]: https://pair.withgoogle.com/guidebook-v2/
[S7]: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
[S8]: https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf
[S9]: https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf
[S10]: https://www.psychologicalscience.org/journals/pspi/1529100612453266/
