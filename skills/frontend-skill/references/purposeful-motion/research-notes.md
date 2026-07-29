# React Purposeful Motion Research Notes

Refreshed on 2026-07-28.

## Primary Principles

- Motion should communicate causality and hierarchy, not decorate.
- Choreography should show relationship and sequence across elements.
- Keep transitions quick enough to preserve flow while still legible.
- Align motion behavior with user preference for reduced motion.

## Practical Timing Guidance

Use these ranges as defaults, then tune by context:
- Micro feedback: 120-180ms.
- Enter transitions: 180-260ms.
- Exit transitions: 140-220ms.
- Shared-element/layout continuity: 220-320ms.
- Desktop UI interactions are often shorter than mobile.
- Avoid long transitions without clear narrative purpose.

## React Stack Recommendations

- Motion for React: best default for component-level and layout-aware motion.
- React Transition Group: minimal dependency path for CSS class enter/exit flows.
- react-spring: strong when physics and gesture continuity are central.
- GSAP: strongest for advanced timeline orchestration and scroll storytelling.
- React ViewTransition: available only in React Canary and Experimental
  channels in the official React reference. Next.js may supply a compatible
  React channel through its App Router, but its integration remains
  experimental and must be verified against the installed Next.js version.

## Accessibility Requirements

- Support `prefers-reduced-motion` for non-essential movement.
- Prefer opacity/fade/instant alternatives for reduced motion mode.
- Keep user-triggered motion suppressible unless essential to function.
- Ensure motion never hides critical state changes from assistive patterns.

## Performance Rules

- Prefer `transform` + `opacity`; avoid layout-heavy property animation.
- Prevent animation from masking slow rendering work.
- Use React `useTransition` to keep interaction responsive during non-urgent updates.
- Use Motion `LazyMotion` where bundle size matters.

## Library-Specific Notes

- Motion: `AnimatePresence`, `layout/layoutId`, `variants`, `MotionConfig`, `useReducedMotion`.
- GSAP + React: use `useGSAP()` and context-safe patterns to avoid cleanup issues.
- React Transition Group: `TransitionGroup` + CSS transitions for low-complexity needs.
- react-spring: `useSpring`, `useTransition`, `useTrail` for physical motion systems.

## Sources

- https://motion.dev/docs/react-animate-presence
- https://motion.dev/docs/react-layout-animations
- https://motion.dev/docs/react-animation
- https://motion.dev/docs/react-transitions
- https://motion.dev/docs/react-motion-config
- https://motion.dev/docs/react-accessibility
- https://motion.dev/docs/react-use-reduced-motion
- https://motion.dev/docs/react-reduce-bundle-size
- https://motion.dev/docs/react-lazy-motion
- https://react.dev/reference/react/useTransition
- https://react.dev/reference/react/ViewTransition
- https://react.dev/reference/react/StrictMode
- https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Animation_performance_and_frame_rate
- https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- https://developer.chrome.com/docs/web-platform/view-transitions
- https://react-spring.dev/docs/getting-started
- https://reactcommunity.org/react-transition-group/transition-group/
- https://gsap.com/resources/React/
