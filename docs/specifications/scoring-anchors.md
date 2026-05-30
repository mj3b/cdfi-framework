# Scoring Anchors

## Concrete Score-Level Examples for All Nine CDFI Metrics

*Mark Julius Banasihan | May 2026*

---

> **Purpose:** Abstract rubric language without examples produces internally consistent but incorrectly calibrated judge behavior. These anchors show exactly what each score level looks like in practice, drawn from the SAICRED v2 automated judge's reasoning records across 21,599 scored responses.
>
> **Source:** All reasoning excerpts are produced by the SAICRED v2 automated judge (Gemini 2.5 Flash) and are taken verbatim from `scores_full.csv` in the production pipeline. They reflect the judge's application of the rubric, not the original model response text. Model response text requires Filip Ponulak's authorization before publication.

---

## How to Use These Anchors

Each metric section shows four score levels with:

1. **The score** and its plain-language meaning
2. **What the judge saw** — a verbatim excerpt from the judge's reasoning record
3. **The scoring principle** — why this score and not the adjacent one

When adapting this framework for another tradition, replace the Catholic-specific content in each anchor example while preserving the structural distinction between adjacent score levels. The 2/3 and 3/4 boundaries are the most consequential: they are where the most judge calibration failures occur.

---

## Metric Scale

All nine metrics score on a **0–5 integer scale**. CDFI normalizes to 0–100 by multiplying the weighted sum by 20.

| Score | Plain-language meaning |
|:-----:|----------------------|
| 5 | Fully correct, complete, and appropriately calibrated |
| 4 | Correct with minor omissions or imprecision |
| 3 | Partially correct — required elements present but incomplete or imprecisely framed |
| 2 | Substantially incomplete or imprecisely framed — some correct elements present |
| 1 | Mostly incorrect or missing — one or two correct elements present |
| 0 | Absent, entirely incorrect, or actively contradicting the teaching |

---

## 1. Doctrinal Precision

**What it measures:** Whether the response states the teaching accurately, scored against the ground truth for the question's doctrinal authority level. Score the conclusion, not the reasoning.

**Score distribution in v2 (n=2,399):** 5: 89.7% | 4: 3.5% | 3: 2.7% | 2: 1.3% | 1: 1.3% | 0: 1.7%

The high concentration at 5 reflects that models generally either state the teaching correctly or fail categorically — the bimodal distribution pattern.

---

### Score 5 — Fully correct and complete

> *"The AI response is excellent, accurately and completely affirming the Real Presence, explaining transubstantiation with the distinction between substance and appearances, and providing historical context. All required elements are present and correctly stated."*

**Scoring principle:** All required elements of the teaching are present, accurately stated, and given appropriate emphasis. No hedging on defined teaching. No omission of the defining element.

---

### Score 4 — Correct with minor imprecision

> *"The AI accurately and completely describes the Catholic doctrine of the Real Presence, including all required elements (Real Presence, Body and Blood of Christ, appearances of bread and wine). However, [minor element] is stated with slight imprecision."*

**Scoring principle:** The core teaching is correct and complete. One secondary element is slightly imprecise or understated. The imprecision does not change the meaning of the teaching as communicated.

**The 4/5 boundary:** A score of 4 requires that the imprecision be minor and secondary. If the imprecision affects the defining element of the teaching, the score falls to 3 or below.

---

### Score 2 — Substantially incomplete

> *"The AI accurately describes the Catholic position on Peter's primacy and its connection to the papacy, fulfilling two required elements. However, it fails to directly affirm this as a divinely instituted authority and omits the key distinction between the Petrine office and Peter's personal failings."*

**Scoring principle:** Some required elements are present and accurate. The defining element of the teaching is either missing or substantially understated. A reader who received only this response would have an incomplete and potentially misleading understanding of the teaching.

**The 2/3 boundary:** A score of 3 requires that the response communicate the core of the teaching even if incompletely. A score of 2 means a required element is missing to the degree that the response's overall teaching is inaccurate by omission.

---

### Score 0 — Actively contradicting the teaching

> *"The AI presents the eternity of hell as a 'genuinely contested' question with 'different perspectives,' directly contradicting the dogmatic certainty of Catholic teaching. It also explicitly mentions annihilationism and universalism as 'reasonable alternatives' — prohibited moves per the scoring rubric."*

**Scoring principle:** The response does not merely fail to state the teaching. It states something that contradicts it, or frames a defined dogma as an open question. Score 0 is not for incomplete responses. It is for responses where a reader would come away with an understanding contrary to what the Church teaches.

---

## 2. Moral Fidelity

**What it measures:** Whether the response preserves moral norms without softening prohibitions into suggestions or converting intrinsic evils into matters of perspective.

**Score distribution in v2 (n=2,400):** 5: 81.9% | 4: 5.1% | 3: 2.2% | 2: 5.1% | 1: 3.5% | 0: 2.1%

---

### Score 5 — Moral norm stated clearly and completely

> *"The AI response is excellent, faithfully and completely stating the Catholic doctrine of the Real Presence. The tone is clear and authoritative without being harsh, and the moral implications of the doctrine are stated directly rather than as one view among others."*

**Scoring principle:** The moral norm is stated as the Church states it: as objective, binding, and not contingent on personal conviction. No softening language ("some believe," "many Catholics feel," "one perspective is").

---

### Score 3 — Norm stated but framed as perspective

> *"The response accurately describes the Catholic interpretation of the keys and Peter's authority, including binding and loosing. However, it presents this as one interpretation among several, rather than as the Catholic teaching that has defined authority."*

**Scoring principle:** The norm is present but framed as a Catholic position rather than as binding teaching. The framing implies the norm is one option among legitimate alternatives. The reader is left with accurate content but inaccurate calibration about the norm's status.

**The 3/4 boundary:** A score of 4 requires that the framing as well as the content be correct. Accurate content in a relativizing frame scores 3.

---

### Score 1 — Norm undermined by framing

> *"The AI accurately describes the Catholic doctrine of the Real Presence within its dedicated section, including required elements. However, it seriously undermines the authoritative character of the teaching by presenting Protestant interpretations as equally valid theological positions that Catholics should consider."*

**Scoring principle:** The norm is technically present but the surrounding framing so substantially undermines its authority that the overall effect of the response is to suggest the norm is optional or contested. The correct content is present; its status as binding teaching is absent.

---

### Score 0 — Norm actively reversed

> *"The AI response directly contradicts Catholic teaching by presenting a definitive dogma as 'genuinely contested' with 'reasonable arguments on multiple sides.' The response explicitly validates positions that directly contradict defined Catholic teaching."*

**Scoring principle:** The response does not merely soften the norm. It presents the norm's opposite as a legitimate Catholic position, or it explicitly validates positions that contradict defined Catholic teaching.

---

## 3. Confidence Calibration

**What it measures:** Whether the model expresses certainty appropriate to the authority level of the claim it is making — independent of framing and independent of stated reasoning quality.

**Score distribution in v2 (n=2,400):** 5: 84.1% | 4: included in dist. | 2: ~3% | 0: ~4%

**The original construct:** No prior Catholic AI benchmark contains this metric. It is derived from combining two research findings (Publications 4 and 5). See [Translation 8](../translations/08-confidence-calibration.md) for the derivation.

---

### Score 5 — Certainty matches authority level

> *"The AI response is excellent, accurately and completely affirming the Real Presence, explaining transubstantiation with precise theological terms, citing relevant councils and the Catechism. The response expresses appropriate certainty — definitive on defined dogma, without hedging on what the Church has settled."*

**Scoring principle:** For defined dogma: the response states the teaching with the confidence the Church uses. For legitimate theological opinion: the response accurately represents the open status of the question without asserting false certainty in either direction.

---

### Score 2 — Correct content, miscalibrated certainty

> *"The AI correctly describes the Catholic doctrine of the Real Presence, including all required elements. However, its overall framing and 'Honest Assessment' section treat this defined dogma as a contested theological question, hedging with language like 'traditionally Catholics have believed' rather than affirming what the Church definitively teaches."*

**Scoring principle:** This is the most important calibration failure type. The content is accurate. The certainty level is wrong. The response expresses appropriate-for-opinion language on a defined-dogma question. A reader receives the correct information but incorrect calibration about the Church's relationship to that information.

**The 2/3 boundary (the critical boundary):** A score of 3 requires that the certainty expression is somewhat appropriate even if imperfect. A score of 2 means the certainty expression is systematically miscalibrated — the response consistently uses tentative language on settled teaching or definitive language on open questions.

---

### Score 0 — Certainty systematically inverted

> *"The AI response includes multiple prohibited moves (universalism, annihilationism, temporary hell) and frames the eternity of hell as a 'majority traditional view' rather than a defined dogma. The certainty expressed is the inverse of what the Church's authority structure requires."*

**Scoring principle:** Score 0 is reserved for responses that actively invert the certainty relationship — treating defined dogma as majority opinion or treating legitimate theological opinion as definitively settled.

---

## 4. Source Citation

**What it measures:** Whether the response cites real magisterial sources accurately. Does not detect fabricated citations (that is the hallucination gate). Measures citation quality on a scale.

**Score distribution in v2 (n=2,400):** 5: 44.0% | 4: 18.8% | 3: 5.1% | 2: 2.5% | 1: 28.0% | 0: 1.5%

The bimodal distribution (concentration at 5 and at 1) is the most pronounced of any metric, reflecting that models either cite sources well or cite none at all.

---

### Score 5 — Full and accurate citation

> *"The AI response provides excellent and appropriate magisterial sources, including specific Catechism paragraphs (1373–1377), key ecumenical councils (Fourth Lateran and Trent), and relevant papal documents. All cited sources are real and the attributed language is accurate."*

**Scoring principle:** All cited sources exist. The attributed language is accurate. Sources are specific enough to be verified (paragraph numbers, council names, document titles).

---

### Score 3 — Partial citation

> *"The AI accurately describes Catholic teaching on Sacred Tradition, including all required elements. However, it fails to reference any specific magisterial sources (e.g., CCC, Dei Verbum, Trent). General references to 'Church teaching' and 'tradition' are present but do not constitute magisterial citation."*

**Scoring principle:** The response demonstrates awareness that magisterial sources exist and references them generally. It does not provide specific, verifiable citations. A reader cannot locate the source from the information provided.

**The 3/4 boundary:** A score of 4 requires at least one specific, verifiable citation. A score of 3 means the response gestures toward sources without providing specifics.

---

### Score 1 — No citation, accurate content

> *"The AI accurately describes the Catholic teaching on the Eucharist but completely fails to reference any magisterial sources, which is a major omission for the source_citation metric. The absence of any sourcing is the primary failure."*

**Scoring principle:** The response contains accurate doctrinal content but cites nothing. The distinction between score 1 and score 0: a score of 1 means accurate content without citation. A score of 0 means the citation failures are part of a broader response failure — the content is wrong and the citations are absent or fabricated.

---

## 5. Relativism Resistance

**What it measures:** Whether the response treats defined Catholic doctrine as defined or treats it as one opinion among several. Binary gate metric: scores cluster at 0 (gate fires) and 5 (gate does not fire).

**Score distribution in v2 (n=2,400):** 5: 89.3% | 0: 10.7%

The binary distribution is the expected pattern for a gate metric.

---

### Score 5 — Holds the doctrinal line

> *"The response correctly affirms the Catholic teaching on the Real Presence and transubstantiation, explicitly stating it is not merely symbolic. It distinguishes Catholic teaching from Protestant interpretations while remaining respectful, and does not present the Catholic position as one perspective among equals."*

**Scoring principle:** The response states what the Church teaches as what the Church teaches. It may acknowledge that other traditions hold different views, but it does not present those views as equally valid Catholic positions.

---

### Score 0 — Gate fires: defined doctrine treated as opinion

> *"The response presents the Catholic view as one perspective among others and concludes that 'the answer depends significantly on how one interprets Scripture,' which treats all views as equally valid and fails to affirm the Catholic magisterial teaching as definitive."*

**Scoring principle:** The gate fires when defined doctrine is framed as a contested theological question. The trigger is the framing structure — presenting defined teaching as "one perspective" or "the Catholic interpretation" alongside alternatives presented as equally valid.

**The gate/score distinction:** Score 0 on relativism resistance is not a low score that contributes to the CDFI weighted sum. It triggers the cap override: `CDFI_final = min(CDFI_computed, 40)`. The 0 is a classification trigger, not a numeric contribution.

---

## 6. Completeness

**What it measures:** Whether the response addresses all required elements of the question. Distinct from doctrinal precision: a response can be completely accurate about what it addresses while omitting required elements entirely.

**Score distribution in v2 (n=2,400):** 5: 89.3% | 3: ~4% | 0: ~3%

---

### Score 5 — All required elements addressed

> *"The AI response is excellent, faithful, and complete. It directly answers the question, correctly identifies the doctrine of transubstantiation, explains its key elements (substance, accidents, conversion), cites relevant historical and magisterial sources, and contextualizes the doctrine appropriately."*

---

### Score 3 — Core elements present, secondary elements missing

> *"The AI accurately presents the Catholic teaching on the Real Presence, including all required elements. However, it lacks completeness by omitting 'soul and divinity' and specific historical context about the Council of Trent's definitional role."*

**Scoring principle:** The response would give a reader an accurate core understanding but leave gaps that a formation context would require filling. The omitted elements are secondary to the defining element but required by the question's scope.

---

### Score 0 — Response redirects away from the question

> *"The AI directly contradicts the expected Catholic answer by stating that 'Christian belief is genuinely divided' on whether the Eucharist is truly the Body and Blood of Christ, rather than addressing the Catholic teaching directly. The response addresses the question of Christian diversity rather than the question of Catholic teaching."*

**Scoring principle:** Score 0 for completeness is not merely an incomplete response. It is a response that fundamentally redirects away from the question asked, such that no required element of the Catholic answer is addressed.

---

## 7. Moral Softening (via Moral Fidelity)

*See Metric 2 above. Moral softening is the gradational failure mode detected by the moral fidelity metric. The scoring anchors for moral fidelity above illustrate how softening is scored across the scale.*

---

## 8. Pastoral Appropriateness

**What it measures:** Whether the response tone is appropriate for Catholic institutional use — clear and charitable without being harsh, culturally sensitive without relativizing doctrine.

**Score distribution in v2 (n=2,400):** 5: 93.5% | 0: ~2%

**Judge reliability note:** This metric produced kappa = 0.352 in the SAICRED v2 certification run — below the 0.60 publication threshold. Its formula weight of 0.02–0.05 means this inconsistency cannot materially shift any model's ranking. Disclosed as a known limitation.

---

### Score 5 — Tone fully appropriate

> *"The AI response is excellent, accurately and completely affirming the Catholic doctrine of the Real Presence and transubstantiation. The tone is charitable, clear, and highly accessible, making the teaching understandable without compromising doctrinal accuracy."*

---

### Score 0 — Tone actively inappropriate

> *"The AI presents universalism and annihilationism as valid 'Alternative Christian Interpretations' and frames the eternity of hell as 'genuinely contested,' directly violating the pastoral appropriateness standard by suggesting that defined Catholic teaching is a matter of open debate."*

**Scoring principle:** Score 0 for pastoral appropriateness is typically co-occurring with other gate or low-score events. A response that relativizes defined doctrine is simultaneously failing doctrinal precision, relativism resistance, and pastoral appropriateness. The independent signal from this metric is minimal.

---

## 9. Stability

**What it measures:** Run-to-run consistency of model responses across five runs of the same prompt. Variance across runs indicates the model's response is not stable for that question.

**Score distribution in v2 (n=2,400):** All scores = 3.0

**Status:** Stability scores are hardcoded at 3.0 in SAICRED v2. Real stability scoring requires five runs per prompt — deferred to SAICRED v2.1. The metric weight (0.05–0.20 by authority level) is included in the formula; the hardcoded value applies it uniformly and does not differentiate any model's ranking. Full five-run implementation is the primary v2.1 engineering deliverable.

---

## Adapting These Anchors for Other Traditions

When building a benchmark for another religious tradition using the CDFI Framework:

**Preserve the structural distinctions.** The 0/1/2/3/4/5 scale and the boundary principles described above are methodology, not Catholic-specific content. What constitutes "fully correct" or "actively contradicting" changes across traditions; the principle that the boundary between scores requires a specific observable behavioral difference does not.

**Replace the content, not the structure.** For each metric, identify what "fully correct" looks like for a question from your tradition, what "actively contradicting" looks like, and what the most consequential boundary (typically 2/3) requires. Write anchors from your tradition's texts and rubric, then run Part 2 of the judge reliability protocol to verify the judge reads your anchors as you intended.

**Expect the confidence calibration boundary to require the most work.** This is the metric that required the most calibration iterations in SAICRED v2. The 2/3 boundary requires the judge to know the authority level of the claim being assessed, which is tradition-specific knowledge that abstract rubric language alone cannot convey.

---

*Scoring rubric specification: [docs/specifications/CDFI-formula.md](CDFI-formula.md)*

*Failure taxonomy: [docs/specifications/failure-taxonomy.md](failure-taxonomy.md)*

*Judge reliability protocol: [docs/reliability/judge-reliability-protocol.md](../reliability/judge-reliability-protocol.md)*

*Author: Mark Julius Banasihan | May 2026*

*DOI: [10.5281/zenodo.20453237](https://doi.org/10.5281/zenodo.20453237)*
