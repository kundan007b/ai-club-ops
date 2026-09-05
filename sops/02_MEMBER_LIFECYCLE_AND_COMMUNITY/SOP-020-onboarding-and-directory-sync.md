# SOP-020: Member Intake, Onboarding, and Directory Synchronization

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-020 |
| **Category** | 02 - Member Lifecycle & Community |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | All New Members, Operations Steward, Technical Steward |
| **Integration** | `Data-science-club/join.html` & Google Apps Script Backend |

---

## 1. Purpose
To ensure zero-friction member intake, immediate integration into the collaborative directory, and automatic pairing based on complementary technical and domain skills.

---

## 2. The Member Intake Funnel

```
 ┌────────────────────────────────────────────────────────┐
 │ 1. Student accesses https://nalandalibrary.com/join.html│
 └───────────────────────────┬────────────────────────────┘
                             │ Submits Web Form
 ┌───────────────────────────▼────────────────────────────┐
 │ 2. Google Apps Script stores row in 'Members' Sheet    │
 │    - Name, Email, WhatsApp, UG Background, Skills,     │
 │      Offerings, Perks Needed                           │
 └───────────────────────────┬────────────────────────────┘
                             │ Webhook / Daily Sync
 ┌───────────────────────────▼────────────────────────────┐
 │ 3. Automated Welcome & Community Placement             │
 │    - WhatsApp/Telegram cohort link dispatched           │
 │    - GitHub org invite sent to candidate GitHub handle  │
 │    - Public Directory profile dynamically rendered     │
 └────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Intake Procedure

### Step 1: Online Registration
* Incoming students navigate to the club portal (`join.html`).
* Fields captured:
  - Full Name & Academic Email (`@nalandauniv.edu.in` or primary verified email)
  - Undergraduate background: Categorized into **Technical** (CS, IT, Physics, Math, Engineering) or **Domain/Qualitative** (Economics, International Relations, History, Ecology, Humanities, Agriculture, Commerce).
  - Explicit skills & methods (Python, SQL, R, Econometrics, Fieldwork, Policy Analysis, Archival Research).
  - Mutual contribution profile: What the member can offer vs. what perks/support they seek.

### Step 2: Instant Welcome & Zero-Barrier Access
* Within 24 hours of submission:
  1. The member is added to the official WhatsApp/Telegram announcement broadcast.
  2. The member's GitHub handle receives an invitation to join the `nalanda-ai-club` organization.
  3. The member is granted read/write access to the shared Google Drive / Hugging Face team repository.

### Step 3: Peer Cohort Pairing ("The First 7 Days")
* The Operations Steward checks the newest entries in the Member Sheet.
* If a domain-specialist joins (e.g. History/IR), they are introduced to a technical partner during the next weekly reading group or coffee sprint to break the ice.

---

## 4. Privacy & Data Handling
* In compliance with **SOP-061 (Data Privacy & DPDP Act)**:
  - Phone numbers and personal emails are never exposed on public web endpoints.
  - The public directory (`directory.html`) only displays first name, UG background, skills, offerings, and portfolio links.
  - Members may update or redact their profile at any time by emailing `aiclub@nalandalibrary.com`.
