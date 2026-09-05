# 🏛️ AI Club Operations & Administrative SOP Package (`ai-club-ops`)
### **Nalanda University (नालन्दा विश्वविद्यालय) — MSc Data Science & AI**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cohort](https://img.shields.io/badge/Cohort-2026--28%20%26%20Beyond-amber.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](#)
[![Governance](https://img.shields.io/badge/Governance-Async%20RFC%20%2F%20Low--Friction-purple.svg)](#)

---

## 📖 Overview

The **AI Club Operations Package** (`ai-club-ops`) is the official governance engine, standard operating procedure (SOP) repository, and operational CLI for the **AI Club at Nalanda University** (Rajgir, Bihar).

Rooted in the ancient intellectual legacy of Nalanda—where diverse minds gathered to pursue open, cross-disciplinary truth—this package codifies administrative practices to **minimize bureaucratic friction**, **stimulate daring innovation**, and guarantee **perpetual institutional succession** across two-year postgraduate master's cohorts.

---

## ⚡ Core Innovation Directives

1. **Default-to-Approve**: No member needs committee permission to prototype a project, test an open-source model, or run an introductory reading circle.
2. **The "2-in-a-Pod" Matching Law**: Every incubated project team must pair at least one technical practitioner (coding, statistics, neural nets) with at least one domain specialist (international relations, economics, history, ecology, policy). *Methods can be taught; a good question is harder to come by.*
3. **72-Hour Asynchronous Consent (RFC)**: Decisions and charter changes are proposed via markdown Pull Requests. Silence implies consent; objections require a concrete alternative.
4. **Compute Commons**: Self-service Tier 1 access (Colab/Hugging Face) with automated 24-hour turnaround for Tier 2 micro-quotas (< ₹3,000).
5. **Perpetual Succession Protocol**: A 60-day overlapping shadow transition window and cryptographic key vault handoff to ensure zero loss of velocity upon cohort graduation.
6. **Dual-Licensing Standard**: Student creators retain 100% intellectual property; public community projects default to MIT (code) and CC-BY 4.0 (research/data).
7. **80% Supermajority Structural Constraint**: To prevent political instability while maximizing operational velocity, all governance roles and the master team structure (`TEAM_STRUCTURE.md`) are protected by a mandatory 80% affirmative cohort consent rule.

---

## 📂 Package Architecture

```
packages/ai-club-ops/
├── pyproject.toml                             # Package dependencies & CLI entrypoint
├── README.md                                  # You are here
├── CHARTER.md                                 # Founding Charter & Constitution
├── TEAM_STRUCTURE.md                          # Master topology, RACI task matrix & 80% consent rule
├── HANDBOOK.md                                # Consolidated publication-ready manual
├── sops/                                      # Codified Standard Operating Procedures
│   ├── 01_GOVERNANCE_AND_SUCCESSION/          # Leadership roles, succession, RFCs, alumni, team structure
│   ├── 02_MEMBER_LIFECYCLE_AND_COMMUNITY/     # Onboarding, 2-in-a-pod, conduct, clinics
│   ├── 03_PROJECT_INCUBATION_AND_INNOVATION/  # 4-stage funnel, compute commons, IP, squads
│   ├── 04_EVENTS_AND_KNOWLEDGE_SHARING/       # Reading groups, guest talks, bootcamps
│   ├── 05_FINANCE_GRANTS_AND_TRANSPARENCY/    # Micro-grants, ethical sponsorship, ledger
│   └── 06_AI_ETHICS_DATA_AND_SAFETY/          # Model cards, DPDP Act 2023 compliance
├── templates/                                 # Fill-in-the-blank operational templates
│   ├── rfc-template.md                        # Standard RFC document
│   ├── project-proposal-template.md           # 1-page incubation proposal with YAML
│   ├── compute-allocation-request.yml         # YAML spec for GPU/API quotas
│   ├── event-runbook-template.md              # Minute-by-minute event execution
│   ├── succession-handoff-checklist.md        # Annual digital asset handoff
│   ├── model-card-template.md                 # Hugging Face / research model card
│   └── post-mortem-template.md                # Blameless sprint / competition debrief
├── schemas/                                   # Machine-verifiable JSON Schemas
│   ├── project_proposal.schema.json           # Schema for incubation briefs
│   └── compute_request.schema.json            # Schema for cloud compute specs
├── src/ai_club_ops/                           # CLI & automation engine
│   ├── __init__.py
│   ├── cli.py                                 # `ai-ops` CLI command router
│   ├── validator.py                           # Schema & '2-in-a-Pod' validator
│   ├── scaffolder.py                          # Rapid template generator
│   └── compiler.py                            # Unified handbook builder & auditor
├── tests/                                     # Pytest test suite
│   ├── test_cli.py
│   ├── test_schemas.py
│   └── test_sops_integrity.py
└── scripts/
    ├── build_docs.py                          # Handbook build runner
    └── verify_all.sh                          # Automated verification gateway
```

---

## 🛠️ Operational CLI (`ai-ops`) Quickstart

Install the package in development mode:

```bash
cd packages/ai-club-ops
pip install -e .
```

### 1. Validate a Project Proposal or Compute Request
Enforces schema validity, auto-shutdown settings, and the **"2-in-a-Pod" interdisciplinary requirement**:
```bash
# Validate project incubation proposal
ai-ops validate templates/project-proposal-template.md

# Validate compute allocation request
ai-ops validate templates/compute-allocation-request.yml
```

### 2. Scaffold a New Artifact
Quickly generate pre-filled templates with automated slugs, dates, and numbers:
```bash
# Scaffold an RFC
ai-ops scaffold --type rfc --title "Deploy-Self-Hosted-Ollama-Node"

# Scaffold a project proposal
ai-ops scaffold --type project --title "pali-nlp-translation"

# Scaffold a compute allocation request
ai-ops scaffold --type compute --title "fine-tuning-mistral-bihar-archives"

# Scaffold an event runbook
ai-ops scaffold --type event --title "Guest-Colloquium-Prof-Patnaik"
```

### 3. Audit Repository Integrity
Verifies all SOP headers, metadata tables, and Charter existence:
```bash
ai-ops audit
```

### 4. Compile the Unified Handbook
Generates a complete, single-file Markdown handbook with auto-indexed links:
```bash
ai-ops compile
```

---

## 📋 Catalog of Standard Operating Procedures

| SOP Code | Title | Category |
| :--- | :--- | :--- |
| **SOP-010** | [Governance Structure and Leadership Roles](sops/01_GOVERNANCE_AND_SUCCESSION/SOP-010-governance-structure-and-roles.md) | 01 - Governance & Succession |
| **SOP-011** | [Annual Succession and Digital Asset Handoff](sops/01_GOVERNANCE_AND_SUCCESSION/SOP-011-annual-succession-and-asset-handoff.md) | 01 - Governance & Succession |
| **SOP-012** | [RFC and Consent-Based Decision-Making](sops/01_GOVERNANCE_AND_SUCCESSION/SOP-012-rfc-and-consent-decision-making.md) | 01 - Governance & Succession |
| **SOP-013** | [Alumni Council and Advisory Board Engagement](sops/01_GOVERNANCE_AND_SUCCESSION/SOP-013-alumni-council-and-advisory-board.md) | 01 - Governance & Succession |
| **SOP-014** | [Team Structure, Task Ownership, and Structural Amendments](sops/01_GOVERNANCE_AND_SUCCESSION/SOP-014-team-structure-and-task-ownership.md) | 01 - Governance & Succession |
| **SOP-020** | [Member Intake, Onboarding, and Directory Sync](sops/02_MEMBER_LIFECYCLE_AND_COMMUNITY/SOP-020-onboarding-and-directory-sync.md) | 02 - Member Lifecycle & Community |
| **SOP-021** | [Cross-Disciplinary Pod Formation & Team Dynamics](sops/02_MEMBER_LIFECYCLE_AND_COMMUNITY/SOP-021-cross-disciplinary-pod-formation.md) | 02 - Member Lifecycle & Community |
| **SOP-022** | [Code of Conduct and Restorative Conflict Resolution](sops/02_MEMBER_LIFECYCLE_AND_COMMUNITY/SOP-022-code-of-conduct-and-restorative-resolution.md) | 02 - Member Lifecycle & Community |
| **SOP-023** | [Peer Mentorship, Office Hours, and Skills Clinics](sops/02_MEMBER_LIFECYCLE_AND_COMMUNITY/SOP-023-peer-mentorship-and-office-hours.md) | 02 - Member Lifecycle & Community |
| **SOP-030** | [Project Lifecycle and Lean Incubation Stages](sops/03_PROJECT_INCUBATION_AND_INNOVATION/SOP-030-project-lifecycle-and-lean-stages.md) | 03 - Project Incubation & Innovation |
| **SOP-031** | [Compute and Cloud Resource Allocation Protocol](sops/03_PROJECT_INCUBATION_AND_INNOVATION/SOP-031-compute-and-cloud-resource-allocation.md) | 03 - Project Incubation & Innovation |
| **SOP-032** | [Open Source, Intellectual Property, and Licensing](sops/03_PROJECT_INCUBATION_AND_INNOVATION/SOP-032-open-source-ip-and-licensing.md) | 03 - Project Incubation & Innovation |
| **SOP-033** | [Hackathons, Case Competitions, and Squad Mobilization](sops/03_PROJECT_INCUBATION_AND_INNOVATION/SOP-033-hackathons-and-competition-squads.md) | 03 - Project Incubation & Innovation |
| **SOP-040** | [Weekly Paper Reading Groups and Literature Dissection](sops/04_EVENTS_AND_KNOWLEDGE_SHARING/SOP-040-weekly-paper-reading-groups.md) | 04 - Events & Knowledge Sharing |
| **SOP-041** | [Guest Lectures and Industry Colloquiums](sops/04_EVENTS_AND_KNOWLEDGE_SHARING/SOP-041-guest-lectures-and-industry-colloquiums.md) | 04 - Events & Knowledge Sharing |
| **SOP-042** | [Skills Clinics, AI Literacy, and Cross-School Bootcamps](sops/04_EVENTS_AND_KNOWLEDGE_SHARING/SOP-042-skills-clinics-and-bootcamps.md) | 04 - Events & Knowledge Sharing |
| **SOP-050** | [Micro-Grants, Seed Allocations, and Expense Reimbursements](sops/05_FINANCE_GRANTS_AND_TRANSPARENCY/SOP-050-micro-grants-and-expense-reimbursement.md) | 05 - Finance, Grants & Transparency |
| **SOP-051** | [Sponsorship Vetting and Ethical Partnerships](sops/05_FINANCE_GRANTS_AND_TRANSPARENCY/SOP-051-sponsorship-vetting-and-ethics.md) | 05 - Finance, Grants & Transparency |
| **SOP-052** | [Public Ledger Accounting and Quarterly Audit](sops/05_FINANCE_GRANTS_AND_TRANSPARENCY/SOP-052-public-ledger-and-audit.md) | 05 - Finance, Grants & Transparency |
| **SOP-060** | [Responsible AI Review and Model Card Enforcement](sops/06_AI_ETHICS_DATA_AND_SAFETY/SOP-060-responsible-ai-review-and-model-cards.md) | 06 - AI Ethics, Data & Safety |
| **SOP-061** | [Data Privacy, Sovereign Compliance, and DPDP Act Guidelines](sops/06_AI_ETHICS_DATA_AND_SAFETY/SOP-061-data-privacy-and-dpdp-compliance.md) | 06 - AI Ethics, Data & Safety |

---

## 🌐 Web Integration (`Data-science-club`)
The web portal in `Data-science-club/` provides the public facing window for new members (`join.html`) and the dynamic member directory (`directory.html`). This operations package provides the operational spine for the club behind the website.

---

## ⚖️ License
The documentation, SOPs, and governance framework are released under the [MIT License](LICENSE) and [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).  
*AI Club, Nalanda University © 2026. Free to fork and adapt for academic institutions worldwide.*
