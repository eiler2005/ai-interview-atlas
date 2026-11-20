# Worked preparation for reported FDE questions

[English](fde-forum-answers.md) · [Русский](../ru/careers/fde-forum-answers.md) · [Reports and evidence limits](fde-forum-reports.md) · [FDE guide](fde.md#interview-prep)

**The prompts come from the five accounts in the [forum section](fde-forum-reports.md); the solutions, contracts, examples, follow-ups and checks below are ours.** They are not official answers or recovered employer rubrics. A missing specification remains missing. When we choose rules to make an exercise executable, we label them as practice assumptions. Behavioral answers explain how to use your own experience; they do not supply a fictional candidate story. The accounts remain unverified participant reports, with the dates and role limits recorded on the evidence page.

Use each section in three passes: explain the decision aloud, work the example, then answer the follow-up without reading. Code is illustrative Python; production concerns are discussed separately.

| Reported topic | Worked preparation |
| --- | --- |
| Interest-sharing design and additional features | [1. Product decomposition](#interest-app) |
| Incomplete `search(user_id, users)` task | [2. An explicit practice contract](#search-contract) |
| Meeting history and interest-array optimisation | [3. Indexes and prefix search](#search-indexes) |
| Customer experience, API experience, languages | [4. Recruiter questions](#recruiter) |
| Why company, government, FDE and computer science | [5. Motivation](#motivation) |
| Internship details, highs/lows and return offers | [6. Experience deep dive](#experience) |
| Recipe matching and cook booking | [7. Matching and transactions](#recipes) |
| Multiplayer War | [8. State and tie rules](#war) |
| Ownership BFS, shares and cycles | [9. Traversal versus ownership](#ownership) |
| Elevator design | [10. State and scheduling](#elevator) |
| Daily Temperatures variation | [11. Canonical stack exercise](#temperatures) |
| Connected datasets; functions from documentation | [12. Learning an unfamiliar interface](#learning) |

## <a id="interest-app"></a>1. Decompose an interest-sharing application

**Reported:** the March 2025 Palantir account asks for interest sharing and later asks what additional functions the design needs. It does not specify a social network, recommendation model or scale.

**A worked answer.** Start with “Who shares what, with whom, and what successful interaction should follow?” For a practice version, assume an opt-in community where members list interests and discover other members with a shared interest. The first complete flow is: edit interests → find eligible people → inspect a profile → request contact. Model `User`, `Interest`, `UserInterest`, `ContactRequest` and `Block`. Store interest IDs separately from display labels, so renaming a label does not break matches. Keep membership, visibility and blocking checks on the server.

`PUT /me/interests` validates allowed IDs and replaces the set. `GET /people?interest_id=...` returns only visible, eligible profiles with pagination. `POST /contact-requests` checks eligibility again: a profile may have become private since the search. A unique pending-request constraint prevents duplicate requests. Start with deterministic matching and a relational store; introduce ranking only after learning what useful discovery means. Measure successful, accepted contacts and unwanted-contact reports, not just clicks.

**Follow-up.** “What else would you implement?” Derive features from broken flows: cancellation and rejection for requests, blocking/reporting for unwanted contact, deletion and visibility controls for data ownership. Meeting history or recommendations belong only if the agreed use case needs them. Do not add chat, feeds and ML merely to fill a diagram.

**Typical mistake:** spending the whole answer on sharding before establishing an interaction. **Self-check:** trace one request from client through permission check, state change and response; explain what happens when two requests race or a user revokes visibility.

## <a id="search-contract"></a>2. Implement a deliberately chosen search contract

**Reported:** `search(user_id, users)` with supplied classes. The report does not publish those classes, return type or constraints. The function below is **our example**, not a reconstruction.

**Practice assumptions:** `users` is a dictionary keyed by integer ID. Each record has a set of canonical interest IDs, a `discoverable` flag and a set of blocked user IDs. Return other discoverable users sharing at least one interest, exclude either-direction blocks, and sort by shared-interest count descending, then ID ascending. An unknown caller raises `KeyError`; no interests yields an empty result. Authentication and real access policy are outside this in-memory example.

```python
def search(user_id, users):
    caller = users[user_id]
    result = []
    for other_id, other in users.items():
        if other_id == user_id or not other["discoverable"]:
            continue
        if other_id in caller["blocked"] or user_id in other["blocked"]:
            continue
        shared = len(caller["interests"] & other["interests"])
        if shared:
            result.append((other_id, shared))
    result.sort(key=lambda item: (-item[1], item[0]))
    return [other_id for other_id, _ in result]
```

For `U` users, at most `I` interests per user and `M` matches, the expected cost is `O(U·(1 + I) + M log M)` with ordinary hash-set behavior; auxiliary memory is `O(M + I)` including the temporary intersection. The scan still costs `O(U)` when interest sets are empty. This is a useful baseline because its correctness is easy to inspect. A production index must preserve every filter, not merely produce similar-looking results faster.

**Worked test:** caller 1 has `{music, running}`; user 2 shares music, user 3 shares both, user 4 shares both but blocks 1. Output is `[3, 2]`. Add equal scores to test the ID tie-break. Also test missing caller, no interests, all private, one-way blocking and no matches.

**Follow-up:** repeated searches can use interest→user-ID postings, then count overlap and apply eligibility filters. Updating interests or access rules must update or invalidate that index. **Typical mistake:** quietly inventing “exclude people already met” or a relevance formula and presenting it as the original condition. **Self-check:** can another person write tests from your contract without asking what “match” means?

## <a id="search-indexes"></a>3. Optimise history lookup and array search

**Meeting history.** Ask whether the query is “have these people met?”, “last meeting” or “all meetings in a period”. For existence, a set of canonical pairs `(min(a,b), max(a,b))` replaces a scan with expected constant-time membership, at linear storage in the number of distinct pairs. For last meeting, map the pair to its latest timestamp. For a time range, keep a sorted event list per pair and locate the boundaries; a boolean set cannot answer that query. Directed interactions require ordered pairs instead. Define deletion, corrections and concurrent updates before caching results.

**Interest array.** Exact search and prefix search differ. For this practice example, the array contains sorted, unique, already-normalised strings and must remain unchanged during a query. Search for the first possible prefix match, then scan only the contiguous matches:

```python
from bisect import bisect_left


def prefix_matches(sorted_interests, prefix):
    if not prefix:  # Practice policy: reject an unbounded query.
        raise ValueError("prefix must be non-empty")
    i = bisect_left(sorted_interests, prefix)
    matches = []
    while i < len(sorted_interests):
        value = sorted_interests[i]
        if not value.startswith(prefix):
            break
        matches.append(value)
        i += 1
    return matches
```

`["art", "arts", "music"]` with `"art"` returns the first two; `"z"` returns none. With bounded string lengths, query work is `O(log N + K)` for `K` results and output memory `O(K)`; character comparisons add string-length cost. Initial sorting costs `O(N log N)` comparisons and inserting into a Python list is linear. A normalisation rule must be applied consistently to stored values and queries; `casefold()` alone does not decide accent or locale policy. [Python's bisect documentation](https://docs.python.org/3/library/bisect.html) explains insertion points and the linear insertion cost.

**Follow-up:** if writes dominate, reconsider the structure or batch updates; “must remain an array” does not imply repeated sorting is free. **Typical mistakes:** binary-searching only the first character, assuming substring matches form a sorted interval, or claiming all work is logarithmic despite returning thousands of results. **Self-check:** test a full-word prefix, absent prefix, longer-than-word prefix and the chosen empty-prefix policy.

## <a id="recruiter"></a>4. Answer the OpenAI recruiter questions with evidence

**Customer-facing experience.** Give one real interaction: user and problem, your personal responsibility, a difficult clarification or disagreement, what changed, and how you know. Distinguish an external customer from an internal stakeholder and implementation ownership from attending a sales call. If you lack direct experience, say so and offer the closest relevant example. A strong answer lets the recruiter locate your contribution without guessing what “we” means.

**OpenAI API knowledge or experience.** Separate what you shipped, what you prototyped and what you have only read. For actual work, explain the application boundary: input and authentication, model request, structured output or tool call, validation, downstream action and user-visible failure. Describe one measured trade-off, such as latency versus quality, with the measurement method. Mention retries, rate limits, secret handling and evaluation only where you can explain what you actually did. API names and model availability change; verify them in current official documentation before interviewing. No particular endpoint is required by the reported question.

**Language preference.** Name the language in which you can implement and debug under time pressure, then justify it with a task: data transformation, backend API or browser interface. Explain an actual limitation and how you handle it. Do not repeat the poster's impression of employer preferences as a universal hiring rule. “I can read this language but need references for its libraries” is more useful than inflated fluency.

**Follow-ups to rehearse:** Which customer assumption was wrong? What failed in the integration? How would you reproduce the error without disclosing customer data? Why that language instead of another? **Typical mistake:** listing products and frameworks without a decision or outcome. **Self-check:** mark each claim as shipped, prototype, study or unknown, and remove any sentence whose evidence you cannot explain.

## <a id="motivation"></a>5. Explain why the company, FDE, government work or computer science

These are distinct questions. Use a short, truthful answer for each, then connect them; do not replace them with one generic mission paragraph.

| Question | Build the answer from | A useful challenge |
| --- | --- | --- |
| Why OpenAI, Palantir or C3.ai? | A current public product or customer problem you have examined; why that work interests you; a relevant capability you bring | What did you learn beyond the company homepage? |
| Why FDE? How do you understand it? | Interest in taking an ambiguous user problem through implementation and adoption; your evidence; the cost of travel, changing context or local constraints | What would you miss about core-product engineering? |
| Why government work? | The particular public mission you actually support, boundaries you need clarified and questions about the deployment | Would your motivation still hold for this actual customer and use case? |
| Why computer science? | A real reason you chose it and how experience changed your understanding | What part still engages you when the work is tedious? |

**Worked structure, not a story:** “The work I am interested in is [specific problem]. I explored it through [real source or experience]. My contribution would be [capability with evidence]. I would want to clarify [material uncertainty].” Fill the brackets yourself. Do not claim enthusiasm for a mission you do not support. Government can mean very different customers; ask which work the team owns rather than assuming a civilian or defense remit.

**Follow-up:** when asked “Why not a different company?”, compare the actual work and your fit without inventing inside knowledge or disparaging competitors. **Typical mistake:** rehearsing a slogan and treating disagreement as disloyalty. **Self-check:** could the answer be sent unchanged to ten employers? If yes, add verifiable specifics and a personal reason. The forum author's explanation for rejection is not proof of a hidden scoring rule.

## <a id="experience"></a>6. Handle the internship or project deep dive

The reports cover personal contribution, technical detail, favorite and least favorite aspects, lessons, and reasons for declining return offers. Prepare a **real** project at three levels: a one-sentence outcome, a two-minute explanation and a deeper architecture walk-through.

For the deeper answer, draw input → transformation → storage → consumer. Name the constraints you actually faced and your decision authority. Explain one choice with an alternative: why it suited the workload, what it cost and what evidence might change your mind. Show how you checked the result: tests, instrumentation, user feedback or a before/after comparison. Attribute team decisions accurately. If no numeric baseline existed, describe the observable result and say that you cannot quantify improvement.

For the high point, explain **why** a piece of work mattered to you: solving a difficult failure, discovering a user need or improving maintainability, with an example. For the low point, describe a constraint or mismatch, your response and what you learned. Blame and disguised strengths answer neither question. For a return offer, state the actual deciding factors and trade-off; do not invent an offer or hide that no offer was made. Keep confidential details abstract while preserving the engineering reasoning.

**Follow-ups:** What exactly did you implement? Which assumption failed? What breaks at ten times the load? Who maintained the result? What would you change now? These are our practice extensions, not additional reported questions. Answer scaling from the bottleneck in your diagram, not by naming a fashionable database.

**Typical mistake:** describing the whole team's system as personal work. **Self-check:** label each element “mine”, “shared” or “someone else's”; then explain one failure and one test without consulting notes. If an interviewer probes beyond your knowledge, state the boundary and describe how you would investigate.

## <a id="recipes"></a>7. Match recipes and keep booking consistent

**Practice contract:** ingredient names are canonical IDs, quantities use a common unit per ingredient, quantities are non-negative, and a recipe is feasible when every required quantity is available. No substitutions, allergies or partial shopping list are implicit. Those need separate requirements. Here is the direct implementation:

```python
def feasible_recipes(stock, recipes):
    # recipes: {recipe_id: {ingredient_id: required_quantity}}
    return [
        recipe_id
        for recipe_id, needs in recipes.items()
        if all(stock.get(ingredient, 0) >= amount for ingredient, amount in needs.items())
    ]
```

With `M` total ingredient requirements, work is `O(M + R)` for `R` recipes, assuming constant-time dictionary lookup; output is `O(R)` in the worst case. Upstream validation rejects negative amounts and incompatible units. Exact quantities may require decimal or integer units rather than binary floating point. Under this contract an empty recipe is feasible; decide explicitly whether validation should forbid it.

**Worked example:** stock has two eggs and 100 g flour. A recipe requiring one egg and 100 g flour is feasible; one requiring three eggs is not. This answers whether **each recipe individually** can be made. It does not promise enough inventory to make every returned recipe together.

Cook booking is a separate state machine: available slot → short-lived hold → confirmed or expired/cancelled. Confirm the slot and any inventory reservation atomically, or define a compensating workflow if they belong to different systems. A stable request ID and uniqueness constraint prevent retries creating duplicate bookings. Availability shown on the page is a snapshot, not a reservation.

**Follow-up:** ingredient→recipe postings can narrow candidates, but quantity checks still follow. **Typical mistakes:** using set inclusion when quantities matter, treating each recipe's feasibility as a combined menu, and checking availability without reserving it. **Self-check:** test missing ingredient, exact equality, zero amount, empty recipe, unit mismatch and two clients booking the same slot.

## <a id="war"></a>8. Model multiplayer War before coding it

**Reported:** multiple players and three face-down cards in a tie. The account does not settle shortage rules, pot order or game termination. **Our practice rules:** each player has a queue; ranks compare numerically; each active player contributes one face-up card. Highest rank wins the pot unless tied. Only tied players continue: three face-down cards and a new face-up card. A tied player with fewer than four cards contributes all remaining cards and cannot continue. If nobody can continue, the battle ends unresolved and the simulator reports that terminal state. If one can continue, that player makes the required contribution and wins. Award the pot in contribution order. Initial contributions are ordered by player ID; in each tie, ineligible players contribute first in ID order, then eligible players in ID order.

The outer game loop handles zero or one active player; invoke `battle` only when at least two players have cards.

```text
battle(decks):
    contenders = players with nonempty decks, ordered by ID
    pot = []
    each contender contributes one face-up card to pot
    contenders = those with the highest face-up rank
    while more than one contender:
        eligible = contenders with at least four remaining cards
        in ID order, each ineligible contender contributes all cards
        if eligible is empty: return UNRESOLVED, pot
        in ID order, each eligible contributes three down and one up
        contenders = eligible players tied for highest new face-up rank
    append pot to the winner's queue; return winner
```

Use a queue with efficient removal from the front, such as Python [`deque`](https://docs.python.org/3/library/collections.html#collections.deque). Work per battle is linear in the cards moved; there is no justified fixed bound on the number of battles in a game. Add a configurable simulation limit or repeated-state detection, returning “limit reached” or “cycle” rather than declaring a winner. The state key must include player order and every deck's order; repeated-state detection uses growing memory.

**Follow-up:** support alternate shortage rules by changing an explicit policy, not scattered branches. **Typical mistakes:** allowing non-tied players into the next tie, losing the earlier pot, or assuming every deterministic game terminates. **Self-check:** no tie, two-way tie among three players, repeated tie, one/no eligible continuation, and conservation of all cards across decks plus pot. Separate card identity from rank so duplicate ranks do not collapse cards.

## <a id="ownership"></a>9. Separate ownership reachability from financial quantities

**Reported:** debug BFS for company owners and share counts, with cycles. The source omits the data model. Start by asking whether an edge means “owns”, “is owned by”, a share count, an economic percentage or voting control. These are different queries.

For the practice reachability query, `owners[company]` lists its direct owners. Return every reachable owner except the starting company:

```python
from collections import deque


def reachable_owners(company, owners):
    seen = {company}
    queue = deque([company])
    while queue:
        current = queue.popleft()
        for owner in owners.get(current, []):
            if owner not in seen:
                seen.add(owner)  # Mark on enqueue, not dequeue.
                queue.append(owner)
    return seen - {company}
```

This visits each reachable vertex and edge once: `O(V + E)` time, `O(V)` memory. It handles cycles for **reachability**, but the visited set is not a method for calculating economic ownership. In a diamond, the second legitimate path may carry an additional contribution; dropping it undercounts.

For a clearly defined acyclic proportional-interest model, multiply fractions along a path and aggregate distinct paths using topological dynamic programming. Example: A directly owns 10% of C and 60% of B; B owns 50% of C. A's modelled direct-plus-indirect interest in C is `0.10 + 0.60 × 0.50 = 0.40`. This is an illustrative economic model, not a legal beneficial-ownership or voting-control conclusion. Share counts in different issuers cannot simply be added; percentages require the right denominator, class and date.

With cross-holdings, arbitrary path traversal can repeatedly count circular holdings. In a specified linear model, equations such as `x = d + W x` may be appropriate; the meanings and orientation of `W` must be fixed, and convergence of the path expansion requires spectral radius below one. A closed 100% cycle can make the system singular. Do not silently “fix” this by excluding visited nodes or capping the answer. Clarify the accounting definition and reject or escalate unsupported structures.

**Typical mistakes:** confusing reachability with quantity, summing percentages across unrelated companies and treating every cycle as harmless. **Self-check:** chain, diamond, cycle, duplicate edge, multiple share classes and missing denominator. State which your implementation answers and which it deliberately does not.

## <a id="elevator"></a>10. Design an elevator with visible invariants

**Reported:** elevator design, without building size, hardware scope or scheduling requirements. For practice, assume one car, numbered floors and a simulation of scheduling; certified physical safety control is outside this exercise.

Represent car state as floor, direction, door state and service mode; requests are cabin destinations and hall calls with direction. Use transitions rather than letting arbitrary code change the floor. A movement command requires doors confirmed closed and a valid target; a door-open command requires the car stopped at the destination. Fault mode disables dispatch until the designated recovery procedure. Real interlocks belong in the safety system, not merely in an application boolean.

A simple collective scheduler serves pending stops in its current direction, then reverses when none remain ahead. Deduplicate repeated calls. At floor 3 moving upward with requests at 5 and 2, serve 5 then 2; a compatible call at 4 arriving before the car passes it can be inserted. Decide explicitly when an opposite-direction hall call is served. If new forward calls keep arriving, track wait age and define a fairness policy instead of claiming starvation is impossible.

For several cars, keep dispatch separate from each car's controller. Estimate pickup time from position, direction, queued stops and capacity; a nearest-car heuristic ignores the route already promised. A scan over `C` cars and their queues is an acceptable baseline; measure demand before introducing a complex optimizer. Separate assigning a request from acknowledging its completion so failed cars can be handled.

**Follow-up:** explain how a request survives restart and how duplicate button events behave. **Typical mistakes:** beginning with inheritance diagrams, moving with open doors, and optimizing average wait while ignoring worst waits. **Self-check:** idle car, repeated calls, request behind direction, full car, fault, restart and sustained traffic. Walk one event sequence through every state transition.

## <a id="temperatures"></a>11. Solve the canonical Daily Temperatures exercise

The C3.ai account reports a **small variation**, but does not give the change. We solve the canonical illustrative contract: for each temperature, return how many days until a **strictly warmer** value; return zero when none exists. This does not reconstruct the reported variant.

```python
def days_until_warmer(temperatures):
    waits = [0] * len(temperatures)
    pending = []
    for day, value in enumerate(temperatures):
        while pending and temperatures[pending[-1]] < value:
            earlier = pending.pop()
            waits[earlier] = day - earlier
        pending.append(day)
    return waits
```

The stack stores unresolved indices in increasing time order with non-increasing temperatures. A new higher value resolves the latest smaller ones; it is their first warmer day because an earlier warmer value would already have removed them. Equal values stay unresolved. Each index is pushed once and popped at most once, so total time is `O(N)`, although one iteration can pop many items. Output and worst-case stack memory are `O(N)`.

For `[73, 74, 75, 71, 69, 72, 76, 73]`, the result is `[1, 1, 4, 2, 1, 1, 0, 0]`. `[70, 70]` produces `[0, 0]`. Test empty input, single day, rising and falling sequences. Compare against a simple quadratic implementation on small inputs to check the invariant.

**Follow-up:** “warmer or equal” changes the comparison; irregular dates require elapsed-time differences, not index differences. A minimum temperature increase is a different condition: do not assume the same stack invariant survives unchanged. **Typical mistake:** counting nested loops and announcing quadratic complexity without amortised reasoning, or popping equal values. **Self-check:** explain why the first matching future day, rather than just any warmer day, is returned.

## <a id="learning"></a>12. Work from unfamiliar documentation and connected datasets

**Reported:** the Government FDSE account describes connected datasets, a schema and documentation, and functions implemented during the interview. It supplies no actual API or task. The following is our preparation method and example.

First read the contract, one example and error behavior. Identify the input/output types, nullability, pagination, ordering, mutability and external side effects. Write the smallest valid call, inspect its result, then implement one complete behavior. Keep a list of uncertainties and ask about the one that blocks correctness before exploring every API method.

**Synthetic exercise:** `list_orders(customer_id, cursor)` returns `items` and `next_cursor`; `None` ends pagination. An order has `id`, `status`, integer `total_cents` and `currency`. Sum completed USD orders for a customer. Agree whether pages are a stable snapshot and IDs can repeat. If repeats are possible, deduplicate by order ID under an explicit rule for conflicting versions; do not silently double count. Reject or separately group other currencies rather than adding unlike units. For `N` rows, a scan takes `O(N)` time; deduplication takes `O(N)` memory. If the API guarantees a unique immutable snapshot, that memory can be avoided.

When designing around several datasets, establish keys and grain before drawing services. Joining customer rows to orders changes cardinality; joining order lines to payments may multiply totals. Check uniqueness and count rows before and after each join. Define missing relationships, permission boundaries and the freshness needed by the user action. Show one concrete example from source rows to the intended screen or result.

**Follow-ups:** What if the next cursor repeats? What if a page fails after earlier pages succeeded? Does retry duplicate a write? A read-only aggregation can restart from a snapshot or resume with consistent state; an external write needs a separate idempotency strategy. **Typical mistakes:** trusting a method name over its contract and proceeding after an unexplained row-count increase. **Self-check:** empty page with another cursor, null fields, duplicates, currency mismatch, missing join key and failure after partial progress. State assumptions before choosing the handling policy.

## Review your answer

For every exercise, check five things: a precise contract, a worked example, a justified trade-off, a failure case and an explicit boundary of knowledge. A correct algorithm with an invented specification is not a complete answer. A persuasive behavioral answer with invented experience is not an acceptable answer. Return to the [reports](fde-forum-reports.md) whenever you need to distinguish what was reported from what we added for practice.
