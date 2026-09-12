import { useState } from 'react';
import { Copy, Check } from 'lucide-react';

/**
 * CopyButton -- One-click copy to clipboard with visual success feedback.
 * Used for wallet addresses, contract IDs, transaction hashes.
 * Implemented based on user feedback: 'No easy way to copy long addresses'
 * See: docs/FEEDBACK_IMPLEMENTATION.md
 */
export default function CopyButton({ text, label = 'Copy', className = '' }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    if (!text) return;
    try {
      await navigator.clipboard.writeText(text);
    } catch {
      const el = document.createElement('textarea');
      el.value = text;
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
    <button
      id={'copy-btn-' + label.toLowerCase().replace(/\s+/g, '-')}
      onClick={handleCopy}
      title={copied ? 'Copied!' : 'Copy ' + label}
      aria-label={copied ? 'Copied to clipboard' : 'Copy ' + label + ' to clipboard'}
      className={[
        'inline-flex items-center gap-1.5 px-2 py-1 rounded-md text-xs font-medium',
        'transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-primary/40',
        copied
          ? 'bg-green-500/10 text-green-400 border border-green-500/30'
          : 'bg-muted/40 text-muted-foreground hover:bg-muted/70 hover:text-foreground border border-border/40',
        className,
      ].join(' ')}
    >
      {copied ? (
        <>
          <Check className=h-3 w-3 />
          <span>Copied!</span>
        </>
      ) : (
        <>
          <Copy className=h-3 w-3 />
          <span>{label}</span>
        </>
      )}
    </button>
  );
}
