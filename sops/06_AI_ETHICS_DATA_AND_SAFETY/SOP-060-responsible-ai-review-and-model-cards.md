# SOP-060: Responsible AI Review and Model Card Enforcement

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-060 |
| **Category** | 06 - AI Ethics, Data & Safety |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | All ML Researchers, Project Leads, Technical Stewards |
| **Compliance** | Mandatory for all public releases and publications |

---

## 1. Purpose
To ensure that all machine learning models, autonomous agents, and synthetic datasets produced under the Club's banner conform to international standards of safety, reproducibility, and ethical transparency.

---

## 2. The Mandatory Model Card Standard
Every model published to Hugging Face, GitHub, or academic conferences must include a standardized `MODEL_CARD.md` based on `templates/model-card-template.md`.

### Required Sections:
1. **Model Details**: Architecture, parameter count, base checkpoint, training hardware.
2. **Intended Use**: Out-of-the-box capabilities, recommended deployment context.
3. **Out-of-Scope / Prohibited Uses**: Military, non-consensual surveillance, deepfake creation, or academic impersonation.
4. **Training Data Provenance**: Source datasets, licensing, demographic coverage, filtering heuristics.
5. **Evaluation & Bias Analysis**: Benchmark performance broken down across subpopulations, error modes, and toxicity/hallucination rates.
6. **Carbon & Energy Footprint**: Estimated GPU hours and CO2 emissions incurred during training.

---

## 3. Fast Ethical Risk Screening
Before public launch, the project pod must answer 4 screening questions:
* **Q1 (Dual Use)**: Could this model be trivially adapted to generate biological/chemical threats, automated cyberattacks, or hate speech?
* **Q2 (Consent)**: Did the training data involve private individuals who did not consent to data harvesting?
* **Q3 (Hallucination Harm)**: If deployed in high-stakes domains (healthcare, legal, public welfare), what are the consequences of false positive/negative predictions?
* **Q4 (Algorithmic Fairness)**: Does the model systematically underperform on marginalized linguistic, regional, or socio-economic demographics?

If any risk is identified, the pod must document mitigations (filtering, guardrails, confidence thresholds) directly in the Model Card.
