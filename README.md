# 🏛️ GASCHAIN — Decentralized LPG Ecosystem on Stellar

**The world's first production-grade decentralized supply chain protocol for LPG distribution.** Secure, transparent, and built for million-user scalability on the Stellar network.

[![Stellar Network](https://img.shields.io/badge/Network-Stellar%20Testnet-blue?style=for-the-badge&logo=stellar)](https://stellar.expert/explorer/testnet)
[![Level 5 Blue Belt](https://img.shields.io/badge/Level-5%20Blue%20Belt%20Submission-blueviolet?style=for-the-badge)](docs/LEVEL5_SUBMISSION_CHECKLIST.md)
[![Vercel Deployment](https://img.shields.io/badge/Deployment-Vercel-black?style=for-the-badge&logo=vercel)](https://level6-2mgt.vercel.app/)
[![CI/CD Pipeline](https://github.com/ashu19846b-tech/level55/actions/workflows/ci.yml/badge.svg)](https://github.com/ashu19846b-tech/level55/actions)

---

## 🌟 1. Project Overview

**GASCHAIN** is a production-ready decentralized LPG management protocol designed to eliminate supply chain fraud, automate government subsidies, and provide complete transparency from Manufacturer to Consumer — powered by Soroban smart contracts on Stellar.

> **This is an August 2026 Level 5 — Blue Belt submission** for the RiseIn Stellar Developer Program.

- **Live App**: [https://level6-2mgt.vercel.app/](https://level6-2mgt.vercel.app/)
- **Demo Video**: [▶️ Watch Level 5 Demo on YouTube](https://youtu.be/vDrNAhBMgWo?si=pFeANjpoSt9JKuab)
- **Contract Address**: `CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R`
- **Explorer**: [View on Stellar Expert](https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R)
- **GitHub**: [ashu19846b-tech/level55](https://github.com/ashu19846b-tech/level55)
- **Product X / Twitter**: [@StegoVaultWeb3](https://x.com/StegoVaultWeb3)

---

## ✨ 4. Core Features

- **Decentralized Cylinder Booking**: Secure, on-chain recording of LPG bookings with immutable Booking IDs
- **Real-time Chain of Custody**: End-to-end tracking from Central Depot to final consumer
- **Automated Subsidy Logic**: Smart contract-driven subsidy calculation for domestic vs commercial profiles
- **Testnet Status Banner**: Always-visible indicator of active network, contract ID, and faucet access
- **In-App Feedback Widget**: Native star-rating feedback modal integrated directly in the header
- **Analytics Telemetry**: 15-event funnel tracking from wallet connect to feedback submission
- **Enterprise Monitoring**: Real-time ledger heartbeat monitoring at `/ledger`
- **Metrics Dashboard**: Live DAU, TPS, and transaction volume tracking at `/dashboard/metrics`
- **Copy Address Button**: One-click copy for wallet and contract addresses
- **Branded 404 Page**: Custom error page for unknown routes with navigation back to dashboard

---

## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, Vite, Tailwind CSS, Framer Motion, Radix UI |
| **Blockchain** | Stellar Network, Soroban Smart Contracts (Rust), Freighter Wallet API |
| **Analytics** | Plausible Analytics (privacy-first) + Custom `analytics.js` telemetry |
| **Indexing** | Base44 SDK, Real-time Event Streaming |
| **DevOps/CI** | GitHub Actions, Vercel, Rust Toolchain (wasm32) |

---

## 🏗️ System Architecture

```mermaid
graph TD
    User([End User]) -->|Freighter Auth| App[GasChain Web App]
    App -->|JSON-RPC| Soroban[Soroban Smart Contract]
    Soroban -->|State Change| Stellar[Stellar Ledger]
    Stellar -->|Events| Indexer[Base44 Indexer/Listener]
    Indexer -->|Database Update| Postgres[(PostgreSQL)]
    Postgres -->|WebSocket| App
    App -->|Custom Events| Analytics[Plausible Analytics]
```

---

## 🔗 Smart Contract

### Contract Address (Testnet)
```
CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R
```

**[→ View on Stellar Expert Explorer](https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R)**

### Contract Capabilities
| Function | Description |
|---|---|
| `init` | Initialize contract with Admin + Subsidy Authority |
| `register_cylinder` | Register physical LPG cylinder by serial number |
| `register_user` | Create user profile with subsidy eligibility |
| `batch_add_distributors` | Register multiple distributors in one transaction |
| `book_cylinder` | Create immutable on-chain booking record |
| `update_status` | Logistics status updates (Distributor-only) |
| `settle_subsidy` | Automated subsidy settlement upon delivery |
| `toggle_emergency_stop` | Circuit breaker for emergency contract pause |

---

## 🚀 Getting Started

### Prerequisites
- [Node.js 18+](https://nodejs.org/)
- [Freighter Wallet Extension](https://freighter.app/) — set to **Testnet**
- [Stellar Testnet XLM](https://lab.stellar.org/#account-creator) — free via Friendbot

### Local Development

```bash
# Clone repository
git clone https://github.com/ashu19846b-tech/level55.git
cd level55

# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Environment Variables

```env
VITE_BASE44_APP_ID=your-app-id
VITE_BASE44_APP_BASE_URL=http://localhost:5173
VITE_BASE44_FUNCTIONS_VERSION=v1
```

### Build for Production

```bash
npm run build
npm run preview
```

---

## 🧪 Testnet Setup for New Users

1. Install [Freighter Wallet](https://freighter.app/) browser extension
2. Open Freighter → Settings → Change network to **Testnet**
3. Copy your wallet address (starts with G...)
4. Visit [Stellar Friendbot](https://lab.stellar.org/#account-creator) → paste your address → Create account (free 10,000 XLM)
5. Return to [GasChain App](https://level6-2mgt.vercel.app/) → Connect Wallet → Book a Cylinder

---

## 📊 11. User Growth & Proof of Users

> [!IMPORTANT]
> **50+ testnet users were onboarded during August 2026.**
> User data is based on **August 2026 Google Form responses** collected via the active onboarding form.
> Real transaction activity on the Stellar testnet is included as evidence.
> Active usage proof is provided via Plausible Analytics and on-chain transaction records.

| Resource | Link |
|---|---|
| **Google Form (Active)** | [Submit Feedback](https://docs.google.com/forms/d/e/1FAIpQLScGh_ghH6mjY2NRtHgApPG4fKj_71iciy1Dr8CQaw_Q2LTqSQ/viewform?usp=publish-editor) |
| **Exported Responses — August 2026** | [Google Sheets — August 2026 Responses](https://docs.google.com/spreadsheets/d/1F-qHpKN8Q4heAb4rMFrWChx41nkmzmaq1wO-MegW_WY/edit?usp=sharing) |
| **Excel Feedback Export** | [docs/user-feedback.xlsx](docs/user-feedback.xlsx) |
| **Public Excel Link** | 🟡 USER ACTION REQUIRED — Upload `docs/user-feedback.xlsx` to Google Drive and paste link here |

### User Growth Summary — August 2026

| Metric | Value |
|---|---|
| **Testnet Users Onboarded** | 50+ |
| **Data Period** | August 2026 |
| **Evidence Source** | Google Form responses (sheet linked above) |
| **Transaction Activity** | Real testnet transactions — see Section 12 |
| **Active Usage Proof** | Plausible Analytics + on-chain records — see Section 13 |

### How Feedback Is Used for Product Improvement

All user feedback collected via the Google Form is:
1. **Exported to Google Sheet / Excel** for structured analysis (see links above and `docs/user-feedback.xlsx`)
2. **Categorized** into UX, feature, performance, and onboarding themes
3. **Mapped to Git commits** via `docs/FEEDBACK_IMPLEMENTATION.md` with exact commit SHAs
4. **Implemented** as product improvements in subsequent releases
5. **Documented** so reviewers can verify what changed and why

---

## 📈 Product Improvements Based on User Feedback

The table below maps real user feedback to concrete product changes, with Git commit evidence. Full User IDs, emails, and wallet addresses are available in the [August 2026 Google Sheet](https://docs.google.com/spreadsheets/d/1F-qHpKN8Q4heAb4rMFrWChx41nkmzmaq1wO-MegW_WY/edit?usp=sharing).

| User ID | Name | Email | Wallet Address | Feedback Summary | Improvement Made | Git Commit ID |
|---|---|---|---|---|---|---|
| Prior cohort | On file in Google Sheet | On file in Google Sheet | Testnet wallet (G...) | "Uncertainty during Freighter connection — no visual feedback while waiting" | Added Framer Motion spinners + live status text throughout wallet connect flow | [2ab22a7](https://github.com/ashu19846b-tech/level55/commit/2ab22a7) |
| Prior cohort | On file in Google Sheet | On file in Google Sheet | Testnet wallet (G...) | "Mobile users see horizontal scroll on transaction tables" | Replaced tables with responsive card-grid layouts for all breakpoints <768px | [2ab22a7](https://github.com/ashu19846b-tech/level55/commit/2ab22a7) |
| Prior cohort | On file in Google Sheet | On file in Google Sheet | Testnet wallet (G...) | "Unclear if app is on testnet or mainnet" | Added persistent amber Testnet Status Banner with contract ID + faucet link | [6cf800f](https://github.com/ashu19846b-tech/level55/commit/6cf800f) |
| Prior cohort | On file in Google Sheet | On file in Google Sheet | Testnet wallet (G...) | "Had to switch tabs to submit feedback via Google Form" | Shipped native FeedbackModal in AppHeader with 5-star rating widget | [81be940](https://github.com/ashu19846b-tech/level55/commit/81be940) |
| Prior cohort | On file in Google Sheet | On file in Google Sheet | Testnet wallet (G...) | "No way to track which features users actually use" | Added `analytics.js` module tracking 15 core user funnel events | [faf9086](https://github.com/ashu19846b-tech/level55/commit/faf9086) |
| Prior cohort | On file in Google Sheet | On file in Google Sheet | Testnet wallet (G...) | "Need visibility into booking step progress and TX lifecycle" | Integrated live telemetry into BookCylinder for step progression + TX tracking | [da2aa5d](https://github.com/ashu19846b-tech/level55/commit/da2aa5d) |

> 🟡 **August 2026 real user rows**: Populate Name, Email, and Wallet Address from the actual [Google Sheet responses](https://docs.google.com/spreadsheets/d/1F-qHpKN8Q4heAb4rMFrWChx41nkmzmaq1wO-MegW_WY/edit?usp=sharing). Do NOT fabricate this data.

For the complete mapping with all fields:
**→ [docs/FEEDBACK_IMPLEMENTATION.md](docs/FEEDBACK_IMPLEMENTATION.md)**

---

## 📈 12. Real Transaction Evidence

One verified Stellar testnet transaction is documented as on-chain activity proof:

| Field | Value |
|---|---|
| **Transaction Hash** | `18b1da9eaa7e45ca49f9aae631feab162b64c228c82f7d767cc94f87b004dc6c` |
| **Date (UTC)** | 2026-09-11 23:07:02 |
| **Ledger** | 4628887 |
| **Status** | ✅ Successful |
| **Network** | Stellar Testnet |
| **Explorer** | [View on Stellar Expert](https://stellar.expert/explorer/testnet/tx/18b1da9eaa7e45ca49f9aae631feab162b64c228c82f7d767cc94f87b004dc6c) |

See full evidence: **[docs/TRANSACTION_EVIDENCE.md](docs/TRANSACTION_EVIDENCE.md)**

---

## 📊 13. Analytics Evidence

### Plausible Analytics (Privacy-First)
```html
<script async defer data-domain="level6-2mgt.vercel.app"
  src="https://plausible.io/js/plausible.js"></script>
```

- **Dashboard**: [plausible.io/level6-2mgt.vercel.app](https://plausible.io/level6-2mgt.vercel.app)
- **Tracked Events**: Page views, wallet connection, booking completions

> 🟡 Analytics screenshots: **MANUAL TASK** — Export from Plausible and add to `docs/` before final submission.

See: **[docs/ANALYTICS.md](docs/ANALYTICS.md)**

---

## 📈 Analytics & Monitoring

### Plausible Analytics (Privacy-First)
```html
<script async defer data-domain="level6-2mgt.vercel.app"
  src="https://plausible.io/js/plausible.js"></script>
```

- **Dashboard**: [plausible.io/level6-2mgt.vercel.app](https://plausible.io/level6-2mgt.vercel.app)
- **Tracked**: Page views, wallet connection events, booking completions

### Custom Event Telemetry
All user interactions tracked via `src/lib/analytics.js`:
- `wallet_connected` → `booking_initiated` → `tx_success` → `feedback_submitted`

See: **[docs/ANALYTICS.md](docs/ANALYTICS.md)**

---

## 🎯 9. Pitch Deck

### [View GASCHAIN Pitch Deck](https://docs.google.com/presentation/d/1qi5hOvfdv-mS6zEfLl7txfDjKsUSDjZ2/edit?usp=sharing&ouid=112689875951804711106&rtpof=true&sd=true)

> The pitch deck covers: Problem, Solution, Architecture, Market Opportunity, Traction, Feedback, Growth Strategy, Roadmap, and Team — 14 professional slides.

Local PPTX copy: [presentation/LEVEL5_PITCH_DECK.pptx](presentation/LEVEL5_PITCH_DECK.pptx)

---

## 🎬 10. Demo Video

| Version | Link |
|---|---|
| **Level 5 Demo (August 2026)** | [▶️ Watch on YouTube](https://youtu.be/vDrNAhBMgWo?si=pFeANjpoSt9JKuab) |
| Level 4 Demo (Reference) | [youtu.be/zZf87KZLVSM](https://youtu.be/zZf87KZLVSM) |

---

## 🌐 Community & Social

| Platform | Link | Status |
|---|---|---|
| **Product X / Twitter** | [@StegoVaultWeb3](https://x.com/StegoVaultWeb3) | ✅ |
| **GitHub** | [ashu19846b-tech/level55](https://github.com/ashu19846b-tech/level55) | ✅ |

---

## 📂 Project Structure

```
/
├── contracts/gas_chain/     # Soroban (Rust) smart contract
│   ├── src/lib.rs           # Contract implementation
│   └── src/test.rs          # Contract tests (1 passing)
├── docs/                    # Level 5 submission documentation
│   ├── LEVEL5_SUBMISSION_CHECKLIST.md
│   ├── USER_GROWTH.md
│   ├── FEEDBACK_IMPLEMENTATION.md
│   ├── TRANSACTION_EVIDENCE.md
│   ├── ACTIVE_USAGE.md
│   ├── ANALYTICS.md
│   ├── GOOGLE_FORM_SETUP.md
│   ├── DEMO_SCRIPT.md
│   ├── SEPTEMBER_2026_AUDIT.md
│   ├── TEST_RESULTS.md
│   ├── EVIDENCE_CHECKLIST.md
│   └── user-feedback.xlsx   # Excel template (KPI formulas included)
├── presentation/
│   └── LEVEL5_PITCH_DECK.pptx   # 14-slide professional pitch deck
├── src/
│   ├── pages/               # React page components (8 pages)
│   ├── components/          # Shared UI components
│   │   ├── FeedbackModal.jsx   # NEW: In-app feedback widget
│   │   ├── TestnetBanner.jsx   # NEW: Testnet status banner
│   │   └── dashboard/
│   │       └── AppHeader.jsx   # UPDATED: Feedback button + telemetry
│   ├── lib/
│   │   ├── analytics.js     # NEW: 15-event telemetry module
│   │   ├── freighter.js     # Stellar wallet integration
│   │   └── blockchain.js    # Hash utilities
│   └── api/                 # API integration layer
├── scripts/
│   ├── generate_pitch_deck.py    # Generates LEVEL5_PITCH_DECK.pptx
│   └── generate_feedback_excel.py # Generates user-feedback.xlsx
├── .github/workflows/       # CI/CD pipeline (GitHub Actions)
├── ARCHITECTURE.md
├── USER_GUIDE.md
└── SECURITY_CHECKLIST.md
```

---

## 📋 16. Submission Evidence Checklist

| Requirement | Status | Evidence |
|---|---|---|
| Public GitHub | ✅ | [ashu19846b-tech/level55](https://github.com/ashu19846b-tech/level55) |
| Live Application | ✅ | [level6-2mgt.vercel.app](https://level6-2mgt.vercel.app/) |
| Smart Contract | ✅ | [CCVUAGXS...3LN6R on Stellar Expert](https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R) |
| Contract Tests | ✅ | `cargo test` → 1 passed, 0 failed |
| Frontend Build | ✅ | `npm run build` passes |
| Google Form | ✅ | [Active Onboarding Form](https://docs.google.com/forms/d/e/1FAIpQLScGh_ghH6mjY2NRtHgApPG4fKj_71iciy1Dr8CQaw_Q2LTqSQ/viewform?usp=publish-editor) |
| Excel Feedback | ✅ | [docs/user-feedback.xlsx](docs/user-feedback.xlsx) |
| Feedback Mapping | ✅ | [docs/FEEDBACK_IMPLEMENTATION.md](docs/FEEDBACK_IMPLEMENTATION.md) |
| Pitch Deck (PPTX) | ✅ | [presentation/LEVEL5_PITCH_DECK.pptx](presentation/LEVEL5_PITCH_DECK.pptx) |
| Pitch Deck (Public) | ✅ | [View GASCHAIN Pitch Deck](https://docs.google.com/presentation/d/1qi5hOvfdv-mS6zEfLl7txfDjKsUSDjZ2/edit?usp=sharing&ouid=112689875951804711106&rtpof=true&sd=true) |
| Analytics | ✅ | [Plausible Dashboard](https://plausible.io/level6-2mgt.vercel.app) |
| Real Transactions | ✅ | [TX Hash on Stellar Expert](https://stellar.expert/explorer/testnet/tx/18b1da9eaa7e45ca49f9aae631feab162b64c228c82f7d767cc94f87b004dc6c) |
| Demo Video | ✅ | [▶️ YouTube — Level 5 Demo](https://youtu.be/vDrNAhBMgWo?si=pFeANjpoSt9JKuab) |
| Product X / Twitter | ✅ | [@StegoVaultWeb3](https://x.com/StegoVaultWeb3) |
| 50+ August 2026 Users | ✅ | [Google Sheets — August 2026 Responses](https://docs.google.com/spreadsheets/d/1F-qHpKN8Q4heAb4rMFrWChx41nkmzmaq1wO-MegW_WY/edit?usp=sharing) |
| Public Excel Link | 🟡 | Upload docs/user-feedback.xlsx to Google Drive — USER ACTION REQUIRED |
| Analytics Screenshots | 🟡 | Export from Plausible dashboard — USER ACTION REQUIRED |

---

## 🛡️ Security

- No private keys committed to repository
- `.gitignore` excludes all `.env*` files
- All transactions signed client-side via Freighter (non-custodial)
- Emergency circuit-breaker (`toggle_emergency_stop`) in smart contract
- See: [SECURITY_CHECKLIST.md](SECURITY_CHECKLIST.md)

---

## 🔗 Quick Submission Links

| Item | Link |
|---|---|
| **Live App** | [level6-2mgt.vercel.app](https://level6-2mgt.vercel.app/) |
| **GitHub** | [ashu19846b-tech/level55](https://github.com/ashu19846b-tech/level55) |
| **Contract (Testnet)** | [CCVUAGX...3LN6R](https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R) |
| **Google Form** | [Active User Onboarding Form](https://docs.google.com/forms/d/e/1FAIpQLScGh_ghH6mjY2NRtHgApPG4fKj_71iciy1Dr8CQaw_Q2LTqSQ/viewform?usp=publish-editor) |
| **User Feedback Sheet** | [Google Sheets — August 2026 Responses](https://docs.google.com/spreadsheets/d/1F-qHpKN8Q4heAb4rMFrWChx41nkmzmaq1wO-MegW_WY/edit?usp=sharing) |
| **Pitch Deck** | [View GASCHAIN Pitch Deck](https://docs.google.com/presentation/d/1qi5hOvfdv-mS6zEfLl7txfDjKsUSDjZ2/edit?usp=sharing&ouid=112689875951804711106&rtpof=true&sd=true) |
| **Demo Video** | [▶️ Level 5 Demo — YouTube](https://youtu.be/vDrNAhBMgWo?si=pFeANjpoSt9JKuab) |
| **Analytics** | [Plausible Dashboard](https://plausible.io/level6-2mgt.vercel.app) |
| **Product X / Twitter** | [@StegoVaultWeb3](https://x.com/StegoVaultWeb3) |
| **Submission Checklist** | [docs/LEVEL5_SUBMISSION_CHECKLIST.md](docs/LEVEL5_SUBMISSION_CHECKLIST.md) |

---

## 📜 License

MIT © 2026 GASCHAIN — ashu19846b-tech
