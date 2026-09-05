# 🏛️ AI Club Team Structure & Task Ownership Matrix
### **Nalanda University — MSc Data Science & AI**

> *"Structure exists to accelerate action, not to create thrones. Every recurring operational duty has one directly responsible individual, backed by community trust."*

---

## 1. Master Team Topology

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Faculty Advisory Board                          │
│               (Academic Sponsorship, University Liaison)               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                        Executive Council (Core)                        │
│ ┌──────────────────────┬──────────────────────┬──────────────────────┐ │
│ │    Club Convenor     │  Technical Steward   │    Domain Steward    │ │
│ ├──────────────────────┼──────────────────────┼──────────────────────┤ │
│ │  Operations Steward  │  Financial Steward   │  AI Safety Steward   │ │
│ └──────────────────────┴──────────────────────┴──────────────────────┘ │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    │                               │                               │
┌───▼──────────────────────┐ ┌──────▼──────────────────────┐ ┌──────▼──────────────────────┐
│     TECHNICAL POD        │ │ MULTIDISCIPLINARY RESEARCH  │ │   COMMUNITY & EVENTS POD    │
│ - Cloud & Compute DRI    │ │ - Economics & Trade DRI     │ │ - Reading Group Facilitator │
│ - Web & Directory DRI    │ │ - Historical Archives DRI   │ │ - Guest Colloquium Lead     │
│ - Open Source & CI DRI   │ │ - Ecology & Environment DRI │ │ - Placement & Mock Review   │
│ - Competition Squad Capt │ │ - Public Policy & Law DRI   │ │ - Campus Logistics Lead     │
└──────────────────────────┘ └─────────────────────────────┘ └─────────────────────────────┘
```

---

## 2. Core Stewardship Roles & Mandates

| Leadership Role | Key Mandate | Primary Deliverables | Selection & Term |
| :--- | :--- | :--- | :--- |
| **Club Convenor** | Overall strategic alignment, external liaison to University leadership, barrier removal. | Annual report, cohort transition, townhalls. | Elected/Consensual; 1 Academic Year. |
| **Technical Steward** | Infrastructure reliability, cloud quotas, repository hygiene, developer tooling. | Cloud budget uptime, GitHub security, CI pipelines. | Elected/Consensual; 1 Academic Year. |
| **Domain Steward** | Representation of non-CS disciplines, interdisciplinary project formulation. | Idea Colliders, 2-in-a-pod pairings, policy whitepapers. | Rotational across non-CS fields; 1 Year. |
| **Operations Steward** | Event execution, room bookings, communications broadcast, attendee experience. | Weekly dispatches, guest hospitality, runbook audits. | Elected/Consensual; 1 Academic Year. |
| **Financial Steward** | Double-entry accounting, fast student expense reimbursements, quarterly audits. | `LEDGER.md` maintenance, 48-hour UPI reimbursements. | Appointed by Council; 1 Academic Year. |
| **AI Safety Steward** | Ethical screening, Model Card compliance, data sovereignty & DPDP Act alignment. | Model card audits, PII protection, safety screening. | Appointed by Council; 1 Academic Year. |

---

## 3. Master Task Ownership & RACI Matrix

**RACI Definitions**:
* **R (Responsible)**: The Single Directly Responsible Individual (DRI) who executes the task.
* **A (Accountable)**: The steward who ultimately approves and bears organizational responsibility.
* **C (Consulted)**: Subject matter contributors consulted during execution.
* **I (Informed)**: Community members kept updated on completion.

| Associated SOP | Operational Task | DRI / Role (R) | Accountable (A) | Backup DRI | Cadence / SLA | Deliverable |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SOP-010** | Governance Coordination & Council Sync | Club Convenor | Faculty Advisory | Operations Steward | Bi-weekly | Council Minutes & Action Items |
| **SOP-011** | Annual Cohort Succession & Key Transfer | Outgoing Convenor | Incoming Convenor | Tech Steward | Spring (60 days) | Signed `succession-handoff-checklist.md` |
| **SOP-012** | RFC Moderation & 72-Hour Consent Closing | Operations Steward | Club Convenor | Tech Steward | Continuous (72h) | PR Status update (`rfcs/approved/`) |
| **SOP-013** | Alumni Office Hours & Mentorship Bridge | Operations Steward | Club Convenor | Alumni Council | Monthly | Event Recording & Referral Roster |
| **SOP-014** | Team Structure Maintenance & Task Auditing| Club Convenor | Active Cohort | Operations Steward | Quarterly | Updated `TEAM_STRUCTURE.md` |
| **SOP-020** | Member Intake & Directory Web Sync | Web Platform DRI | Tech Steward | Operations Steward | Within 24 hours | Updated Google Sheet & `directory.html` |
| **SOP-021** | "2-in-a-Pod" Matching & Idea Colliders | Domain Steward | Club Convenor | Academic DRI | Monthly | Matched project incubation list |
| **SOP-022** | Code of Conduct & Restorative Mediation | Domain Steward | Club Convenor | Faculty Advisor | Within 48 hours | Confidential resolution log |
| **SOP-023** | Weekly Debugging Clinic & Peer Prep | Tech Steward | Operations Steward | Senior Mentors | Weekly (Wed) | Resolved bug clinic report |
| **SOP-030** | Project Incubation Funnel Progression | Tech Steward | Domain Steward | Project Leads | Bi-weekly sprints| Merged codebases & preprints |
| **SOP-031** | Cloud Compute Quotas & API Vault | Cloud & Compute DRI| Tech Steward | Convenor | Within 24 hours | Provisioned API keys & `compute.yml` |
| **SOP-032** | Open Source Licensing & IP Clearances | Open Source DRI | Tech Steward | Project Leads | Per Release | Verified `LICENSE` & `CREDITS.md` |
| **SOP-033** | Hackathon Squad Mobilization & War-Room | Competition Capt. | Operations Steward | Cloud DRI | Per Event | Squad roster & 72h `post-mortem.md` |
| **SOP-040** | Weekly Paper Reading Group Dissection | Literature Lead | Domain Steward | Rotating Member | Weekly (Fri) | Curated reading notes in archive |
| **SOP-041** | Guest Lecture Logistics & Host Runbook | Guest Lead | Operations Steward | Convenor | Monthly | Executed runbook & published video |
| **SOP-042** | AI Literacy Bootcamps for Non-STEM Schools | Academic Outreach | Domain Steward | Tech Mentors | Once per semester| Workshop certificates & code repo |
| **SOP-050** | Micro-Grant & Expense Reimbursements | Financial Steward | Club Convenor | Operations Steward | Within 48 hours | UPI receipt & cleared voucher |
| **SOP-051** | Sponsor Vetting & Corporate Ethics Review | Club Convenor | Faculty Advisory | Financial Steward | Per Sponsor Offer| Vetted partner agreement |
| **SOP-052** | Public Ledger Maintenance & Audit Deck | Financial Steward | Student Audit Cmt | Convenor | Quarterly | Published `LEDGER.md` update |
| **SOP-060** | Model Card Enforcement & Bias Screen | AI Safety Steward | Tech Steward | Project Authors | Per Model Release| Compliant `MODEL_CARD.md` |
| **SOP-061** | DPDP Compliance & PII Scrubbing Audit | AI Safety Steward | Tech Steward | Web Platform DRI | Per Dataset Launch| Anonymization verification report |

> [!IMPORTANT]
> **Founder Asset & Domain Exemption**: The root domain `nalandalibrary.com` is the non-transferable private property of the Founder. The Web Platform DRI and Technical Steward administer delegated DNS records for `aiclub.nalandalibrary.com` only; root registrar ownership is strictly non-transferable and excluded from cohort transitions.

---

## 4. Provisions for Changing Team Structure (The 80% Supermajority Rule)

To prevent arbitrary power consolidation, hasty restructuring by small factions, or political instability across cohorts, **any structural modification to the team hierarchy is strictly protected by an 80% supermajority threshold**.

### 4.1 Scope of Structural Changes
The 80% Supermajority Rule applies to:
1. Creating, merging, renaming, or abolishing any Executive Council seat (Convenor, Tech Steward, Domain Steward, Operations Steward, Financial Steward, AI Safety Steward).
2. Modifying the mandatory RACI task ownership assignments or removing accountability layers.
3. Modifying the 60-day cohort succession framework or voting eligibility criteria.
4. Altering this amendment threshold itself.

*(Routine operational changes—such as scheduling clinics, assigning ad-hoc project pods, or updating tool versions—do NOT require 80% and proceed via standard 72h RFC consent under SOP-012).*

### 4.2 Step-by-Step Structural Amendment Procedure

```
  Step 1: Structural RFC Draft (14-Day Notice)
  - Proposer drafts an RFC under `rfcs/structural/` outlining proposed changes & rationale.
  - Requires co-sponsorship by at least 3 active cohort members from different undergrad disciplines.
       │
       ▼
  Step 2: Campus Deliberation & Townhall
  - A formal 45-minute open-floor cohort townhall is convened on the Nalanda campus.
  - Arguments for and against the restructuring are recorded openly.
       │
       ▼
  Step 3: Supermajority Secret Ballot (48-Hour Window)
  - Administered digitally to all verified registered active cohort members.
  - Criterion: At least 80% of ALL active registered members must vote AFFIRMATIVE.
  - Example: If the active cohort has 40 registered members, at least 32 members must vote YES.
       │
       ▼
  Step 4: Faculty Endorsement & Ratification
  - The Faculty Advisory Board reviews the ballot verification to ensure institutional compliance.
  - Upon sign-off, `TEAM_STRUCTURE.md` and `SOP-014` are updated and committed to `main`.
```

### 4.3 Voter Eligibility
* Only enrolled students in the active MSc Data Science & AI cohorts who are registered in the official directory (`directory.html`) and have attended at least two club activities in the preceding 60 days are eligible voting members.
