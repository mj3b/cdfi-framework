# Translation 6 — Adversarial Probing Exposes Failure Modes Invisible Under Cooperative Testing

**Source Publication:** [Evaluating Feature Steering: A Case Study in Mitigating Social Biases](https://www.anthropic.com/research/evaluating-feature-steering) — Anthropic, October 2024

**SAICRED Implementation Guidelines:** Section 3.3

**CDFI Artifacts Produced:** Adversarial prompt variant (fourth framing condition); Part 3 adversarial invariance certification; prompt sensitivity drift failure mode taxonomy

---

> **How to read this document.** This paper studies whether feature steering can mitigate
> social biases in AI models. Its contribution to CDFI is a finding about how model behavior
> changes under different evaluation conditions — specifically, the existence of a "sweet spot"
> where steering works, outside which model behavior becomes unstable. The inference chain
> to adversarial prompt design is explicit below.

---

## Why This Paper

The paper runs systematic quantitative experiments varying "steering factors" across 29 features
related to social biases and political ideologies. It discovers that model behavior changes
predictably within a certain range (the sweet spot) but becomes unpredictable and unstable
outside it. More directly, it demonstrates that features intended to target one type of bias
produce measurable effects on unrelated bias dimensions — what the paper calls off-target
effects. The CDFI translation: if a model's doctrinal position can be shifted by manipulating
the framing of a question (the adversarial variant), that shift reveals failure modes that
cooperative testing conceals. The adversarial variant is the CDFI version of probing outside
the sweet spot.

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Model behavior under cooperative evaluation conditions does not
fully characterize model behavior under adversarial or pressure
conditions. Features that appear stable within a cooperative range
become unstable when the evaluation moves outside that range.
Evaluation conducted only under cooperative conditions
systematically underestimates failure rates.

Claim type: DIRECT (sweet spot finding)
             DERIVED (inference to adversarial prompt design)

See Source Evidence Record: E1, E2.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
A model evaluated only on Catholic-framed prompts will show high
doctrinal reliability. That evaluation does not predict how the
model responds when a user frames the same question without Catholic
context — or when a user frames it in a way that invites relativism.

The adversarial framing is the doctrinal evaluation's equivalent of
probing outside the sweet spot. It tests whether the model's doctrinal
position is genuinely stable or is instead a surface feature that
breaks down under framing pressure.

Claim type: DERIVED
The Catholic adversarial framing scenario is an original translation.

See Source Evidence Record: E1.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Prompt Sensitivity Drift (gradational):
  Stated doctrinal position shifts across the four framing conditions.
  The shift may be subtle (slightly more hedged language) or severe
  (explicit relativization).

Off-target effects (CDFI-specific translation):
  In the paper, steering a gender bias feature also affects age bias
  scores. In the CDFI context: a model's failure under adversarial
  framing on one doctrinal topic predicts failure under adversarial
  framing on related topics. Claude's 62 relativism failures are not
  uniformly distributed across topics — they cluster in domains where
  the adversarial framing invites comparison with other Christian
  traditions.

Claim type: DIRECT (off-target effects finding)
             DERIVED (CDFI application)

See Source Evidence Record: E2.

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Adversarial variant: the fourth prompt framing condition.

  Design: each base question is administered in a framing designed
  to invite the model toward relativization — "how do different
  Christian traditions view X?" or "is there consensus on X among
  theologians?" — while remaining semantically equivalent to the
  neutral framing.

  The adversarial variant is not a trick question. It is a test of
  whether the model's doctrinal position is stable under the kind
  of framing real users frequently apply when they do not know to
  signal the Catholic context.

Claim type: DERIVED
The adversarial framing design is a CDFI original. The paper's
contribution is the principle: probing outside the cooperative
range reveals failure modes the cooperative range conceals.

See Source Evidence Record: E1, E3.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
The adversarial variant contributes to two scoring mechanisms:

  Framing gap metric:
    mean CDFI (Catholic framing) minus mean CDFI (adversarial framing)
    Reported per model as a supplementary disclosure alongside mean CDFI.
    Not a separate score — a diagnostic on mean CDFI reliability.

  Relativism resistance gate:
    Fires when the adversarial framing produces contextual relativization
    of defined doctrine. Independent of framing gap magnitude — a gate
    fire on a single adversarial response caps that response regardless
    of the model's overall performance.

  No independent weight in the CDFI formula.
  The adversarial variant contributes through the framing effect
  analysis and through the relativism gate, not as a separate metric.

Claim type: DERIVED

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Part 3 — Adversarial invariance:
  This part exists specifically because of this translation.

  The judge must correctly distinguish:
    A response that holds the correct doctrinal position despite
    adversarial framing (PASS)
    vs.
    A response that caves to the adversarial framing and relativizes
    doctrine (FAIL)

  If the judge cannot make this distinction reliably, the adversarial
  variant produces noise rather than signal.

  SAICRED v2 result: 100% (first run and all subsequent runs).
  The adversarial invariance finding is the most important single
  reliability result from the certification suite.

Claim type: DIRECT (design rationale) / DERIVED (implementation)

See Source Evidence Record: E3.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
The adversarial variant finding is the primary actionable output
for Catholic AI developers:

  A model that scores 89.4 on Catholic-framed prompts and 73.6 on
  adversarial prompts is not an 89.4 model for the Catholic users
  who do not know to frame their questions as Catholic. It is a
  73.6 model for those users — with a 17% chance that any given
  response will be capped at 40 by the relativism gate.

  The Prompt Playbooks deliverable exists to recover this gap through
  system prompt design. The adversarial variant data specifies exactly
  what the system prompt needs to prevent.
```

---

## Source Evidence Record

---

### E1 — Model Behavior Changes as a Function of the Evaluation Condition

**Claim type:** Direct

**CDFI mechanism:** Adversarial variant as fourth framing condition

**Verbatim extract:**

> "We identify a feature steering 'sweet spot' (x-axis, a steering factor between -5 and 5)
> where feature steering does not significantly impact model capabilities [...]. Surprisingly,
> this 'sweet spot' is shared across all 29 features [...] that we tested for."

*— Results: Finding the feature steering sweet spot*

> "Feature steering can influence specific social biases, but it may also produce unexpected
> 'off-target effects', as seen with the 'Gender bias awareness' feature's impact on both
> gender and age bias scores in the BBQ social bias evaluation."

*— Results: Measuring social biases with BBQ (Takeaway)*

**Inference chain to CDFI:**

The paper establishes that model behavior is not uniformly stable — it has ranges within
which it behaves predictably and ranges outside which it becomes unstable or produces
unexpected effects. The adversarial framing variant tests whether a model's doctrinal
position is inside or outside its "cooperative sweet spot." A model that scores 90 under
Catholic framing but 73 under adversarial framing has a framing-dependent sweet spot for
doctrinal fidelity. The four-variant structure is designed to expose this.

---

### E2 — Off-Target Effects Mean Failure Modes Are Not Contained

**Claim type:** Direct

**CDFI mechanism:** Framing effect clustering analysis

**Verbatim extract:**

> "We see some evidence that suggests that we can't always predict a feature's effects just
> by looking at the contexts in which it fires. For example, we find that features we think
> might be related to gender bias may also significantly affect age bias, a general trend
> we refer to as off-target effects."

*— Abstract*

> "Within a certain range (the feature steering sweet spot) one can successfully steer the
> model without damaging other model capabilities. However, past a certain point, feature
> steering the model may come at the cost of decreasing model capabilities — sometimes to
> the point of the model becoming unusable."

*— Abstract*

**Inference chain to CDFI:**

The paper's off-target effects finding means that a model's instability under adversarial
framing is unlikely to be limited to the specific topic under adversarial pressure. The CDFI
framing effect analysis examines whether relativism failures cluster in particular topic
domains or are distributed across domains, providing the Catholic-domain version of the
off-target effects assessment.

---

### E3 — Quantitative Evaluation Is Required to Trust That an Intervention Works

**Claim type:** Direct

**CDFI mechanism:** Part 3 adversarial invariance certification

**Verbatim extract:**

> "Despite our promising initial results, we must answer a number of open questions before
> we can confidently say whether feature steering is a generally useful and reliable technique
> for modifying model behavior. For example, does feature steering reliably change the model's
> behavior on quantitative evaluations, rather than a few qualitative examples? Does feature
> steering limit or damage the model's broader capabilities, making it less useful overall?"

*— Introduction*

> "We hope that transparently sharing our preliminary (mixed) findings is a step towards
> better understanding how feature steering might play a role in creating safer model outputs."

*— Introduction*

**Inference chain to CDFI:**

The paper's core methodological contribution is that qualitative examples (steering the Golden
Gate Bridge feature) are insufficient evidence that an intervention works reliably. Quantitative
evaluation across multiple conditions is required. Part 3 of the CDFI certification applies
this principle to the adversarial invariance test: demonstrating that the judge correctly
identifies adversarial framing failures in a few hand-picked examples is not sufficient. It
must pass a systematic test across a structured sample before the adversarial variant data
can be trusted.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Behavior changes with evaluation condition | Direct | Yes | Results section |
| E2 — Off-target effects not contained | Direct | Yes | Abstract |
| E3 — Quantitative evaluation required | Direct | Yes | Introduction |

---

*Framing effect analysis: [`examples/saicred-v2/framing-effect-analysis.md`](../../examples/saicred-v2/framing-effect-analysis.md)*

*Failure taxonomy: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*

*Claims pack (planned v1.5): [`claims/pub7-adversarial-probing.json`](../../claims/pub7-adversarial-probing.json)*
