---
name: frontend-skill
description: Design, build, review, debug, and polish coherent frontend experiences across product interfaces, websites, and interactive prototypes. Use for visual systems, information hierarchy, responsive layouts, accessibility, UI state, motion, micro-interactions, scroll storytelling, design systems, React View Transitions, anime.js, browser validation, or any request to improve frontend UI or UX quality.
---

# Frontend Experience Design and Engineering

**Compiled knowledge:** 2026-07-28

Build interfaces as coherent systems: specific to the product, truthful in every state, stable during interaction, accessible, responsive, and verified in the browser.

## Required context

Before planning or editing:

1. Read `references/frontend-quality-standards.md` completely.
2. Read the active repository's instructions, product brief, design system, vocabulary, and nearest frontend-specific guidance.
3. Inspect the existing implementation and preserve approved behavior unless replacement is explicitly authorized.
4. If a reference is interactive, inspect the actual experience across scroll, clicks, and viewport sizes. Do not infer a system from one screenshot or loop.
5. When library or framework behavior matters, refresh current official documentation before implementation.
6. Read `references/sources-and-recency.md` before making version-sensitive library, browser, accessibility-standard, or framework claims.

Use the bundled specialist references only when relevant:

- anime.js: `references/animejs/`
- purposeful React motion: `references/purposeful-motion/research-notes.md`
- React View Transitions: `references/react-view-transitions/`
- source precedence, refresh dates, and offline behavior: `references/sources-and-recency.md`

## Current API and portability gate

1. Inspect the repository's manifest, lockfile, imports, framework configuration, and locally installed type declarations before selecting an API.
2. Treat bundled version snapshots as routing evidence, not as permission to upgrade or proof that an API exists locally.
3. React's `<ViewTransition>` and `addTransitionType` remain Canary or Experimental APIs in React's official documentation as of 2026-07-28. Use them only when the installed React or framework integration exposes them.
4. Next.js View Transition integration remains experimental. Verify the exact Next.js version, App Router usage, configuration flag, component types, and runtime behavior.
5. Anime.js references were refreshed against v4.5.0. Verify the installed version before using features marked with a minimum version.
6. Do not require a documentation connector, browser automation product, hosted service, or named third-party agent tool. Use current official sources when available and the local package plus focused build evidence when offline.

## Working model

Write these before building:

- **Visual thesis:** mood, material, brand character, and dominant visual idea in one sentence.
- **Content plan:** the job and takeaway of each section or screen.
- **Interaction thesis:** two or three interactions that improve comprehension, continuity, or control.
- **State matrix:** every user-visible state, including transient, loading, empty, error, success, expanded, and mobile-only states.

If these cannot be stated clearly, inspect the product and references further before adding components.

## Design workflow

### 1. Establish truth and hierarchy

- Identify the primary user, job, promise, and proof.
- Make each section or view do one job.
- Start product UI with the working surface; start marketing UI with a clear promise and a dominant visual.
- Preserve the active brand's own geography, history, tone, materials, and vocabulary. Never collapse it into a generic trend or clone the reference brand.
- Treat theme inspiration as mood and system guidance, not a literal layout template.

### 2. Design the responsive system

- Define shared tokens for color, type, spacing, container width, radii, borders, shadows, and motion.
- Use a small type and color system. Apply accent color to meaning, not decoration.
- Design mobile as a distinct composition where density or interaction demands it.
- Define every layout mode explicitly: phone, intermediate tablet/small-laptop, and wide desktop. Do not let the intermediate range inherit a half-mobile/half-desktop combination of display, grid, or sizing rules.
- Keep a safe band around common physical viewport widths and zoom equivalents. Browser scaling can make media queries evaluate a fractional CSS width even when `innerWidth` rounds to the breakpoint; both sides of every critical boundary must therefore remain coherent, and a one-pixel miss must never expose an unusable composition.
- When a breakpoint reveals or hides a grid/flex child, explicitly place every remaining sibling for that mode. Never rely on auto-placement when a newly visible tab bar, rail, or control can push the primary surface into an implicit row or narrow track.
- Establish one section rhythm instead of stacking unrelated top and bottom margins.
- Budget fixed headers against the initial viewport and anchored destinations.
- Prefer reflow, state switching, or progressive disclosure over inner scroll regions.

### 3. Design truthful interaction

- Ensure every control changes a real state and every visible state agrees with the product model.
- Remove dead controls and staged inputs that imply unavailable behavior.
- Keep sent data out of cleared composers; acknowledge already-present files and context.
- Label examples, defaults, customization, automation, memory, and permissions accurately.
- Keep the outer interaction surface stable while content changes inside it.
- Plan unhappy paths: rapid repeated input, long content, narrow screens, missing data, errors, interruption, and reduced motion.

### 4. Choose motion deliberately

Every animation must communicate one of:

- feedback
- continuity
- hierarchy
- focus
- status

If it communicates none of these, remove it.

Use the lightest suitable mechanism:

| Need | Preferred mechanism |
|---|---|
| Hover, focus, press, simple reveal | CSS transitions/keyframes |
| React mount/unmount and shared layout | Motion or framework-native transition |
| Native shared-element route/state continuity | React View Transitions |
| Framework-agnostic timelines, SVG, text, or FLIP | anime.js |
| Complex pinned scroll choreography | GSAP when justified |

Defaults:

- Micro feedback: 120-180ms.
- State mutation: 180-260ms.
- Shared/layout continuity: 220-320ms.
- Prefer opacity and transform.
- For necessary height changes, measure old and new bounds, keep the top edge anchored, and animate a bounded transition.
- Respect `prefers-reduced-motion`; reduced motion must preserve information and state.
- Tune scroll-linked timing separately for mobile and desktop, with enough dwell time to read.

### 5. Implement as a system

- Reuse existing tokens, primitives, and semantic structures.
- Keep DOM order, focus order, and visual order aligned.
- Use semantic HTML, visible focus, proper labels, and accessible names.
- Reserve predictable space for async or mutating content.
- Avoid fixed tallest-state shells when they create large empty mobile regions; stabilize the mutable subregion instead.
- Keep controls reachable and content readable without horizontal page scrolling or unintended card/bubble scrollbars.
- Clean up animation scopes, observers, event listeners, and inline styles.

## Stable mutation patterns

Choose in this order:

1. **Normalize the mutable region:** equalize predictable copy, media, controls, and status areas.
2. **Overlay exclusive states:** place mutually exclusive panels in the same grid area and crossfade them.
3. **Reserve local space:** set a sensible minimum on the internal region, not the entire section.
4. **Use shared layout or FLIP:** preserve spatial continuity when elements genuinely move.
5. **Animate measured height:** only when content must change the outer dimension; anchor the top and avoid viewport jumps.
6. **Progressively disclose exceptional detail:** keep the primary state compact without hiding required information.

Never allow a transient state to collapse a finished card and expand it again. Never hide instability behind a decorative animation.

## Accessibility and readability gates

- Meet WCAG contrast for text and controls; atmosphere is not an exception.
- Use at least 16px body text on mobile unless a clearly readable product convention justifies otherwise.
- Keep body line height roughly 1.5-1.75 and line length near 45-75 characters.
- Maintain comfortable separation between adjacent lines, labels, and controls at real wrap points.
- Use minimum 44x44px touch targets for primary mobile interactions.
- Provide keyboard access and visible focus for every control.
- Do not rely on color alone for state.
- Give meaningful images useful alt text and decorative images empty alt text.
- Preserve functionality with reduced motion, zoom, long text, and narrow viewports.

## Review workflow

Apply `references/frontend-quality-standards.md` first. When network access is available, optionally cross-check current primary platform guidance and the public Web Interface Guidelines:

`https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`

Treat external review checklists as supplementary evidence, not as a required dependency or authority over the active product, repository, accessibility standard, or installed framework.

Report findings with evidence: file and line, affected viewport/state, user impact, and the smallest systemic fix. Prioritize accessibility failures, content/state contradictions, overflow, layout shift, blocked interaction, and mobile abandonment points over ornamental preferences.

## Validation evidence

Before handoff:

1. Build the real page and inspect it visually.
2. Exercise every state-changing control, not only the default state.
3. Test the responsive viewport matrix: a narrow phone, a representative phone, every layout-changing breakpoint at one pixel below and above, an intermediate tablet/small-laptop viewport, and a normal desktop. Include a short laptop height and a tall tablet height. Treat browser zoom as a reduced CSS viewport and verify at least one 125% or 150% equivalent when the layout is dense.
   - At each critical boundary, record the actual CSS viewport, document client width, device pixel ratio, and whether the intended media query matched. Do not infer query activation from a rounded `innerWidth` or screenshot dimensions.
   - Verify the composition on both sides of the boundary even when the query intentionally has a safe gap. A layout is not robust if it depends on the breakpoint firing at an exact common device width.
4. At every layout mode, inspect the computed grid/flex geometry for the primary surface. Confirm newly shown controls do not create implicit rows or columns, no content is squeezed into a leftover track, and the content order remains intentional.
5. Measure stage/card dimensions before, during, and after mutations.
6. Confirm zero unintended horizontal overflow and zero unwanted inner scrollbars.
7. Follow anchor links and verify fixed navigation does not cover the destination.
8. Check transient timing, readable dwell, clipping, text wrapping, contrast, focus, and tap targets.
9. Test reduced motion.
10. Verify visible copy, attachments, inputs, status, results, and controls are mutually consistent.
11. Recheck earlier approved behavior after the latest correction.
12. For multi-section marketing pages, visit every anchored scene at each layout mode; a passing hero and zero page overflow do not prove that below-fold grids, fixed-header clearance, or interactive panels are responsive. Add an executable repository contract for critical breakpoint, placement, anchor, and artwork invariants when the project has a validation gate.

Do not call a UI polished from a static screenshot alone.

If interactive browser access is unavailable, run every available static, build, unit, accessibility, and layout-contract check. Provide the exact manual viewport and interaction matrix still required, and label visual, runtime, and assistive-technology claims unverified. Limited tools reduce the proof boundary, not the quality standard.

## Handoff

Lead with the resulting experience, then summarize:

- what changed visually and behaviorally
- how responsive and mutation stability were handled
- accessibility and motion behavior
- browser states and viewports verified
- validation run
- what was deliberately preserved
