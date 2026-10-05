# Engineering research: two complementary routes

[English](ENGINEERING_RESEARCH.md) · [Русский](../ru/research/ENGINEERING_RESEARCH.md) · [Learning path](../LEARNING_PATH.md)

Checked **2026-10-05**. The editorial decision is to add [AI-assisted coding](../learning/AI_ASSISTED_CODING.md) and [Production AI engineering](../learning/PRODUCTION_AI_ENGINEERING.md) inside the existing Engineering track. One practises ownership of a coding session; the other practises a bounded model-backed service. The existing eight-week baseline remains useful for broad foundations. This report supports curriculum design, not new claims about company interviews.

## Inputs and access boundary

[Hello Interview's AI coding guide](https://www.hellointerview.com/learn/ai-coding/overview/introduction) supplies a useful topic inventory for coding-session practice. Its company claims remain secondary unless separately supported. The sidebar contains **30 entries including Introduction**: four overview pages, five fundamentals, seven pattern pages, one example-session entry and thirteen problem breakdowns. We inspected accessible material on 28 entries; two article bodies were unavailable. A visible heading is not evidence that the underlying section was read. No login, subscription, practice submission or access bypass was used.

| Inventory group | Entries | What was accessible |
| --- | --- | --- |
| Overview (4) | [Introduction](https://www.hellointerview.com/learn/ai-coding/overview/introduction), [Interview Formats](https://www.hellointerview.com/learn/ai-coding/overview/interview-formats), [Patterns](https://www.hellointerview.com/learn/ai-coding/overview/patterns), [How to Prepare](https://www.hellointerview.com/learn/ai-coding/overview/how-to-prepare) | Public bodies for three; Patterns repeatedly timed out, so inventory only |
| Fundamentals (5) | [Codebase Orientation](https://www.hellointerview.com/learn/ai-coding/fundamentals/codebase-orientation), [Planning Your Approach](https://www.hellointerview.com/learn/ai-coding/fundamentals/planning-your-approach), [Driving the AI](https://www.hellointerview.com/learn/ai-coding/fundamentals/driving-the-ai), [Verification & Testing](https://www.hellointerview.com/learn/ai-coding/fundamentals/verification-and-testing), [Communication](https://www.hellointerview.com/learn/ai-coding/fundamentals/communication) | Public article text; no Premium boundary observed in the retrieved bodies |
| Patterns (7) | [Graph Search](https://www.hellointerview.com/learn/ai-coding/patterns/graph-search), [Topological Sort](https://www.hellointerview.com/learn/ai-coding/patterns/topological-sort), [Backtracking](https://www.hellointerview.com/learn/ai-coding/patterns/backtracking), [Greedy](https://www.hellointerview.com/learn/ai-coding/patterns/greedy-algorithms), [Dynamic Programming](https://www.hellointerview.com/learn/ai-coding/patterns/dynamic-programming), [Strings](https://www.hellointerview.com/learn/ai-coding/patterns/string-matching), [Data Structures](https://www.hellointerview.com/learn/ai-coding/patterns/data-structure-design) | Introductory excerpts and headings; all seven show a Premium continuation |
| Example session (1) | [Example Sessions](https://www.hellointerview.com/learn/ai-coding/open-ended-sessions) | Repeated timeout; inventory only, no session analysis |
| Problems (13) | [Battleship](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/battleship), [Inventory Packer](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/inventory-packer), [Spell Checker](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/spell-checker), [Card Game](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/card-game), [Friend Recommender](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/friend-recommender), [Maze Solver](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/maze-solver), [Route Planner](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/route-planner), [Task Scheduler](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/task-scheduler), [Word Container](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/word-container), [Connect Four](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/connect-four), [Kitchen Orders](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/kitchen-orders), [Maximize Unique Characters](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/maximize-unique-chars), [Nonogram Solver](https://www.hellointerview.com/learn/ai-coding/problem-breakdowns/nonogram-solver) | Public excerpts and headings; all thirteen show a Premium continuation. Implementations, full benchmarks and paid explanations were not assessed |

The [AI4DEV roadmap](https://ai4dev.ru/posts/ai-engineer-roadmap/) is a broad application-engineering checklist with an anecdotal interview basis. It is useful for topic discovery, not a representative market sample. Its rigid role boundaries and universal interview language should not become Atlas requirements. The curriculum replaces checklist completion with observable outputs.

An unsourced eight-page competence-map PDF was also supplied for analysis. Its overlapping screenshots depict one map rather than eight independent documents. Visual inspection found software foundations, ML/LLM concepts, retrieval, tools, operations and mathematics. Original authorship, publication date and its relationship to the web article could not be established. Treat it only as an input for coverage questions, not independent corroboration. The PDF and its images are not republished.

## Critical comparison and corrections

The coding guide is strongest as a prompt to practise work in an unfamiliar repository under time pressure. The competence roadmap is broader but does not by itself supply a learning sequence, executable acceptance tests or calibrated proficiency levels. Neither establishes that a curriculum graduate is ready for production or that a particular employer will permit AI tools. The following decisions are Atlas editorial synthesis.

| Issue to resolve | Primary check or existing evidence | Curriculum decision |
| --- | --- | --- |
| AI assistance and accountability | [Canva's interviewer account](https://www.canva.dev/blog/engineering/ai-interview-success/) describes ownership and judgement; [Sierra](https://sierra.ai/blog/the-ai-native-interview) describes building and review | Practise both; preserve the source-specific constraints in existing questions. Check the actual employer's rules |
| “Valid JSON” versus correct service behaviour | [Claude structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) documents refusal and completion exceptions | Validate status, schema, evidence references and business rules; bound recovery |
| “Deterministic evals” | [Anthropic's eval article](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) distinguishes code, model and human graders | Separate deterministic assertions from repeated model trials and calibrated judgements |
| Sanitisation as security | [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) includes least privilege and trust separation | Enforce authority outside the model and test indirect injection |
| MCP as sufficient integration safety | [MCP security guide](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) identifies authorisation and transport risks | Require a trust-boundary and revocation account, not protocol familiarity alone |
| More retrieval machinery means better quality | Existing [retrieval](../themes/rag-retrieval.md) and [evaluation](../themes/evals-observability.md) questions already require comparisons | Start with a lexical baseline; add one justified change and evaluate it on held-out cases |
| Tracing means retaining everything | Existing [observability](../themes/evals-observability.md) and [security](../themes/safety-security-governance.md) coverage | Record versions, actions, results and resource use with minimised content; do not require private reasoning traces |

## Initial P0 repository coverage and gaps

The initial audit inspected the learning path, generated Engineering start page and theme entries against YAML at `6648af25ee5f04f1141b96a81900032af06a460d`. The table records that baseline and the original curriculum proposal, not the current answer inventory. These are existing anchors, not new questions. Their different evidence markers remain unchanged.

| Existing coverage | Current limitation | Added practice |
| --- | --- | --- |
| [AI-assisted build](../themes/coding-practical.md#code-ai-assisted-build) and [agent PR review](../themes/coding-practical.md#code-agent-pr-review): company-backed Sierra entries | Two question outlines do not form a progression through reading, scoped change and review | Four-week route with separate bugfix, feature and review outputs |
| [Product structure](../themes/coding-practical.md#code-product-structure): candidate-reported Cursor task, targeted syntax assistance only | Not evidence for unrestricted AI use | A restricted-assistance rehearsal preserving that distinction |
| [Session choices](../themes/coding-practical.md#code-agent-session-choices): participant account with unnamed employers | No universal best model or workflow established | Context brief, budget and recorded acceptance/rejection decisions |
| [Ownership](../themes/coding-practical.md#code-ai-assisted-ownership): Canva-backed priority question | One answer cannot demonstrate executable judgement | Explain the diff, run independently chosen probes and defend omissions |
| [Practical coding](../themes/coding-practical.md), including cache and scheduler questions | No compact seven-family choice-and-counterexample map in the existing learning path | Original small drills with public algorithm reading; no paid-problem reconstruction |
| Existing eight-week Engineering baseline; [retrieval](../themes/rag-retrieval.md), [agents](../themes/agents-tools.md), [cost](../themes/inference-economics.md), [security](../themes/safety-security-governance.md) | Broad topic coverage; experienced application developers need a tighter service-lifecycle route | Eight weeks from task/baseline to contracts, evals, retrieval, tools, operations, release and defence |
| Existing 0–3 rubric and delayed retries | No standard runnable artifact or automatic assessment for these new routes | Reuse the rubric and specify manual/test evidence now; executable labs and evaluators remain future work |

## Content update — 2026-10-05

The subsequent authorised content phase filled all **30 missing-reading entries in the ten technical themes**, added **12 EN/RU answers** to existing questions with Engineering priorities **71–82**, and strengthened the five existing AI-assisted coding outlines. It added **24 primary reference records** for learning support, not interview corroboration. No new formal Engineering question was added: the thin Engineering radar and curriculum guides do not justify inventing employer questions.

The two routes now use questions, explanations, counterexamples and checklists. All seven algorithm families and eight production modules remain; Python assignments, runnable labs and project implementation are deferred by the maintainer. New answers cover bounded coding, structured output and authority, goal drift, harness evaluation, scarce labels, action consequences, rollback, document extraction and index freshness. The source registry records checked URLs and dates. New reading spans official language/database/protocol documentation, primary research and health, legal-service and safety guidance; these last sources have explicit domain limits and do not replace professional review.

The five coding entries preserve their evidence and IDs, including Cursor’s restricted syntax assistance and Sierra’s evolving review format. The original access inventory below is unchanged: new technical reading does not retroactively make Premium bodies accessible or independently corroborate the supplied map. See the [current coverage addendum](ATLAS_COVERAGE_AUDIT.md) for integrated counts.

## Source register for this report

All rows were retrieved **2026-10-05**. “Public” describes access at the check, not an open-content licence. These document references do not automatically add entries to the core YAML source registry or strengthen interview-evidence markers.

| Source / publisher | Published or version | Access and status | Evidence role |
| --- | --- | --- | --- |
| [AI coding guide / Hello Interview](https://www.hellointerview.com/learn/ai-coding/overview/introduction) | Undated live guide | Mixed: 28 entries inspected within access limits, 2 unavailable; details above | Secondary preparation guide; all pages share one publisher |
| [AI engineer roadmap / AI4DEV](https://ai4dev.ru/posts/ai-engineer-roadmap/) | 2026-09-05 | Public, checked | Editorial roadmap with anecdotal basis; not market measurement |
| Supplied competence-map PDF | Unknown | Eight overlapping screenshot pages visually inspected; unsourced, not published here | Input only; not counted as independent evidence |
| [AI Interview Success / Canva](https://www.canva.dev/blog/engineering/ai-interview-success/) | 2025-10-20 | Public, checked | First-party interviewer account; Canva-specific |
| [The AI-native interview / Sierra](https://sierra.ai/blog/the-ai-native-interview) | 2026-04-22 | Public, checked | First-party format description; Sierra-specific |
| [Structured outputs / Anthropic](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) | Live, undated | Public, checked | Provider contract documentation, not interview evidence |
| [Demystifying evals / Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 2026-01-09 | Public, checked | Technical account; same publisher as preceding row, not independent corroboration |
| [Prompt injection / OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | LLM01:2025 | Public, checked | Primary project guidance |
| [Security best practices / MCP project](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | 2026-07-28 path | Public, checked; latest URL redirected here | Primary protocol guidance; recheck version before implementation |
| [6.006 / MIT OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) | Spring 2020 | Public index checked | Primary course reading; selected lectures, not a course-completion claim |
| [Algorithms / Sedgewick and Wayne, Princeton](https://algs4.cs.princeton.edu/home/) | Fourth-edition booksite; live | Public, relevant graph/string pages checked | Authors' educational reference |
| [Algorithms / Jeff Erickson](https://jeffe.cs.illinois.edu/teaching/algorithms/) | 2019 textbook | Public index checked | Author's reading for backtracking and greedy methods |

The curriculum workload, drill sizes and gates are editorial choices. No assessment-validity study was performed. Independent final review and repository checks are separate from authors' source inspection; a draft is not a publication decision.
