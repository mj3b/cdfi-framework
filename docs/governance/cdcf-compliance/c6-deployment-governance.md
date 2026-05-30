# C6 — Deployment Governance Specification

**CDCF Criterion Version:** v0.2 | Gate 1 — Required for Incubation Acceptance
**Criterion Text:** [catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria#criterion-6](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria)

---

## Doctrinal and Canonical Grounding

**Canon 1609** of the Code of Canon Law dictates that judges in a collegiate tribunal must submit written conclusions with reasons in law and in fact, followed by structured discussion. Judges retain the right to withdraw from an original conclusion and to demand that dissent be transmitted to a higher tribunal. This canonical standard establishes that Catholic decision-making requires:

- Conscious reasoning recorded in writing
- The capacity to revise judgments
- Structured deliberative process before commitment
- Transparent mechanisms for appeal and escalation

A deployment governance specification must preserve these capacities in human hands. A governance structure that routes consequential decisions through an automated system with no documented deliberative process, no named decision-maker, and no appeal mechanism does not satisfy the Canon 1609 standard that the CDCF criterion operationalizes.

**The Governance-as-Code Design Pattern**

The CDCF criteria draw explicitly on the governance-as-code design pattern, in which deployment policies are expressed as machine-readable, auditable specifications rather than policy documents that exist separately from the systems they govern. A mature implementation treats the gate decision itself as the primary artifact: a structured record assembling evidence, confidence levels, named ownership, identified gaps, and explicit rationale before any downstream commitment is made.

This pattern is **aspirational at the incubation stage, not required.** What is required at incubation is:

1. A written, reviewable governance specification exists as a document
2. The project's architecture is compatible with enforcement as institutional capacity develops

The CDFI Framework satisfies both requirements. The `configs/threshold_gates.yaml` file is a machine-readable governance specification. The deployment tier thresholds, gate logic, and escalation triggers are all expressed as auditable parameters. The four decision states described below can be implemented as a structured decision record at the Level 3 authority's discretion.

---

## The Four Decision States

Every deployment decision involving a CDFI-scored model resolves to one of four states. Each carries distinct documentation requirements and escalation obligations.

```
GO
────────────────────────────────────────────────────────────
Condition:  CDFI score clears the relevant tier threshold;
            cap rate is within expected range for the tier;
            framing gap is disclosed and acceptable;
            authority level classification complete (final CDFI);
            human theological review complete;
            C5 subgroup data available or acknowledged gap
            documented with enhanced oversight plan

Documentation: Full decision record (see c2-human-accountability.md
               Level 3 template); signed by named Level 3 authority

Escalation: None required; standard temporal versioning applies

────────────────────────────────────────────────────────────
CONDITIONAL-GO
────────────────────────────────────────────────────────────
Condition:  CDFI score clears threshold BUT one or more of:
            — Authority level classification pending
              (preliminary CDFI, not final)
            — Human theological review pending
            — C5 subgroup data absent (no analysis conducted)
            — Framing gap requires prompt wrapper mitigation

Documentation: Decision record includes explicit disclosure
               of each open condition; enhanced oversight
               requirements for each gap; re-evaluation
               trigger date when condition closes

Escalation: Notify Level 2 (Project Lead) that deployment
            is proceeding with open conditions; document
            that notification

────────────────────────────────────────────────────────────
NO-GO
────────────────────────────────────────────────────────────
Condition:  CDFI score below tier threshold; OR
            cap rate materially exceeds benchmark; OR
            either gate failure at disqualifying frequency;
            OR C1 pre-screening identifies out-of-scope tool

Documentation: Written record of no-go determination with
               reasoning; retained in institutional governance log

Escalation: None required unless a higher authority
            disagrees with the no-go determination —
            in which case, escalate per Canon 1609 pattern
            (written dissent to next level)

────────────────────────────────────────────────────────────
DEFER
────────────────────────────────────────────────────────────
Condition:  Insufficient information to make a go/no-go
            determination; missing data that would change
            the decision; open publication gates not yet
            resolved; temporal versioning triggered but
            re-evaluation not yet complete

Documentation: Record of what information is missing;
               named owner of each missing item;
               timeline for resolution;
               interim operating instructions (continue
               current use, pause, or suspend pending
               more information)

Escalation: Notify Level 3 authority of deferred status;
            set calendar trigger for resolution review
```

---

## Decision Authority Mapping

| Deployment Context | Minimum Decision Authority | Decision State Options |
|-------------------|---------------------------|----------------------|
| Formation and Catechesis (CDFI ≥ 85) | Vicar General, Principal, or Rector | Go or Conditional-Go (with disclosed gaps) |
| General Information (CDFI 70–84) | Pastor, Department Head, or designee | Go, Conditional-Go, or Defer |
| R&D Only (CDFI 50–69) | Institutional AI governance officer | Conditional-Go (R&D scope only) |
| Not Recommended (below 50 or gate failure) | No deployment authorized | No-Go only |
| Pending re-evaluation (version update) | Same as original deployment authority | Defer until re-evaluation complete |

**The committee-without-owner failure condition:** Accountability distributed across a committee without a named decision owner fails C2 and, by extension, fails C6. The decision authority column above requires a specific named person — not a committee, working group, or team designation without an individual attached to it.

---

## Escalation Conditions

### Mandatory suspension (suspend immediately, then notify)

| Trigger | Action | Owner |
|---------|--------|-------|
| Model receives major version update | Suspend; move to Defer state; initiate re-evaluation | Level 3 |
| Hallucination event reported in production (fabricated magisterial citation) | Suspend; log response verbatim; notify Evals Expert; re-evaluate before restoring | Level 3 |
| Relativism resistance failure reported (defined doctrine presented as opinion) | Suspend; log; assess whether framing gap or new failure mode; re-evaluate | Level 3 |
| Named Level 3 authority leaves the institution | New authority must review and re-sign deployment authorization before continuing | Incoming Level 3 |

### Review escalation (continue with enhanced oversight, notify Level 3)

| Trigger | Action | Owner |
|---------|--------|-------|
| Production cap rate exceeds benchmark cap rate by > 5 percentage points | Escalate to Level 3; document pattern; consider tier reclassification | Level 4 → Level 3 |
| User population changes materially (e.g., adult formation → youth formation) | Re-evaluate tier assignment for new population; do not assume prior approval transfers | Level 3 |
| User reports response that cites a source they cannot locate | Level 4 review; if fabrication confirmed, treat as hallucination event above | Level 4 |

---

## Human Review Triggers

These triggers apply to all deployed models regardless of tier. Level 4 authority (formation director, catechist, teacher) must review the specific AI response before the user acts on it.

| Trigger | Required Action |
|---------|----------------|
| Response cites a specific magisterial document by title and paragraph number | Verify the citation exists and contains the attributed language before using in teaching or publication |
| User identifies the question as affecting a significant life decision | Human review and pastoral conversation before treating AI response as guidance |
| User is a minor | Adult supervisor review of all responses in youth formation contexts |
| Response expresses uncertainty on a question the user believes is settled teaching | Supervisor clarification before user acts on the response |
| Response addresses a topic with known framing sensitivity (eschatology, moral theology) | These domains produced the highest cap rates in SAICRED v2; confirm response against cooperative-framing query |
| Response involves a topic where the model's framing gap exceeds 10 CDFI points | Enhanced oversight: the adversarial and neutral framing variants of this question are known failure surfaces |

---

## Appeal Pathway (Canon 1609 Standard)

The appeal pathway preserves, in institutional form, the Canon 1609 requirements: written conclusions, structured deliberation, the right to contest a judgment, and transmission of dissent to a higher authority.

```
STEP 1 — Report (no technical knowledge required)
  Any person who believes they received doctrinally incorrect
  AI-generated information contacts the Level 4 supervisor
  (catechist, teacher, formation director) in plain language.

STEP 2 — Initial Response (within 5 business days)
  Level 4 escalates to Level 3 institutional authority.
  Level 3 reviews the specific AI response against the
  CDFI rubric and relevant Church teaching.
  Level 3 produces a written determination (Canon 1609:
  written conclusions with reasons in law and in fact).

STEP 3 — Determination: Two paths

  Path A — Scoring failure confirmed:
    → Suspend the model from the permitted use context
    → Log the response in the institutional governance record
    → Notify the Evals Expert (Mark Julius Banasihan)
    → Initiate model re-evaluation before restoring deployment
    → Document re-evaluation result and restoration decision

  Path B — Response within expected behavior at tier:
    → Document the determination with supporting rationale
    → Provide pastoral response to the affected person
    → Log the incident and outcome in governance record

STEP 4 — Response to Affected Person (within 30 days)
  Level 3 authority provides a written response that:
    □ Acknowledges the concern
    □ States the determination (Path A or Path B)
    □ Describes what corrective action was taken
    □ Provides the correct Church teaching on the matter

STEP 5 — Further Recourse (Canon 1609: dissent to higher tribunal)
  If the affected person contests the Level 3 determination:
    → Diocese/religious institute: bishop or superior
    → CDCF-governed projects: CDCF Board
    → Normal canonical recourse channels
```

**What the appeal pathway is not:** A technical dispute about the CDFI score or methodology. The affected person does not need to understand CDFI. The pathway is a pastoral accountability mechanism. The CDFI score is one input; the pastoral response to the affected person is what the process produces.

---

## Canonical and Magisterial Citations

- *Code of Canon Law*, Canon 1609, Vatican City: Libreria Editrice Vaticana, 1983. https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib7-cann1501-1670_en.html

- CDCF Research, "Governance-as-Code for Catholic Technology Deployment." https://catholicdigitalcommons.org/governance/research/governance-as-code-catholic-technology

---

*Related: [c2-human-accountability.md](c2-human-accountability.md) — full accountability matrix*

*Related: [docs/specifications/deployment-tiers.md](../../specifications/deployment-tiers.md) — tier definitions*

*Related: [docs/governance/temporal-versioning.md](../temporal-versioning.md) — version expiration protocol*
