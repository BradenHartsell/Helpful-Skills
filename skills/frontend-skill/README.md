# Frontend Experience Design and Engineering

**Skill ID:** `frontend-skill`

**Compiled:** 2026-07-28

**Knowledge snapshot:** Current frontend accessibility, browser, React,
Next.js, and anime.js guidance, with version-sensitive APIs clearly marked

Design, build, review, debug, and polish websites, product interfaces, and
interactive prototypes as coherent user experiences. This skill coordinates
visual design, information hierarchy, responsive behavior, accessibility,
truthful UI state, motion, frontend implementation, and validation.

## What it helps with

- product interfaces, websites, landing pages, and interactive prototypes;
- visual theses, content hierarchy, design tokens, and design systems;
- phone, tablet, small-laptop, desktop, zoom, and breakpoint behavior;
- semantic HTML, keyboard access, focus, contrast, readable type, and touch;
- loading, empty, error, success, transient, expanded, and mobile-only states;
- purposeful motion, layout stability, reduced motion, and animation cleanup;
- anime.js v4, React View Transitions, and Next.js integration when installed;
- evidence-based UI reviews and browser validation.

## Use it when

Example requests include:

- "Design and build a distinctive landing page for this product."
- "Audit this web app for accessibility and responsive problems."
- "Polish this interface without changing its approved behavior."
- "Add purposeful motion and reduced-motion behavior."
- "Fix layout shifts and unstable loading states."
- "Implement React View Transitions if this project supports them."

## Portable by design

The core skill does not require Context7, an MCP server, a browser automation
product, a hosted service, a particular framework, or an internet connection.
It uses the active repository and locally installed packages first.

When current documentation is available, the skill uses primary sources to
refresh version-sensitive guidance. When it is offline, it relies on local
manifests, lockfiles, type declarations, builds, tests, and runtime evidence,
then labels recency-sensitive conclusions as local-only.

Interactive browser access improves visual proof but is not a loading
requirement. Without it, the skill runs available checks, provides the exact
manual validation matrix, and avoids claiming that the experience was visually
verified.

## Install or load

Copy the complete `frontend-skill` directory into your agent's skills location,
or configure the agent to read [`SKILL.md`](SKILL.md) directly. Keep
[`references/`](references/) beside it because the main workflow routes into
those files as needed.

The [`agents/openai.yaml`](agents/openai.yaml) file is optional interface
metadata. Agents that do not use that format can ignore it.

If your agent supports named invocation, use `frontend-skill`.

## How it works

The skill begins by reading the active product and repository truth. It then
creates a visual thesis, content plan, interaction thesis, and complete
user-visible state matrix before selecting layout or motion mechanisms.

The main workflow stays compact. Specialist references are loaded only when the
task needs detailed anime.js, purposeful motion, React View Transition, or
frontend quality guidance.

## Package contents

| File or directory | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Main design, implementation, review, and validation workflow |
| [`references/frontend-quality-standards.md`](references/frontend-quality-standards.md) | Cross-project frontend quality gates |
| [`references/animejs/`](references/animejs/) | anime.js v4 animation, scope, layout, SVG, text, timeline, drag, scroll, migration, and performance guidance |
| [`references/purposeful-motion/research-notes.md`](references/purposeful-motion/research-notes.md) | Motion purpose, timing, accessibility, and library selection |
| [`references/react-view-transitions/`](references/react-view-transitions/) | React and Next.js View Transition patterns, CSS recipes, implementation, and troubleshooting |
| [`references/sources-and-recency.md`](references/sources-and-recency.md) | Source precedence, exact refresh date, known conflicts, and offline behavior |
| [`agents/openai.yaml`](agents/openai.yaml) | Optional interface metadata |

## Current version gates

The 2026-07-28 refresh observed anime.js 4.5.0, React 19.2.8, and Next.js
16.2.12. These are research snapshot values, not upgrade recommendations.

React's `<ViewTransition>` and `addTransitionType` remain Canary or Experimental
in React's official documentation. Next.js View Transition integration remains
experimental. The skill requires installed package, type, configuration, and
runtime evidence before using these APIs.

## Validation performed

- passed the skill structural validator;
- passed the repository catalog and internal-link validator;
- refreshed anime.js, React, Next.js, WCAG, reduced-motion, and browser guidance
  against current primary sources on 2026-07-28;
- checked current npm package versions for anime.js, React, and Next.js;
- scanned the package for project-specific identifiers and machine paths;
- confirmed the core workflow has no required connector or hosted-service
  dependency;
- checked official source links for successful responses.

## Limits

The skill cannot prove visual quality, browser compatibility, accessibility,
performance, or production readiness without the corresponding evidence. It
does not assume a framework API is available simply because current upstream
documentation describes it.

Brand identity, product claims, user state, and approved behavior must come from
the active project. The skill never imports those facts from an unrelated
example or design reference.

## License and notice

This package is original instructional material published under the
repository's [MIT License](../../LICENSE). Third-party names and linked
documentation remain the property of their respective owners. See the
repository [NOTICE](../../NOTICE.md).
