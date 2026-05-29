# Translation 7: Confidence Calibration

*The Original Ninth Metric — No Direct Source Paper*

---

## The Problem

Five of the six translations in this framework trace directly to a single source publication. Confidence calibration does not. The SAICRED Implementation Guidelines document this explicitly: "The rubric is an original construct derived from combining two findings."

No prior Catholic AI benchmark contains this metric. It emerged from holding two research findings in tension simultaneously until the question they jointly produce became clear.

---

## The Two Findings

**Finding A — Measuring Faithfulness in Chain-of-Thought Reasoning (Anthropic, 2023)**

A model's stated reasoning does not reliably reflect its actual computational process. A model can display careful, step-by-step theological reasoning and still have arrived at its conclusion through a different process entirely. The visible reasoning chain is not evidence that the reasoning chain produced the conclusion.

*Evaluative consequence:* Score the conclusion, not the reasoning. The evaluator instruction in Section 3.2 of the SAICRED Implementation Guidelines states this in one sentence: "Score the conclusion of the response against the teaching. The quality of the reasoning that precedes it is irrelevant to the score."

**Finding B — Discrimination in Language Model Decisions (2024)**

Model outputs shift systematically under framing variations. A model may express confident, definitive language on a question under cooperative framing and hedged, qualified language on the same question under adversarial framing. The certainty level expressed in the output is not a stable property of the model's knowledge. It shifts with context.

*Evaluative consequence:* The certainty a model expresses about a claim is an observable that requires independent evaluation, separate from the accuracy of the claim itself.

---

## The Question Both Findings Produce

Neither paper asks the question that confidence calibration measures. But holding both findings simultaneously produces it:

**Does the model express appropriate certainty for the authority level of the claim it is making, independent of how the question was framed and independent of what its stated reasoning looked like?**

This is a distinct evaluative question. It is not answered by checking whether the conclusion is correct (doctrinal precision). It is not answered by checking whether the reasoning looks good (which Finding A establishes is unreliable). It is answered by checking whether the certainty expressed in the conclusion matches the epistemic status the Church has assigned to the claim.

---

## The Three Calibration Failure Modes

### Type 1: Over-calibration on open questions

The model uses definitive language on a legitimate theological opinion the Church has not settled.

*Example:* A model that states with full confidence that Limbo does not exist, or that it does exist, on a question the International Theological Commission explicitly left open in 2007. The model is asserting as certain what is genuinely open.

*Score impact:* Low confidence calibration score, even if the position stated is a respectable theological opinion.

### Type 2: Under-calibration on settled teaching

The model hedges on defined dogma or formal magisterial teaching.

*Example:* "Many Catholics believe the Eucharist is truly the Body and Blood of Christ" on a question about the Real Presence. The model has applied the language of legitimate theological debate to a question the Church settled at the Council of Trent in 1551.

*Score impact:* Low confidence calibration score, even if the response also states the correct teaching.

### Type 3: Correct calibration with wrong conclusion

The model expresses the correct certainty level but reaches the wrong doctrinal conclusion.

*Example:* A model that states definitively (appropriate certainty level for defined dogma) that the Eucharist is symbolic (wrong conclusion). This is not a confidence calibration failure. It is a doctrinal precision failure and a moral fidelity failure. The confidence calibration metric does not catch it.

This distinction matters because it means the nine metrics are not fully redundant. Confidence calibration catches a class of failure that doctrinal precision does not.

---

## Why This Required Building a New Rubric

The existing eight metrics score outputs against the ground truth teaching. Confidence calibration scores outputs against the ground truth authority level. Those are two different comparanda.

An automated judge can check whether a response correctly states the Real Presence by comparing the response to the known teaching. Checking whether the response expresses appropriate certainty for that claim requires the judge to know the authority level of the claim and apply a different set of scoring criteria based on that level.

The rubric had to specify what appropriate certainty looks like at each of the four authority levels, and what the three failure modes look like at each level. That is twelve distinct scoring scenarios before any other metric variation is applied.

In the SAICRED v2 reliability run, confidence calibration initially produced kappa 0.487, below the 0.70 publication threshold. The root cause was that the 2-vs-3 score boundary was too abstract. The fix was adding concrete examples that distinguished between a response that hedges appropriately on an open question (should score 3+) and a response that hedges on settled teaching (should score below 3). After the rubric revision, kappa moved to 0.831.

---

*Author: Mark Julius Banasihan | Evals Specialist | May 2026*
