import React from 'react';
import { ExternalLink, ShieldCheck, Zap } from 'lucide-react';

export default function TestnetBanner() {
  return (
    <div className="bg-gradient-to-r from-amber-500/10 via-blue-500/10 to-amber-500/10 border-b border-amber-500/20 text-xs py-1.5 px-4">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2 text-slate-300">
        <div className="flex items-center gap-2">
          <span className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-medium border border-amber-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse"></span>
            Stellar Testnet Active
          </span>
          <span className="hidden md:inline text-slate-400">
            Contract: <code className="text-blue-400 font-mono">CCVUAGXS...3LN6R</code>
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
            href="https://stellar.expert/explorer/testnet/contract/CCVUAGXSXDATPMZC5ZGH6G47LUM4BPZLJ2NU47BAQ5W74CMS2YX3LN6R"
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
