## 📋 Pull Request Type
Please select the relevant option:
- [ ] **Project Proposal** (New incubation pod / Spark / Sprint)
- [ ] **Compute Quota Request** (YAML allocation specification)
- [ ] **Standard Operational RFC** (72-hour consent proposal)
- [ ] **SOP Revision or Addition** (Document update)
- [ ] **Structural / Governance Change** (Requires 80% supermajority cohort vote)
- [ ] **Tooling / Bug Fix** (CLI, validator, docs compiler)

---

## 🔍 Pre-Submission Verification Checklist

### For All Contributions
- [ ] I have run `bash scripts/verify_all.sh` locally and all 16 tests pass.
- [ ] I have recompiled `HANDBOOK.md` via `python scripts/build_docs.py` (or `ai-ops compile`) if any SOP or Charter was modified.
- [ ] No API keys, passwords, or personal phone numbers are exposed in this PR.

### For Project Incubation Proposals
- [ ] Enforces the **"2-in-a-Pod" Matching Law** (at least one computational lead and at least one domain specialist named).
- [ ] Metadata YAML code block satisfies `schemas/project_proposal.schema.json`.

### For Compute Allocation Requests
- [ ] Tier-2 requests are within the ₹3,000 micro-quota limit.
- [ ] Auto-shutdown idle timeout is set to $\le 30$ minutes.

### For Structural Changes (`TEAM_STRUCTURE.md` or Executive Seats)
- [ ] Attached record or link to the verified **80% Supermajority Cohort Vote**.
- [ ] Endorsed by the Faculty Advisory Board.

---

## 📝 Summary of Changes
Provide a brief summary of what this change accomplishes and its benefit to the AI Club cohort.
