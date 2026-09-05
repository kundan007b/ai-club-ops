# SOP-031: Compute and Cloud Resource Allocation Protocol

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-031 |
| **Category** | 03 - Project Incubation & Innovation |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | All Project Teams, Technical Stewards, Convenor |
| **Philosophy** | "Zero waiting for basic compute; transparent quotas for heavy workloads" |

---

## 1. Purpose
To maximize access to computational hardware (GPUs, TPU credits, and LLM APIs) while preventing runaway cloud bills, idle server waste, or resource hoarding.

---

## 2. Compute Tiers & Access Channels

```
┌────────────────────────────────────────────────────────────────────────┐
│                        COMPUTE COMMONS TIERS                           │
├───────────────┬────────────────────────────┬───────────────────────────┤
│ Tier Level    │ Hardware / Budget Spec     │ Approval Latency          │
├───────────────┼────────────────────────────┼───────────────────────────┤
│ Tier 1: Free  │ Google Colab, Kaggle,      │ Instant (Self-Service)    │
│ Commons       │ Hugging Face Spaces (CPU)  │ Zero approval required    │
├───────────────┼────────────────────────────┼───────────────────────────┤
│ Tier 2: Micro │ Up to ₹3,000 / $35 per pod │ 24-Hour Asynchronous Sync │
│ Quota         │ (RunPod / OpenAI / Gemini) │ Validated via YAML schema │
├───────────────┼────────────────────────────┼───────────────────────────┤
│ Tier 3: Heavy │ Multi-GPU clusters         │ 72-Hour Fast RFC          │
│ Research      │ (> ₹3,000, A100 / H100)    │ Faculty endorsement       │
└───────────────┴────────────────────────────┴───────────────────────────┘
```

---

## 3. Tier 2 Request & Allocation Workflow

### Step 1: Submit YAML Specification
Teams generate and fill out `templates/compute-allocation-request.yml` or run:
```bash
ai-ops scaffold --type compute --title "fine-tuning- IndicLLM"
```

### Step 2: Validate via CLI
Teams run the schema validator locally:
```bash
ai-ops validate compute-allocation-request.yml
```

### Step 3: Fast Technical Steward Review
* The Technical Steward checks:
  1. Is the estimated runtime and cost realistic?
  2. Have local/free resources (Tier 1) been exhausted or proven inadequate?
  3. Is there an automatic shutdown / max spending limit configured?
* Within 24 hours, API keys or credit vouchers are provisioned via the Club's encrypted key vault.

---

## 4. Usage Rules & Cost Controls
1. **Mandatory Auto-Shutdown**: Any deployed cloud VM (AWS/GCP/RunPod) must have an idle-shutdown script configured to terminate after 30 minutes of zero GPU utilization.
2. **Never Commit Secrets**: Any repository found containing plaintext API keys will have the key immediately revoked and the pod temporarily downgraded to Tier 1.
3. **Reproducibility Requirement**: All pods receiving Tier 2 or 3 compute must push their training scripts and loss curves to the project repository upon run completion.

---

## 5. Dispute & Fairness Arbitration
* If total compute demand exceeds monthly pooled reserves:
  - Priority is given to projects with upcoming conference submission deadlines (within 30 days).
  - Teams that have successfully published post-mortems or papers in past sprints receive bonus priority.
