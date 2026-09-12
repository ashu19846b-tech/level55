import * as React from 'react';

const Dialog = ({ open, onOpenChange, children }) => {
  if (!open) return null;
  return (
    <div role='dialog' aria-modal='true' className='fixed inset-0 z-50 flex items-center justify-center'>
      <div className='fixed inset-0 bg-black/60 backdrop-blur-sm' onClick={() => onOpenChange && onOpenChange(false)} aria-hidden='true' />
      <div className='relative z-10 w-full max-w-lg'>{children}</div>
    </div>
  );
};

const DialogContent = React.forwardRef(({ className = '', children, ...props }, ref) => (
  <div ref={ref} className={'relative mx-4 rounded-2xl border border-border/60 bg-background p-6 shadow-2xl ' + className} {...props}>
    {children}
  </div>
));
DialogContent.displayName = 'DialogContent';

const DialogHeader = ({ className = '', ...props }) => (
  <div className={'flex flex-col space-y-1.5 mb-4 ' + className} {...props} />
);

const DialogTitle = React.forwardRef(({ className = '', ...props }, ref) => (
  <h2 ref={ref} className={'text-lg font-semibold leading-none tracking-tight ' + className} {...props} />
));
DialogTitle.displayName = 'DialogTitle';

const DialogDescription = React.forwardRef(({ className = '', ...props }, ref) => (
  <p ref={ref} className={'text-sm text-muted-foreground ' + className} {...props} />
));
DialogDescription.displayName = 'DialogDescription';

export { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription };
