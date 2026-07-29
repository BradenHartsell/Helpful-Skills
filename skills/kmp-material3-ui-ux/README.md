# Kotlin Multiplatform Material 3 UI/UX Design and Engineering

- **Skill ID:** `kmp-material3-ui-ux`
- **Compiled:** 2026-07-28
- **Knowledge snapshot:** Official Material 3 and Compose Multiplatform sources reviewed through 2026-07-28

This skill helps an agent design, build, redesign, polish, or audit beautiful product interfaces made with Kotlin Multiplatform and Compose Multiplatform.

It joins visual design and implementation discipline in one workflow: Material 3 foundations, product-specific design systems, adaptive layouts, accessibility, keyboard and pointer behavior, honest UI states, motion, source-set ownership, target parity, and visual validation.

## What it is for

Use this skill for:

- new Compose Multiplatform screens and flows;
- Material 3 themes, tokens, typography, color, shape, and elevation;
- choosing and configuring Material components;
- compact, medium, expanded, and freely resized window behavior;
- list-detail, feed, and supporting-pane layouts;
- Android, iOS, desktop, and web input and accessibility planning;
- loading, empty, partial, offline, blocked, error, success, and destructive states;
- reduced motion and meaningful transitions;
- Figma or screenshot translation into maintainable Compose UI;
- cross-target implementation and parity reviews;
- visual, behavioral, and accessibility QA.

It is deliberately not a collection of copy-paste Android snippets. The skill separates Material design guidance from API availability, checks the actual repository and installed artifacts, and prevents Android-only APIs from being presented as shared KMP capabilities.

## What it does not promise

Using this skill does not by itself prove:

- that an API exists in the installed artifact or every target;
- pixel-identical rendering across operating systems and devices;
- WCAG conformance or correct native screen-reader output;
- production readiness, release readiness, or platform-store compliance;
- that the dated knowledge snapshot remains current.

The skill requires repository, build, target, and accessibility evidence before making those claims.

## Design philosophy

The skill follows five durable rules:

1. The product and repository remain the authority. Material supports the product rather than replacing its brand, navigation, state, copy, or architecture.
2. Design guidance and code availability are different facts.
3. Shared UI belongs in shared code only when its behavior and dependencies are genuinely portable.
4. A beautiful happy path is unfinished if loading, failure, resize, focus, localization, or reduced motion breaks it.
5. Semantic tokens and reusable product components are more maintainable than per-screen styling.

## No required third-party dependency

The skill requires no particular documentation service, browser plugin, companion skill, or proprietary agent feature.

It can work with:

- repository and filesystem inspection;
- ordinary source search;
- Gradle and the project's existing build tools;
- locally resolved artifacts and generated API references;
- any available way to read official documentation.

When network access is unavailable, it uses the repository and installed artifacts as local truth, labels recency-sensitive claims `[local-only]`, and avoids claiming that an API or recommendation is the latest.

## Installation

### Generic installation

Copy the complete `kmp-material3-ui-ux` directory into the skills location recognized by your agent. Keep `SKILL.md`, `agents/`, and `references/` together.

If your agent can load a skill from an arbitrary path, point it to:

```text
skills/kmp-material3-ui-ux/SKILL.md
```

### Named invocation

Agents that support named skills can invoke:

```text
$kmp-material3-ui-ux
```

The included [`agents/openai.yaml`](agents/openai.yaml) provides optional interface metadata. The core skill does not depend on that file or on a specific agent vendor.

## Example requests

```text
Use $kmp-material3-ui-ux to design an adaptive list-detail mail screen for
Android, iOS, and desktop. Separate verified shared APIs from proposals.
```

```text
Use $kmp-material3-ui-ux to audit this Compose settings screen for hierarchy,
keyboard behavior, resize failures, accessibility, and state honesty.
```

```text
Use $kmp-material3-ui-ux to translate this Figma screen into our existing KMP
theme and components without creating a second token or navigation system.
```

```text
Use $kmp-material3-ui-ux to build an accessible profile editor that remains
usable with large text, RTL content, reduced motion, and a narrow desktop window.
```

## How the skill works

The main workflow:

1. proves repository, target, theme, navigation, state, copy, and validation ownership;
2. fingerprints exact Kotlin, Compose Multiplatform, Material, artifact, target, and source-set facts;
3. defines the user job, visual thesis, content hierarchy, components, adaptive behavior, states, input, and accessibility contract;
4. loads only the references relevant to the task;
5. extends the existing design system instead of creating parallel owners;
6. implements from semantic structure through visual finish;
7. validates breakpoint edges, unhappy paths, input modes, assistive technology, themes, localization, motion preferences, and supported targets.

Every version-sensitive recommendation includes a receipt for local proof, official source URL, version scope, retrieval date or `local-only` status, and conflict resolution.

## Package contents

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Trigger boundary, portable evidence method, workflow, reference router, output contract, and quality bar |
| [`references/material3-foundations.md`](references/material3-foundations.md) | Material principles, expressive restraint, tokens, spacing, RTL, elevation, and icon guidance |
| [`references/theming-and-design-system.md`](references/theming-and-design-system.md) | Semantic theme architecture, color, typography, shape, elevation, and validation |
| [`references/compose-material3-components.md`](references/compose-material3-components.md) | Component selection and custom-component obligations |
| [`references/adaptive-layouts-and-navigation.md`](references/adaptive-layouts-and-navigation.md) | Breakpoints, transformations, panes, canonical layouts, navigation, and resize tests |
| [`references/accessibility-and-input.md`](references/accessibility-and-input.md) | Semantics, focus, keyboard, pointer, touch, screen readers, contrast, text, RTL, and platform proof |
| [`references/state-feedback-and-motion.md`](references/state-feedback-and-motion.md) | Product states, progress, feedback, motion, reduced motion, interruption, and failure |
| [`references/kmp-target-parity.md`](references/kmp-target-parity.md) | Shared versus platform ownership, API portability, resources, target differences, and testing |
| [`references/visual-qa-checklist.md`](references/visual-qa-checklist.md) | Visual, behavioral, adaptive, accessibility, state, target, and evidence review |
| [`references/sources-and-recency.md`](references/sources-and-recency.md) | Official source map, dated compatibility snapshot, and refresh procedure |

## Validation performed

Before publication, the package passed:

- skill structure validation;
- relative-link validation;
- official source URL and rendered not-found checks;
- forbidden-character and unfinished-template checks;
- a greenfield multi-target design forward test;
- a read-only audit against a real Compose desktop surface;
- a no-network, no-plugin, no-helper forward test;
- an independent environment-portability audit.

These checks validate the skill package and its instructions. They do not imply that every future UI created with the skill is automatically accessible, portable, or production-ready. Each implementation still needs evidence from its own repository and supported targets.

## Recency and maintenance

The compiled knowledge date is 2026-07-28. Material and Compose Multiplatform evolve independently, and Android APIs can appear before equivalent shared KMP support.

Before making a current API claim, follow the portable refresh process in [`references/sources-and-recency.md`](references/sources-and-recency.md). If official documentation cannot be reached, use local artifact evidence and label the result honestly.

## Sources, license, and acknowledgment

The official source map and retrieval process live in [`references/sources-and-recency.md`](references/sources-and-recency.md).

The original skill text and metadata are distributed under the repository's [MIT License](../../LICENSE). Linked Material, Android, Kotlin, Compose Multiplatform, and other third-party documentation remains governed by its respective owner. This is an independent project and is not affiliated with or endorsed by Google or JetBrains. See the repository [NOTICE.md](../../NOTICE.md).
