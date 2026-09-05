# SOP-061: Data Privacy, Sovereign Compliance, and DPDP Act Guidelines

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-061 |
| **Category** | 06 - AI Ethics, Data & Safety |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | Data Curators, Researchers, Operations Stewards |
| **Statutory Law** | Digital Personal Data Protection (DPDP) Act 2023 (India) |

---

## 1. Purpose
To protect individual privacy rights, govern data ingestion pipelines, and guarantee full statutory compliance with Indian digital privacy laws across all club activities.

---

## 2. Core Data Governance Principles

### 2.1 Explicit Notice and Consent
* When collecting surveys, user interactions, or student demographic information, participants must receive a clear notice stating:
  - Exact purpose of processing.
  - Retention duration.
  - Instructions for requesting complete deletion of data.

### 2.2 Strict PII Anonymization
* **Personally Identifiable Information (PII)**: Full names, Aadhaar numbers, phone numbers, exact residential addresses, biometric data, and personal health metrics.
* **Protocol**:
  1. All raw PII must be scrubbed or pseudonymized using irreversible hashing (SHA-256 with salt) prior to exploratory analysis or model training.
  2. Public datasets released by the Club must never contain recoverable raw PII.

### 2.3 Synthetic Data Preference
* Wherever feasible, student pods are strongly encouraged to train on high-fidelity synthetic datasets or public government open data (e.g. `data.gov.in`, Open Government Data Platform) rather than scraping private consumer interfaces.

---

## 3. Data Breach & Incident Response
* If any member discovers an accidental leak of student phone numbers, credentials, or private interview notes:
  1. Notify the Technical Steward within **2 hours** at `aiclub@nalandalibrary.com`.
  2. Revoke public access to the affected repository, spreadsheet, or bucket immediately.
  3. Rotate all associated secrets.
  4. Issue a transparent notice to affected individuals detailing the extent of exposure and remedial actions taken.
