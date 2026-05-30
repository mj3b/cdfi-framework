# C4 — Independent Validation of Claimed Capabilities

**CDCF Criterion Version:** v0.2 | Gate 1 — Required for Incubation Acceptance
**Criterion Text:** [catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria#criterion-4](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria)

---

## The Proportionality Principle

The CDCF criterion applies C4 requirements proportionate to stakes. A project that assists with internal scheduling carries different validation requirements than one that informs formation decisions for thousands of Catholics annually. SAICRED v2 is in the high-stakes category: its scores inform whether dioceses and Catholic institutions authorize AI tools in faith formation, catechesis, and doctrinal instruction. That stakes level demands the most rigorous form of independent validation.

---

## The Conditional Graduation Path

The CDCF criterion explicitly permits a project to be accepted into incubation with C4 marked as a **condition of graduation** rather than a barrier to entry, provided the submitter discloses the pending validation explicitly and provides a concrete plan and timeline.

The CDFI Framework uses this path for one of its two validation columns. The technical audit column is cleared. The theological accuracy review column is open and is an explicit condition of SAICRED v2 publication claims. This document names that condition, states the plan, and identifies the owner.

---

## Validation Status

### Column 1: Third-Party Technical Audit — CLEARED

**What it validates:** Does the automated judge apply the rubric consistently and accurately?

**Form of validation:** Documented red-team assessment and independent test execution, as specified in the CDCF criteria's acceptable validation forms.

**Independence:** The reliability certification protocol was designed by Mark Julius Banasihan (Evals Expert). The full test suite was executed independently by Naveen Kumar Puppala (Lead Engineer) in a separate computing environment with proven API quota and no rate-limit interruptions. These are different individuals with different roles. Naveen's execution was not supervised or directed by the Evals Expert during the run.

**Evidence record:**

```
test_judge_reliability.py
github.com/naveenp2708/saicred-benchmark/eval_data/tests/

Run history:
  Apr 29, 2026  FAIL  Part 1 blocker: confidence_calibration kappa=0.487
                       Root cause: 2/3 scoring boundary too abstract
  May 4,  2026  FAIL  Part 4: 80% — context question mismatch (test construction)
  May 6,  2026  FAIL  Part 1: rubric revision in progress
  May 6,  2026  FAIL  Part 1: rubric revision continued
  May 7,  2026  PASS  Part 1: confidence_calibration kappa=0.831 after revision
  May 7,  2026  PASS  Part 2: anchor calibration 98.3%
  May 11, 2026  PASS  Part 4: 100% after exact question-pairing fix
                      publication_ready: true (confirmed in JSON output)

All four parts cleared: May 11, 2026
```

**Final Part 1 kappa values (n=50, May 7, 2026):**

| Metric | kappa | Interpretation |
|--------|:-----:|---------------|
| Hallucination | 1.000 | Perfect |
| Source Citation | 0.859 | Strong |
| Relativism Resistance | 0.846 | Strong |
| Confidence Calibration | 0.831 | Strong |
| Completeness | 0.802 | Strong |
| Doctrinal Precision | 0.644 | Substantial |
| Moral Fidelity | 0.636 | Substantial |
| Pastoral Appropriateness | 0.352 | Below threshold — disclosed (weight 0.02–0.05; non-blocking) |

**Status: CLEARED**

---

### Column 2: Peer-Reviewed Theological Validation — PENDING (Condition of Graduation)

**What it validates:** Does the rubric, as applied by the automated judge, correctly reflect Catholic theological standards? A judge can be statistically consistent in applying a rubric that is theologically wrong. Column 1 does not catch this. Column 2 does.

**Form of validation:** Human theological expert review of a representative sample of automated scores against independent Catholic theological judgment (SAICRED Addendum E protocol).

**Why this is a condition of graduation, not a barrier to entry:** The CDFI Framework is an evaluation governance methodology. The SAICRED v2 reference implementation has completed the technical audit. The theological accuracy validation requires qualified theological advisors whose review constitutes the independent subject-matter evaluation the CDCF criterion requires. That review is in process.

**Plan and timeline:**

| Step | Owner | Required by |
|------|-------|-------------|
| Authority level classification of all 400 prompts | Theological advisors + Dr. Filip Ponulak | Before final CDFI scores published |
| Sample selection for human review (Addendum E) | Dr. Filip Ponulak | Before full publication |
| Theological expert review of sample | Qualified theological advisors | Before full publication |
| Final sign-off on theological accuracy | Dr. Filip Ponulak, Project Lead | July 2026 (book chapter deadline) |

**Status: PENDING — explicit condition of graduation from incubation to active CDCF project status**

---

## C4 to Publication Gate Cross-Reference

This table maps the CDFI publication gates directly to the C4 validation columns, so a CDCF reviewer does not need to construct the mapping:

| CDFI Publication Gate | C4 Validation Form | Status |
|----------------------|-------------------|:------:|
| Gate 1: Judge reliability certification (4 parts) | Documented red-team + independent execution | **CLEARED May 11, 2026** |
| Gate 2: Authority level classification | Theological advisor input independent of Evals Expert | **PENDING** |
| Gate 3: Human theological review (Addendum E) | Peer-reviewed theological validation | **PENDING** |

Gates 2 and 3 are open. They are conditions of graduation. Current CDFI scores are preliminary and must be cited with the disclosure language in `LIMITATIONS.md`.

---

## What the CDFI Framework Currently Claims vs. Does Not Claim

**Currently claims (Column 1 cleared):**
- The automated judge applies the rubric with statistical consistency across all critical metrics (kappa >= 0.60)
- The judge correctly reads the rubric as the authors intended (98.3% anchor calibration)
- The judge correctly distinguishes responses that held firm on Catholic doctrine from those that relativized (100% adversarial invariance)
- The gates fire correctly on responses designed to trigger them (100% cap gate precision)

**Does not yet claim (Column 2 pending):**
- The rubric, as applied by the judge, has been validated by independent theological experts to accurately represent Catholic teaching
- The automated scores carry the weight of theological peer review

---

*Related: [docs/reliability/publication-gates.md](../../reliability/publication-gates.md)*

*Related: [docs/reliability/judge-reliability-protocol.md](../../reliability/judge-reliability-protocol.md)*

*Related: [LIMITATIONS.md](../../../LIMITATIONS.md) — L2 and L3*
