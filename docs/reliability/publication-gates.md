# Publication Gates

*What must pass before CDFI scores appear in any publication*

---

Three gates must clear before CDFI rankings carry full publication weight. Two require action from the implementing team. One requires external input.

---

## Gate 1: Judge Reliability Certification

**What it requires:** All four parts of the judge reliability protocol passing their thresholds.

| Part | Threshold | What it certifies |
|------|-----------|-------------------|
| 1 — Intra-rater consistency | kappa >= 0.70 per metric | Judge applies the rubric consistently |
| 2 — Anchor calibration | >= 90% accuracy | Judge reads the rubric as intended |
| 3 — Adversarial invariance | >= 90% accuracy | Judge distinguishes hold-firm from relativization |
| 4 — Cap gate precision | >= 90% accuracy | Gates fire correctly on triggering responses |

**Owner:** Evals Expert + Lead Engineer

**What blocks publication if not cleared:** All CDFI scores. A benchmark whose judge reliability is unknown cannot make institutional deployment claims.

**SAICRED v2 status:** Cleared May 11, 2026.

---

## Gate 2: Authority Level Classification

**What it requires:** Every question in the dataset tagged with its doctrinal authority level before CDFI scores are presented as final.

**Why this gate exists:** If all questions are scored using the same default weight column (e.g., ordinary_magisterium), the resulting CDFI scores are preliminary. They answer: how did this model perform when every question was treated as ordinary magisterium? They do not answer: how did this model perform when each question was scored at the weight appropriate to its actual authority level? Those are different measurements, and they will produce different rankings.

**Owner:** Theological advisors (content expertise required)

**What blocks publication if not cleared:** Final CDFI scores. Preliminary scores (with explicit disclosure) can be published with appropriate limitation language.

**Closing condition:** Theological advisors classify each question; pipeline re-runs with --cdfi-only flag (no new API calls required). Naveen executes Phase 1 within 15 minutes of receiving the classification file.

**SAICRED v2 status:** Pending.

---

## Gate 3: Human Theological Review

**What it requires:** A representative sample of automated judge scores validated against human theological expert judgment per the methodology's human review protocol (Addendum E).

**Why this gate exists:** The judge reliability certification certifies statistical consistency. It does not certify theological accuracy. A judge can be perfectly consistent in applying a rubric that is theologically wrong. Human theological review catches the case where the rubric or the judge's application of it systematically mischaracterizes the tradition's teaching.

**Owner:** Project Lead + theological advisors

**What blocks publication if not cleared:** Full publication. Papers published without human theological review should include explicit disclosure.

**SAICRED v2 status:** Pending.

---

## What Can Be Published Before All Gates Clear

**Before Gate 1 (reliability) clears:** Nothing. Unreliable judge scores cannot be published in any form.

**After Gate 1, before Gates 2 and 3:** Preliminary rankings with explicit limitation disclosures. The SAICRED v2 board narrative and interpretation memos are examples: they report directionally valid preliminary scores, name the two pending gates, and specify exactly what will change when they close.

**After all three gates clear:** Final CDFI scores.

---

*Author: Mark Julius Banasihan | Evals Specialist | May 2026*
