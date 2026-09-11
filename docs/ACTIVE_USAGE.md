# 📊 ACTIVE USAGE PROOF — GasChain September 2026

> This document tracks evidence of active product usage during the September 2026 challenge period.

---

## Usage Evidence Categories

### 1. Analytics Dashboard (Plausible)
- **URL**: https://plausible.io/level6-2mgt.vercel.app
- **Tracked Events**: page views, wallet connections, booking completions
- **Status**: 🟡 USER ACTION REQUIRED — Capture Plausible dashboard screenshot in September 2026

> Capture a screenshot of the Plausible dashboard showing September 2026 traffic and attach it here or to `docs/EVIDENCE_CHECKLIST.md`.

---

### 2. Custom Event Telemetry (In-App)
As of September 2026, the app tracks these events via `src/lib/analytics.js`:

| Event | What It Tracks |
|---|---|
| `page_view` | Every page navigation |
| `wallet_connect_attempt` | When user clicks connect wallet |
| `wallet_connected` | Successful wallet connection |
| `wallet_connect_failed` | Failed connection (error tracking) |
| `booking_initiated` | User starts the booking flow |
| `tx_sign_prompt` | Freighter signing popup triggered |
| `tx_submitted` | Transaction sent to Horizon |
| `tx_success` | Transaction confirmed on ledger |
| `tx_failed` | Transaction rejected or timed out |
| `feedback_modal_opened` | User opened in-app feedback |
| `feedback_submitted` | User submitted feedback |

All events are also stored in `sessionStorage` under `gaschain_telemetry` for session review.

---

### 3. Blockchain Ledger Activity

Visit the GasChain contract on Stellar Expert to see all on-chain interactions:
- **Contract**: https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R

Evidence of usage:
- Number of `book_cylinder` invocations in September
- Number of unique wallet addresses that called the contract
- Contract event emission logs

---

### 4. Google Form Response Activity

Google Form response timestamps serve as direct evidence of user engagement:
- Each form response has a submission timestamp (visible in Sheets column A)
- September 2026 submissions will be visible as September dates
- Export and verify: `docs/user-feedback.xlsx`

---

## 🟡 USER ACTION REQUIRED

1. Screenshot the **Plausible Analytics dashboard** for September 2026 showing:
   - Total visitors
   - Unique visitors
   - Top pages
   - Any custom events if available

2. Screenshot the **Stellar Expert contract page** showing September transaction activity

3. Screenshot the **Google Sheets** responses tab showing September 2026 timestamps

4. Place all screenshots in `public/screenshots/` directory

---

## Active Usage Metrics Table

> Fill with REAL data only from September 2026

| Metric | Value | Evidence Source |
|---|---|---|
| Total September Page Views | [ADD REAL NUMBER] | Plausible Dashboard |
| Unique September Visitors | [ADD REAL NUMBER] | Plausible Dashboard |
| Wallet Connections in September | [ADD REAL NUMBER] | Analytics Events |
| Successful Transactions in September | [ADD REAL NUMBER] | Stellar Expert |
| Google Form Responses in September | [ADD REAL NUMBER] | Google Sheets |
| Average Session Duration | [ADD REAL VALUE] | Plausible Dashboard |

---

## 📁 Related Documents

- [TRANSACTION_EVIDENCE.md](./TRANSACTION_EVIDENCE.md) — Per-transaction hashes
- [ANALYTICS.md](./ANALYTICS.md) — Analytics technical setup
- [USER_GROWTH.md](./USER_GROWTH.md) — User registry
