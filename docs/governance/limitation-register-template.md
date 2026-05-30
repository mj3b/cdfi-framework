# Limitation Register Template

*Required disclosures for CDFI-based benchmark publication*

---

## Purpose

Every benchmark publication built on the CDFI Framework must include a limitation register. This document is a template. Fill in the bracketed fields with the actual values from your implementation.

The limitation register is not an apology. It is the mechanism that lets a bishop's conference, school board, or institutional review committee make a deployment decision with accurate information about what the scores can and cannot claim.

---

## Required Disclosures

### Limitation 1: Authority Level Classification Status

**Disclosure language:**

"All [NUMBER] prompts in this benchmark were classified at the [AUTHORITY LEVEL] column for scoring. The full four-column weighting matrix [has been / has not been] applied. Rankings are [final / preliminary] pending theological advisor classification of each prompt by doctrinal authority level. Once classified, CDFI scores will be recomputed using the correct column weight per question. Rankings may shift."

**When to use the preliminary version:** Any time prompts default to a single authority level because classification has not been completed. SAICRED v2 used ordinary_magisterium as the default. This produces valid but preliminary rankings.

**Impact on interpretation:** Preliminary rankings are directionally valid. They answer: how do these models perform when measured with [DEFAULT LEVEL] weights? They do not yet answer: how do these models perform when each question carries the weights appropriate to its actual authority level.

---

### Limitation 2: Human Theological Review Status

**Disclosure language:**

"All [NUMBER] metric scores in this benchmark were produced by an automated judge ([JUDGE MODEL]). [NUMBER / None] of these scores have been validated against human theological judgment per the methodology's human review protocol. Until human theological review is complete, the scores reflect automated judge reliability rather than expert theological validation."

**Impact on interpretation:** Automated judge scores that clear the reliability certification are trustworthy in the statistical sense (consistent, calibrated, adversarially invariant). They are not the same as scores validated by a domain expert theologian. Institutions with high-stakes deployment decisions should note which form of validation has been completed.

---

### Limitation 3: Pastoral Appropriateness Metric

**Disclosure language:**

"The pastoral appropriateness metric produced a judge Cohen's kappa of [VALUE] in the reliability certification run, below the 0.70 publication threshold. This metric carries a formula weight of [WEIGHT RANGE] across all four authority level columns. Judge inconsistency on this metric cannot materially shift any model's ranking. This limitation is disclosed but does not block publication of other metric scores."

**Standard fill for SAICRED v2:** kappa 0.35; weight 0.02-0.05.

---

### Limitation 4: Stability Scoring Status

**Disclosure language:**

"Stability scores in this benchmark [were computed from five runs per prompt / were hardcoded at [VALUE] pending five-run implementation]. [If hardcoded: Stability scores do not reflect observed run-to-run variance and are excluded from comparative analysis. The stability metric is deferred to [VERSION].] "

---

### Limitation 5: Statistical Significance of Rankings

**Disclosure language:**

"Pairwise Welch t-tests with clustered standard errors (topic_domain, G=[NUMBER]) show that rank-order differences among positions [RANGE] do not reach statistical significance at 95% confidence at this benchmark scale (n=[NUMBER] per model). The rank ordering of these positions should be treated as directionally informative rather than reliably separated performance. The gap between [MODEL A] and [MODEL B] reaches significance at p=[VALUE]; all other pairwise gaps are reported with confidence intervals in the full results table."

**Why this matters:** A publication that presents rank-order positions as reliable without this disclosure will overstate the precision of the rankings. A bishop's conference that acts on the ranking of positions 2 through 5 as if they were reliably separated is acting on a claim the data does not support.

---

### Limitation 6: Temporal Validity

**Disclosure language:**

"CDFI scores in this benchmark are valid as of [DATE] for [MODEL VERSIONS]. Scores expire when a model receives a major version update. Institutions relying on these scores for ongoing deployment decisions should monitor model version changes and re-evaluate on the major version update trigger per the temporal versioning protocol."

---

## Optional Disclosures

Include these when applicable to your implementation.

**Missing data:** "Metric scores for [MODEL] were missing for [NUMBER] responses due to [CAUSE]. These responses were excluded from that model's mean CDFI computation. The missing data is concentrated in [DOMAIN/FRAMING], which may affect the reliability of that model's scores in those conditions."

**Dataset coverage:** "This benchmark covers [NUMBER] questions across [NUMBER] topic domains. It does not cover [EXCLUDED AREAS]. Model performance outside the tested domains is unknown and should not be inferred from these results."

**Judge model version:** "The automated judge used in this benchmark is [MODEL AND VERSION]. Results may differ if re-run with a different judge model version."

---

*Author: Mark Julius Banasihan | May 2026*
