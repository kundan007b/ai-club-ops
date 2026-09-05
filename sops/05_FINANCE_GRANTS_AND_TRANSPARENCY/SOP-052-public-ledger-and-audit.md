# SOP-052: Public Ledger Accounting and Quarterly Audit

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-052 |
| **Category** | 05 - Finance, Grants & Transparency |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | Treasurer, Convenor, All Members, University Auditors |
| **Mandate** | 100% Radical Transparency |

---

## 1. Purpose
To ensure irreproachable financial honesty, eliminate suspicions of embezzlement or favoritism, and provide incoming cohorts with historical fiscal trends.

---

## 2. The Open Ledger Architecture
* The Club maintains an open-access ledger (`LEDGER.md`) in the operations repository.
* Every single inflow (grant, donation, sponsorship, university fund) and outflow (API bill, reimbursement, refreshments, hardware purchase) is logged in chronological order.

### Ledger Format
```markdown
| Date | Tx ID | Category | Description | Inflow (₹) | Outflow (₹) | Balance (₹) | Verified By |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-10 | TX-001 | Grant | Alumni Seed Grant (Cohort 2026) | 25,000 | - | 25,000 | R. Ranjan |
| 2026-09-15 | TX-002 | Compute | RunPod GPU Credits (Pod-04) | - | 2,400 | 22,600 | Tech Steward |
```

---

## 3. Quarterly Audit Protocol
1. **At the end of each academic quarter** (November, February, May, August):
   - An independent 2-member student audit committee (drawn from non-executive members) reviews all bank statements against `LEDGER.md`.
   - Any discrepancy > ₹100 triggers an inquiry.
2. **The Transparency Deck**:
   - A 3-slide visual summary of receipts, expenditures, and remaining runway is shared during the next cohort meeting.
