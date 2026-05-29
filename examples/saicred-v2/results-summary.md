# SAICRED v2 — Results Summary

*Complete benchmark findings across six frontier AI models*

---

## Dataset

| Dimension | Detail |
|-----------|--------|
| Models tested | o3, Gemini 3.1 Pro, GPT-5.4, DeepSeek V4, Grok 4, Claude Sonnet 4.6 |
| Questions | 100 Catholic doctrinal questions across 7 topic domains |
| Topic domains | Sacramental Theology, Moral Theology, Church Authority, Apologetics, Eschatology, Mariology, Social Teaching |
| Prompt variants | 4 per question: neutral, Christian context, Catholic context, adversarial |
| Total prompts | 400 |
| Total responses | 2,400 |
| Metric scores | 21,599 across 9 metrics (99.99% complete after gap fill) |
| Automated judge | Gemini 2.5 Flash |
| Reliability certified | May 11, 2026 — all four parts passed |

---

## Headline Rankings

| # | Model | Mean CDFI | Median | Std Dev | Cap Rate | Deployment Tier |
|---|-------|:---------:|:------:|:-------:|:--------:|----------------|
| 1 | o3 | **85.0** | 94.0 | 17.21 | 8.0% | **Formation and Catechesis** |
| 2 | DeepSeek V4 | 83.4 | 91.6 | 19.03 | 11.8% | General Information |
| 3 | Gemini 3.1 Pro | 82.5 | 91.6 | 19.92 | 14.5% | General Information |
| 4 | GPT-5.4 | 82.1 | 84.4 | 15.83 | 8.0% | General Information |
| 5 | Grok 4 | 82.1 | 94.0 | 21.82 | 15.2% | General Information |
| 6 | Claude Sonnet 4.6 | 78.0 | 89.2 | 22.34 | 17.0% | General Information |

> **Status:** Scores are preliminary pending authority level classification of all 400 prompts. Rankings may shift when the full four-column weighting matrix is applied. The pipeline reads `authority_level` at runtime; no schema changes required for recomputation.

---

## Statistical Significance

Pairwise Welch t-tests with clustered standard errors (topic_domain, G=7).

| Comparison | Difference | p-value | Reliable? |
|------------|:----------:|:-------:|:---------:|
| Claude vs. o3 | 7.1 pts | p < 0.001 | Yes |
| Claude vs. DeepSeek | 5.4 pts | p < 0.001 | Yes |
| Claude vs. Gemini | 4.5 pts | p < 0.01 | Yes |
| Claude vs. GPT-5.4 | 4.1 pts | p < 0.01 | Yes |
| Claude vs. Grok | 4.1 pts | p < 0.01 | Yes |
| o3 vs. GPT-5.4 | 2.9 pts | p < 0.05 | Marginal |
| o3 vs. Grok | 2.9 pts | p < 0.05 | Marginal |
| DeepSeek vs. Gemini | 0.9 pts | p = 0.533 | No |
| Gemini vs. GPT-5.4 | 0.4 pts | p = 0.747 | No |
| GPT-5.4 vs. Grok | 0.0 pts | p = 0.998 | No |

**Publication implication:** The rank ordering of positions 2 through 5 is directionally informative but not statistically separated at this benchmark scale. Publications should not present those positions as reliably differentiated performance.

---

## Score Distribution Shape

All models except GPT-5.4 show a bimodal distribution. Responses either score in the 85-to-94 range or cap at 9.0 or 40.0. The middle range is thin.

The mean-median gap is the clearest signal of bimodal distribution:

| Model | Mean | Median | Gap | Interpretation |
|-------|:----:|:------:|:---:|----------------|
| Grok 4 | 82.1 | 94.0 | **11.9** | Scores 94.0 on 72.5% of responses; specific failure mode subset pulls mean down |
| Claude Sonnet 4.6 | 78.0 | 89.2 | **11.2** | Highest cap rate (17%) concentrated in non-Catholic framings |
| DeepSeek V4 | 83.4 | 91.6 | 8.2 | High-scoring majority with framing-sensitive failure subset |
| Gemini 3.1 Pro | 82.5 | 91.6 | 9.1 | Similar bimodal pattern to DeepSeek |
| o3 | 85.0 | 94.0 | 9.0 | Low variance; 71% of responses at formation tier |
| GPT-5.4 | 82.1 | 84.4 | 2.3 | Near-normal distribution; rounding artifact at 84.4 (see below) |

---

## Cap Rate Analysis

305 of 2,400 responses triggered a cap event.

| Gate Type | Count | % of All Responses |
|-----------|:-----:|:-----------------:|
| Relativism resistance only | 181 | 7.5% |
| Both gates (hallucination + relativism) | 76 | 3.2% |
| Hallucination only | 48 | 2.0% |
| **Total cap events** | **305** | **12.7%** |

**By model:**

| Model | Cap Events (of 400) | Cap Rate |
|-------|:-------------------:|:--------:|
| Claude Sonnet 4.6 | 68 | 17.0% |
| Grok 4 | 61 | 15.2% |
| Gemini 3.1 Pro | 58 | 14.5% |
| DeepSeek V4 | 47 | 11.8% |
| o3 | 32 | 8.0% |
| GPT-5.4 | 32 | 8.0% |

---

## Three Findings That Require Careful Interpretation

### Finding 1: The GPT-5.4 formation tier percentage is a formula artifact

GPT-5.4 ranks fourth by mean CDFI (82.1) but only 42.8% of its responses reach the formation tier. o3 reaches 71.0% formation. That gap looks like substantially worse formation readiness. It is not.

149 of GPT-5.4's 400 responses score exactly 84.4 — placing them 0.6 points below the formation threshold. This pattern appears across all four prompt framings and five of seven topic domains. It is a rounding artifact at a specific combination of metric scores, not a behavioral finding. Any board presentation that uses formation tier percentage without this context will produce a misleading conclusion about GPT-5.4.

### Finding 2: The top five models are not statistically distinguishable

The 7.0-point gap between o3 (85.0) and Claude (78.0) does not reach significance at p = 0.142 at this benchmark scale. o3 is the only model cleared for formation use on the mean CDFI threshold. The relative ordering of positions 2 through 5 should be treated as directional, not definitive.

### Finding 3: Score distribution shape matters as much as the mean

A model with mean CDFI 82 and cap rate 15% has a materially different risk profile than a model with mean CDFI 82 and cap rate 8%. Institutions should consult both figures alongside the framing effect data before making deployment decisions.

---

## Pre-Publication Gate Status

| Gate | Status | Blocks Final CDFI? |
|------|:------:|:-----------------:|
| Judge reliability certification | **CLEARED — May 11, 2026** | N/A |
| Authority level classification | Pending — theological advisors | Yes |
| Human theological review | Pending — project lead + advisors | Yes |
| Stability scoring (5 runs/prompt) | Deferred to v2.1 | No |

---

*May 2026*

*Live dashboard: [mj3b.github.io/saicred-v2-dashboard](https://mj3b.github.io/saicred-v2-dashboard)*
