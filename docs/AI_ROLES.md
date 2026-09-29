# AI roles: responsibilities and preparation

[English](AI_ROLES.md) · [Русский](ru/AI_ROLES.md) · [Learning path](LEARNING_PATH.md)

Choose a role by the work you want to own. AI hiring combines established professions with changing specialisms; these six families are not six newly invented occupations. Titles overlap, and an “AI engineer” may build customer applications, operate infrastructure or conduct experiments. The useful distinction is the deliverable, the decision authority and the failure the person must resolve.

This is a **2026-09-29 snapshot**, based on public employer descriptions checked that day. Their publication dates are unknown. These examples illustrate responsibilities at two frontier-model employers; they are not a representative market survey or a guarantee that a vacancy remains open. Preparation routes and exercises below are editorial recommendations. Job descriptions do **not** establish interview stages or prove that linked questions were asked for these roles; each question retains its own provenance.

## 1. Forward Deployed Engineer (FDE)

**FDE means Forward Deployed Engineer**; “Forward Deployed AI Engineer” makes the AI specialism explicit. The central responsibility is getting a useful system working in a customer's environment. OpenAI's Seattle posting spans discovery, implementation and production rollout, with adoption and workflow impact as outcomes. Anthropic's Munich posting combines embedded customer work, production applications, reusable deployment patterns and feedback to product teams. Together they support a delivery role with substantial engineering and customer contact. [OpenAI FDE][S1] · [Anthropic FDE][S2]

Expected evidence therefore spans both code and decisions: a scoped workflow, integrated application, evaluation results, rollout plan and a supportable handoff. The postings require production engineering, communication under ambiguity and understanding of customer systems. Anthropic also names agent development and evaluation frameworks. Travel, languages, seniority and account responsibilities depend on the particular posting; a requirement in one location is not a universal FDE qualification. [OpenAI FDE][S1] · [Anthropic FDE][S2]

For preparation, distinguish four boundaries. A solutions architect may concentrate on design and technical adoption; an FDE remit should be checked for implementation ownership. Presales may centre on winning an evaluation; deployment work continues into operational use. A product engineer usually improves a shared product; an FDE also handles a customer's local integration constraints. A consultant can do overlapping work: the title alone says little about who maintains the result or turns it into reusable product capability. These are comparison questions, not rigid employer-wide definitions.

**Preparation route:** take the engineering [learning path](LEARNING_PATH.md), deepen [customer scenarios](themes/applied-scenarios.md), and practise [enterprise access design](themes/ai-system-design.md#sd-enterprise-rag), [safe ERP writes](themes/agents-tools.md#agt-erp-writes) and [release gates](themes/evals-observability.md#eval-release-gate). Add a short discovery conversation: identify the user, current workaround, permitted data, useful outcome and owner after launch.

**Practice deliverable:** build a small fictional service workflow with one external integration stub. Demonstrate a denied permission, a timeout after a possible write, and a quality regression. Explain the acceptance evidence and handoff. A polished demo without those checks is incomplete preparation. For a target vacancy, clarify who owns implementation, production support, commercial decisions and travel before choosing your strongest real examples.

## 2. Applied AI / agent product engineer

This family turns model capabilities into usable workflows. Anthropic's **Product Engineer, Computer Use** is one concrete variant: it combines interfaces, agent runtime and backend delivery with instrumentation and robustness work. OpenAI's **Codex Core Agents** posting illustrates a neighbouring infrastructure-heavy variant, including orchestration, sandboxing and persistent state. “Agent engineer” alone does not distinguish these scopes. [Computer Use][S3] · [Core Agents][S4]

**Deliverables and skills:** working product behaviour, tool integrations, observable execution and recoverable failures; the mix of full-stack development and distributed systems depends on the variant. For preparation, distinguish adapting an application around a model from changing model weights, and a user-facing workflow from the shared runtime beneath many workflows.

**Preparation route:** engineering baseline, then [agents](themes/agents-tools.md), [retrieval](themes/rag-retrieval.md) when external knowledge matters, and [practical coding](themes/coding-practical.md). Practise [tool retries](themes/agents-tools.md#agt-retries) and [human approval](themes/agents-tools.md#agt-approval). Build a bounded agent beside a simpler fixed workflow; compare task success, latency, cost and failure recovery on the same cases. Defend whether the extra autonomy earns its complexity.

## 3. AI evaluation and reliability engineer

The defining output is trustworthy evidence about system behaviour. Anthropic's **Research Engineer, Post-Training Model Evaluations** owns measurement strategy, live evaluation monitoring, regression investigation and reports that inform training and release decisions. It asks for Python and evaluation experience; statistics and experimental design are additional relevant strengths. This particular role concerns model training, rather than every form of application reliability. [Post-Training Model Evaluations][S5]

Use the broader family label carefully: evaluation, quality engineering and service reliability overlap but have different units of failure. A service can be available while producing poor answers. An application-quality role may study real task outcomes; the cited model-evaluation role studies behaviour during training. Ask what decisions the measurements actually control.

**Preparation route:** deepen [evaluation and observability](themes/evals-observability.md), especially [benchmark/product mismatch](themes/evals-observability.md#eval-benchmark-mismatch) and [model-upgrade complaints](themes/evals-observability.md#eval-upgrade-complaint). Produce a versioned test set, repeatable runner and regression report. Separate sampling changes, noisy measurements and a real behavioural change; show an important slice that an aggregate score could conceal. Explain what additional evidence a release decision would require.

## 4. Inference / AI platform engineer

This family makes AI computation and shared services usable under performance and operating constraints. Anthropic's **Performance Engineer, Inference Systems** investigates across serving layers, measures throughput and latency, and checks output correctness across hardware and configurations. It explicitly works with component owners rather than owning every component. OpenAI's agent-platform example adds shared execution and rollout infrastructure. [Inference Systems][S6] · [Core Agents][S4]

**Deliverables and skills:** a diagnosed bottleneck, validated optimization, useful telemetry and reliable shared interfaces. Profiling, numerical reasoning and distributed-systems knowledge matter; writing accelerator kernels is one specialism, not a requirement to infer from every platform title. Distinguish model-serving performance from application orchestration when reading the remit.

**Preparation route:** engineering baseline with extra [inference depth](themes/inference-economics.md), [latency metrics](themes/inference-economics.md#inf-latency-metrics) and [runtime comparison](themes/inference-economics.md#inf-runtime-choice). Produce a load-test report that fixes workload and quality requirements, separates queueing from execution, and tests a tail-latency regression. A platform-lead variant also needs [operating ownership](themes/ai-operating-model.md); a cost worksheet alone does not prove serving performance.

## 5. AI product leadership

The output is a defensible product decision and measurable customer value. Anthropic's **Product Manager, New Markets and Monetization** provides a platform-oriented example: market choices, commercial design, instrumentation and outcome ownership, with technical fluency and direct analysis. Its scope includes several alternative focus areas, not a requirement that one person own them all. [Platform product management][S7]

Product leadership can be senior individual-contributor work; a PM title does not establish people management. Engineering leadership separately owns technical and team decisions. For preparation, identify the actual authority over priorities, launch criteria and resources, and distinguish product outcomes from model benchmark progress.

**Preparation route:** the leadership [learning path](LEARNING_PATH.md), [AI product strategy](themes/ai-product-strategy.md), [capability versus cost](themes/ai-product-strategy.md#prod-capability-cost) and [feature metrics](themes/ai-product-strategy.md#prod-ai-feature-metrics). Write an opportunity brief and decision memo covering a non-AI alternative, user outcome, evaluation, economics, rollout and stop condition. Defend a priority change when quality improves but task completion falls. Add people-management practice only when the role actually includes it.

## 6. Research engineer

Research engineering combines experiments with the software that makes them possible. Anthropic's **Research Engineer, Pretraining** covers architecture, algorithms, data and optimization, scientific experiments and training infrastructure. It includes independent research projects, so “engineer implements, scientist thinks” is a misleading division. This posting names advanced education; requirements should be checked per team, not generalized to all research-engineering roles. [Pretraining][S8]

**Deliverables and skills:** reproducible experiments, training or data code and an analysis of what changed and why. The key distinction from applied product work is investigating or improving model capabilities and training methods, although teams overlap.

**Preparation route:** strengthen mathematics, ML and [LLM fundamentals](themes/llm-fundamentals.md), then the learning path's advanced branch and [post-training](themes/post-training.md) where relevant. Practise [method selection](themes/post-training.md#pt-method-choice) and [LoRA experiments](themes/post-training.md#pt-lora). Reproduce a small result with a baseline, controlled ablation and held-out check. State compute limits and failed hypotheses. The atlas is a starting map; eight weeks of application exercises do not establish frontier research readiness.

[S1]: https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/
[S2]: https://job-boards.greenhouse.io/anthropic/jobs/5391016008
[S3]: https://job-boards.greenhouse.io/anthropic/jobs/5238637008
[S4]: https://openai.com/careers/software-engineer-codex-core-agents-san-francisco/
[S5]: https://job-boards.greenhouse.io/anthropic/jobs/5198255008
[S6]: https://job-boards.greenhouse.io/anthropic/jobs/5224564008
[S7]: https://job-boards.greenhouse.io/anthropic/jobs/5386182008
[S8]: https://job-boards.greenhouse.io/anthropic/jobs/5119713008
