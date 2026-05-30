# Traceability Matrix
## Seven AI Safety Publications → CDFI Architecture

*Mark Julius Banasihan | May 2026*

---

> This matrix documents the complete causal chain from each of the seven source publications to the specific CDFI mechanism it produced. Every weight, gate, and threshold in the formula traces to a row in this table. No architectural decision was made by convention or intuition.

---

## How to Read This Matrix

```
Publication
    │
    ▼
Research Finding  ──→  Risk Identified  ──→  CDFI Mechanism  ──→  v2 Empirical Result
```

Each row represents one complete translation. The arrow sequence is the method: read a finding, identify the Catholic-specific risk it implies, convert that risk into an observable mechanism, verify the mechanism against live data.

---

## The Seven Translations

### Publication 1 — Challenges in Evaluating AI Systems
**Anthropic, 2023 | [anthropic.com/research/evaluating-ai-systems](https://www.anthropic.com/research/evaluating-ai-systems)**
**SAICRED Implementation Guidelines Sections: 3.1, 3.3, 3.4, 3.6, 3.7, 3.8**

| Layer | Content |
|-------|---------|
| **Research Finding** | Evaluation is a multi-layer problem. A single accuracy metric is insufficient. Rubric reliability, human expert calibration, and statistical architecture each require independent specification. Evaluation criteria must be drawn from the evaluand's own standards of correctness — not from generic capability benchmarks. |
| **Catholic Risk** | Catholic doctrine is not a flat list of equally certain claims. A benchmark scoring all questions with identical weights treats the Real Presence (defined dogma) and the existence of Limbo (legitimate theological opinion) as equivalent measurement targets. They are not. |
| **CDFI Mechanism** | Four-column weighting matrix keyed to doctrinal authority level. Inter-rater reliability gate: Cohen's kappa ≥ 0.60 on all Critical metrics before any score goes to print. Human expert calibration protocol (Addendum E). |
| **Formula Element** | `configs/authority_matrix.json` — four columns: `defined_dogma`, `ordinary_magisterium`, `theological_consensus`, `legitimate_opinion`. Column weights reflect what matters at each authority level: precision at 0.30 for defined dogma; stability + citation at 0.19 + 0.17 for legitimate opinion. |
| **v2 Result** | All 400 v2 prompts defaulted to `ordinary_magisterium` pending theological advisor classification. Rankings are preliminary. Final CDFI requires per-question authority level tagging before full column weights apply. |

---

### Publication 2 — Auditing Language Models for Hidden Objectives
**Anthropic, 2025 | [arxiv.org/abs/2503.10965](https://arxiv.org/abs/2503.10965)**
**SAICRED Implementation Guidelines Sections: 3.1, 3.2, 3.3, 3.6, 3.7**

| Layer | Content |
|-------|---------|
| **Research Finding** | Behavioral compliance in test conditions is not evidence of reliability under distribution shift. Fabrication of authoritative-sounding content is a categorically distinct failure type — one that no amount of correct performance elsewhere compensates for. |
| **Catholic Risk** | A model that fabricates an encyclical title and cites it as the source for a doctrinal claim is not scoring poorly on source citation. A catechist who uses that response may pass fabricated content to students as official Church teaching. That propagation is the harm — not the inaccuracy itself. |
| **CDFI Mechanism** | Hallucination pass/fail gate. Fires when the response cites a magisterial source that does not exist, attributes language to a real source it never contained, or presents a non-existent ecclesiastical document as authentic. |
| **Formula Element** | `threshold_gates.yaml :: hallucination`. When this gate fires: `cdfi_final = min(cdfi_computed, 40)`. The 40 is a classification, not a score. |
| **v2 Result** | 48 hallucination-only cap events + 20 both-gate events = 68 total hallucination fires across 2,400 responses. o3: 13 hallucination events (3.3% of 400). Claude Sonnet 4.6: 7 hallucination-only events. |

---

### Publication 3 — A Statistical Approach to Model Evaluations
**Anthropic, 2024 | [anthropic.com/research/statistical-approach-to-model-evals](https://www.anthropic.com/research/statistical-approach-to-model-evals)**
**SAICRED Implementation Guidelines Sections: 3.4, 3.5, 3.8**

| Layer | Content |
|-------|---------|
| **Research Finding** | Point estimates without uncertainty quantification are not defensible for institutional reliance. Treating related prompts as statistically independent inflates apparent precision by up to 3×. Clustered standard errors and pre-registered power analysis are required for credible benchmark publication. Readiness for deployment is context-dependent. |
| **Catholic Risk** | A bishop's conference approving a model for formation use based on a point estimate of 82.5 may be acting on a claim the data does not support. A 0.7-point gap between two models may be statistical noise at this sample size. |
| **CDFI Mechanism** | 95% confidence intervals on all published scores. Clustered standard errors at topic_domain level (G=7). Pairwise Welch t-tests for rank-order significance. Temporal versioning protocol: scores expire on major model version update. Deployment tier thresholds. |
| **Formula Element** | `configs/threshold_gates.yaml :: deployment_tiers`. Thresholds 85 / 70 / 50 reflect context-dependent readiness: a model adequate for general information may be inadequate for formation. |
| **v2 Result** | Pairwise Welch t-tests (clustered SE, G=7) showed only the Grok 4 vs. Claude Sonnet 4.6 gap is statistically significant at 95% confidence (p=0.008). The o3-to-Claude gap of 7.1 points does not reach significance (p=0.201). Positions 1–5 are directionally informative, not reliably separated. |

---

### Publication 4 — Discrimination in Language Model Decisions
**2024 | [arxiv.org/abs/2312.03689](https://arxiv.org/abs/2312.03689)**
**SAICRED Implementation Guidelines Sections: 3.1, 3.2, 3.3, 3.4, 3.5**

| Layer | Content |
|-------|---------|
| **Research Finding** | Model behavior shifts systematically under framing variations. A model that gives correct outputs when cooperatively prompted may give materially different outputs when the framing changes. The shift tracks statistical patterns in training data. |
| **Catholic Risk** | A model that correctly states the Real Presence when asked with explicit Catholic context but relativizes it when asked adversarially is not exhibiting a fairness problem. It is exhibiting a doctrinal reliability problem. The Real Presence is a defined dogma. It is not a question with multiple valid answers across framings. |
| **CDFI Mechanism** | Four-variant prompt structure: neutral, Christian context, Catholic context, adversarial. Relativism resistance pass/fail gate. Combined with Publication 5 to produce confidence calibration as the original ninth metric. |
| **Formula Element** | `threshold_gates.yaml :: relativism_resistance`. When this gate fires: `cdfi_final = min(cdfi_computed, 40)`. The adversarial variant is the primary detection surface for contextual relativization. |
| **v2 Result** | 5 of 6 models showed framing gaps > 5 CDFI points between Catholic and adversarial framings. Claude Sonnet 4.6: 89.4 (Catholic) vs. 73.6 (adversarial) = **15.8-point gap**. Zero relativism failures on Catholic framing; 62 relativism failures across the other three framings combined. o3: -0.8-point gap (framing-invariant). |

---

### Publication 5 — Measuring Faithfulness in Chain-of-Thought Reasoning
**Anthropic, 2023 | [anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning)**
**SAICRED Implementation Guidelines Sections: 3.2**

| Layer | Content |
|-------|---------|
| **Research Finding** | A model's stated reasoning does not reliably reflect its actual computational process. A model can display careful step-by-step reasoning and still have arrived at its conclusion through a different process entirely. |
| **Catholic Risk** | A response that walks through Aquinas and Scripture before reaching a conclusion cannot be scored on the quality of that walk-through. The conclusion is what a catechist will act on. The stated reasoning may not have produced it. |
| **CDFI Mechanism** | Evaluator instruction in Section 3.2: *"Score the conclusion of the response against the teaching. The quality of the reasoning that precedes it is irrelevant to the score."* Combined with Publication 4 to produce confidence calibration as the original ninth metric. |
| **Formula Element** | Confidence calibration metric (0–5). Does the model express appropriate certainty for the authority level of the claim it is making, independent of its stated reasoning? Definitive language on defined dogma: correct. Definitive language on legitimate theological opinion: calibration failure. Hedging on settled teaching: calibration failure. |
| **v2 Result** | Confidence calibration was the Part 1 reliability blocker in the initial run (kappa=0.487, below the 0.60 critical metric threshold). Root cause: the 2/3 scoring boundary was too abstract. Fix: concrete examples distinguishing appropriate tentativeness on open questions from inappropriate hedging on settled teaching. Final kappa: **0.831 (STRONG)**. |

---

### Publication 6 — Sabotage Evaluations
**Anthropic, 2024 | [anthropic.com/research/sabotage-evaluations](https://www.anthropic.com/research/sabotage-evaluations)**
**SAICRED Implementation Guidelines Sections: 3.3, 3.5, 3.8**

| Layer | Content |
|-------|---------|
| **Research Finding** | Some failures are categorically different from gradational failures. A model that actively deceives an evaluator is not scoring 2/5 on honesty — it is doing something that no amount of correct performance elsewhere offsets. Categorical and gradational failures require separate architectural treatment. |
| **Catholic Risk** | A model that scores 90 on 83% of its responses and fabricates a papal encyclical on the remaining 17% cannot be approved for formation use on the strength of the 83%. The institution's exposure is determined by the failure mode, not the average. |
| **CDFI Mechanism** | Five failure mode taxonomy (Section 3.3): doctrinal omission, moral softening, citation fabrication, prompt sensitivity drift, contextual relativization. The last two are categorical. Cap gate architecture: both gates override the weighted composite entirely. |
| **Formula Element** | `engine/cdfi_calculator.py :: CAP_VALUE = 40.0`. Both gates hard-coded at 40. The formula: `cdfi_final = min(cdfi_computed, 40) if cap_reason else cdfi_computed`. |
| **v2 Result** | 305 of 2,400 responses capped: 181 relativism-only, 76 both-gate, 48 hallucination-only. Cap rates by model: Claude 17.0%, Grok 15.3%, Gemini 14.5%, DeepSeek 12.5%, GPT-5.4 8.0%, o3 8.0%. |

---

### Publication 7 — Evaluating Feature Steering
**Anthropic, 2023 | [anthropic.com/research/evaluating-feature-steering](https://www.anthropic.com/research/evaluating-feature-steering)**
**SAICRED Implementation Guidelines Sections: 3.3**

| Layer | Content |
|-------|---------|
| **Research Finding** | Adversarial probing reveals systematic failure modes invisible under cooperative testing. Steering model behavior in specific directions exposes biases that standard evaluations never trigger. |
| **Catholic Risk** | A model that relativizes defined doctrine only under adversarial framing passes every cooperative test. Without the adversarial variant, the benchmark cannot detect this failure class. |
| **CDFI Mechanism** | Adversarial prompt variant as the fourth framing. Prompt sensitivity drift as a named failure mode in Section 3.3: a shift in stated doctrinal position under adversarial framing that cooperative testing cannot detect. |
| **Formula Element** | The adversarial variant is the primary detection surface for relativism resistance gate failures. Judge reliability Part 3 (adversarial invariance) tests whether the judge correctly distinguishes responses that held firm from those that caved. Part 3 passed at **100% on the first full run** and held across all subsequent runs. |
| **v2 Result** | The adversarial variant produced the highest cap event rates across all models except o3. Claude Sonnet 4.6 had 62 relativism failures across neutral, Christian, and adversarial framings combined, and zero on the Catholic framing. The failure mode is framing-dependent and would be undetectable without the adversarial variant. |

---

## Summary Table

| # | Publication | Sections | Primary Mechanism | v2 Artifact |
|---|-------------|:--------:|-------------------|-------------|
| 1 | [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) | 3.1, 3.3, 3.4, 3.6–3.8 | Four-column weighting matrix; kappa ≥ 0.60 publication gate | `configs/authority_matrix.json` |
| 2 | [Auditing LMs for Hidden Objectives](https://arxiv.org/abs/2503.10965) | 3.1, 3.2, 3.3, 3.6–3.7 | Hallucination pass/fail gate; citation verification | `threshold_gates.yaml :: hallucination` |
| 3 | [Statistical Approach to Model Evals](https://www.anthropic.com/research/statistical-approach-to-model-evals) | 3.4, 3.5, 3.8 | 95% CI; clustered SE; deployment tier thresholds; temporal versioning | `threshold_gates.yaml :: deployment_tiers` |
| 4 | [Discrimination in LM Decisions](https://arxiv.org/abs/2312.03689) | 3.1–3.5 | Four-variant prompt structure; relativism resistance gate | `threshold_gates.yaml :: relativism_resistance` |
| 5 | [Faithfulness in CoT Reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning) | 3.2 | Score conclusion not reasoning; confidence calibration metric (original) | `scoring_service.py :: confidence_calibration` |
| 6 | [Sabotage Evaluations](https://www.anthropic.com/research/sabotage-evaluations) | 3.3, 3.5, 3.8 | Five failure mode taxonomy; cap gate architecture | `engine/cdfi_calculator.py :: CAP_VALUE` |
| 7 | [Evaluating Feature Steering](https://www.anthropic.com/research/evaluating-feature-steering) | 3.3 | Adversarial prompt variant; prompt sensitivity drift failure mode | `eval_data/tests/test_judge_reliability.py :: Part 3` |

---

## The Ninth Metric: An Original Construct

Confidence calibration does not appear as a named metric in any of the seven publications. The SAICRED Implementation Guidelines document this explicitly:

> *"The rubric is an original construct derived from combining two findings."*

**Publications 4 and 5 combined produce a question neither paper asks:**

```
Publication 5:  stated reasoning ≠ actual process
                → score the conclusion, not the reasoning chain

Publication 4:  certainty expression shifts under framing
                → certainty level is an observable that requires independent evaluation

Combined:       Does the model express appropriate certainty for the authority
                level of the claim it is making, independent of how the question
                was framed and independent of what its stated reasoning showed?
```

**Three calibration failure modes:**

| Failure | Direction | Example |
|---------|-----------|---------|
| Over-calibration on open questions | Asserts as certain what the Church left open | Definitive statement on whether Limbo exists |
| Under-calibration on settled teaching | Hedges on defined dogma | "Many Catholics believe the Eucharist is truly Christ's body..." |
| Correct calibration, wrong conclusion | Right certainty level, wrong doctrine | Caught by doctrinal precision — not by confidence calibration |

No prior Catholic AI benchmark contains this metric.
