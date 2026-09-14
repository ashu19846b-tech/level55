# 📈 ANALYTICS SETUP — GasChain

> This document describes the complete analytics implementation for GasChain, covering both Plausible (privacy-first external analytics) and the custom in-app telemetry module.

---

## 1. Plausible Analytics (External)

### Configuration
Plausible is integrated via a `<script>` tag in `index.html`:

```html
<script async defer data-domain="level6-2mgt.vercel.app"
  src="https://plausible.io/js/plausible.js"></script>
```

### What Plausible Tracks (Automatic)
- Page views and unique visitors
- Traffic sources (referrers)
- Browser, device, OS
- Country / region of users
- Session duration

### Custom Event Tracking via Plausible
The `analytics.js` module sends named custom events to Plausible when `window.plausible` is available:

```javascript
window.plausible('wallet_connected', { props: { wallet: 'G...' } });
```

### Dashboard
- **URL**: https://plausible.io/level6-2mgt.vercel.app
- **Access**: Private — login required (account owner only). Export screenshots for submission evidence.

---

## 3. SPA Route-Change Tracking (`App.jsx`)

Plausible's script auto-tracks the initial hard page load. For client-side React Router navigations, a `PlausiblePageTracker` component is mounted inside the Router in `App.jsx`:

```jsx
function PlausiblePageTracker() {
  const location = useLocation();
  useEffect(() => {
    if (typeof window.plausible === 'function') {
      window.plausible('pageview');
    }
  }, [location.pathname]);
  return null;
}
```

This ensures every route change (`/dashboard`, `/book`, `/bookings`, `/supply-chain`, etc.) is recorded as a pageview in Plausible.

---

## 2. Custom In-App Telemetry (`src/lib/analytics.js`)

### Implementation
The `analytics.js` module provides a unified `trackEvent()` function used throughout the app:

```javascript
import { trackEvent, ANALYTICS_EVENTS } from '@/lib/analytics';

// Example usage in BookCylinder.jsx
trackEvent(ANALYTICS_EVENTS.TX_SUCCESS, {
  feature: 'book_cylinder',
  wallet: publicKey,
  amount: hashEstimate
});
```

### Full Event Catalog

| Event Name | Constant | When Fired |
|---|---|---|
| `page_view` | `PAGE_VIEW` | On any page navigation |
| `onboarding_started` | `ONBOARDING_STARTED` | Landing → App transition |
| `onboarding_completed` | `ONBOARDING_COMPLETED` | First booking flow complete |
| `wallet_connect_attempt` | `WALLET_CONNECT_ATTEMPT` | Connect button clicked |
| `wallet_connected` | `WALLET_CONNECTED` | Freighter returns public key |
| `wallet_connect_failed` | `WALLET_CONNECT_FAILED` | Freighter returns error |
| `wallet_disconnected` | `WALLET_DISCONNECTED` | User disconnects wallet |
| `feature_used` | `FEATURE_USED` | Any main feature interaction |
| `booking_initiated` | `BOOKING_INITIATED` | Book Cylinder form started |
| `tx_sign_prompt` | `TX_SIGN_PROMPT` | Freighter signing popup shown |
| `tx_submitted` | `TX_SUBMITTED` | Transaction sent to Horizon |
| `tx_success` | `TX_SUCCESS` | Transaction confirmed on ledger |
| `tx_failed` | `TX_FAILED` | Transaction failed/rejected |
| `feedback_modal_opened` | `FEEDBACK_MODAL_OPENED` | Feedback modal opened |
| `feedback_submitted` | `FEEDBACK_SUBMITTED` | User submitted feedback form |

### Session Storage Buffer
Events are stored in `sessionStorage` under key `gaschain_telemetry` (max 100 events):
```javascript
const events = JSON.parse(sessionStorage.getItem('gaschain_telemetry') || '[]');
```

This enables session replay analysis and debugging during user tests.

---

## 3. How to Capture Analytics Evidence for Submission

### Plausible Dashboard Screenshots
1. Visit: https://plausible.io/level6-2mgt.vercel.app
2. Select date range: September 1–30, 2026
3. Screenshot showing:
   - Total page views
   - Unique visitors
   - Countries
   - Top pages
4. Save to `public/screenshots/analytics-september.png`

### Stellar Expert Activity Screenshots
1. Visit contract page: https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R
2. Screenshot the contract invocations list showing September dates
3. Save to `public/screenshots/contract-activity-september.png`

---

## 4. Monitoring

### Transaction Error Monitoring
All failed transactions are caught in `src/lib/freighter.js` and:
- Logged to console with `console.error()`
- Shown to user via `toast({ variant: "destructive" })`
- Tracked via `trackEvent(ANALYTICS_EVENTS.TX_FAILED, { error: codes })`

### CI/CD Monitoring
- GitHub Actions workflow runs on every push to `main`
- Sends email notification on build failure
- Vercel auto-deploys only on successful CI

---

## 📁 Related Documents

- [ACTIVE_USAGE.md](./ACTIVE_USAGE.md) — Active usage evidence
- [EVIDENCE_CHECKLIST.md](./EVIDENCE_CHECKLIST.md) — Screenshots required
