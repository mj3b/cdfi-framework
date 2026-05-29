# The Framing Effect — Primary Policy Finding

*SAICRED v2 | How prompt framing determines doctrinal reliability*

---

## The Finding

Five of six frontier AI models perform significantly better when the Catholic context is explicit in the prompt. This is not a marginal quality improvement. For several models, the Catholic context cue eliminates categorical failure modes that appear consistently under neutral and adversarial framing.

This is the most practically important finding in the SAICRED v2 dataset for any Catholic institution making deployment decisions.

---

## The Data

| Model | Neutral | Christian | Catholic | Adversarial | Gap (C minus A) |
|-------|:-------:|:---------:|:--------:|:-----------:|:---------------:|
| o3 | 84.9 | 81.8 | 86.2 | 86.8 | **-0.6** |
| GPT-5.4 | 78.0 | 79.1 | 87.8 | 83.3 | +4.5 |
| Gemini 3.1 Pro | 79.5 | 78.1 | 90.3 | 82.0 | +8.3 |
| Grok 4 | 72.6 | 79.4 | 86.9 | 76.1 | +10.8 |
| DeepSeek V4 | 73.8 | 80.8 | 87.5 | 76.4 | +11.1 |
| Claude Sonnet 4.6 | 74.3 | 74.7 | 89.3 | 73.6 | **+15.7** |

*Gap = Catholic framing mean CDFI minus adversarial framing mean CDFI. Amber threshold: gap > 5 points.*

---

## The Mechanism

The discrimination paper (Publication 4) established that model outputs shift systematically under framing variations. In Catholic evaluation, the relevant shift is not a general quality degradation under adversarial prompting. It is specific: the model relativizes defined doctrine.

**What relativization looks like in practice:**

When asked without Catholic context: *"Is the Eucharist truly the Body and Blood of Christ?"*

A model exhibiting contextual relativization opens with: *"This is a significant theological question with different perspectives across Christian traditions..."*

The Real Presence is a defined dogma settled at the Council of Trent in 1551. Presenting it as a question with multiple valid perspectives is not a low-quality answer. It is a misrepresentation of the Church's teaching authority. The relativism resistance gate fires.

When the same question is asked with explicit Catholic context, the same model correctly states the doctrine without qualification.

---

## Claude Sonnet 4.6: The Largest Gap

Claude's 15.7-point gap is the sharpest illustration of the framing effect.

**Catholic framing performance:** CDFI 89.3 — second in the field, above the formation threshold of 85.

**Adversarial framing performance:** CDFI 73.6 — general information tier, with 17.0% cap rate.

**Relativism failures by framing:**

| Framing | Relativism Gate Failures | Cap Rate |
|---------|:------------------------:|:--------:|
| Catholic | **0** | Low |
| Christian | Significant | Elevated |
| Neutral | Significant | Elevated |
| Adversarial | Significant | 17.0% overall |

The Catholic context cue did not slightly improve Claude's average. It eliminated its categorical failure mode entirely. Zero relativism resistance failures across 400 Catholic-framed responses. 62 relativism failures across the other three framings combined.

---

## o3: Framing-Invariant Performance

o3's gap is -0.6 points. That negative value means it performs marginally better under adversarial framing than under Catholic framing — effectively zero variance.

o3 does not depend on the Catholic context cue to hold the doctrinal line. Its relativism resistance gate failure rate is low and consistent across all four framings. This framing invariance is the primary reason o3 is the only model in v2 cleared for formation use. A formation context exposes users to all four framing conditions. A model that requires explicit Catholic framing to perform reliably is not suited for formation use without prompt engineering controls.

---

## What This Means for Deployment Decisions

**For institutions deploying without prompt wrappers:**

The neutral and adversarial framing scores are the relevant performance figures. Five of six models score below 80 under those conditions. Only o3 maintains formation-tier performance across all framings.

**For developers building Catholic AI products:**

A prompt wrapper supplying the Catholic context cue should recover most of the performance gap for models like Claude and DeepSeek. The magnitude of the problem is now empirically established:

- Claude: recover approximately 15 CDFI points with Catholic context
- DeepSeek: recover approximately 11 CDFI points
- Grok: recover approximately 11 CDFI points
- Gemini: recover approximately 8 CDFI points

The Prompt Playbook deliverable (SAICRED Steps 7 and 8) provides the specific wrapper structures validated against this data.

**For the CDFI Formula:**

The framing effect does not change CDFI scores. It explains their distribution. A model's mean CDFI is the average across all four framings. The framing effect analysis disaggregates that average to show where the failures are concentrated.

---

## Research Basis

The framing effect analysis was motivated by the finding in Discrimination in Language Model Decisions (2024) that model behavior shifts systematically under framing variations. That paper established the mechanism. SAICRED v2 measured its magnitude in the Catholic doctrinal domain.

The adversarial prompt variant — the fourth framing — was specifically designed based on the feature steering research (Publication 7) finding that adversarial probing reveals failure modes invisible under cooperative testing. Without the adversarial variant, the 15.7-point gap for Claude would not have been detectable.

---

*May 2026*
