# 🎬 DEMO SCRIPT — GasChain Level 5 Product Walkthrough

> **Duration**: 3–5 minutes  
> **Audience**: RiseIn Stellar Level 5 evaluators  
> **Goal**: Show real product, real testnet usage, real user flow, real Stellar transaction

---

## 🟡 USER ACTION REQUIRED — RECORD DEMO VIDEO

A real demo video must be recorded. The old video (`youtu.be/zZf87KZLVSM`) was made for Level 4 and does not show Level 5 features. Record a new video following this script.

**Recording Tools:**
- OBS Studio (free) — https://obsproject.com
- Loom (browser-based) — https://loom.com
- Windows Game Bar (Win + G)

**Upload To:** YouTube (Unlisted or Public) and paste the URL in README.

---

## 📋 Demo Script — Scene-by-Scene

### Scene 1: Introduction (0:00–0:25)
**Say:**
> "Hi, I'm [Your Name]. This is GasChain — the world's first decentralized LPG supply chain and automated subsidy protocol built on the Stellar blockchain.
> 
> GasChain eliminates black market diversion of LPG cylinders, automates government subsidy settlements, and provides cryptographic chain-of-custody from manufacturer to consumer — all on Stellar Testnet."

**Show:** The GasChain landing page at `level6-2mgt.vercel.app`

---

### Scene 2: Problem Statement (0:25–0:45)
**Say:**
> "The problem is massive. Billions of dollars in subsidized fuel are stolen annually through ghost bookings and counterfeit cylinders. There's zero cryptographic proof before subsidies are disbursed.
> 
> GasChain fixes this using Soroban smart contracts on Stellar — making every booking, delivery, and subsidy settlement immutable and publicly auditable."

**Show:** The landing page statistics or the architecture diagram

---

### Scene 3: Wallet Connection (0:45–1:10)
**Say:**
> "Let me show you how a real user connects. I'm using Freighter Wallet on Stellar Testnet."

**Do:**
1. Click **Connect Wallet** on the landing page
2. Freighter extension popup appears — show it on screen
3. Click **Approve**
4. Show the wallet address populating in the UI
5. Show the **Testnet Active** banner at the top

**Say:**
> "Connected. Notice the amber Testnet banner confirming we're on Stellar Testnet, not Mainnet — and the verified contract address is visible."

---

### Scene 4: Main Product — Book Cylinder (1:10–2:30)
**Say:**
> "The core feature is booking a certified LPG cylinder on-chain."

**Do:**
1. Navigate to `/book`
2. Fill in user details (Name, Phone)
3. Select State → City
4. Select cylinder type: **14.2 KG Domestic**
5. Show the automatic subsidy calculation: ₹200 discount
6. Click **Next → Next → Confirm Booking**
7. Freighter popup appears — click **Sign**
8. Show the transaction status: Signing → Submitted → Confirmed
9. Show the success toast with the Booking ID

**Say:**
> "That transaction is now permanently recorded on the Stellar Testnet. The booking ID is immutable. Let's verify it on-chain."

---

### Scene 5: Transaction Verification (2:30–3:00)
**Do:**
1. Navigate to `/ledger` (Blockchain Ledger page)
2. Find the transaction in the list
3. Show the transaction hash
4. Open `stellar.expert/explorer/testnet/tx/[HASH]` in a new tab
5. Show the transaction details on-chain

**Say:**
> "Here's our transaction on the Stellar Expert explorer. The timestamp, wallet address, and transaction hash all match. This is real on-chain data — fully verifiable by anyone."

---

### Scene 6: Supply Chain & Dashboard (3:00–3:30)
**Do:**
1. Navigate to `/supply-chain`
2. Show real-time logistics tracking
3. Navigate to `/dashboard/metrics`
4. Show DAU, TPS, and system metrics

**Say:**
> "Distributors can track every cylinder's logistics status in real-time. The metrics dashboard shows network health and transaction throughput — all live."

---

### Scene 7: Feedback System (3:30–3:50)
**Do:**
1. Click the **Review & Feedback** button in the top header
2. Show the FeedbackModal
3. Rate the product (5 stars)
4. Type a quick feedback message
5. Click **Submit**

**Say:**
> "Users can submit product feedback directly from within the app. This is linked to our Level 5 user onboarding pipeline — collecting real ratings and suggestions that drive product improvements."

---

### Scene 8: Closing & Value Proposition (3:50–4:10)
**Say:**
> "GasChain demonstrates that Stellar is production-ready for enterprise-scale commodity tracking and social benefit delivery systems.
>
> We've onboarded 50+ real testnet users in September 2026, collected genuine product feedback, and shipped measurable improvements — all with a live Soroban contract on Stellar Testnet.
>
> The contract address is `CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R`. Thank you!"

---

## 📌 Post-Recording Checklist

- [ ] Video is at least 3 minutes, maximum 5 minutes
- [ ] Freighter wallet connection is visible on screen
- [ ] At least one real testnet transaction was signed during recording
- [ ] Transaction is shown on Stellar Expert explorer
- [ ] Product name and Stellar branding are visible
- [ ] Video is uploaded to YouTube (not private — at minimum Unlisted)
- [ ] YouTube URL is added to README.md

---

## 🔗 Demo Resources

- Live App: https://level6-2mgt.vercel.app/
- Contract Explorer: https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R
- Testnet Faucet: https://lab.stellar.org/#account-creator
- Freighter Download: https://freighter.app/
