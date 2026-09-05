# SOP-010: Governance Structure and Leadership Roles

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-010 |
| **Category** | 01 - Governance & Succession |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | All Club Members, Core Leads, Faculty Advisory |
| **Review Cadence** | Annual (start of each academic autumn semester) |

---

## 1. Purpose
To define a resilient, non-hierarchical governance model that minimizes bureaucratic overhead, distributes decision-making power, and empowers student pods to act autonomously while maintaining accountability.

## 2. Guiding Principles
* **Servant Leadership**: Club leadership exists to clear obstacles, secure resources, and unblock member initiatives—not to police or micro-manage.
* **Dual-Stewardship**: Core functions pair a senior-year steward with a junior-year co-lead to build unbroken institutional continuity.
* **Zero Artificial Hierarchy**: Project leaders lead within their project pods without needing executive titles.

---

## 3. Organizational Topology

```
┌──────────────────────────────────────────────────────────┐
│                   Faculty Advisory Board                 │
│              (Academic & Institutional Guidance)         │
└────────────────────────────┬─────────────────────────────┘
                             │
┌────────────────────────────▼─────────────────────────────┐
│                   Club Convenor & Co-Lead                │
│             (Ecosystem Facilitation & External Sync)     │
└──────┬─────────────────────┬──────────────────────┬──────┘
       │                     │                      │
┌──────▼──────┐       ┌──────▼──────┐        ┌──────▼──────┐
│  Technical  │       │   Domain    │        │ Operations  │
│  Stewards   │       │  Stewards   │        │ & Community │
│  (Compute/  │       │ (Policy/IR/ │        │  (Comms/PR/ │
│   Git/Ops)  │       │  Econ/Hum)  │        │   Events)   │
└──────┬──────┘       └──────┬──────┘        └──────┬──────┘
       │                     │                      │
       └─────────────────────┼──────────────────────┘
                             │
     ┌───────────────────────▼────────────────────────┐
     │       Autonomous Multidisciplinary Pods        │
     │      (Projects, Reading Groups, Hackathons)    │
     └────────────────────────────────────────────────┘
```

---

## 4. Role Specifications

### 4.1 Club Convenor (Elected / Consensual)
* **Term**: 1 Academic Year (September to August).
* **Responsibilities**:
  1. Act as primary liaison to Nalanda University administration, School Dean, and visiting dignitaries.
  2. Protect the "Default-to-Approve" culture; intervene when friction or bottlenecks arise.
  3. Lead quarterly transparency reports and annual cohort transitions.
  4. Ensure all members in the directory have access to shared tools and compute channels.

### 4.2 Technical Steward(s) (1 to 2 members)
* **Responsibilities**:
  1. Administer the GitHub organization (`nalanda-ai-club`), cloud accounts, and shared GPU/API quotas.
  2. Maintain automated CI/CD tools, the documentation package, and the public directory website (`Data-science-club`).
  3. Provide architectural feedback on incubated technical projects.
  4. Ensure zero credential leaks; perform quarterly key rotations.

### 4.3 Domain Stewards (2 to 3 members across non-CS fields)
* **Fields**: International Relations, Economics, Historical Studies, Ecology/Agriculture, Philosophy/Ethics.
* **Responsibilities**:
  1. Lead the articulation of real-world research questions and policy challenges.
  2. Guide data collection, qualitative fieldwork methods, and domain relevance.
  3. Ensure non-engineering students are never marginalized and actively co-lead technical initiatives.
  4. Curate interdisciplinary papers for the weekly Reading Group.

### 4.4 Operations & Community Steward (1 to 2 members)
* **Responsibilities**:
  1. Manage event scheduling, venue bookings on campus, and guest hospitality.
  2. Moderate official communications (WhatsApp/Telegram/Slack/Email announcements).
  3. Ensure meeting notes, post-mortems, and session recordings are cataloged within 48 hours.
  4. Track peer mock interviews and resume clinics during placement seasons.

---

## 5. Pod Autonomy & The Rule of 2
1. Any two active members (at least one computational + at least one domain specialist) may self-constitute an official **Project Pod**.
2. Pods do not require prior committee approval to begin research, hold meetings, or prototype code.
3. Pods automatically unlock **Tier 1 Compute** (Google Colab / Hugging Face Spaces) immediately upon submitting a one-page project brief.

---

## 6. Accountability & Term Limits
* No member may hold the Convenorship for more than one full year.
* If any steward fails to fulfill duties for 30 consecutive days, an open RFC for co-lead reassignment may be initiated by any 3 active members.

---

## 7. Master Team Structure & Structural Amendment Constraint
* The definitive task ownership mapping and RACI assignments are maintained in `TEAM_STRUCTURE.md` and `SOP-014`.
* Any proposal to modify the core team structure, add/remove executive steward seats, or alter pod mandates requires an **affirmative supermajority consent of eighty percent (80%)** of the active cohort.
