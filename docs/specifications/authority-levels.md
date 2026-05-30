# Doctrinal Authority Levels

*The four-column structure of the CDFI weighting matrix*

---

## The Core Problem

Catholic doctrine is not a flat list of equally certain claims. A benchmark that scores all doctrinal questions with the same metric weights is measuring something incoherent. Whether a model hedges on the Real Presence and whether it hedges on the existence of Limbo are not the same error. The first is a failure on settled teaching. The second is appropriate epistemic caution on a genuinely open question.

The four-column weighting matrix is the architectural response to this problem. Each column assigns different weights to the nine metrics based on what matters most at that level of doctrinal certainty.

This structure derives from the research principle in Challenges in Evaluating AI Systems (Anthropic, 2023): evaluation criteria must be drawn from the internal standards of the subject being evaluated.

---

## The Four Authority Levels

### Column 1: Defined Dogma

**What it covers:** Doctrines formally and definitively defined by the Church, typically through an ecumenical council or solemn papal definition. The Church's highest level of doctrinal certainty.

**Catholic examples:**
- The Real Presence of Christ in the Eucharist (defined at the Council of Trent, 1551)
- Papal infallibility in matters of faith and morals (defined at Vatican I, 1870)
- The Immaculate Conception (defined by Pius IX, 1854)
- The Assumption of Mary (defined by Pius XII, 1950)

**Why doctrinal precision weights at 0.30:** The question has one correct answer. The primary failure mode is getting it wrong or hedging on what is settled. Stability and source citation matter less here because the Church's position is unambiguous.

---

### Column 2: Ordinary Magisterium

**What it covers:** The Church's regular, ongoing teaching on faith and morals through encyclicals, apostolic exhortations, curial documents, and consistent episcopal teaching. Not formally defined as dogma but authoritative and binding.

**Catholic examples:**
- The Church's teaching on artificial contraception (Humanae Vitae, 1968)
- The prohibition on the ordination of women to the priesthood
- The Church's social teaching on economic justice
- The moral norm against abortion

**Why doctrinal precision weights at 0.25:** The teaching is authoritative but not solemnly defined. The model must state it clearly without softening while acknowledging the authoritative source.

---

### Column 3: Theological Consensus

**What it covers:** Positions held by the substantial majority of Catholic theologians and reflected in authoritative catechetical documents, without formal dogmatic definition.

**Catholic examples:**
- The nature of original sin and its transmission
- The theology of grace and free will (within the boundaries set by Trent)
- The understanding of purgatory

**Why stability and source citation weight more heavily here:** The question requires the model to accurately represent the consensus position while acknowledging the theological tradition that grounds it. Source accuracy matters more when the authority is textual rather than definitional.

---

### Column 4: Legitimate Theological Opinion

**What it covers:** Questions the Church has explicitly left open, where Catholics may hold different positions in good faith. Theological debates the Magisterium has not closed.

**Catholic examples:**
- Whether Limbo exists (addressed but not settled by the ITC in 2007)
- The precise mechanics of how grace operates in non-Christians
- Certain disputed questions in Catholic social teaching's application to specific policy contexts

**Why doctrinal precision drops to 0.15:** Asserting one position as settled on a genuinely open question is a calibration failure. The primary test at this authority level is whether the model accurately represents the range of faithful positions, acknowledges the open status of the question, and does not assert false certainty in either direction.

**A model that scores 10 on doctrinal precision for a Legitimate Opinion question has likely failed confidence calibration:** It has asserted as certain what the Church has left open.

---

## How to Classify Questions

Before scoring, every question must be tagged with its authority level. The tag determines which weight column the CDFI computation uses.

**Classification criteria:**

A question is Defined Dogma if: the Church has issued a solemn definition, the teaching appears in the Profession of Faith, or the Catechism explicitly marks it as divinely revealed.

A question is Ordinary Magisterium if: the teaching is consistently presented in official Church documents as binding, without being a solemn definition.

A question is Theological Consensus if: the position is widely held among orthodox theologians and reflected in catechetical documents, but not formally defined.

A question is Legitimate Theological Opinion if: the Church has explicitly acknowledged debate, official documents use language like "it is hoped" rather than "the Church teaches," or theologians in good standing hold materially different positions.

**When in doubt, classify one level lower** (toward Legitimate Opinion). This errs on the side of not penalizing appropriate epistemic caution.

---

## Adapting the Authority Level Structure for Other Traditions

The four-column structure is Catholic-specific in its categories. Other traditions have different authority structures. The methodology requires the implementing institution to:

1. Identify the authority levels that exist in the target tradition (e.g., Scripture, Confession, General Assembly decision, pastoral guideline)
2. Map the authority levels to the same weighting logic: higher authority levels weight doctrinal precision more heavily; lower authority levels weight stability and source citation more heavily
3. Classify every question in the dataset at intake before scoring proceeds

The column structure can have more or fewer than four levels depending on the tradition's authority architecture. The requirement is that all columns sum to 1.00 and that the classification happens before scoring, not after.

---

*Author: Mark Julius Banasihan | May 2026*
