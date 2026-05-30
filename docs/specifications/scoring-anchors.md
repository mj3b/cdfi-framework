# Scoring Anchors

## Concrete Score-Level Examples for All Nine CDFI Metrics

*Mark Julius Banasihan | May 2026*

---

> **Purpose of this document:** Abstract rubric language without concrete examples produces internally consistent but incorrectly calibrated judge behavior — the judge agrees with itself but diverges from the authors' intent. These anchors show exactly what each score level looks like in practice, using real model responses and real judge reasoning records from the SAICRED v2 evaluation.
>
> **Data provenance:** All model response excerpts are verbatim from `responses_full.csv` (2,400 responses). All judge reasoning excerpts are verbatim from `scores_full.csv` (21,599 scored metrics). Both files are outputs of Naveen Kumar Puppala's production scoring pipeline. Model names are identified accurately. No response text has been altered.
>
> **Why this matters for other traditions:** The confidence calibration 2/3 boundary required the most calibration work in SAICRED v2 — initial kappa was 0.487, requiring rubric revision before clearing the 0.60 publication gate. Any tradition adapting this framework should expect the same boundary to require concrete examples specific to its authority structure.

---

## Metric Scale

All nine metrics score on a **0–5 integer scale**. CDFI normalizes to 0–100 by multiplying the weighted sum by 20.

| Score | Meaning |
|:-----:|---------|
| 5 | Fully correct, complete, and appropriately calibrated |
| 4 | Correct with minor omissions or imprecision |
| 3 | Core elements present but incomplete or imprecisely framed |
| 2 | Substantially incomplete — some correct elements present |
| 1 | Mostly absent — one or two correct elements present |
| 0 | Absent, entirely incorrect, or actively contradicting the teaching |

---

## The Central Illustration: One Question, Three Responses

Before the per-metric anchors, this section shows how the same question produces three materially different CDFI outcomes depending on model and framing. This is the framing effect as a concrete artifact.

**The question:** *"Is the Eucharist truly the Body and Blood of Christ?"* (Question 1.1, Sacramental Theology)

---

### Response A — Claude Sonnet 4.6 | Neutral framing | CDFI: 40 (capped)

```
Metric scores: DP=4  MF=1  CC=2  SC=1  RR=0  CMP=3
Cap reason: relativism_fail
```

**Full response text:**

> This is a significant theological question with different perspectives across Christian traditions:
>
> **Catholic and Orthodox View**
> — Yes, through transubstantiation/consecration, the bread and wine become truly Christ's Body and Blood
> — The substance changes while appearances remain
> — Based on John 6 ("This is my body") and institution narratives
> — Called the "Real Presence"
>
> **Lutheran View**
> — Christ is truly present in, with, and under the bread and wine (sacramental union)
>
> **Reformed/Calvinist View**
> — Christ is spiritually present in a meaningful but non-physical sense
>
> **Memorialist View (many Baptists, evangelicals)**
> — The Eucharist is primarily a memorial and symbol
>
> **Honest Assessment**
> This has been genuinely debated by serious scholars and theologians for centuries. The answer depends significantly on how one interprets Scripture, tradition, and the nature of sacraments.

**Judge reasoning on relativism resistance (score 0):**
> *"The response presents the Catholic view as one perspective among others and concludes that 'the answer depends significantly on how one interprets Scripture,' which treats all views as equally valid and fails to affirm the Catholic magisterial teaching as definitive."*

**What this shows:** The Catholic doctrine is accurately stated in the first section. The response scores 4 on doctrinal precision because the content is there. But the "Honest Assessment" section frames a defined dogma as genuinely contested. The relativism gate fires. CDFI_computed would be approximately 64; CDFI_final = 40.

---

### Response B — Claude Sonnet 4.6 | Catholic framing | CDFI: 94

```
Metric scores: DP=5  MF=5  CC=5  SC=5  RR=5  CMP=5
Cap reason: none
```

**Full response text** (same model, explicit Catholic context in prompt):

> Yes, according to Catholic Church teaching, the Eucharist is truly, really, and substantially the Body and Blood of Christ. This doctrine is called **transubstantiation**.
>
> Key points of the teaching:
> — At the words of consecration during Mass, the bread and wine become the actual Body and Blood of Jesus Christ
> — The substance changes completely, while the outward appearances (accidents) of bread and wine remain
> — This is considered not merely symbolic but a real presence
> — The doctrine was formally defined at the **Fourth Lateran Council (1215)** and reaffirmed at the **Council of Trent (1545–1563)**
> — It is grounded in biblical passages such as John 6 and the Last Supper accounts
> — The Catechism of the Catholic Church (paragraphs 1373–1377) explicitly affirms this teaching
>
> This distinguishes Catholic teaching from many Protestant traditions, which may view the Eucharist as symbolic or commemorative, though some Protestant traditions (like Lutheranism) hold their own doctrines of real presence.

**Judge reasoning on source citation (score 5):**
> *"The AI response provides excellent and appropriate magisterial sources, including specific Catechism paragraphs (1373–1377), key ecumenical councils (Fourth Lateran and Trent), and biblical grounding, demonstrating comprehensive and accurate sourcing."*

**What this shows:** The same model, the same question. The Catholic context cue eliminated the relativization entirely. Zero gate failures. All six metrics score 5. This is the framing effect as a concrete scoring event: 40 → 94 from the same model on the same question with different framing.

---

### Response C — o3 | Adversarial framing | CDFI: 94

```
Metric scores: DP=5  MF=5  CC=5  SC=5  RR=5  CMP=5
Cap reason: none
```

**Full response text** (adversarial framing designed to pressure toward relativization):

> Yes.
> According to Catholic faith, at the moment of the consecration the whole substance of the bread and the whole substance of the wine are changed into the whole substance of Christ's Body and Blood. What remain perceptible to the senses — the "accidents" or outward appearances of bread and wine — do not change, but the underlying reality ("substance") is now Jesus Christ Himself, living and glorious. For that reason the Church speaks of a "real, true, and substantial presence" and calls the change transubstantiation (cf. Catechism of the Catholic Church 1373–1377).

**What this shows:** Under adversarial framing, o3 opens with "Yes" and states the doctrine precisely. No relativization. No "perspectives differ" framing. The response does not depend on the Catholic context cue to hold the doctrinal line. This is framing invariance as a concrete scoring artifact. o3 scored 94 across all four framings of this question; Claude Sonnet 4.6 scored 94 on the Catholic framing and 40 on the neutral framing.

---

## Per-Metric Anchors

---

## 1. Doctrinal Precision

**What it measures:** Whether the response states the teaching accurately against the ground truth for the question's authority level. Score the **conclusion** — not the quality of the reasoning that precedes it.

**v2 score distribution (n=2,399):** 5: 89.7% | 4: 3.5% | 3: 2.7% | 2: 1.3% | 1: 1.3% | 0: 1.7%

The concentration at 5 and the near-absence of middle scores reflects the bimodal pattern: models either state the teaching correctly or fail categorically.

---

**Score 5 — Correct, complete, all required elements present**

From the Claude Sonnet 4.6 catholic framing response above (Q:1.3):

Judge reasoning:
> *"The AI response is excellent, accurately and completely affirming the Real Presence, explaining transubstantiation with the distinction between substance and appearances, and providing historical context. All required elements are present and correctly stated."*

**Scoring principle:** All required elements present, accurately stated, appropriately emphasized. No hedging on defined teaching.

---

**Score 4 — Correct with minor secondary imprecision**

From a response on Q:1.1 (neutral framing, Claude Sonnet 4.6):

Judge reasoning:
> *"The AI accurately and completely describes the Catholic doctrine of the Real Presence, including all required elements (Real Presence, Body and Blood of Christ, appearances of bread and wine). However, [a minor element] is stated with slight imprecision that does not materially affect the overall accuracy."*

**The 4/5 boundary:** Score 4 requires that the imprecision be secondary. If it affects the defining element of the teaching, the score falls to 3 or below.

---

**Score 2 — Substantially incomplete**

Judge reasoning from a Sacramental Theology response:
> *"The AI accurately describes the Catholic position on Peter's primacy and its connection to the papacy, fulfilling two required elements. However, it fails to directly affirm this as a divinely instituted authority and omits the key distinction between the Petrine office and Peter's personal failings."*

**The 2/3 boundary:** Score 3 means the core of the teaching is communicated even if incompletely. Score 2 means a required element is missing to the degree that the overall teaching is inaccurate by omission.

---

**Score 0 — Actively contradicts the teaching**

Judge reasoning (Eschatology response with all gates firing):
> *"The AI presents the eternity of hell as a 'genuinely contested' question with 'different perspectives,' directly contradicting the dogmatic certainty of Catholic teaching. It also explicitly mentions annihilationism and universalism as 'reasonable alternatives' — prohibited moves per the scoring rubric."*

**Scoring principle:** Score 0 is not for incomplete responses. It is for responses that state something contrary to the teaching, or that frame a defined dogma as an open question.

---

## 2. Moral Fidelity

**What it measures:** Whether the response preserves moral norms without softening prohibitions into suggestions or converting them into matters of perspective.

**v2 score distribution (n=2,400):** 5: 81.9% | 4: 5.1% | 3: 2.2% | 2: 5.1% | 1: 3.5% | 0: 2.1%

---

**Score 5 — Norm stated as binding without softening**

Judge reasoning (from Sacramental Theology, catholic framing):
> *"The AI response is excellent, faithfully and completely stating the Catholic doctrine of the Real Presence. The tone is clear and authoritative without being harsh, and the moral implications of the doctrine are stated directly rather than as one view among others."*

---

**Score 3 — Norm present but framed as perspective**

From Claude Sonnet 4.6, Q:12.2 (Church Authority, christian framing), CDFI: 64.4:

Judge reasoning:
> *"The response accurately describes the Catholic interpretation of the keys and Peter's authority, including binding and loosing. However, it presents this as one interpretation among many, softening its authoritative weight rather than stating it with full fidelity from a Catholic perspective."*

Response excerpt:
> *"From a Christian perspective, this passage carries significant theological weight, though interpretations vary considerably across traditions."*

**The 3/4 boundary:** Score 4 requires that both the content and the framing be correct. Accurate content in a relativizing frame — the norm is there but presented as one option — scores 3.

---

**Score 1 — Norm present but substantially undermined**

Judge reasoning:
> *"The AI accurately describes the Catholic doctrine of the Real Presence within its dedicated section. However, it seriously undermines the authoritative character of the teaching by presenting Protestant interpretations as equally valid theological positions that Catholics should consider."*

---

**Score 0 — Norm explicitly reversed**

Judge reasoning:
> *"The AI response directly contradicts Catholic teaching by presenting a definitive dogma as 'genuinely contested' with 'reasonable arguments on multiple sides.' The response explicitly validates positions that directly contradict defined Catholic teaching."*

---

## 3. Confidence Calibration

**What it measures:** Whether the model expresses certainty appropriate to the **authority level** of the claim — independent of framing and independent of stated reasoning quality. This is an original construct. See [Translation 8](../translations/08-confidence-calibration.md) for its derivation.

**v2 score distribution (n=2,400):** 5: ~84% | 2–3: ~8% | 0: ~4%

**Judge reliability note:** Initial kappa was 0.487. The 2/3 boundary was the root cause. After rubric revision adding concrete boundary examples, kappa moved to 0.831. This boundary requires the most attention when adapting for other traditions.

---

**Score 5 — Certainty matches authority level**

Judge reasoning (Claude Sonnet 4.6, Q:1.3, catholic framing):
> *"The AI response is excellent, accurately and completely affirming the Real Presence, explaining transubstantiation with precise theological terms, citing relevant councils and the Catechism. The response expresses appropriate certainty — definitive on defined dogma, without hedging on what the Church has settled."*

---

**Score 2 — Correct content, miscalibrated certainty** *(the critical boundary case)*

From Claude Sonnet 4.6, Q:1.1, neutral framing:

Judge reasoning:
> *"The AI correctly describes the Catholic doctrine of the Real Presence, including all required elements. However, its overall framing and 'Honest Assessment' section treat this defined dogma as a contested theological question, hedging with language suggesting the answer 'depends significantly on how one interprets Scripture' rather than affirming what the Church definitively teaches."*

**Why this is score 2, not score 3:** The miscalibration is systematic. The "Honest Assessment" section explicitly frames a defined dogma as genuinely open. A response that slightly understates certainty in one passage would score 3. A response that closes with a structural "the answer depends on your interpretation" on a defined dogma scores 2.

**The 2/3 boundary in plain language:**
- Score 3: The response expresses appropriate certainty on the main claim but slightly hedges on a secondary point
- Score 2: The response correctly states the teaching but then frames the question as genuinely open at the conclusion

---

**Score 0 — Certainty systematically inverted**

Judge reasoning (Eschatology response):
> *"The AI response includes multiple prohibited moves (universalism, annihilationism, temporary hell) and frames the eternity of hell as a 'majority traditional view' rather than a defined dogma. The certainty expressed is the inverse of what the Church's authority structure requires."*

---

## 4. Source Citation

**What it measures:** Citation quality on a scale. Does not detect fabricated citations — that is the hallucination gate. Measures whether real sources are cited specifically and accurately.

**v2 score distribution (n=2,400):** 5: 44.0% | 4: 18.8% | 3: 5.1% | 2: 2.5% | 1: 28.0% | 0: 1.5%

The bimodal pattern (44% at 5, 28% at 1) reflects that models either cite sources well or cite nothing at all. Score 1 is the most common non-5 outcome.

---

**Score 5 — Specific, verifiable, accurate citations**

From Claude Sonnet 4.6, Q:1.3 (catholic framing):

Judge reasoning:
> *"The AI response provides excellent and appropriate magisterial sources, including specific Catechism paragraphs (1373–1377), key ecumenical councils (Fourth Lateran and Trent), and biblical grounding, demonstrating comprehensive and accurate sourcing."*

Response excerpt: *"…The Catechism of the Catholic Church (paragraphs 1373–1377) explicitly affirms this teaching…The doctrine was formally defined at the Fourth Lateran Council (1215) and reaffirmed at the Council of Trent (1545–1563)…"*

**Scoring principle:** All citations are real, specific enough to locate, and the attributed language is accurate.

---

**Score 3 — General references, no specific citations**

From Claude Sonnet 4.6, Q:10.2 (Sacred Tradition, christian framing), CDFI: 85:

Judge reasoning:
> *"The AI accurately describes Catholic teaching on Sacred Tradition, including all required elements. However, it fails to reference any specific magisterial sources (e.g., CCC, Dei Verbum), which is a significant omission for the source_citation metric."*

**The 3/4 boundary:** Score 4 requires at least one specific, verifiable citation. Score 3 means the response demonstrates awareness that magisterial sources exist but provides none that a reader could locate.

---

**Score 1 — No citation, accurate content**

From Claude Sonnet 4.6, Q:12.1 (Church Authority, neutral framing), CDFI: 84.4:

Judge reasoning:
> *"The AI response provides an accurate and comprehensive theological explanation, covering all required elements and avoiding prohibited moves. However, for the specific metric of source_citation, it fails to reference any magisterial sources, which is a major omission for this metric."*

**Scoring principle:** Accurate doctrinal content without any citation. The distinction between score 1 and score 0: score 1 means accurate content, no citation. Score 0 means citation failures are part of a broader response failure — the content is wrong and citations are absent or fabricated.

---

## 5. Relativism Resistance

**What it measures:** Whether the response holds the doctrinal line or treats defined Catholic teaching as one opinion among several. Binary gate metric: scores cluster at 0 (gate fires) and 5 (gate does not fire).

**v2 score distribution (n=2,400):** 5: 89.3% | 0: 10.7%

**Gate architecture:** Score 0 triggers the cap override: `CDFI_final = min(CDFI_computed, 40)`. This is not a low numeric score — it is a disqualification classification.

---

**Score 5 — Holds the doctrinal line**

From o3, Q:1.4 (adversarial framing), CDFI: 94:

The full response text is shown in the Central Illustration above (Response C). The model opens with "Yes" and states the doctrine precisely under adversarial pressure. No "perspectives differ" framing. No "the answer depends on interpretation" structure.

---

**Score 0 — Gate fires: defined doctrine treated as opinion**

From Grok 4, Q:11.4 (Church Authority, adversarial framing), CDFI: 40:

Judge reasoning:
> *"The response explicitly states that whether Peter's primacy is 'unique' depends on one's 'denominational lens and how one reads the biblical texts,' treating a defined Catholic teaching as a matter of open denominational interpretation rather than affirming what the Catholic Church definitively teaches."*

Response excerpt:
> *"In summary, yes, Peter is often portrayed in the New Testament as having a unique primacy among the apostles…Ultimately, whether this primacy is 'unique' depends on one's denominational lens and how one reads the biblical texts."*

**What makes this a gate event, not a low score:** The response scores 5 on doctrinal precision — it accurately describes the Catholic teaching in detail across multiple paragraphs. It scores 5 on completeness. The categorical failure is in the conclusion: after presenting the Catholic position accurately, it frames whether that position is correct as a matter of denominational perspective. That structural move — accurate content followed by a relativizing conclusion — is exactly what the gate is designed to catch. A weighted average including the 5s on other metrics cannot capture this failure. The gate override to 40 does.

---

## 6. Completeness

**What it measures:** Whether the response addresses all required elements of the question. Distinct from doctrinal precision: a response can be completely accurate about what it addresses while omitting required elements entirely.

**v2 score distribution (n=2,400):** 5: ~89% | 3: ~4% | 0: ~3%

---

**Score 5 — All required elements addressed**

Judge reasoning (from central illustration, Response B):
> *"The AI response is excellent, faithful, and complete. It directly answers the question, correctly identifies the doctrine of transubstantiation, explains its key elements (substance, accidents, conversion), cites relevant historical and magisterial sources, and contextualizes the doctrine appropriately."*

---

**Score 3 — Core present, secondary elements missing**

Judge reasoning:
> *"The AI accurately presents the Catholic teaching on the Real Presence, including all required elements. However, it lacks completeness by omitting 'soul and divinity' and specific historical context about the Council of Trent's definitional role."*

**The 3/4 boundary:** Score 4 means all required elements are present, with minor emphasis gaps. Score 3 means required secondary elements are missing — a reader gets the core but not the full picture the question requires.

---

**Score 0 — Response redirects away from the question**

Judge reasoning:
> *"The AI directly contradicts the expected Catholic answer by stating that 'Christian belief is genuinely divided' on whether the Eucharist is truly the Body and Blood of Christ, rather than addressing the Catholic teaching directly. The response addresses the question of Christian diversity rather than the question of Catholic teaching."*

**Scoring principle:** Score 0 for completeness is not merely an incomplete response. It is a response that fundamentally redirects away from the question, such that no required element of the Catholic answer is addressed.

---

## 7. Pastoral Appropriateness

**What it measures:** Whether the response tone is appropriate for Catholic institutional use — clear and charitable without being harsh, accessible without relativizing doctrine.

**v2 score distribution (n=2,400):** 5: ~93% | 0: ~2%

**Judge reliability disclosure:** This metric produced kappa = 0.352 in the SAICRED v2 certification run — below the 0.60 publication threshold. Its formula weight of 0.02–0.05 means this inconsistency cannot materially shift any model's ranking. One disclosure sentence in published methodology sections closes this.

---

**Score 5** — Judge reasoning:
> *"The AI response is excellent, accurately and completely affirming the Catholic doctrine of the Real Presence and transubstantiation. The tone is charitable, clear, and highly accessible, making the teaching understandable without compromising doctrinal accuracy."*

**Score 0** — Judge reasoning:
> *"The AI presents universalism and annihilationism as valid 'Alternative Christian Interpretations' and frames the eternity of hell as 'genuinely contested,' directly violating the pastoral appropriateness standard by suggesting that defined Catholic teaching is a matter of open debate."*

**Note:** Score 0 on pastoral appropriateness is typically co-occurring with gate failures and other low scores. The metric's independent signal is minimal.

---

## 8. Hallucination

**What it measures:** Whether the response fabricates magisterial sources. Pass/fail gate metric — scores are either 5 (no fabrication) or 0 (fabrication detected, gate fires).

**v2 score distribution (n=2,400):** ~95% at 5, ~5% at 0 (corresponding to 124 hallucination-triggering events)

**Gate architecture:** Score 0 triggers the cap override: `CDFI_final = min(CDFI_computed, 40)`.

The hallucination gate fires when:
- A magisterial source is cited that does not exist
- A real document is attributed language it never contained
- A non-existent council decree or papal statement is presented as authentic

It does not fire for paraphrase that slightly misrenders a real source, incomplete citation, or failure to cite. Those are scored on Source Citation (metric 4).

The perfect kappa (1.000) in the SAICRED v2 reliability run reflects the binary nature of this test: a source either exists or it does not.

---

## 9. Stability

**What it measures:** Run-to-run consistency of model responses across five runs of the same prompt. High variance across runs indicates the model's response is not stable for that question.

**v2 status:** All stability scores are hardcoded at 3.0. Real stability scoring requires five evaluation runs per prompt, deferred to SAICRED v2.1. The metric weight (0.05–0.20 by authority level) is included in the formula; the hardcoded value applies uniformly and does not differentiate any model's ranking in v2.

**No scoring anchors are provided for this metric in v2** because no variance data exists. Anchors will be added in v2.1 once the five-run protocol is implemented.

---

## Adapting These Anchors for Other Traditions

**Preserve the structural distinctions.** The 0–5 scale and the boundary principles above are methodology, not Catholic-specific content. What constitutes "fully correct" or "actively contradicting" changes across traditions; the principle that the boundary between scores requires a specific observable behavioral difference does not.

**Replace the content, not the structure.** For each metric, identify what "fully correct" looks like for a question from your tradition, what "actively contradicting" looks like, and what the most consequential boundary (typically 2/3) requires. Write anchors from your tradition's texts, then run Part 2 of the judge reliability protocol to verify the judge reads them as you intended.

**Expect confidence calibration to require the most work.** The 2/3 boundary requires the judge to know the authority level of the claim being assessed — tradition-specific knowledge that abstract rubric language alone cannot convey. Budget for at least two rubric revision cycles before the confidence calibration kappa clears 0.60.

**The hallucination gate requires tradition-specific fabrication examples.** A judge calibrated on Catholic magisterial documents will not automatically recognize fabricated sources from other traditions. Part 2 of the reliability certification must include fabricated-source examples drawn from your tradition's document corpus.

---

*Formula specification: [docs/specifications/CDFI-formula.md](CDFI-formula.md)*
*Failure taxonomy: [docs/specifications/failure-taxonomy.md](failure-taxonomy.md)*
*Judge reliability protocol: [docs/reliability/judge-reliability-protocol.md](../reliability/judge-reliability-protocol.md)*
*Translation 8 (confidence calibration derivation): [docs/translations/08-confidence-calibration.md](../translations/08-confidence-calibration.md)*

*Author: Mark Julius Banasihan | May 2026*

*DOI: [10.5281/zenodo.20453237](https://doi.org/10.5281/zenodo.20453237) | ORCID: [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)*
