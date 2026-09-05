# Model Card: [Model Name]

```yaml
model_name: "nalanda-bert-pali"
version: "1.0.0"
base_checkpoint: "google/bert_uncased_L-4_H-512_A-8"
license: "Apache-2.0"
authors:
  - "Researcher One (MSc Data Science & AI)"
  - "Researcher Two (School of Historical Studies)"
institution: "AI Club, Nalanda University"
release_date: "YYYY-MM-DD"
```

---

## 1. Model Overview
* **Architecture**: Transformer encoder / decoder / causal language model.
* **Intended Task**: Named entity recognition, OCR error correction, sentiment analysis, causal classification.
* **Supported Languages**: English, Hindi, Sanskrit, Pali, Magahi, Bhojpuri.

## 2. Intended Use & Target Deployments
* **Primary Uses**: Academic research, archival exploration, educational demonstrations.
* **Prohibited Uses**: Automated surveillance, non-consensual profiling, academic fraud, weapon guidance.

## 3. Training Data & Provenance
* **Dataset Name(s)**:
* **Source & Collection Protocol**:
* **Data Preprocessing & PII Scrubbing**: Detail how emails, phone numbers, and identifying tokens were removed (SOP-061).
* **Licensing of Underlying Data**:

## 4. Evaluation & Bias Metrics
* **Validation Benchmark Results**:
  - Accuracy / F1-Score:
  - Perplexity / BLEU / ROUGE:
* **Subgroup & Fairness Disaggregation**:
  - Performance across dialects / domains:
  - Error distribution analysis:

## 5. Environmental & Compute Footprint
* **Hardware Utilized**: e.g., 1x NVIDIA RTX 4090 / 2x A100 (80GB).
* **Training Time**: ~28 GPU hours.
* **Estimated CO2e emissions**: ~3.4 kg CO2e.
