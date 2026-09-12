import React, { useState } from 'react';
import { ExternalLink, ShieldCheck, Zap, Copy, Check } from 'lucide-react';

const CONTRACT_ID = 'CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R';

export default function TestnetBanner() {
  const [copied, setCopied] = useState(false);

  const handleCopyContract = async () => {
    try {
      await navigator.clipboard.writeText(CONTRACT_ID);
    } catch {
      const el = document.createElement('textarea');
      el.value = CONTRACT_ID;
      el.style.position = 'absolute';
      el.style.opacity = '0';
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);
    }
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="bg-gradient-to-r from-amber-500/10 via-blue-500/10 to-amber-500/10 border-b border-amber-500/20 text-xs py-1.5 px-4">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2 text-slate-300">
        <div className="flex items-center gap-2">
          <span className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-medium border border-amber-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
            Stellar Testnet Active
          </span>
          <span className="hidden md:inline text-slate-400 flex items-center gap-1.5">
            Contract: <code className="text-blue-400 font-mono">CCVUAGXS...3LN6R</code>
            <button
              id="copy-contract-address"
              onClick={handleCopyContract}
              title={copied ? 'Copied!' : 'Copy full contract address'}
              aria-label={copied ? 'Contract address copied' : 'Copy contract address'}
              className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] transition-all duration-200 border
                hover:border-blue-500/40 focus:outline-none focus:ring-1 focus:ring-blue-500/30"
              style={{
                background: copied ? 'rgba(34,197,94,0.08)' : 'rgba(148,163,184,0.08)',
                borderColor: copied ? 'rgba(34,197,94,0.3)' : 'rgba(148,163,184,0.2)',
                color: copied ? 'rgb(134,239,172)' : 'rgb(148,163,184)',
              }}
            >
              {copied ? <Check className="w-2.5 h-2.5" /> : <Copy className="w-2.5 h-2.5" />}
              {copied ? 'Copied!' : 'Copy'}
            </button>
          </span>
        </div>

        <div className="flex items-center gap-4 text-slate-400">
          <a
            href="https://lab.stellar.org/#account-creator"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-amber-300 transition-colors flex items-center gap-1"
          >
            <Zap className="w-3 h-3 text-amber-400" />
            Get Testnet XLM (Friendbot)
          </a>
          <a
            href={`https://stellar.expert/explorer/testnet/contract/${CONTRACT_ID}`}
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-blue-300 transition-colors flex items-center gap-1"
          >
            <ShieldCheck className="w-3 h-3 text-blue-400" />
            Verified Explorer
            <ExternalLink className="w-2.5 h-2.5" />
          </a>
        </div>
      </div>
    </div>
  );
}
