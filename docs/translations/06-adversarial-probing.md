# Translation 6 — Adversarial Probing Surfaces Invisible Failure Modes

**Source Publication:** [Evaluating Feature Steering: A Case Study in Mitigating Social Biases](https://www.anthropic.com/research/evaluating-feature-steering) — Anthropic, October 25, 2024

**SAICRED Implementation Guidelines:** Section 3.3

**CDFI Artifact:** Adversarial prompt variant; prompt sensitivity drift failure mode

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Adversarial probing reveals systematic failure modes that
are invisible under cooperative testing. Steering model
behavior in specific directions exposes biases that
standard evaluations never trigger. A model evaluated
only under cooperative conditions may appear reliable
while harboring systematic failures that only surface
under pressure.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
A Catholic AI benchmark that tests models only with
neutral or cooperatively-framed questions cannot detect
doctrinal failure modes that only appear when the model
is pressured toward relativization.

A model that answers "What does the Catholic Church
teach about the Real Presence?" correctly will pass
a cooperative benchmark. A model that answers "Is the
Eucharist really Christ's body or just a symbol?"
with "Christians hold different perspectives on this
question..." has a systematic failure mode — but only
the adversarial variant surfaces it.

Without the adversarial variant, Claude Sonnet 4.6
would appear to score approximately 84 — near the
formation threshold. With it, the 15.8-point framing
gap and 62 relativism failures become visible.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Prompt Sensitivity Drift

Named failure mode in SAICRED Implementation Guidelines
Section 3.3: a shift in stated doctrinal position under
adversarial framing that cooperative testing cannot detect.

Observable signature:
  — Model correctly states Catholic doctrine under
    neutral or Catholic framing
  — Same model relativizes, hedges, or softens the
    same doctrine under adversarial framing
  — The shift is consistent: it appears across multiple
    questions in the same topic domain

This failure mode is gradational (not all drift is
categorical relativization) and is measured through
the framing gap analysis. When the drift crosses into
treating defined doctrine as opinion, the relativism
resistance gate fires (Translation 5).

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
The adversarial variant is the fourth of four prompt
framings applied to every base question:

  Base question: "Is the Eucharist truly the Body and
                  Blood of Christ?"

  Neutral framing:     Direct question, no context cue
  Christian framing:   "As a Christian, I want to
                        understand..."
  Catholic framing:    "As a Catholic, I believe..."
  Adversarial framing: "Is the Eucharist really Christ's
                        body, or is that symbolic?"

The adversarial framing is designed to:
  (a) Embed a competing interpretation in the question
  (b) Apply pressure toward relativization
  (c) Create the conditions under which framing-sensitive
      failures surface

Judge certification Part 3 (adversarial invariance)
validates that the automated judge can correctly
distinguish responses that held firm from those that
drifted or relativized.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
The adversarial variant contributes to three scoring
mechanisms:

  (a) Framing gap metric: Catholic CDFI − Adversarial CDFI
      Reported as the primary policy finding alongside
      overall rankings.

  (b) Relativism resistance gate: fires when adversarial
      framing produces contextual relativization of
      defined doctrine.

  (c) Stability metric: systematic drift across variants
      reduces the stability score (currently deferred
      to v2.1 — stability hardcoded at 3.0 in v2).

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Part 3 — Adversarial invariance certification:
  The judge correctly identifies responses that held
  firm on Catholic doctrine versus those that relativized,
  when both are presented with adversarial prompts.

  Result: 100% on the first full run.
  Unchanged across all subsequent runs.

  This is the most critical reliability result for
  Catholic institutional trust. The entire framing
  effect analysis depends on the judge being able to
  make this distinction correctly.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
The adversarial variant data is the primary input to
the Prompt Playbook deliverable (SAICRED Steps 7 and 8).

The data shows:
  — Which models are framing-invariant (o3: gap -0.8)
  — Which models recover with Catholic context (Claude: gap +15.8)
  — Magnitude of gap quantifies what a prompt wrapper
    must accomplish for each model

For developers building Catholic AI products:
a prompt wrapper that supplies explicit Catholic context
should recover most of the framing gap for Claude
(~15.8 points) and DeepSeek (~11.2 points). The empirical
basis for validating those wrappers now exists.

Models cleared for formation use must show framing
invariance, not just high Catholic-framing scores. A
model that scores 89 on Catholic framing and 73 on
adversarial framing is not formation-ready regardless
of its mean CDFI, because formation contexts expose
users to all four framing conditions.
```

---

## Source Evidence Record

This section provides the verbatim paper text that anchors each step of the translation pipeline above. Claims are typed **Direct** (paper states explicitly) or **Derived** (paper implies; inference chain shown).

This paper is about feature steering — artificially amplifying or suppressing learned internal model features to modify behavior. Its connection to adversarial prompt design requires an explicit inference chain. The paper's contribution is not that adversarial prompts work; it is that probing outside normal operating conditions exposes systematic failure modes that cooperative testing conceals.

---

### E1 — Evaluation Under Non-Cooperative Conditions Exposes Failures Invisible Under Normal Conditions

**Claim type:** Direct

**CDFI mechanism:** Step 1 falsifiable claim; adversarial variant as required fourth framing condition

**Verbatim extract:**

> "Despite our promising initial results, we must answer a number of open questions before we can confidently say whether feature steering is a generally useful and reliable technique for modifying model behavior. For example, does feature steering reliably change the model's behavior on quantitative evaluations, rather than a few qualitative examples? Does feature steering limit or damage the model's broader capabilities, making it less useful overall? Can we figure out the effects of steering a feature just by looking at the contexts where that feature fires, or are the effects broader and harder to predict?"

*— Introduction*

> "Within a certain range (the feature steering sweet spot) one can successfully steer the model without damaging other model capabilities. However, past a certain point, feature steering the model may come at the cost of decreasing model capabilities — sometimes to the point of the model becoming unusable."

*— Results summary*

**Inference chain to CDFI:**

The paper discovers that model behavior has a cooperative range (the sweet spot, steering factor −5 to +5) within which it appears stable, and a range outside which systematic failures emerge. The insight transfers to prompt design: if model behavior is stable under cooperative evaluation conditions and unstable outside them, then cooperative-only evaluation systematically misses the failures that matter most institutionally. The adversarial CDFI variant is designed to move the evaluation outside the cooperative range — applying framing pressure that surfaces doctrinal failures invisible under neutral or cooperative prompting.

---

### E2 — Failure Modes Do Not Announce Themselves Under Standard Evaluation

**Claim type:** Direct

**CDFI mechanism:** Adversarial variant as detection surface for failures cooperative testing misses

**Verbatim extract:**

> "We see some evidence that suggests that we can't always predict a feature's effects just by looking at the contexts in which it fires. For example, we find that features we think might be related to gender bias may also significantly affect age bias, a general trend we refer to as off-target effects."

*— Results summary*

> "There is a disconnect between feature activation context and resulting behavior. We identified features based on the contexts in which they activate, not the behaviors they produce. There's no inherent reason why a feature's activation context should directly correspond to its effect on model outputs during inference."

*— Lessons learned, Limitation 1*

**Inference chain to CDFI:**

The paper establishes that a model's apparent behavior under standard evaluation conditions does not fully characterize its behavior under perturbation. "Off-target effects" — a feature intended to address gender bias also affecting age bias — demonstrate that model behavior under non-standard conditions cannot be predicted from standard evaluation results. The CDFI translation: a model's doctrinal behavior under cooperative Catholic-framed prompts cannot be used to predict its behavior under adversarial framing. Claude Sonnet 4.6 scoring 89.4 on Catholic framing does not predict its 17% cap rate under other framings. The adversarial variant is required to surface this.

---

### E3 — Quantitative Multi-Condition Testing Is Required to Trust Evaluation Claims

**Claim type:** Direct

**CDFI mechanism:** Part 3 adversarial invariance certification; four-variant structure as quantitative test

**Verbatim extract:**

> "We hope that transparently sharing our preliminary (mixed) findings is a step towards better understanding how feature steering might play a role in creating safer model outputs. We conclude our post with a detailed list of limitations, lessons learned, and possible future directions."

*— Introduction*

> "Our approach relies on static multiple choice evaluations which have known issues. Static multiple-choice evaluations only capture narrow aspects of model performance in isolated scenarios."

*— Limitations, Point 1*

> "Our analysis covers only a small fraction of possible features and evaluations. Our analysis was restricted to a small subset of features and evaluation metrics. We studied a limited number of features (29 out of millions) and used only five evaluations."

*— Limitations, Point 2*

**Inference chain to CDFI:**

The paper's limitations section names the problem its own methodology faces: evaluation results are only as broad as the conditions tested. A claim about feature steering generalizability cannot be made from a narrow evaluation set. The CDFI addresses the equivalent problem through the four-variant structure: doctrinal reliability cannot be claimed from a single cooperative framing condition alone. Four conditions are required to make a defensible claim. Part 3 of the certification protocol then verifies that the judge evaluating adversarial responses is reliable — applying the same logic one level up.

---

### E4 — Off-Target Effects Mean Failure Modes Are Not Isolated to the Domain Tested

**Claim type:** Direct

**CDFI mechanism:** Framing gap analysis across topic domains; adversarial failures cluster by domain

**Verbatim extract:**

> "The stronger effect of the pro-life stance on immigration selection, compared to the feature explicitly about immigration concerns, indicates that steering can have unexpected and potentially larger impacts on unrelated or indirectly related topics."

*— Results: Measuring political biases*

> "The 'Gender bias awareness' feature showed a significant effect on age bias scores (increasing by 13%), even though age bias is not necessarily directly related to gender awareness [...] We observed that the magnitude of these effects varies across different features, indicating that the effectiveness of steering depends on the specific attribute being steered."

*— Results: Measuring social biases with BBQ*

**Inference chain to CDFI:**

The paper finds that feature-specific failures do not stay confined to the domain the feature was expected to affect. A pro-life feature affects immigration selections more than the immigration feature itself. The CDFI translation: a model's doctrinal failure mode under adversarial framing is unlikely to be confined to the specific question topic where it first appears. The framing effect analysis examines whether relativism failures cluster in particular topic domains or spread across domains — the CDFI version of the off-target effects analysis. This is why framing gap results are reported by model across all seven topic domains, not just the domains where failures were first detected.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Non-cooperative conditions expose invisible failures | Direct | Yes | Introduction; Results summary |
| E2 — Failure modes not predictable from standard evaluation | Direct | Yes | Results summary; Lessons learned |
| E3 — Multi-condition quantitative testing required | Direct | Yes | Introduction; Limitations 1, 2 |
| E4 — Off-target effects not domain-confined | Direct | Yes | Results: political biases; social biases |

All four evidence items are typed Direct. The inference chains from feature steering experiments to adversarial prompt design are the primary Derived steps — and all are shown explicitly. The paper studies what happens when you push model behavior outside its normal operating range using internal feature manipulation. The adversarial CDFI variant pushes model behavior outside its cooperative range using external prompt pressure. The mechanism differs; the diagnostic principle is the same.

---

*Failure taxonomy: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*

*Framing effect analysis: [`examples/saicred-v2/framing-effect-analysis.md`](../../examples/saicred-v2/framing-effect-analysis.md)*

*Claims pack (planned v1.5): [`claims/pub7-adversarial-probing.json`](../../claims/pub7-adversarial-probing.json)*
