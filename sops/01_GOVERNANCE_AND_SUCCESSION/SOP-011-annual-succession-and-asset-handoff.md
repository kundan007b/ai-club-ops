# SOP-011: Annual Succession and Digital Asset Handoff

| Metadata | Value |
| :--- | :--- |
| **SOP Code** | SOP-011 |
| **Category** | 01 - Governance & Succession |
| **Effective Date** | 2026-09-01 |
| **Target Audience** | Outgoing & Incoming Stewards, Convenor, Technical Leads |
| **Trigger Event** | Spring Semester (March–April annually) |

---

## 1. Purpose
To eliminate the institutional memory cliff inherent in 2-year postgraduate cycles by enforcing a standardized 60-day overlapping transition window and a cryptographically verified digital asset handover.

---

## 2. The 60-Day "Relay Race" Timeline

```
  T - 60 Days                T - 30 Days                T - 7 Days               T = 0
 (Early March)               (Early April)             (Late April)            (Convocation)
      │                           │                         │                       │
      ├───────────────────────────┼─────────────────────────┼───────────────────────┤
      ▼                           ▼                         ▼                       ▼
Open Nomination           Co-Shadowing             Full Credential         Formal Ascension
& Consent Call            Active Meetings          Rotation & Vault        & Alumni Advisory
(Incoming Cohort)         Joint Decisions          Access Verification     Transition
```

---

## 3. Step-by-Step Succession Protocol

### Phase I: Call for Leadership & Consent-Based Nomination (T - 60 Days)
1. **Notice Issuance**: Outgoing Convenor posts a transparent notification across all cohort channels inviting interest in Technical, Domain, and Operations Steward roles.
2. **Intent Submissions**: Interested candidates from the junior cohort submit a brief (1-page) statement outlining their vision, track record in club activities, and proposed projects.
3. **Consensus Circle**: If multiple candidates contest a role, the cohort convenes an informal open-floor consensus circle. If consensus cannot be reached within 5 business days, a simple ranked-choice secret ballot is administered.

### Phase II: The Shadow Period (T - 60 to T - 15 Days)
1. Each incoming lead is paired 1-on-1 with the respective outgoing steward.
2. Incoming leads must co-author at least one RFC, co-organize one major event, and observe one quarterly budget reconciliation.
3. Outgoing leads document unwritten operational nuances in the `docs/` repository.

### Phase III: Digital Asset & Credential Transfer (T - 14 to T - 7 Days)
All transitions must execute the verified **Asset Transfer Protocol**:

> [!IMPORTANT]
> **Founder Asset Protection**: The root domain `nalandalibrary.com` is the exclusive, non-transferable private property of the Founder. Under no circumstances is root registrar ownership transferred across cohorts. The Club operates solely on delegated DNS access for `aiclub.nalandalibrary.com`.

| Asset / Account | Transfer / Delegation Method | Verification Criterion |
| :--- | :--- | :--- |
| **Root Domain (`nalandalibrary.com`)** | **NON-TRANSFERABLE** | Sole property of Founder. Retained permanently. |
| **Subdomain DNS (`aiclub.nalandalibrary.com`)** | Cloudflare DNS manager access delegated to incoming lead | Incoming lead updates record; root ownership verified intact |
| **GitHub Org (`nalanda-ai-club`)** | Transfer `Owner` role; downgrade outgoing to `Member` / `Alumni` | Incoming lead successfully merges a test PR |
| **Google Apps Script & Sheet** | Transfer Ownership of Sheet and Script project | Incoming lead verifies `loadMembers()` and write triggers |
| **Cloud Accounts (RunPod/GCP/AWS)** | Add new billing admins; rotate root API keys | Old API tokens revoked; verified zero residual billing liability |
| **Official Email (`aiclub@nalandalibrary.com`)** | Update forwarding aliases or Google Workspace access | Outgoing passwords invalidated |
| **Social / WhatsApp / Telegram** | Promote incoming leads to Group Admins | Outgoing leads transitioned to Alumni observer status |

---

## 4. The Handover Audit & Verification Sign-Off
Before outgoing leads receive their formal "Founding Leadership & Service Honors":
1. Both outgoing and incoming Convenors must run `ai-ops audit` from the CLI to ensure all repositories, documentation links, and financial records are clean.
2. Complete and sign the `succession-handoff-checklist.md`.
3. Submit the signed checklist to the Faculty Advisory archive.

---

## 5. Failure Mode & Contingency
* **Sudden Vacancy**: If an elected lead departs or becomes inactive, the co-lead instantly assumes full responsibilities for 14 days while an emergency 48-hour RFC is posted to ratify a replacement.
* **Orphaned Credentials**: All shared secrets and secondary recovery codes must be stored in the Club's encrypted password vault (Bitwarden/1Password team vault) accessible by at least two active faculty/staff advisors as emergency escrow.
