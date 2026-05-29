# SAICRED v2 — Reference Implementation

*Standard for Assessing AI for Catholic Reliability and Doctrinal Fidelity*

---

SAICRED v2 is the first benchmark built on the CDFI Framework. It is the existence proof: a complete, scored, published implementation of the methodology across six frontier AI models.

---

## What Was Tested

| Dimension | Detail |
|-----------|--------|
| Models | o3, Gemini 3.1 Pro, GPT-5.4, DeepSeek V4, Grok 4, Claude Sonnet 4.6 |
| Questions | 100 Catholic doctrinal questions across 7 topic domains |
| Framings | 4 per question (neutral, Christian, Catholic, adversarial) = 400 prompts |
| Total responses | 2,400 |
| Metric scores | 21,599 across 9 metrics (99.99% complete) |
| Automated judge | Gemini 2.5 Flash |
| Reliability certified | May 11, 2026 — all four parts passed |

---

## Headline Rankings

| # | Model | Mean CDFI | Median | Cap Rate | Deployment Tier |
|---|-------|:---------:|:------:|:--------:|----------------|
| 1 | o3 | **85.0** | 94.0 | 8.0% | **Formation and Catechesis** |
| 2 | DeepSeek V4 | 83.4 | 91.6 | 11.8% | General Information |
| 3 | Gemini 3.1 Pro | 82.5 | 91.6 | 14.5% | General Information |
| 4 | GPT-5.4 | 82.1 | 84.4 | 8.0% | General Information |
| 5 | Grok 4 | 82.1 | 94.0 | 15.2% | General Information |
| 6 | Claude Sonnet 4.6 | 78.0 | 89.2 | 17.0% | General Information |

*Scores are preliminary pending authority level classification of all 400 prompts. Rankings may shift.*

**Statistical note:** Pairwise Welch t-tests with clustered standard errors (topic_domain, G=7) show that only the Grok 4 vs. Claude Sonnet 4.6 gap reaches significance at 95% confidence (p=0.008). Positions 1-5 are directionally informative, not reliably separated performance.

---

## Three Findings That Change How the Rankings Should Be Read

**The scores are bimodal.** Most models either score in the 85-to-94 range or cap at 9.0 or 40.0. The mean is dragged downward by categorical failures and understates how well the model performs on the majority of questions. Grok 4's mean is 82.1; its median is 94.0. That 11.9-point gap is the signature of a high-performing model with a specific failure mode subset.

**The top five models are not statistically distinguishable.** Only the Claude-vs-others gaps reach p < 0.01. The 7.0-point gap between o3 (85.0) and Claude (78.0) does not reach significance at this scale (p=0.142). Publications should not present positions 1-5 as reliably separated performance.

**The GPT-5.4 formation tier percentage is a formula artifact.** 149 of its 400 responses score exactly 84.4, placing them 0.6 points below the formation threshold. This pattern appears across all four framings and five of seven topic domains. It is a rounding artifact, not a behavioral finding.

---

## The Primary Policy Finding: The Framing Effect

| Model | Catholic | Neutral | Adversarial | Gap (C minus A) |
|-------|:--------:|:-------:|:-----------:|:---------------:|
| o3 | 86.2 | 84.9 | 86.8 | **-0.6** |
| GPT-5.4 | 87.8 | 78.0 | 83.3 | +4.5 |
| Gemini 3.1 Pro | 90.3 | 79.5 | 82.0 | +8.3 |
| Grok 4 | 86.9 | 72.6 | 76.1 | +10.8 |
| DeepSeek V4 | 87.5 | 73.8 | 76.4 | +11.1 |
| Claude Sonnet 4.6 | 89.3 | 74.3 | 73.6 | **+15.7** |

Five of six models perform significantly better when the Catholic context is explicit in the prompt.

Claude Sonnet 4.6 scored 89.3 on the Catholic framing and 73.6 on the adversarial framing — a 15.7-point gap. It had zero relativism resistance gate failures on the Catholic framing across 400 responses and 62 relativism failures across the other three framings combined. The Catholic context cue eliminated its categorical failure mode entirely.

o3's gap is -0.6 points, effectively zero. It does not depend on the Catholic context cue to hold the doctrinal line. This framing invariance is the primary reason o3 is the only model cleared for formation use.

**For developers:** A prompt wrapper supplying the Catholic context cue should recover most of the performance gap for models like Claude and DeepSeek. The Prompt Playbook deliverable (SAICRED Steps 7 and 8) can now be built on this empirical foundation.

---

## Cap Rate Analysis

305 of 2,400 responses triggered a cap event: 181 relativism-only failures, 76 both-gate failures, 48 hallucination-only failures.

| Model | Cap Rate | Cap Events (of 400) |
|-------|:--------:|:-------------------:|
| Claude Sonnet 4.6 | 17.0% | 68 |
| Grok 4 | 15.2% | 61 |
| Gemini 3.1 Pro | 14.5% | 58 |
| DeepSeek V4 | 11.8% | 47 |
| o3 | 8.0% | 32 |
| GPT-5.4 | 8.0% | 32 |

---

## What Remains Before Final Publication

| Item | Status | Blocks Final CDFI? |
|------|--------|--------------------|
| Authority level classification of all 400 prompts | Pending — theological advisors | Yes |
| Human theological review of automated scores | Pending — Filip Ponulak + advisors | Yes |
| Judge reliability certification | Cleared May 11, 2026 | N/A |
| Stability scoring (five runs per prompt) | Deferred to v2.1 | No |

---

Full results: [mj3b.github.io/saicred-v2-dashboard](https://mj3b.github.io/saicred-v2-dashboard)

*Catholic Digital Commons Foundation | SAICRED v2 | May 2026*
