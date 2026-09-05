# SOP-040: Weekly Paper Reading Groups and Literature Dissection

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-040 |
| **Category** | 04 - Events & Knowledge Sharing |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | All Members, Reading Group Facilitators |
| **Cadence** | Weekly (Friday 18:00 – 19:30 IST) |

---

## 1. Purpose
To cultivate intellectual depth by running structured, dual-lens reading groups that analyze both cutting-edge algorithmic mechanisms and their socio-political, economic, and ethical ramifications.

---

## 2. The Dual-Lens Reading Model
Every paper selected is unpacked through two complementary vantage points:

```
┌────────────────────────────────────────────────────────┐
│                   SELECTED PAPER                       │
└───────────────────────────┬────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
   Lens A: Technical & Math    Lens B: Domain & Policy
   - Architectural novelty     - Economic incentives
   - Loss functions & bounds   - Institutional impact
   - Compute complexity        - Historical precedent
   - Benchmark validity        - Regulatory/safety risks
```

---

## 3. Weekly Operational Routine

### Monday (Paper Selection & Rotation)
* The designated Facilitator of the week posts 2 candidate papers in the `#reading-group` channel.
* Criteria: 1 foundational technical paper (e.g. FlashAttention, Mixture-of-Depths) OR 1 interdisciplinary milestone (e.g. Algorithmic Bias in Causal Inference, AI in Historical Philology).
* Members vote via emoji reaction; winning paper is locked by Monday 20:00 IST.

### Wednesday (Segment Assignment)
* The Facilitator splits the paper into 3 manageable chunks:
  - Part 1: Problem statement, related work, and real-world motivation.
  - Part 2: Mathematical formulation, architecture, and training recipe.
  - Part 3: Empirical evaluation, error breakdown, and ethical/societal implications.
* Volunteers claim chunks.

### Friday (The Colloquium Session)
* **Format**:
  - 10 min: Quick context and high-level premise.
  - 35 min: Walkthrough of mathematics, pseudo-code, and ablation experiments.
  - 30 min: Open interdisciplinary critique (Is the benchmark realistic? What happens when this hits public policy or resource-constrained environments?).
  - 15 min: "What can we build from this?" (Brainstorming sprint ideas).

### Saturday (Archival)
* The 1-page summary and curated notes are pushed to `nalanda-ai-club/reading-archive` under `CC-BY-4.0`.
