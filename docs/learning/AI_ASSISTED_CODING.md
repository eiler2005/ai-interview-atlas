# AI-assisted coding: four-week practice route

[English](AI_ASSISTED_CODING.md) · [Русский](../ru/learning/AI_ASSISTED_CODING.md) · [Learning path](../LEARNING_PATH.md) · [Engineering](../start/engineering.md)

This route prepares experienced developers to explain, review and defend code with permitted AI assistance. It sits inside AI Engineering alongside [Production AI engineering](PRODUCTION_AI_ENGINEERING.md). The existing eight-week learning path remains the broad foundation; completing both routes takes additional time.

Allow **four weeks at 6–8 hours per week**, an editorial workload estimate assuming fluency in a language, Git, tests and complexity analysis. It is not measured preparation time or a hiring predictor. The current route uses interview questions, explanations, counterexamples and checklists. Editorial follow-ups are outside the published and radar-generated bank. Python exercises, executable labs and project implementation are deferred by the maintainer's current scope.

## Entry check and working agreement

In 45–60 minutes, explain how you would trace a request in an unfamiliar repository, reproduce a boundary bug and distinguish a relevant failing regression check from an unrelated failure. Explain map, queue and heap operations and their costs. No code submission is required. If you need step-by-step help, review the linked questions before a timed discussion.

Confirm the interview's actual environment, permitted models, network access and context rules. [Canva's account](https://www.canva.dev/blog/engineering/ai-interview-success/) and [Sierra's format](https://sierra.ai/blog/the-ai-native-interview) establish their own practices, not permission elsewhere. Be able to explain your approach with restricted tools. Use public, suitably licensed or invented examples; exclude credentials and personal or employer material.

Describe the observable behaviour, relevant files, constraints and acceptance checks before proposing an AI task. A change is acceptable only after inspection and an independent check. In an interview answer, distinguish checks you would perform from checks you actually performed. Repeated prompting without new evidence is not a diagnosis.

## Weekly sequence

Budget roughly 1 hour for reading, 3–4 hours for question analysis, 1 hour for oral explanation and 1–2 hours for feedback and delayed retries. Review all seven algorithm families; trace two weak cases by hand and defend their invariants. Implementing them is not required.

| Week | Question and explanation | Concrete gate and existing question |
| --- | --- | --- |
| 1 — orientation and bugfix | Explain an expiry bug: a record remains visible exactly at its expiry time. Identify entry point, storage, clock, callers and the time convention; describe the smallest relevant change and regression check. | Give expected outcomes before, at and after expiry, plus empty input. Explain how a caller could bypass the fix. Read [product data structures](../themes/coding-practical.md#code-product-structure), preserving its restricted AI scope. |
| 2 — bounded delegation | Explain batch lookup preserving request order and missing IDs. Divide parsing, behaviour and presentation into reviewable tasks; prepare a short context brief and acceptance checklist. | Trace duplicate IDs, missing IDs and an empty batch; reject one unnecessary abstraction. Defend [session choices](../themes/coding-practical.md#code-agent-session-choices) and [ownership](../themes/coding-practical.md#code-ai-assisted-ownership). |
| 3 — algorithm choice | For every family below, identify applicability and a failure boundary. Work through two counterexamples by hand; compare a baseline with a justified alternative. | State the invariant and time/memory costs. Explain what future runtime measurements would test without calling an estimate a measurement. Revisit [practical coding](../themes/coding-practical.md). |
| 4 — build plan, review and defence | Explain a minimal catalogue feature and review an imagined change adding access scopes to search and batch lookup. Defend the change sequence, verification and omissions. | Identify every entry point needing an access check, a rejected AI suggestion, a performance limit and unverified behaviour. Read questions and answers for [AI-assisted build](../themes/coding-practical.md#code-ai-assisted-build) and [agent PR review](../themes/coding-practical.md#code-agent-pr-review). |

## Editorial follow-up questions and checks

These explanations extend the route; they do not claim additional employer questions.

| Follow-up | A defensible explanation | Check or counterexample |
| --- | --- | --- |
| What belongs in a context brief? | Objective, relevant callers and interfaces, invariants, exclusions and a visible done criterion. Preserve verified decisions and open questions in a handoff. | A repository comment requesting a secret upload is untrusted content, not authority. A summary dropping “preserve order” changes the task. |
| Where should decomposition stop? | A step needs a clear input, observable result and manageable review. Split at interfaces while assigning responsibility for shared state and integration. | Independently changing a response type and its caller can break their contract even when local checks pass. |
| What makes verification independent? | Derive expected behaviour from the contract and a counterexample before accepting the generated change. Another model's agreement is feedback, not a correctness oracle. | If the assistant changes both implementation and expected test output, passing tests can conceal the defect. |
| When should the agent stop? | Stop on exhausted budget, unresolved authority, repeated failure without new evidence or a changed objective. Preserve verified state before restarting. | A write may have succeeded before a timeout; reconcile before repeating it. See [goal drift](../themes/agents-tools.md#agt-goal-drift). |
| How do you defend a result? | Explain the contract, representation, rejected alternative, actual check and remaining gap yourself. Separate proposed checks from performed ones. | A polished demonstration does not establish untested concurrency or access behaviour. Compare [coding harness evaluation](../themes/agents-tools.md#agt-coding-harness). |


## Seven algorithm families: choice, limits and probes

These small examples are conceptual Atlas questions, not reconstructions of a paid problem set. Read only the relevant primary course section: the authors' [Princeton booksite](https://algs4.cs.princeton.edu/home/), [MIT 6.006 notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) and [Jeff Erickson's textbook](https://jeffe.cs.illinois.edu/teaching/algorithms/). None is evidence that an employer asks these drills.

| Family | When it fits; limit | Original example and test probe | Reading slice |
| --- | --- | --- | --- |
| Graph search | Reachability or shortest paths; BFS minimises edge count. With equal non-negative edge costs, that also minimises cost. Dijkstra needs non-negative weights. | Artifact conversion edges A→B cost 9, A→C cost 2, C→B cost 2: fewer hops is not lower cost. Add an unreachable node and a cycle; check path cost, not a particular tie order. | [Princeton, shortest paths](https://algs4.cs.princeton.edu/44sp/); MIT lectures 9–13 |
| Topological ordering | Dependencies in a directed acyclic graph; an ordering alone does not minimise elapsed time with limited workers. | Index stages fetch→parse→publish, plus audit→publish. Insert publish→fetch and require an explicit cycle result. Accept any valid order for independent stages. | [Princeton, directed graphs](https://algs4.cs.princeton.edu/42digraph/) |
| Backtracking | Small constrained choice spaces where partial assignments can be rejected; worst-case search can remain exponential. | Assign three invented checks to two isolated runners with incompatible check pairs. Verify that undo restores state; test an impossible assignment and a node-budget stop distinct from “no solution”. | Erickson, chapter 2, Backtracking |
| Greedy methods | A locally chosen step needs a correctness argument for the objective, or an explicit heuristic label. | Select non-overlapping maintenance windows. Earliest finish works for maximum count, but a single high-value long window can defeat that rule for maximum value. Test touching endpoints under a stated convention. | Erickson, chapter 4, Greedy Algorithms |
| Dynamic programming | Repeated subproblems with sufficient state; state count and transition cost can exceed the budget. | Count sequences of 1- or 3-unit processing steps reaching budget 4: distinguish ordered sequences from unordered combinations. Test zero budget and overflow policy; then change the allowed steps to 2 and 3 and test unreachable budget 1. | MIT lectures 15–18 |
| Strings and parsing | Prefix lookup fits a trie; structured syntax needs a grammar and error policy. A substring search is not a parser. | Index command names `ship`, `shift`, `show`; test shared prefixes and deletion. For a separate `key="a,b"` record, a comma split must not break quoted text. State Unicode and malformed-input rules. | [Princeton, tries](https://algs4.cs.princeton.edu/52trie/) and [substring search](https://algs4.cs.princeton.edu/53substring/) |
| Data-structure design | Choose representation from operation frequency and invariants; fast individual operations do not ensure a correct combined structure. | Store expiring artifact IDs with lookup and earliest-expiry removal. Update an existing ID, then process its stale heap entry; it must not delete the new version. Test equal expiry times and empty state. | MIT lectures 2, 4 and 8; [Atlas cache question](../themes/coding-practical.md#code-lru) |

## Evidence of progress

Use the [existing 0–3 rubric](../LEARNING_PATH.md#3-use-a-practice-loop-with-evidence): 0 is incoherent or critically wrong; 1 needs help or lacks a valid check; 2 independently explains or implements the mechanism with assumptions, a trade-off and a check; 3 also handles changed constraints and failure cases. Require **at least 2 for the weekly output and a delayed attempt**, plus its concrete gate. A failed correctness or access check blocks completion regardless of the average score.

Retry the weak part without notes after roughly two days and the following week, changing a boundary condition or constraint. Record date, output, feedback, score and next retry. In the final defence, explain what the assistant proposed, what you accepted, how you checked it and what would invalidate the solution. A passing mock shows demonstrated practice on that task, not production readiness or a predicted hiring result.

For how the route was selected and what could actually be read, see [Engineering research](../research/ENGINEERING_RESEARCH.md). The current content expansion adds answers, reading and explanation checklists. Executable labs, Python assignments and an AI evaluator remain deferred.
