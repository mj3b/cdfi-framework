# Deployment Tiers

*How CDFI scores map to institutional use permissions*

---

## Overview

The CDFI is not a leaderboard. A higher score does not simply mean "better." It means the model has demonstrated a level of doctrinal reliability that permits specific institutional uses. The deployment tiers convert a number into an institutional decision.

This design follows the principle from A Statistical Approach to Model Evaluations (Anthropic, 2024) that readiness is context-dependent: a model adequate for low-stakes information retrieval may be inadequate for high-stakes formation.

---

## The Four Tiers

### Tier 1: Formation and Catechesis (CDFI 85-100)

**Permitted uses:** RCIA programs, classroom faith formation, homily preparation materials, seminary study support, parish catechesis programs, faith formation curriculum development.

**What this means:** The model demonstrated sufficient doctrinal reliability across all question types and framings that a formation director can use it in contexts where users are being formed in the faith rather than simply informed about it. The distinction matters: a formation context assumes the user will act on the content, not merely read it.

**Gate behavior at this tier:** A model scoring in this range has a low cap rate. Cap events are present but infrequent enough that they do not materially affect the majority of formation interactions.

**SAICRED v2 status:** o3 (CDFI 85.0) is the only model to clear this threshold.

---

### Tier 2: General Information (CDFI 70-84)

**Permitted uses:** General Catholic information and reference, answering factual questions about Church history and practice, supporting adult faith discussions that are not formation contexts.

**What this means:** The model handles most Catholic doctrinal questions correctly but has a meaningful cap rate or shows framing sensitivity that makes it unsuitable for formation use without mitigation. The primary mitigation: a prompt wrapper that supplies explicit Catholic context with every query.

**The prompt wrapper requirement:** SAICRED v2 data shows that five of six models perform 10-16 CDFI points better when the Catholic context is explicit in the prompt. A well-constructed prompt wrapper can move a General Information tier model close to Formation tier performance for specific use cases. The Prompt Playbook deliverable (SAICRED Steps 7 and 8) documents the specific wrapper structures that accomplish this.

**Gate behavior at this tier:** Cap events present but concentrated in specific framing conditions (typically adversarial or neutral framings). Catholic framing performance may clear the Formation threshold.

---

### Tier 3: Research and Development Only (CDFI 50-69)

**Permitted uses:** Internal research and development, testing and evaluation, academic study of AI doctrinal failure modes.

**What this means:** The model has systematic reliability problems across enough questions that it is not suitable for any public-facing Catholic deployment. Its failures are not concentrated in specific conditions; they are distributed across question types.

**No public-facing deployment** means: no use by parish staff, formation directors, educators, or lay Catholics in any context where the model's output may be taken as representing Catholic teaching.

---

### Tier 4: Not Recommended (CDFI below 50 or any gate failure at disqualifying frequency)

**Permitted uses:** None.

**What this means:** The model's doctrinal reliability is below the minimum threshold for any Catholic institutional use, or its cap rate indicates that categorical failures are too frequent to manage through prompt engineering or contextual controls.

---

## How Cap Rate Interacts with Tier Assignment

Two models can have the same mean CDFI with very different deployment risk profiles.

A model with mean CDFI 82 and cap rate 8% has approximately 32 cap events across 400 responses. Those are concentrated in specific framing conditions and can largely be addressed with prompt wrapper mitigation.

A model with mean CDFI 82 and cap rate 17% has approximately 68 cap events across 400 responses. That frequency suggests a more systematic failure pattern that a prompt wrapper will not fully resolve.

Tier assignment is based on mean CDFI. Risk assessment for specific deployment decisions should consider both mean CDFI and cap rate.

---

## Adapting Tiers for Other Traditions

The threshold values (85, 70, 50) were set for Catholic institutional contexts. Institutions in other traditions should set their own thresholds based on:

1. The highest score achieved by any tested model on their tradition's questions (a threshold unreachable by current models is not useful governance)
2. The institutional risk profile of the highest-stakes deployment context (a formation program has different risk tolerance than a general information chatbot)
3. The reliability certification results (if the automated judge has lower kappa on tradition-specific metrics, more conservative thresholds may be warranted)

---

*Research basis: A Statistical Approach to Model Evaluations (Anthropic, 2024)*

*Author: Mark Julius Banasihan | Evals Specialist | May 2026*
