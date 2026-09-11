# 📝 GOOGLE FORM SETUP GUIDE — GasChain Level 5

> This document provides complete instructions for creating, sharing, and exporting the official Google Form for GasChain Level 5 user onboarding and feedback collection.

---

## Step 1: Create the Google Form

1. Go to [https://forms.google.com](https://forms.google.com)
2. Click **Blank** to create a new form
3. Title the form: `GasChain Testnet User Onboarding & Feedback — September 2026`
4. Add this description:
   ```
   Thank you for testing GasChain — the decentralized LPG supply chain protocol on Stellar!
   
   This form collects your onboarding details and product feedback for our Level 5 
   RiseIn Stellar submission. Your responses will be used to improve the product and
   demonstrate real user activity.
   
   PRIVACY: Your wallet address and email are collected solely for onboarding verification.
   Your feedback will be anonymized in public reports.
   ```

---

## Step 2: Add Required Fields

Add these sections and fields in this exact order:

### Section 1: Basic Information

| Field | Type | Required | Validation |
|---|---|---|---|
| User ID (leave blank — will be auto-assigned) | Short answer | No | — |
| Your Full Name | Short answer | ✅ Yes | — |
| Your Email Address | Short answer | ✅ Yes | Email validation |
| Your Stellar Testnet Wallet Address | Short answer | ✅ Yes | Must start with G, 56 chars |

**Instructions to add next to Wallet field:**
> "Connect Freighter Wallet → Click on the G... address at the top → Copy it here. Your wallet must be on Stellar Testnet."

---

### Section 2: Product Usage

| Field | Type | Required | Options |
|---|---|---|---|
| Which feature did you primarily use? | Multiple choice | ✅ Yes | Book Cylinder, Supply Chain Tracking, Subsidy View, Blockchain Ledger, Metrics Dashboard |
| How many times did you use the product? | Multiple choice | ✅ Yes | First time (1), 2-3 times, 4-5 times, 5+ times |
| Did you successfully complete a testnet transaction? | Multiple choice | ✅ Yes | Yes / No / I tried but got an error |
| Transaction Hash (if completed — from Stellar Explorer) | Paragraph | No | — |

---

### Section 3: Product Feedback

| Field | Type | Required |
|---|---|---|
| What did you like most about GasChain? | Paragraph | ✅ Yes |
| What was confusing or difficult to use? | Paragraph | ✅ Yes |
| What should we improve or change? | Paragraph | No |
| What new feature would you like to see next? | Paragraph | No |

---

### Section 4: Rating

| Field | Type | Required | Scale |
|---|---|---|---|
| Overall product rating | Linear scale | ✅ Yes | 1 (Poor) to 5 (Excellent) |
| Wallet connection experience | Linear scale | No | 1 to 5 |
| Ease of completing a booking | Linear scale | No | 1 to 5 |

---

### Section 5: Consent

Add a **Checkbox** field at the bottom:
> ☐ I consent to my feedback being used to improve GasChain and as evidence for the RiseIn Stellar Level 5 submission. My wallet address and email may be visible to evaluators.

Make this **Required**.

---

## Step 3: Set Sharing Settings

1. Click the **Send** button (top right)
2. Click the **link icon** (chain link)
3. Check **"Shorten URL"**
4. Click **Copy**
5. Share this URL with all testers

---

## Step 4: Export Responses to Excel/Sheets

### Automatic Google Sheets Export:
1. Open your form
2. Click the **Responses** tab
3. Click the **green Sheets icon** (Create Spreadsheet)
4. Choose "Create a new spreadsheet"
5. Click **Create**
6. This auto-populates responses in real-time

### Manual Excel Export:
1. In the Responses tab → click **⋮ (More options)**
2. Click **Download responses (.csv)**
3. Open CSV in Excel → **Save As → Excel Workbook (.xlsx)**
4. Copy data into `docs/user-feedback.xlsx` Sheet 1 (matching column schema)

---

## Step 5: Make the Spreadsheet Public for README Link

1. Open the Google Sheet with responses
2. Click **Share** (top right)
3. Under "General access" → change to **Anyone with the link**
4. Set permission to **Viewer**
5. Click **Copy link**
6. Add this link to README.md in the "User Feedback Data" section

---

## Step 6: Link in README

Open `README.md` and update the feedback section:

```markdown
## 📊 User Feedback Data

| Resource | Link |
|---|---|
| Google Form (Active) | [Submit Feedback](https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform) |
| Live Response Sheet | [View Responses (Public)](https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit) |
| Excel Download | [user-feedback.xlsx](./docs/user-feedback.xlsx) |
```

---

## 🔗 Existing Form Links

| Resource | URL |
|---|---|
| Current Google Form | https://docs.google.com/forms/d/e/1FAIpQLSeEEkw9WKm8rf73X4fk0EcvWSQWT8G3TvID-9w_82UFZOEj2w/viewform |
| Existing Response Sheet | https://docs.google.com/spreadsheets/d/1EUd0swodawwLFv8Btvce9rkJ55qmvpYR-9wI3NWukZw/edit |

> ⚠️ Verify the existing form is still accepting responses and has NOT been closed.
> If it is closed, create a new form following Steps 1-4 above.
