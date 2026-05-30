# Adapting the CDFI Framework for Other Traditions

*A practical guide for Lutheran synods, Anglican provinces, Orthodox jurisdictions, Jewish institutions, and any other tradition evaluating AI against its doctrinal standards*

---

## What Transfers and What You Replace

The CDFI Framework has two layers. The methodology layer is tradition-agnostic: the seven-step translation sequence, the gate architecture, the four-part judge reliability protocol, the statistical requirements, and the deployment tier logic all transfer intact. The content layer is Catholic-specific: the four authority columns, the scoring anchors, the failure mode examples, and the specific threshold values were built for Catholic institutional use.

Adapting the framework means keeping the methodology layer and replacing the content layer with the content of your tradition.

---

## Step 1: Map Your Authority Structure

Catholic doctrine has four authority levels. Your tradition has its own. Before building the weighting matrix, you need to identify what those levels are and what distinguishes them.

**Questions to answer:**

What is the highest level of doctrinal authority in your tradition? (Ecumenical council? Scripture itself? Confessional document? General Assembly vote?)

What are the intermediate levels? (Denominational policy? Pastoral guideline? Theological consensus among ordained leaders?)

What questions does your tradition explicitly leave open for individual conscience or scholarly debate?

**Examples across traditions:**

*Lutheran:* Scripture (norma normans), Lutheran Confessions/Book of Concord (norma normata), synodical resolutions, pastoral guidance

*Anglican/Episcopal:* Scripture, the 39 Articles, General Convention resolutions, diocesan policies

*Eastern Orthodox:* Ecumenical Councils (dogma), Holy Tradition, synodal decisions, patristic consensus, theological opinion

*Jewish:* Torah (written), Talmud, later halachic codes (Shulchan Aruch), responsa literature, contemporary rabbinic consensus, minority opinions

Each of these structures maps to a different column configuration. The requirement is that your columns capture the genuine authority distinctions in your tradition and that all column weights sum to 1.00.

---

## Step 2: Define Your Failure Modes

The five CDFI failure modes (doctrinal omission, moral softening, citation fabrication, prompt sensitivity drift, contextual relativization) are Catholic instantiations of a more general pattern. For each, ask: what is the version of this failure in my tradition?

**Doctrinal omission** is tradition-agnostic. Every tradition has teachings with required elements. Identify what those are for your most common question types.

**Moral softening** applies wherever your tradition has clear moral norms. A Lutheran benchmark would test whether the model softens Lutheran teachings on specific moral questions. An Orthodox benchmark would test preservation of the Church Fathers' moral teaching.

**Citation fabrication** is tradition-agnostic. No tradition wants an AI to invent sources. The specific check is whether the fabricated source would plausibly deceive a member of your tradition. For a Jewish institution, fabricating a Talmudic tractate or inventing a responsum from a named posek is the equivalent failure.

**Prompt sensitivity drift** is tradition-agnostic. It applies to any tradition where the correct answer to a doctrinal question is framing-invariant.

**Contextual relativization** requires care. It fires when a model treats a settled question as open. You need to be explicit about which questions your tradition has settled and which it has not. Do not classify a genuinely disputed question in your tradition as settled simply because one position is dominant. The gate must only fire when your tradition has actually closed the question.

---

## Step 3: Build Your Scoring Anchors

Each metric rubric needs concrete examples drawn from your tradition's texts. The scoring anchors are what tell the automated judge how to apply the rubric correctly. Abstract rubric language without tradition-specific examples will produce high Part 1 kappa (intra-rater consistency) but low Part 2 accuracy (anchor calibration).

**For each metric, at each score level (0, 2, 4, 6, 8, 10), write:**

- One example response that earns exactly that score
- One sentence explaining why the example earns that score and not the adjacent level

Anchor examples are the most time-intensive part of adaptation. Plan for a qualified theologian or scholar in your tradition to review all anchors before the judge reliability run.

---

## Step 4: Set Your Deployment Tier Thresholds

The CDFI threshold values (85 for formation, 70 for general information) were set for Catholic institutional contexts after review against the theological criteria in the SAICRED white paper. They are not universal constants.

Your tradition's threshold values should reflect your institutional risk profile. Questions to consider:

What is the cost of a formation-use error in your tradition? (A Catholic RCIA director passing on a fabricated encyclical citation is a serious institutional harm. Your tradition's equivalent harm may be higher or lower severity.)

What is the realistic baseline for frontier AI models on your tradition's questions? (If the best model scores 72 on your benchmark due to lower representation of your tradition in training data, a formation threshold of 85 may be unreachable at this time. Setting an unachievable threshold does not protect your institution; it produces a benchmark where every model is Not Recommended regardless of actual reliability differences.)

What institutional approvals are required before a model is used for formation purposes in your tradition? (The deployment tier structure should connect to those existing governance processes, not replace them.)

---

## Step 5: Run the Reliability Protocol Without Modification

Parts 1 through 4 of the judge reliability protocol apply without modification to any tradition. The kappa thresholds, accuracy thresholds, and test construction requirements are statistical and methodological. They do not depend on the content of the doctrinal tradition being evaluated.

The only tradition-specific work in the reliability protocol is Part 2 (anchor calibration): the anchor responses must be drawn from your tradition's questions, not from the SAICRED Catholic dataset.

---

## What You Can Cite

If you build a benchmark using this framework, you can cite the CDFI Framework methodology document and the SAICRED v2 reference implementation. Your benchmark is a distinct instrument built on a shared methodology. Citing the shared methodology is accurate attribution. Claiming your benchmark is SAICRED, or that SAICRED's findings apply to your tradition's questions, would not be accurate.

---

## A Note on Inter-Tradition Comparisons

The CDFI score is not cross-tradition comparable. A Lutheran benchmark using the CDFI methodology and a Catholic benchmark using the CDFI methodology produce scores that reflect reliability against different doctrinal standards. Comparing the scores directly would be comparing different measurements.

What is cross-tradition comparable: the framing effect magnitude, the cap rate, and the distribution shape. If five of six models show framing sensitivity gaps greater than 5 points on Lutheran questions, that finding parallels the SAICRED v2 Catholic finding and suggests a systemic pattern in how frontier AI models handle doctrinal content across traditions.

---

*Author: Mark Julius Banasihan | May 2026*
