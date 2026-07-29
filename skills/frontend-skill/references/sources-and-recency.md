# Frontend sources and recency

## Compiled knowledge snapshot

This skill was refreshed on 2026-07-28.

Current package versions observed during the refresh:

```text
animejs: 4.5.0
react: 19.2.8
next: 16.2.12
```

These are research snapshot values, not recommended project versions. Always
inspect the target repository before choosing an API or proposing an upgrade.

## Source priority

Use evidence in this order:

1. the active repository's instructions, product truth, package manifest,
   lockfile, imports, configuration, and tests;
2. the locally installed package, exported types, framework source, and a
   focused build or runtime check;
3. official documentation for the exact installed version;
4. current official documentation for an explicit upgrade proposal;
5. standards bodies and browser documentation for platform behavior;
6. reputable secondary guidance for discovery or an additional review lens.

When sources disagree, the local package and focused proof determine what code
is available in the project. The official documentation for the installed
version determines the intended contract. Record unresolved documentation,
type, runtime, or browser conflicts instead of silently choosing the newest
example.

## Current official source map

### Accessibility and browser platform

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions)
- [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion)
- [Chrome View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions)

### Anime.js

- [Anime.js documentation](https://animejs.com/documentation/)
- [Module imports](https://animejs.com/documentation/getting-started/module-imports/)
- [React integration](https://animejs.com/documentation/getting-started/using-with-react/)
- [Scope](https://animejs.com/documentation/scope/)
- [Layout](https://animejs.com/documentation/layout/)

### React and Next.js

- [React ViewTransition](https://react.dev/reference/react/ViewTransition)
- [React addTransitionType](https://react.dev/reference/react/addTransitionType)
- [Next.js View Transition configuration](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition)
- [Next.js useRouter](https://nextjs.org/docs/app/api-reference/functions/use-router)
- [Next.js 16.2 release](https://nextjs.org/blog/next-16-2)

## Known current conflicts

React's official reference labels `<ViewTransition>` and
`addTransitionType` as Canary or Experimental. Next.js 16 uses a React Canary
line in the App Router and exposes experimental integration behind
`experimental.viewTransition`.

Next.js documentation may differ across the configuration reference, component
reference, release notes, and the installed package about navigation transition
types. Verify the installed `next/link` and router types, App Router scope,
configuration, and runtime behavior before using `transitionTypes`.

## Implementation receipt

For version-sensitive work, record:

```text
Framework and version:
Relevant library versions:
Installed API or type evidence:
Browser and version:
Feature stability: stable, experimental, canary, or local-only
Official source URLs:
Sources retrieved on:
Focused build or runtime proof:
Fallback or reduced-motion behavior:
Conflict and resolution:
```

## Offline mode

When current documentation is unavailable, inspect the local package,
configuration, lockfile, imports, type declarations, and existing tests. Run the
focused build or runtime check available in the repository. Label
recency-sensitive conclusions `local-only`, avoid upgrades based on memory, and
do not claim universal browser or framework support.
