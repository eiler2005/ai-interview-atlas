# Reasoning models: budgets and evidence

[English](REASONING_MODELS.md) · [Русский](ru/REASONING_MODELS.md) · [Atlas](README.md)

These are generated practice exercises grounded in the published [requirements radar](radar.md), not reports of questions asked by an employer. The papers and documentation below explain the technical background; they do not establish interview provenance. Sources checked on 2026-09-29.

## What changes at training and inference

Training can change how a model solves problems; inference can spend additional computation on a particular request. These are distinct choices. The original [DeepSeek-R1 report](https://arxiv.org/html/2501.12948v1) describes RL without preliminary SFT for R1-Zero, while R1 adds cold-start data and a multistage pipeline. Calling every reasoning model “RL without supervised training” would erase that distinction.

For [the supervision exercise](themes/evals-observability.md#eval-reasoning-supervision), separate the feedback target from when it is used. Outcome supervision grades a result; process supervision grades intermediate steps. A verifier can also select candidates during inference without updating the generator. [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) compares supervision methods on mathematics. It supports that bounded comparison, not a universal ranking. In a design answer, explain how you would detect a verifier that accepts plausible but wrong solutions.

## Spend compute where it helps

For [the budget exercise](themes/inference-economics.md#inf-reasoning-budget), compare one longer run with several candidates plus selection. [Snell and colleagues](https://arxiv.org/abs/2408.03314) find that useful compute allocation depends on problem difficulty in their experiments. A production router must estimate difficulty using information available before the answer is known.

As an interview design proposal, make a table with task success, full elapsed time, deadline misses and total cost for each strategy. Include failed attempts and verification in the numerator of cost per successful task. A parallel strategy can lower elapsed time while spending more compute. Choose the policy against the service's constraints, then check that its routing mistakes do not erase the gain.

For [the incomplete-response exercise](themes/inference-economics.md#inf-reasoning-incomplete), inspect status and usage before retrying. OpenAI's [reasoning documentation](https://developers.openai.com/api/docs/guides/reasoning) says the output limit includes reasoning tokens and can be exhausted before visible output. A larger allowance is one possible response; it is not a diagnosis for every empty answer. Propose a total recovery budget and a way to prevent duplicate tool effects.

## Show what caused the improvement

[The controlled-comparison exercise](themes/evals-observability.md#eval-reasoning-counterfactual) asks what would have happened on the same tasks under another configuration. Use a fixed evaluation set and independent scoring; OpenAI's [evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices) provides the objective–dataset–metrics–comparison workflow.

A useful proposed experiment keeps tools and prompts fixed for a model comparison, then tests their changes separately. Where interactions matter, test combinations too. Report both matched-budget results and the system you would actually ship: they answer different questions. Repeated trials and slices reveal whether a mean improvement conceals unstable or costly failures.

## Explanations are diagnostic evidence

For [the faithfulness exercise](themes/evals-observability.md#eval-reasoning-trace-faithfulness), score the answer separately from the explanation. [Chen and colleagues](https://arxiv.org/abs/2505.05410) show cases where reasoning models use hints without acknowledging them in their displayed reasoning. A clean explanation therefore cannot rule out the influence of a misleading hint.

Compare paired tasks with and without the hint, recording answer changes and acknowledgements separately. This tests observable behaviour; it does not expose hidden chain of thought. A provider's summary, a displayed reasoning trace and a tool-call log are different objects. Use whichever is available to investigate failures, while judging success by independently checked outputs and actions.
