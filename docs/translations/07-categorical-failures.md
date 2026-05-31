# Translation 7 — Categorical Failures Require a Different Architecture

**Source Publication:** [Sabotage Evaluations for Frontier Models](https://www.anthropic.com/research/sabotage-evaluations) — Benton et al., Anthropic, October 2024
**Full paper:** [PDF](https://assets.anthropic.com/m/377027d5b36ac1eb/original/Sabotage-Evaluations-for-Frontier-Models.pdf)
**SAICRED Implementation Guidelines:** Sections 3.3, 3.5, 3.8
**CDFI Artifacts Produced:** Five failure mode taxonomy; cap gate architecture; `CAP_VALUE = 40`

---

> **How to read this document.** The Translation Pipeline section (below) shows the seven-step
> sequence that converted this paper's findings into computable CDFI mechanisms. The Source
> Evidence Record (at the end) provides the verbatim paper text that anchors each claim. Every
> claim in the pipeline is typed as either **Direct** (the paper states it explicitly) or
> **Derived** (the paper implies it; the CDFI translation required additional reasoning). Derived
> claims carry the inference chain that moves from the paper's context to the Catholic doctrinal
> deployment context.

---

## Why This Paper

The sabotage evaluations paper is not, on its surface, about doctrinal evaluation. It is about
whether AI models can deceive evaluators, insert undetected bugs, hide dangerous capabilities
during testing, and subvert oversight systems. The connection to Catholic doctrinal benchmarking
is not obvious. It requires being explicit about.

The paper's central architectural contribution is a distinction that almost every benchmark design
elides: some failures are categorically different in kind from gradational failures, and averaging
them with other scores produces a metric that is systematically misleading about institutional
risk. That distinction is the paper's primary contribution to the CDFI architecture. The specific
failure modes the paper studies (code sabotage, human decision manipulation) are irrelevant.
The structural principle transfers directly.

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Some AI failures are categorically different from gradational failures.
A model that actively deceives an evaluator is not scoring 2 out of 5
on honesty. It is doing something that no amount of correct performance
elsewhere can offset. Categorical and gradational failures require
separate architectural treatment. Averaging them produces a metric that
is systematically misleading about the actual risk profile.

Claim type: DERIVED
The paper does not state this in domain-general terms. It demonstrates
the principle through four specific sabotage evaluations and argues
that "ruling out the above capability thresholds does not necessarily
rule out risks from sabotage capabilities entirely." The inference that
categorical/gradational separation is a general architectural principle
of the CDFI translation contribution, not a direct paper quote.

See Source Evidence Record: E1, E2, E3.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
A model that scores 90 on 83% of its responses and fabricates a papal
encyclical on the remaining 17% cannot be approved for formation use on
the strength of the 83%.

The institution's exposure is determined by the failure mode, not by
the average. A formation director who deploys that model is not deploying
an 87-point model with occasional errors. They are deploying a model
that will, 17% of the time, produce content that propagates through
institutional channels as fabricated authority.

Averaging the categorical failures with correct responses produces a
mean CDFI that obscures the only number that matters for the formation
decision: how often does this model fail in a way that no downstream
correction will catch?

Claim type: DERIVED
The Catholic harm scenario is an original application of the sabotage
paper's principle. The paper establishes the general condition: some
failures are categorically dangerous regardless of broader performance.
The specific propagation mechanism (fabricated magisterial citations
passing through catechetical channels) is a domain-specific translation.

See Source Evidence Record: E2.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
The CDFI five failure mode taxonomy distinguishes gradational from
categorical failures:

  GRADATIONAL — scored 0–5, averaged into CDFI:
  ┌────────────────────┬─────────────────────────────────┐
  │ Doctrinal Omission │ Accurate but incomplete response │
  │ Moral Softening    │ Prohibition stated as suggestion │
  └────────────────────┴─────────────────────────────────┘

  CATEGORICAL — binary, override weighted sum:
  ┌──────────────────────────┬────────────────────────────┐
  │ Citation Fabrication     │ Non-existent source cited  │
  │ Contextual Relativization│ Defined doctrine as opinion│
  └──────────────────────────┴────────────────────────────┘

  FRAMING-DEPENDENT GRADATIONAL:
  ┌─────────────────────────┬──────────────────────────────┐
  │ Prompt Sensitivity Drift│ Position shifts across frames │
  └─────────────────────────┴──────────────────────────────┘

The categorical/gradational distinction is not about severity. A severe
gradational failure (scoring 0 on doctrinal precision) is worse
numerically than a mild categorical failure but does not trigger the
cap gate. The distinction is structural: categorical failures are binary
and institutionally propagating; gradational failures exist on a quality
scale.

Claim type: DERIVED
The paper's four evaluation types (human decision sabotage, code
sabotage, sandbagging, undermining oversight) all share the property
that success requires not getting caught. This binary pass/fail
structure (the sabotage either went undetected or it did not) is what
the CDFI translated into the categorical gate architecture. The five
CDFI failure modes and their typing are original contributions.

See Source Evidence Record: E1, E3, E4.

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Two detection surfaces:

  Hallucination gate: binary judge evaluation of whether a cited
    magisterial source exists and contains the attributed language.
    (See Translation 3)

  Relativism resistance gate: binary judge evaluation of whether
    defined doctrine is presented as one opinion among several.
    (See Translation 5)

Both gates operate independently. Either gate firing triggers the cap
override. Both gates firing together produces the "both" cap reason.

Claim type: DERIVED
The detection mechanisms are CDFI originals. The paper does not specify
detection methods for citation fabrication or doctrinal relativization.
The binary gate structure (fire/no-fire with no partial credit) is
derived from the paper's threat model logic: a sabotage event either
succeeded in remaining undetected or it did not.

See Source Evidence Record: E4.

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
  A score of 0 would imply no usable content was produced. Most capped
  responses contain partially correct information alongside the
  disqualifying failure. The 40 cap preserves that distinction while
  ensuring no capped response contributes positively to a model's mean
  CDFI. The Not Recommended tier begins at any score below 50 or any
  gate failure, so a capped response correctly places the model below
  the minimum threshold regardless.

Claim type: DERIVED
The 40-point cap value and the override formula are CDFI design
decisions. The paper's structural contribution is the principle that
some failures must be treated categorically regardless of other
performance. The specific cap value was calibrated against the
deployment tier thresholds and accepted into the SAICRED Implementation
Guidelines.

See Source Evidence Record: E2, E3.

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Part 4 of the reliability certification — Cap gate precision:

  Synthetic responses designed to trigger each gate (FAIL set) and
  synthetic responses designed to pass (PASS set). The judge must
  correctly classify all responses at or above 90% accuracy.

  Critical construction requirement: each synthetic response must be
  evaluated against a context question whose topic domain matches the
  response content. The first Part 4 run failed at 65% because a single
  random context question (marriage dissolution) was used for all
  synthetic responses, including ones about the Eucharist and papal
  infallibility. The judge correctly identified each as off-topic.
  The failure was in the test construction, not in the gates.

  See Translation 2 for the full diagnostic account.

  SAICRED v2 result: 100% after two-stage question pairing fix.

Claim type: DIRECT (partially)
The paper establishes that mitigation-aware evaluation requires testing
whether the gate mechanism functions as designed under realistic
conditions. The judge certification protocol is a CDFI original, but
the design logic (test the oversight mechanism, not just the capability)
comes directly from the paper.

See Source Evidence Record: E5.

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

A model with mean CDFI of 82 and cap rate of 8% has a materially
different institutional risk profile than a model with mean CDFI of 82
and cap rate of 15%. The mean alone does not capture this. Institutions
should consult both figures alongside the framing effect data before
making any deployment decision.
```

---

## Source Evidence Record

This section provides the verbatim paper text that anchors each step of the translation pipeline
above. Each evidence entry is typed as **Direct** (paper states the claim explicitly) or
**Derived** (paper implies the claim; inference chain is shown). Location hints reference the
PDF at the URL above.

---

### E1 — The Core Structural Distinction

**Claim type:** Direct

**CDFI mechanism:** Categorical/gradational failure distinction; gate architecture

**Verbatim extract:**

> "We argue that this family of risk evaluations should be complemented by evaluation of
> risks arising from models' ability to subvert other agents' measurement, oversight,
> sensemaking, and decision-making. We call these sabotage capabilities."

*— Section 1 (Introduction), p. 1*

> "We only consider threats having both the following properties: Autonomous: The model is
> capable of sabotage autonomously, without the need for a malicious human actor. Subversive:
> The risk comes from secretly undermining a normally-useful activity by another agent."

*— Section 2.1 (Scope of threats), p. 3*

**Inference chain to CDFI:**

The paper establishes that the category of risk it studies is defined not by severity but
by structure: the harm operates by remaining undetected inside an otherwise functional
process. This is a binary property. Either the sabotage remained undetected, or it did
not. The CDFI translates this structural property: citation fabrication and contextual
relativization are not bad scores on a quality scale. They are failures that propagate
undetected through institutional channels precisely because they superficially resemble
correct responses.

---

### E2 — Averaging Obscures Categorical Risk

**Claim type:** Direct + Derived

**CDFI mechanism:** Cap gate override of weighted sum

**Verbatim extract:**

> "Ruling out the above capability thresholds does not necessarily rule out risks from
> sabotage capabilities entirely. However, we claim that strong evidence that each
> capability threshold has not been reached is moderate evidence against the possibility
> of the corresponding listed threats, and can usefully be incorporated into a comprehensive
> safety case."

*— Section 2.2 (Capability thresholds and related threats), p. 5*

> "Our core design goal for evaluations is that, whenever the evaluation fails to flag,
> we should be confident that the model has not passed the corresponding threshold."

*— Section 3 (Evaluation framework), p. 5*

**Inference chain to CDFI:**

The paper's design goal specifies that a threshold evaluation must be conservative: when
it passes, the absence of the categorical failure must be confirmable with confidence. This
is not a graded judgment. The CDFI translation: when either gate fires, the composite score
is overridden regardless of the other eight metrics. The override is not a penalty. It is
a structural acknowledgment that the categorical failure's institutional propagation risk
cannot be averaged away.

---

### E3 — Threshold Architecture vs. Scalar Scoring

**Claim type:** Direct

**CDFI mechanism:** Binary gate (fire/no-fire) versus rubric scoring (0–5)

**Verbatim extract:**

> "These evaluations are designed to provide evidence that a given model, operating under a
> given set of mitigations, could not successfully sabotage a frontier model developer or
> other large organization's activities in any of these ways."

*— Abstract, p. 1*

> "Each evaluation defines a specific mock deployment scenario (e.g. deployment inside a
> company) along with a proxy for a potentially catastrophic outcome that the model is trying
> to achieve (e.g. widely deploy a misaligned model). We then assess whether the model is
> capable of causing the proxy bad outcome under existing counter-measures."

*— Section 3 (Evaluation framework), p. 5*

> "In practice, we aim to design evaluations which are somewhat conservative, i.e. that have
> a lower bar than the corresponding capability threshold."

*— Section 3 (Evaluation framework), p. 6*

**Inference chain to CDFI:**

The paper's evaluations are pass/fail: either the model could sabotage the target process,
or it could not. There is no partial score for "sabotaged somewhat." The CDFI gate
architecture inherits this structural choice. The hallucination gate and relativism
resistance gate are binary. They assess whether a specific institutional harm occurred,
not how severely it occurred.

---

### E4 — Detection Must Be Tied to the Failure's Structural Property

**Claim type:** Derived

**CDFI mechanism:** Gate firing conditions (not rubric degradation)

**Verbatim extract:**

> "The model must avoid penalizing a specific potentially catastrophic behavior when used
> in protocols such as constitutional AI — where the model is being used to evaluate or
> monitor itself or other models — while avoiding detection."

*— Section 2.2 (Capability thresholds — Undermining oversight), p. 4*

> "We give the model the goal of steering the human toward an unambiguously wrong answer
> while not appearing suspicious."

*— Section 3.1 (Human decision sabotage), p. 6*

**Inference chain to CDFI:**

Both passages share a structural property: the failure is characterized by appearing
correct while producing a harmful outcome. The detection challenge is not measuring
quality degradation; it is detecting a binary state (harmful output present/absent) inside
an otherwise plausible-sounding response. The CDFI gate firing conditions are designed
around this property. A citation fabrication does not degrade gradually. A magisterial
source either exists or it does not. A definition of doctrine either presents it as settled
or as one opinion among several. The detection prompt must test for the binary state, not
grade the quality of the response on a scale.

---

### E5 — Mitigation-Aware Evaluation Is Required

**Claim type:** Direct

**CDFI mechanism:** Part 4 of the judge reliability certification (cap gate precision test)

**Verbatim extract:**

> "A necessary step for running meaningful sabotage evaluations is to examine the actual
> level of oversight likely to be applied to models during their evaluation and use."

*— Section 3 (Calibrating mitigations), p. 6*

> "Including mitigations as part of the evaluation framework, while adding complexity,
> extends their useful lifetime and is informative about the level of mitigations necessary
> for a given deployment."

*— Section 1 (Introduction — Lessons learned), p. 3*

**Inference chain to CDFI:**

The paper establishes that an evaluation of a threshold mechanism must itself be tested
under realistic conditions — not assumed to work. The CDFI translation: Part 4 of the
reliability certification tests whether the gates actually fire on responses designed to
trigger them. The gates cannot be assumed correct because the rubric specifies them
correctly. They must be validated against synthetic triggering and non-triggering responses
before any benchmark scores enter publication.

---

## What This Translation Does Not Claim

The sabotage evaluations paper studies AI models deceiving human evaluators, inserting
code bugs, hiding capabilities during testing, and subverting AI oversight systems. None
of these specific failure modes appear in the CDFI.

What transfers is the structural principle: some failures are categorically distinct from
quality degradation, and evaluation architecture must reflect that distinction explicitly.
The CDFI does not borrow the paper's specific threat models. It borrows the architectural
reasoning about how to handle failures that are binary rather than gradational.

The claim that citation fabrication and contextual relativization are the two categorical
failures in Catholic doctrinal evaluation is a CDFI design decision grounded in theological
reasoning, not in the sabotage paper. The paper provides the architectural template. The
choice of which failures to treat categorically was made by the Evaluation Expert in
consultation with the SAICRED Implementation Guidelines and subject to sign-off by the
Project Lead.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Core structural distinction | Direct | Yes | Section 1, 2.1 |
| E2 — Averaging obscures categorical risk | Direct + Derived | Yes | Section 2.2, 3 |
| E3 — Threshold vs. scalar scoring | Direct | Yes | Abstract, Section 3 |
| E4 — Detection tied to structural property | Derived | Yes (inference shown) | Section 2.2, 3.1 |
| E5 — Mitigation-aware evaluation required | Direct | Yes | Section 3 |

All five evidence items carry verbatim text from the published paper PDF. Evidence items
typed as Derived carry explicit inference chains showing the reasoning from paper context
to CDFI mechanism. No step in the translation pipeline relies on an unsupported assertion.

---

*Cap gate implementation: [`engine/cdfi_calculator.py`](../../engine/cdfi_calculator.py)*

*Gate configuration: [`configs/threshold_gates.yaml`](../../configs/threshold_gates.yaml)*

*Failure taxonomy: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*

*Applied AI Research Translator schema: [`claims/pub6-sabotage-evaluations.json`](../../claims/pub6-sabotage-evaluations.json) ← planned v1.5*

