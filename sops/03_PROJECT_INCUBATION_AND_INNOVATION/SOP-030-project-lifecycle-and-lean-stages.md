# SOP-030: Project Lifecycle and Lean Incubation Stages

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-030 |
| **Category** | 03 - Project Incubation & Innovation |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | Project Leads, All Pod Members, Technical Stewards |
| **Philosophy** | "Working software & tangible findings over speculative proposals" |

---

## 1. Purpose
To provide an accelerated, frictionless incubation pathway that transitions raw interdisciplinary ideas into published research, open-source repositories, or venture-backed prototypes without bureaucratic paralysis.

---

## 2. The 4-Stage Incubation Funnel

```
 ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
 │ Stage 1: SPARK  │       │ Stage 2: SPRINT │       │Stage 3: FLAGSHIP│       │ Stage 4: LAUNCH │
 │ (48-hr Ideation)├──────►│ (2-Week Proto)  ├──────►│ (Peer-Reviewed /├──────►│  (Open-Source / │
 │                 │       │                 │       │  Production)    │       │   Spin-Out)     │
 └────────┬────────┘       └────────┬────────┘       └────────┬────────┘       └────────┬────────┘
          │                         │                         │                         │
     No Approval              Self-Service              Faculty Sync             Demo Day & PR
     Required                 Tier 1 Compute            Tier 2/3 Compute         Global Release
```

---

## 3. Detailed Stage Protocols

### Stage 1: Spark (48 Hours)
* **Goal**: Define the problem statement, formulate the core hypothesis, and identify data sources.
* **Requirements**:
  - Minimum 2 members (1 computational + 1 domain specialist).
  - Submit a 1-page proposal via CLI:
    ```bash
    ai-ops scaffold --type project --title "pali-manuscript-ocr"
    ```
* **Approval**: **Instant / Automatic**. No committee vote required.

### Stage 2: Sprint (2 Weeks)
* **Goal**: Build an end-to-end working baseline (minimum viable proof-of-concept).
* **Deliverables**:
  - A clean GitHub repository under `nalanda-ai-club` with README and reproducible environment (`pyproject.toml` / `requirements.txt` / Docker).
  - Baseline metrics evaluated on actual sample data.
* **Compute**: Automatic allocation of **Tier 1 Compute** (Google Colab Pro credits or Hugging Face Space).

### Stage 3: Flagship (4 to 8 Weeks)
* **Goal**: Scale model, refine domain insights, run full error analysis, and write the draft paper or production release.
* **Deliverables**:
  - Pre-print paper draft (LaTeX / arXiv format) OR production application with interactive frontend.
  - Standardized **Model Card** (SOP-060) and Ethical Risk Assessment.
* **Compute**: Access to **Tier 2 or Tier 3 Compute** (RunPod/GCP GPU instances) reviewed within 24 hours.

### Stage 4: Launch & Knowledge Archival
* **Goal**: External dissemination to the scientific and global community.
* **Outcomes**:
  - ArXiv / Conference submission (NeurIPS, ACL, ICML, CVPR, FAccT, or domain journals).
  - Public open-source release with MIT/Apache-2.0 license.
  - Featured presentation during the Nalanda AI Annual Showcase.

---

## 4. Abandonment Protocol ("Fail Fast, Learn Forward")
* If a pod determines that a hypothesis is invalid or data is inaccessible, the project may be archived gracefully without stigma.
* The team submits a brief 1-page **Post-Mortem** documenting why the approach failed so future cohorts do not repeat the dead end.
