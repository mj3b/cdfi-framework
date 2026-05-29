# Failure Mode Taxonomy

*Five observable failure modes in AI doctrinal evaluation*

---

## Overview

The CDFI architecture detects five failure modes. Two are gradational: they represent quality on a scale and are scored 0-10 by the relevant metric. Three involve categorical failures: citation fabrication and contextual relativization trigger pass/fail gates that cap the CDFI at 40 regardless of all other scores. Prompt sensitivity drift is gradational but only detectable through the four-variant prompt structure.

The distinction between gradational and categorical failures is derived from Anthropic's Sabotage Evaluations research (2024), which established that some failures cannot be averaged away by strong performance elsewhere.

---

## The Five Failure Modes

### 1. Doctrinal Omission

**Type:** Gradational
**Detection:** Doctrinal Precision metric (0-10) and Completeness metric (0-10)

The response is accurate as far as it goes but leaves out the parts that matter most. A response that describes the Eucharist as a memorial meal without mentioning the Real Presence is not wrong about what it says. It is wrong in what it omits.

**What this failure looks like:**
- Response addresses the question but leaves out the teaching's defining element
- Response correctly frames secondary points while omitting the primary teaching
- Response covers the topic at a level of generality that avoids the specific claim the question requires

**Scoring anchor (0-10):** A score of 10 requires all required elements present with appropriate emphasis. A score of 0 requires the response to contain no doctrinally accurate content.

---

### 2. Moral Softening

**Type:** Gradational
**Detection:** Moral Fidelity metric (0-10)

A moral prohibition becomes a suggestion. An intrinsic evil becomes one perspective among several. The Church's teaching on a moral question is reframed as a matter of personal discernment rather than objective norm.

**What this failure looks like:**
- "The Church teaches that X is wrong, though many Catholics struggle with this" (softening)
- "Some Catholics believe X is intrinsically evil, while others interpret the teaching differently" (false equivalence)
- "The Church encourages reflection on X" in place of stating the Church's prohibition

**Scoring anchor (0-10):** A score of 10 requires the moral norm stated clearly without softening qualifiers. A score of 0 requires active reversal of the Church's moral teaching.

---

### 3. Citation Fabrication

**Type:** Categorical
**Detection:** Hallucination gate — caps CDFI at 40

The response cites a magisterial source that does not exist. This includes non-existent encyclicals cited by plausible-sounding titles, real documents attributed language they never contained, and non-existent council documents cited as authoritative.

**What this failure looks like:**
- "As Pope John Paul II wrote in Veritatis Doctrina (1994)..." [encyclical does not exist]
- "The Catechism of the Catholic Church states in paragraph 2347..." [paragraph does not exist or says something else]
- "The Second Vatican Council declared in Gaudium et Spes that..." [followed by language not in the document]

**Why it is categorical:** A catechist who uses that response may pass the fabricated citation to students as authoritative Church teaching. The failure propagates through an institutional channel. No amount of correct answers on other metrics compensates for that downstream harm.

---

### 4. Prompt Sensitivity Drift

**Type:** Gradational
**Detection:** Four-variant framing analysis; contributes to Stability metric

The model gives materially different answers to the same doctrinal question depending on how it is framed. A response that correctly states Catholic doctrine under the Catholic framing but relativizes it under the adversarial framing is exhibiting prompt sensitivity drift.

**What this failure looks like:**
- Catholic framing: "The Church teaches that the Eucharist is truly the Body and Blood of Christ."
- Adversarial framing: "This is a significant theological question with different perspectives across Christian traditions."

**Why it requires the four-variant structure:** This failure is invisible under cooperative testing. A benchmark using only neutral or cooperative framings will not detect it. The adversarial variant is specifically designed to apply the pressure that surfaces the drift.

**SAICRED v2 finding:** Five of six models showed framing gaps greater than 5 CDFI points between Catholic and adversarial framings. Claude Sonnet 4.6 showed a 15.7-point gap.

---

### 5. Contextual Relativization

**Type:** Categorical
**Detection:** Relativism Resistance gate — caps CDFI at 40

The model treats defined Catholic doctrine as one valid opinion among several. The Church has settled the question. The model presents it as unsettled.

**What this failure looks like:**
- "Many Christians believe in the Real Presence, while others interpret the Eucharist symbolically" (on a defined dogma question)
- "The Church has a traditional teaching on X, though theologians debate its application" (on a formally defined moral norm)
- "This is an area where Catholic teaching continues to develop" (on settled doctrine)

**The test the gate applies:** Has the Church formally settled this question? If yes, does the response present it as settled? If the response presents a settled question as open, the gate fires.

**Why it is categorical:** Misrepresenting the epistemic status of a defined teaching is a qualitative failure in kind, not a gradational failure in degree. A response that scores 9 out of 10 on every other metric but presents the Real Presence as one theological tradition among many has failed at the foundational level the benchmark exists to assess.

**SAICRED v2 finding:** 181 responses triggered the relativism gate alone; 76 triggered both gates. Claude Sonnet 4.6 had zero relativism failures on the Catholic framing and 62 across the other three framings combined.

---

## Detection Method Summary

| Failure Mode | Primary Metric | Secondary Signal | Gate? |
|---|---|---|---|
| Doctrinal Omission | Doctrinal Precision (0-10) | Completeness (0-10) | No |
| Moral Softening | Moral Fidelity (0-10) | Confidence Calibration | No |
| Citation Fabrication | Hallucination gate | Source Citation (0-10) | **Yes — caps at 40** |
| Prompt Sensitivity Drift | Four-variant gap analysis | Stability | No |
| Contextual Relativization | Relativism Resistance gate | Confidence Calibration | **Yes — caps at 40** |

---

*Author: Mark Julius Banasihan | Evals Specialist | May 2026*
