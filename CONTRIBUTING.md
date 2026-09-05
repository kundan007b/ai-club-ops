# 🤝 Contributing to the AI Club — Nalanda University

Welcome! The **AI Club at Nalanda University** is an open, multidisciplinary research and engineering collective. We bring together students and scholars from computer science, economics, international relations, history, ecology, mathematics, and public policy.

We value **clarity, speed, rigorous empirical inquiry, and low administrative friction**.

---

## ⚡ Core Contribution Rules

Before submitting any Pull Request, ensure your proposal respects our foundational directives:

1. **The "2-in-a-Pod" Matching Law ([SOP-021](sops/02_MEMBER_LIFECYCLE_AND_COMMUNITY/SOP-021-cross-disciplinary-pod-formation.md))**:
   - Every project incubation pod must pair at least **one computational practitioner** (code, machine learning, data engineering) with at least **one domain specialist** (economics, policy, historical archives, ecology, etc.).
   - Pure toy engineering clone apps without domain grounding are discouraged.
2. **Default-to-Approve for Experiments**:
   - Proposing an exploratory idea (Spark / Sprint) or using Tier-1 compute (Colab/Kaggle) does not require committee approval.
3. **72-Hour Asynchronous Consent (RFCs)**:
   - Operational policy updates and standard expenditures proceed via 72-hour silent consent RFCs. Silence implies consent; objections require an actionable alternative.
4. **The 80% Supermajority Rule for Structural Changes**:
   - Any modification to `TEAM_STRUCTURE.md` or Executive Council seats requires a formal 14-day townhall process and an affirmative vote of at least **80% of registered active cohort members**.
5. **Founder Asset Protection**:
   - The root domain `nalandalibrary.com` is the non-transferable private property of the Founder. The Club operates on the delegated subdomain `aiclub.nalandalibrary.com`. Never submit PRs attempting to transfer root registrar ownership.

---

## 🛠️ How to Submit Common Contributions

### 1. Propose a New Project (Incubation Track)
1. Scaffold a proposal using the CLI:
   ```bash
   ai-ops scaffold --type project --title "Your-Project-Name"
   ```
2. Fill out the sections in the generated markdown file. Ensure the YAML header includes both a `technical_lead` and a `domain_lead`.
3. Validate your proposal locally:
   ```bash
   ai-ops validate proposal-your-project-name.md
   ```
4. Submit a Pull Request with the tag `[PROJECT]`.

### 2. Request Compute Quota (Tier 2 Micro-Grant)
1. Scaffold a compute allocation spec:
   ```bash
   ai-ops scaffold --type compute --title "your-project-name"
   ```
2. Ensure:
   - Estimated cost is $\le ₹3,000$.
   - `idle_auto_shutdown_minutes` is set to $\le 30$.
3. Validate locally:
   ```bash
   ai-ops validate compute-request-your-project-name.yml
   ```
4. Open a PR with the tag `[COMPUTE]`. Technical Stewards review within 24 hours.

### 3. Propose an Operational RFC
1. Scaffold an RFC:
   ```bash
   ai-ops scaffold --type rfc --title "RFC-Title"
   ```
2. Fill out motivation, specification, budget, and trade-offs.
3. Open a PR with the tag `[RFC-VOTE]`. The 72-hour consent clock starts upon posting.

### 4. Edit or Add an SOP
1. Edit the relevant file in `sops/` or create a new one following the `SOP-XXX: Title` header format.
2. Recompile the unified handbook:
   ```bash
   python scripts/build_docs.py
   ```
3. Run the audit and test suite:
   ```bash
   bash scripts/verify_all.sh
   ```
4. Commit both the SOP file and the updated `HANDBOOK.md`.

---

## 💻 Local Development & Verification

Ensure you have Python 3.9+ installed.

```bash
# 1. Clone your fork
git clone https://github.com/<your-username>/ai-club-ops.git
cd ai-club-ops

# 2. Install dependencies in editable mode
pip install -e .

# 3. Run the full verification gateway (audit + compile + tests)
bash scripts/verify_all.sh
```

### Required Checks Before Opening a PR
* All 16 unit tests must pass.
* `ai-ops audit` reports zero errors.
* If modifying any SOP, `HANDBOOK.md` must be recompiled.
* No API keys, passwords, or personal telephone numbers exposed.

---

## ⚖️ Intellectual Property & Licensing
* **Your Code**: You retain 100% of your intellectual property and commercialization rights.
* **Community Contributions**: All shared scripts and SOPs are licensed under the [MIT License](LICENSE).
* **Research & Notes**: Curricula and reading archives are licensed under **CC-BY 4.0**.
