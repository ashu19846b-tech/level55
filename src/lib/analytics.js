/**
 * GasChain Telemetry & Event Analytics Module
 * Privacy-first event tracker for Stellar testnet user flows, onboarding steps,
 * wallet lifecycle, and transaction conversions.
 */

// Event catalog definition
export const ANALYTICS_EVENTS = {
  PAGE_VIEW: 'page_view',
  ONBOARDING_STARTED: 'onboarding_started',
  ONBOARDING_COMPLETED: 'onboarding_completed',
  WALLET_CONNECT_ATTEMPT: 'wallet_connect_attempt',
  WALLET_CONNECTED: 'wallet_connected',
  WALLET_CONNECT_FAILED: 'wallet_connect_failed',
  WALLET_DISCONNECTED: 'wallet_disconnected',
  FEATURE_USED: 'feature_used',
  BOOKING_INITIATED: 'booking_initiated',
  TX_SIGN_PROMPT: 'tx_sign_prompt',
  TX_SUBMITTED: 'tx_submitted',
  TX_SUCCESS: 'tx_success',
  TX_FAILED: 'tx_failed',
  FEEDBACK_MODAL_OPENED: 'feedback_modal_opened',
  FEEDBACK_SUBMITTED: 'feedback_submitted',
};

// In-memory event buffer for session analysis
const sessionEvents = [];

/**
 * Track user interaction event
 * @param {string} eventName - Standardized event name from ANALYTICS_EVENTS
 * @param {Object} properties - Metadata properties (wallet, feature, duration, status)
 */
export function trackEvent(eventName, properties = {}) {
  const eventPayload = {
    event: eventName,
    properties: {
      ...properties,
      timestamp: new Date().toISOString(),
      url: window.location.pathname,
      screenResolution: `${window.innerWidth}x${window.innerHeight}`,
      network: 'stellar_testnet',
    },
  };

  sessionEvents.push(eventPayload);

  // Send to Plausible custom event if available
  if (typeof window !== 'undefined' && window.plausible) {
    try {
      window.plausible(eventName, { props: properties });
    } catch (e) {
      console.debug('[Analytics Plausible]', e);
    }
  }

  // Console logging in development mode
  if (import.meta.env.DEV) {
    console.log('[Telemetry]', eventName, properties);
  }

  // Persist locally for session telemetry view in ledger dashboard
  try {
    const stored = JSON.parse(sessionStorage.getItem('gaschain_telemetry') || '[]');
    stored.push(eventPayload);
    if (stored.length > 100) stored.shift();
    sessionStorage.setItem('gaschain_telemetry', JSON.stringify(stored));
  } catch (e) {
    // Ignore storage quota errors
  }
}

/**
 * Retrieve session telemetry history
 * @returns {Array} List of logged events
 */
export function getSessionEvents() {
  try {
    return JSON.parse(sessionStorage.getItem('gaschain_telemetry') || '[]');
  } catch (e) {
    return sessionEvents;
  }
}
