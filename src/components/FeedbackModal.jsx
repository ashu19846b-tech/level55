import React, { useState } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { Star, MessageSquarePlus, CheckCircle, ExternalLink } from 'lucide-react';
import { trackEvent, ANALYTICS_EVENTS } from '@/lib/analytics';
import { toast } from 'sonner';

export default function FeedbackModal({ isOpen, onClose, walletAddress = '' }) {
  const [rating, setRating] = useState(5);
  const [hoverRating, setHoverRating] = useState(0);
  const [feature, setFeature] = useState('Book Cylinder');
  const [feedback, setFeedback] = useState('');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    trackEvent(ANALYTICS_EVENTS.FEEDBACK_SUBMITTED, {
      rating,
      feature,
      wallet: walletAddress || 'not_connected',
      hasEmail: !!email,
    });

    // Store in local storage for demonstration and audit
    try {
      const existing = JSON.parse(localStorage.getItem('gaschain_user_feedbacks') || '[]');
      existing.push({
        name: name || 'Anonymous Tester',
        email: email || 'N/A',
        wallet: walletAddress || 'N/A',
        rating,
        feature,
        feedback,
        date: new Date().toISOString(),
      });
      localStorage.setItem('gaschain_user_feedbacks', JSON.stringify(existing));
    } catch (err) {
      console.error(err);
    }

    setTimeout(() => {
      setIsSubmitting(false);
      setIsSubmitted(true);
      toast.success('Thank you! Your feedback has been recorded.');
    }, 600);
  };

  const handleReset = () => {
    setIsSubmitted(false);
    setFeedback('');
    onClose();
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-md bg-slate-900 border-slate-800 text-slate-100">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2 text-lg font-semibold text-white">
            <MessageSquarePlus className="w-5 h-5 text-amber-400" />
            Product Feedback & Review
          </DialogTitle>
          <DialogDescription className="text-slate-400 text-xs">
            Help us refine the GasChain decentralized LPG protocol for Stellar Level 5.
          </DialogDescription>
        </DialogHeader>

        {isSubmitted ? (
          <div className="py-6 text-center space-y-4">
            <div className="w-12 h-12 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto">
              <CheckCircle className="w-6 h-6" />
            </div>
            <h3 className="text-base font-medium text-white">Feedback Received!</h3>
            <p className="text-xs text-slate-400 max-w-xs mx-auto">
              Your insights directly guide our smart contract updates and frontend UX optimizations.
            </p>
            <div className="pt-2">
              <Button onClick={handleReset} variant="outline" className="border-slate-700 text-slate-200">
                Close
              </Button>
            </div>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4 pt-2">
            <div>
              <Label className="text-xs text-slate-300">Rate your experience (1 to 5 Stars)</Label>
              <div className="flex items-center gap-1.5 mt-1.5">
                {[1, 2, 3, 4, 5].map((star) => (
                  <button
                    key={star}
                    type="button"
                    onClick={() => setRating(star)}
                    onMouseEnter={() => setHoverRating(star)}
                    onMouseLeave={() => setHoverRating(0)}
                    className="p-1 rounded hover:bg-slate-800 transition-colors"
                  >
                    <Star
                      className={`w-6 h-6 ${
                        (hoverRating || rating) >= star
                          ? 'text-amber-400 fill-amber-400'
                          : 'text-slate-600'
                      }`}
                    />
                  </button>
                ))}
                <span className="text-xs text-amber-400 font-semibold ml-2">
                  {rating} / 5
                </span>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-2">
              <div>
                <Label htmlFor="name" className="text-xs text-slate-300">Your Name (Optional)</Label>
                <Input
                  id="name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="e.g. Alex"
                  className="bg-slate-800/80 border-slate-700 text-xs mt-1 text-slate-100"
                />
              </div>
              <div>
                <Label htmlFor="email" className="text-xs text-slate-300">Email (Optional)</Label>
                <Input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="alex@example.com"
                  className="bg-slate-800/80 border-slate-700 text-xs mt-1 text-slate-100"
                />
              </div>
            </div>

            <div>
              <Label htmlFor="feature" className="text-xs text-slate-300">Primary Feature Used</Label>
              <select
                id="feature"
                value={feature}
                onChange={(e) => setFeature(e.target.value)}
                className="w-full mt-1 px-3 py-2 bg-slate-800/80 border border-slate-700 rounded-md text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-amber-400"
              >
                <option value="Book Cylinder">Book Cylinder (On-Chain Booking)</option>
                <option value="Supply Chain Tracking">Supply Chain Tracking</option>
                <option value="Subsidy Verification">Subsidy Calculation & Settlement</option>
                <option value="Blockchain Ledger">Blockchain Ledger Monitor</option>
                <option value="Metrics Dashboard">Metrics & Telemetry</option>
              </select>
            </div>

            <div>
              <Label htmlFor="feedback" className="text-xs text-slate-300">Feedback / Suggestions / Issues Encountered</Label>
              <Textarea
                id="feedback"
                required
                rows={3}
                value={feedback}
                onChange={(e) => setFeedback(e.target.value)}
                placeholder="What did you like? What was confusing? What feature would you like to see next?"
                className="bg-slate-800/80 border-slate-700 text-xs mt-1 text-slate-100"
              />
            </div>

            <div className="pt-2 flex items-center justify-between">
              <a
                href="https://docs.google.com/forms/d/e/1FAIpQLSeEEkw9WKm8rf73X4fk0EcvWSQWT8G3TvID-9w_82UFZOEj2w/viewform"
                target="_blank"
                rel="noopener noreferrer"
                className="text-[11px] text-blue-400 hover:text-blue-300 flex items-center gap-1"
              >
                Official Google Form
                <ExternalLink className="w-2.5 h-2.5" />
              </a>
              <div className="flex gap-2">
                <Button type="button" variant="ghost" size="sm" onClick={onClose} className="text-xs text-slate-400">
                  Cancel
                </Button>
                <Button
                  type="submit"
                  size="sm"
                  disabled={isSubmitting || !feedback.trim()}
                  className="bg-amber-500 hover:bg-amber-600 text-black font-semibold text-xs"
                >
                  {isSubmitting ? 'Submitting...' : 'Submit Feedback'}
                </Button>
              </div>
            </div>
          </form>
        )}
      </DialogContent>
    </Dialog>
  );
}
