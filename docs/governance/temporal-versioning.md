# Temporal Versioning Protocol

*How CDFI scores expire with model versions*

---

## The Problem

A CDFI score is a measurement of a specific model version at a specific point in time. A model that scores 82 today may score 88 or 74 after its next update. An institution that relies on a score from six months ago to govern current deployment decisions is relying on stale data.

This is not a hypothetical concern. Frontier AI models receive major version updates on timescales of months. The training data, RLHF objectives, and safety fine-tuning change with each update. A model's doctrinal reliability profile can shift materially across versions.

---

## The Protocol

**Score expiration trigger:** A CDFI score expires when the model receives a major version update, defined as any change to model weights through additional training, fine-tuning, or RLHF updates.

**Minor version updates** (e.g., bug fixes, system prompt changes, API changes that do not affect model weights) do not expire the score.

**Re-evaluation requirement:** After a major version update, the model must be re-evaluated against the full benchmark before its CDFI score can be cited in institutional deployment decisions.

**Score labeling convention:** All published CDFI scores must include the model version and evaluation date:

```
o3 (OpenAI): CDFI 85.0 [evaluated May 2026, model version as of evaluation date]
Claude Sonnet 4.6 (Anthropic): CDFI 78.0 [evaluated May 2026, model version as of evaluation date]
```

---

## Why This Matters for Institutional Governance

A diocese that approves a specific model for formation use based on its CDFI score has made a deployment decision tied to that model version. If the model is subsequently updated, the approval is no longer backed by current data.

The temporal versioning protocol formalizes that the approval is conditional on the model version, not on the model name. Institutional governance policies built on CDFI scores should include a re-evaluation clause triggered by major model version updates.

---

## Practical Implementation

The benchmark pipeline should log the model API version string alongside each evaluation run. This creates a traceable record that ties each CDFI score to a specific model version.

When a new model version is released, institutions with deployment approvals based on prior CDFI scores should:

1. Check whether the update constitutes a major version update (weight changes vs. infrastructure changes)
2. If major: flag the existing approval as pending re-evaluation
3. Schedule a re-evaluation run using the existing benchmark dataset (no new questions required)
4. Update the deployment approval based on the new score

The re-evaluation run requires no new API calls beyond the benchmark prompts themselves. The pipeline, dataset, and rubrics are unchanged. Only the model version changes.

---

*Research basis: A Statistical Approach to Model Evaluations (Anthropic, 2024)*
*Author: Mark Julius Banasihan | Evals Specialist | May 2026*
