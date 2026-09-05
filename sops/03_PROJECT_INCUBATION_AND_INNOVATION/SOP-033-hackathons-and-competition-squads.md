# SOP-033: Hackathons, Case Competitions, and Squad Mobilization

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-033 |
| **Category** | 03 - Project Incubation & Innovation |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | Hackathon Participants, Squad Leads, Operations Stewards |
| **Objective** | High-velocity squad mobilization, rapid prototyping, post-mortem capture |

---

## 1. Purpose
To systematize how the Club mobilizes multidisciplinary competition squads for national and international hackathons (Smart India Hackathon, Kaggle competitions, policy datathons, global generative AI challenges) to maximize wins and preserve shared tooling.

---

## 2. The Squad Mobilization Protocol

```
  T - 14 Days                T - 7 Days                T - 0 (Kickoff)          T + 3 Days
  (Squad Call)               (War-Room Prep)           (Sprint)                 (Debrief)
       │                          │                         │                       │
       ▼                          ▼                         ▼                       ▼
  Opportunity posted         Cross-disciplinary        Shared boilerplate,      Post-mortem &
  to cohort; members         squad assembled &         compute budget           reusable code
  express interest           strategy locked           provisioned              archived
```

---

## 3. Step-by-Step Operations

### Step 1: Opportunity Scouting
* Any member may post a competition link in `#competitions`.
* If at least 3 members express commitment, an official **Squad Channel** is spawned.

### Step 2: Squad Composition (The Interdisciplinary Advantage)
* Squads should ideally balance:
  - 1 Pipeline / Data Specialist (wrangling, feature engineering, vector DBs)
  - 1 Model / Fine-Tuning Specialist (architectures, evaluation loops)
  - 1 Domain / Presentation Specialist (business case, slide deck, UI mockup, pitch delivery)

### Step 3: Fast Compute & War-Room Provisioning
* The Technical Steward provisions a 48-hour high-burst compute allowance (e.g. ₹2,000 cloud credits or dedicated local GPU access).
* Operations Steward coordinates an all-night campus war-room with power, stable internet, and snacks.

### Step 4: Mandatory 72-Hour Post-Mortem
* Within 3 days of competition close:
  1. The squad must submit a brief 1-page **Post-Mortem** (`templates/post-mortem-template.md`).
  2. Any reusable code (API wrappers, preprocessing scripts, slide templates) must be merged into `nalanda-ai-club/hackathon-starter-kit`.
  3. Win or lose, the team receives public cohort recognition for representing Nalanda University.
