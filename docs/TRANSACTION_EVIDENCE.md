# 🔗 TRANSACTION EVIDENCE — GasChain Stellar Testnet

> This document describes how to capture, record, and present real testnet transaction evidence for the Level 5 submission.

---

## Why Transaction Evidence Matters

The Level 5 requirement states: **"Real transaction activity required."**
Every user who onboards must:
1. Connect their Freighter wallet to the GasChain app
2. Initiate a cylinder booking that triggers a real Stellar transaction
3. Have that transaction verifiable on Stellar Expert (Testnet)

---

## How to Capture Transaction Evidence

### For Users:
1. Visit [https://level6-2mgt.vercel.app/](https://level6-2mgt.vercel.app/)
2. Connect Freighter Wallet (Testnet mode)
3. Go to **Book Cylinder**
4. Complete the 3-step booking form
5. Click **Confirm Booking** → Freighter popup appears → **Sign**
6. Copy the transaction hash shown in the confirmation toast
7. Visit: `https://stellar.expert/explorer/testnet/tx/[PASTE_HASH_HERE]`
8. Share the screenshot of the explorer page in your feedback form

### For the Developer:
1. Export all transaction hashes from Google Form responses
2. Verify each hash on Stellar Expert (must show September 2026 date)
3. Record in the table below (REAL data only)

---

## 🌐 Smart Contract Reference

```
Contract Address: CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R
Network: Stellar Testnet
Horizon: https://horizon-testnet.stellar.org
Explorer: https://stellar.expert/explorer/testnet
```

---

## 📊 September 2026 Transaction Registry

> 🚨 USER ACTION REQUIRED — Fill with REAL transaction hashes only.
> Every hash must be verifiable on Stellar Expert.

| User ID | Wallet Address | Transaction Hash | Date | Feature | Explorer Link |
|---|---|---|---|---|---|
| USR-001 | G... | [REAL TX HASH] | Sep 2026 | Book Cylinder | [Add Link] |
| USR-002 | G... | [REAL TX HASH] | Sep 2026 | Book Cylinder | [Add Link] |
| ... | ... | ... | ... | ... | ... |

---

## Testnet Faucet Setup

New users who do not have testnet XLM must first fund their wallet:

1. Go to [https://lab.stellar.org/#account-creator](https://lab.stellar.org/#account-creator)
2. Paste your Freighter wallet public key (G...)
3. Click **Create account** — receive 10,000 free testnet XLM instantly

Alternative: [https://friendbot.stellar.org/?addr=YOUR_WALLET_ADDRESS](https://friendbot.stellar.org)

---

## ✅ Verification Checklist Per Transaction

- [ ] Transaction hash is a valid 64-character hex string
- [ ] Hash is visible on `stellar.expert/explorer/testnet/tx/[HASH]`
- [ ] Transaction date shows September 2026
- [ ] Source account matches the user's wallet address (G...)
- [ ] Transaction involves the GasChain contract or XLM payment

---

## 📁 Related Documents

- [USER_GROWTH.md](./USER_GROWTH.md) — Full user registry
- [ACTIVE_USAGE.md](./ACTIVE_USAGE.md) — Active usage tracking
- [FEEDBACK_IMPLEMENTATION.md](./FEEDBACK_IMPLEMENTATION.md) — Feedback mapping
