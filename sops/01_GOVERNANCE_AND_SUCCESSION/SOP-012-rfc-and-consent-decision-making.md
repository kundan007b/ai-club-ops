# SOP-012: RFC and Consent-Based Decision-Making

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-012 |
| **Category** | 01 - Governance & Succession |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | All Club Members |
| **Principle** | "Silence implies consent; objections require alternatives." |

---

## 1. Purpose
To eliminate lengthy, circular committee debates by establishing an asynchronous, written, transparent **Request for Comments (RFC)** mechanism modeled after open-source engineering governance (IETF / Python PEP / Rust RFC).

---

## 2. When is an RFC Required?

| Action / Initiative | RFC Required? | Decision Path |
| :--- | :--- | :--- |
| Starting a new project prototype / research paper | **NO** | Autonomous (Rule of 2, SOP-030) |
| Requesting Tier 1 Compute (< ₹1,000 / Colab) | **NO** | Instant self-registration (SOP-031) |
| Requesting Tier 2 Compute (₹1,000 - ₹10,000) | **NO** | Technical Steward 24h review |
| Spending Club funds > ₹10,000 | **YES** | Standard 72h RFC |
| Amending operational SOPs | **YES** | Standard 72h RFC |
| Modifying Team Structure / Governance seats | **YES** | **Structural RFC (80% Supermajority Cohort Consent)** |
| Signing partnerships with external companies / sponsors | **YES** | Standard 72h RFC + Faculty Review |
| Hosting a major multi-college hackathon / conference | **YES** | Standard 72h RFC |

---

## 3. The 72-Hour Consent Decision Cycle

```
  T = 0                     T + 48h                   T + 72h
  (RFC Published)           (Review & Feedback)       (Consensus Reached)
     │                         │                         │
     ▼                         ▼                         ▼
  PR opened on              Members review;           Zero unresolved blocking
  `ops/rfcs/` with          suggest refinements       objections -> Merged &
  template metadata         or constructive edits     Auto-Approved
```

### Step 1: Draft and Scaffold
1. The proposer runs the CLI scaffolder:
   ```bash
   ai-ops scaffold --type rfc --title "Introduce-Dedicated-RunPod-GPU-Cluster"
   ```
2. Fill out the sections in `templates/rfc-template.md`:
   - Motivation & Context
   - Proposed Specification
   - Budget / Resource Implications
   - Trade-offs and Rejected Alternatives
   - Multidisciplinary Impact

### Step 2: Publish & Announce
1. Open a Pull Request in the Club operations repository (`nalanda-ai-club/ops`).
2. Post a direct link to the PR in the official communication channel with the tag `[RFC-VOTE]`.
3. The 72-hour countdown begins immediately upon posting.

### Step 3: Consent vs. Objection Norms
* **Consent is the Default**: A proposal does not need 100% "yes" votes. If members do not object, they are presumed to consent.
* **The Rule of Constructive Objection**: An objection is only valid if:
  1. It identifies a demonstrable harm or risk to the Club, members, or Nalanda University.
  2. The objector provides a concrete, workable alternative.
  3. Personal taste, bikeshedding, or passive skepticism are not valid blocking objections.
* **Friendly Amendments**: The author may amend the PR during the 72-hour window. If major amendments occur, an extension of 24 hours is automatically granted.

### Step 4: Resolution & Merging
* If no blocking objection remains at the 72-hour mark: The RFC is marked **APPROVED** and merged into `rfcs/approved/`.
* If an impasse arises: The Convenor hosts a 20-minute time-boxed synchronous discussion. If no consensus emerges, a simple 60% majority vote of active members decides.
