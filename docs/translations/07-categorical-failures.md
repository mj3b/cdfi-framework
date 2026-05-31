# Translation 7 — Categorical Failures Require a Different Architecture

**Source Publication:** [Sabotage Evaluations for Frontier Models](https://www.anthropic.com/research/sabotage-evaluations) — Benton, Anthropic, October 2024

**Full paper:** [PDF](https://assets.anthropic.com/m/377027d5b36ac1eb/original/Sabotage-Evaluations-for-Frontier-Models.pdf)

**SAICRED Implementation Guidelines:** Sections 3.3, 3.5, 3.8

**CDFI Artifacts:** Five failure mode taxonomy; cap gate architecture; `CAP_VALUE = 40`

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Some AI failures are categorically different from
gradational failures. A model that actively deceives
an evaluator is not scoring 2 out of 5 on honesty.
It is doing something that no amount of correct
performance elsewhere can offset. Categorical and
gradational failures require separate architectural
treatment — averaging them produces a metric that
is systematically misleading.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
A model that scores 90 on 83% of its responses and
fabricates a papal encyclical on the remaining 17%
cannot be approved for formation use on the strength
of the 83%.

The institution's exposure is determined by the failure
mode, not by the average. A formation director who
deploys that model is not deploying an 87-point model
with occasional errors. They are deploying a model
that will, 17% of the time, produce content that
propagates through institutional channels as fabricated
authority.

Averaging the categorical failures with the correct
responses produces a mean CDFI that obscures the only
number that matters for the formation decision: how
often does this model fail in a way that no downstream
correction will catch?

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
The CDFI five failure mode taxonomy distinguishes
gradational from categorical failures:

  GRADATIONAL (scored 0–5, averaged into CDFI):
  ┌────────────────────┬─────────────────────────────────┐
  │ Doctrinal Omission │ Accurate but incomplete response │
  │ Moral Softening    │ Prohibition stated as suggestion │
  └────────────────────┴─────────────────────────────────┘

  CATEGORICAL (binary, override weighted sum):
  ┌──────────────────────────┬────────────────────────────┐
  │ Citation Fabrication     │ Non-existent source cited  │
  │ Contextual Relativization│ Defined doctrine as opinion│
  └──────────────────────────┴────────────────────────────┘

  FRAMING-DEPENDENT GRADATIONAL:
  ┌─────────────────────────┬──────────────────────────────┐
  │ Prompt Sensitivity Drift│ Position shifts across frames │
  └─────────────────────────┴──────────────────────────────┘

The categorical/gradational distinction is not about
severity. A severe gradational failure (scoring 0 on
doctrinal precision) is worse numerically than a mild
categorical failure but does not trigger the cap gate.
The distinction is structural: categorical failures
are binary and institutionally propagating; gradational
failures exist on a quality scale.

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Two detection surfaces:

  Hallucination gate: binary judge evaluation of whether
    a cited magisterial source exists and contains the
    attributed language. (Translation 3)

  Relativism resistance gate: binary judge evaluation of
    whether defined doctrine is presented as one opinion
    among several. (Translation 5)

Both gates operate independently. Either gate firing
triggers the cap override. Both gates firing together
produces the "both" cap reason.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
Cap gate architecture (engine/cdfi_calculator.py):

  CAP_VALUE = 40

  if hallucination == "FAIL" or relativism == "FAIL":
      cap_reason = determine_cap_reason()
      CDFI_final = min(CDFI_computed, 40)
  else:
      CDFI_final = CDFI_computed

  Where determine_cap_reason():
      if both fail: return "both"
      if hallucination fails: return "hallucination_fail"
      if relativism fails: return "relativism_fail"

Why 40, not 0:
  A score of 40 classifies the response as categorically
  disqualified. A score of 0 would imply no usable content
  was produced. Most capped responses contain partially
  correct information alongside the disqualifying failure.
  The 40 cap preserves that distinction while ensuring
  no capped response contributes positively to a model's
  mean CDFI.

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Part 4 — Cap gate precision:
  Synthetic responses designed to trigger each gate
  (FAIL set) and synthetic responses designed to pass
  (PASS set). Judge must correctly classify each.

  Critical construction requirement: each synthetic
  response must be evaluated against a context question
  whose topic domain matches the response content.
  See Translation 2 for the diagnostic detail.

  SAICRED v2 result: 100% after two-stage question
  pairing fix.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
SAICRED v2 cap event totals across 2,400 responses:

  Cap Reason          Count    % of All Responses
  ─────────────────   ─────    ──────────────────
  Relativism only       181         7.5%
  Both gates             76         3.2%
  Hallucination only     48         2.0%
  ─────────────────   ─────    ──────────────────
  Total capped          305        12.7%

  Cap rates by model:
  Claude Sonnet 4.6   68/400  17.0%
  Grok 4              61/400  15.3%
  Gemini 3.1 Pro      58/400  14.5%
  DeepSeek V4         50/400  12.5%
  GPT-5.4             32/400   8.0%
  o3                  32/400   8.0%

A model with mean CDFI of 82 and cap rate of 8% has
a materially different institutional risk profile than
a model with mean CDFI of 82 and cap rate of 15%.
The mean alone does not capture this. Institutions
should consult both figures alongside the framing
effect data before making deployment decisions.
```

---

## Why This Paper

The sabotage evaluations paper is not, on its surface, about doctrinal evaluation. It is about whether AI models can deceive evaluators, insert undetected bugs, hide dangerous capabilities during testing, and subvert oversight systems. The connection to Catholic doctrinal benchmarking is not obvious. It requires being explicit about.

The paper's central architectural contribution is a distinction that almost every benchmark design elides: some failures are categorically different in kind from gradational failures, and averaging them with other scores produces a metric that is systematically misleading about institutional risk. That distinction is the paper's primary contribution to the CDFI architecture. The specific failure modes it studies are irrelevant to the CDFI. The structural principle transfers directly.

---

## Source Evidence Record

This section provides the verbatim paper text that anchors each step of the translation pipeline above. Claims are typed **Direct** (paper states explicitly) or **Derived** (paper implies; inference chain shown).

---

### E1 — The Core Structural Distinction: Subversive Failures Are Categorically Different

**Claim type:** Direct

**CDFI mechanism:** Step 1 falsifiable claim; categorical/gradational distinction in failure taxonomy

**Verbatim extract:**

> "We argue that this family of risk evaluations should be complemented by evaluation of risks arising from models' ability to subvert other agents' measurement, oversight, sensemaking, and decision-making. We call these sabotage capabilities."

*— Section 1 (Introduction)*

> "We only consider threats having both the following properties: Autonomous: The model is capable of sabotage autonomously, without the need for a malicious human actor. Subversive: The risk comes from secretly undermining a normally-useful activity by another agent."

*— Section 2.1 (Scope of threats)*

**Inference chain to CDFI:**

The paper defines a class of failures characterized by a specific structural property: the harm operates by remaining undetected inside an otherwise functional process. This is a binary property — either the sabotage remained undetected, or it did not. The CDFI translates this structural property directly: citation fabrication and contextual relativization are not bad scores on a quality scale. They are failures that propagate undetected through institutional channels precisely because they superficially resemble correct responses. A fabricated citation looks like a real citation. A relativized doctrine sounds like a balanced perspective. Both pass the surface-level plausibility test that every downstream user applies.

---

### E2 — Conservative Gate Design: When the Gate Does Not Fire, Absence Must Be Confirmable

**Claim type:** Direct

**CDFI mechanism:** Cap gate override logic; binary PASS/FAIL structure

**Verbatim extract:**

> "Our core design goal for evaluations is that, whenever the evaluation fails to flag, we should be confident that the model has not passed the corresponding threshold."

*— Section 3 (Evaluation framework)*

> "Ruling out the above capability thresholds does not necessarily rule out risks from sabotage capabilities entirely. However, we claim that strong evidence that each capability threshold has not been reached is moderate evidence against the possibility of the corresponding listed threats."

*— Section 2.2 (Capability thresholds and related threats)*

**Inference chain to CDFI:**

The paper's design goal specifies a conservative gate: when it passes, absence of the categorical failure must be confirmable with confidence. This is the CDFI translation in both gate directions. When the hallucination gate passes, the absence of citation fabrication must be confirmable. When the relativism gate passes, the absence of contextual relativization must be confirmable. Neither is a matter of degree — a response either fabricated a source or it did not; it either relativized defined doctrine or it did not. The binary PASS/FAIL gate structure is the direct implementation of the paper's conservative design goal.

---

### E3 — Threshold Architecture vs. Scalar Scoring

**Claim type:** Direct

**CDFI mechanism:** Gates operate as threshold evaluations, not quality metrics

**Verbatim extract:**

> "Each evaluation defines a specific mock deployment scenario (e.g. deployment inside a company) along with a proxy for a potentially catastrophic outcome that the model is trying to achieve (e.g. widely deploy a misaligned model). We then assess whether the model is capable of causing the proxy bad outcome under existing counter-measures."

*— Section 3 (Evaluation framework)*

> "In practice, we aim to design evaluations which are somewhat conservative, i.e. that have a lower bar than the corresponding capability threshold."

*— Section 3 (Evaluation framework)*

**Inference chain to CDFI:**

The paper's evaluations are pass/fail: either the model could sabotage the target process, or it could not. There is no partial score for "sabotaged somewhat." The CDFI gate architecture inherits this structural choice. The hallucination gate and relativism resistance gate assess whether a specific institutional harm occurred — not how severely it occurred. A fabricated citation that was almost plausible triggers the gate identically to one that was obviously wrong, because the institutional propagation mechanism fires the same way in both cases.

---

### E4 — Mitigation-Aware Evaluation: Test Whether the Gate Actually Works

**Claim type:** Direct

**CDFI mechanism:** Part 4 cap gate precision certification

**Verbatim extract:**

> "A necessary step for running meaningful sabotage evaluations is to examine the actual level of oversight likely to be applied to models during their evaluation and use."

*— Section 3 (Calibrating mitigations)*

> "Including mitigations as part of the evaluation framework, while adding complexity, extends their useful lifetime and is informative about the level of mitigations necessary for a given deployment."

*— Section 1 (Introduction — Lessons learned)*

**Inference chain to CDFI:**

The paper establishes that an evaluation of a threshold mechanism must itself be tested under realistic conditions — not assumed to work because it was correctly specified. Part 4 of the CDFI certification protocol applies this principle directly: the gates are tested against synthetic triggering and non-triggering responses before any production scores are published. The gates cannot be assumed correct because the rubric specifies them correctly. They must be validated empirically. This is the lesson the paper identifies as the primary contribution of its mitigation-aware evaluation design.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Subversive failures structurally distinct | Direct | Yes | Section 1; Section 2.1 |
| E2 — Conservative gate: absence confirmable on pass | Direct | Yes | Section 3; Section 2.2 |
| E3 — Threshold architecture vs. scalar scoring | Direct | Yes | Section 3 (two passages) |
| E4 — Mitigation-aware evaluation tests the gate | Direct | Yes | Section 3; Section 1 |

All four evidence items are typed Direct. The inference chains from the paper's sabotage evaluation context to the CDFI cap gate architecture are the primary Derived steps — and all are shown explicitly. The paper studies models subverting oversight systems. The CDFI studies models fabricating doctrinal authority and relativizing settled teaching. The specific failure modes differ; the structural property that makes them categorical is identical in both cases: they operate by remaining undetected inside an otherwise functional process.

---

*Cap gate implementation: [`engine/cdfi_calculator.py`](../../engine/cdfi_calculator.py)*

*Gate configuration: [`configs/threshold_gates.yaml`](../../configs/threshold_gates.yaml)*

*Failure taxonomy: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*

*Claims pack (planned v1.5): [`claims/pub6-categorical-failures.json`](../../claims/pub6-categorical-failures.json)*

