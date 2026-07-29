---
name: kmp-material3-ui-ux
description: Design, implement, redesign, polish, or audit beautiful Material 3 user interfaces in Kotlin Multiplatform and Compose Multiplatform. Use for KMP screens, themes, design systems, component selection, adaptive layouts, desktop or mobile input, accessibility, UI state presentation, motion, screenshot or Figma translation, and cross-target visual parity. Use when the task must turn product intent into maintainable Compose UI while respecting the repository's existing theme, navigation, state, copy, source-set, and platform owners.
---

# Kotlin Multiplatform Material 3 UI/UX Design and Engineering

Build interfaces that feel intentional, clear, accessible, and native to the product. Treat Material 3 as a design language and toolkit inside the repository's product system, not as permission to replace local ownership or produce generic sample-app UI.

**Compiled knowledge:** 2026-07-28

## Contents

- Core law
- Portable evidence method
- Seven-step workflow
- Reference routing
- Output contract
- Quality bar

## Core law

1. Local product and architecture authority wins. Read the applicable `AGENTS.md`, design docs, theme owner, component library, copy owner, navigation owner, state owner, and validation gates before proposing a new system.
2. Design guidance and API availability are separate facts. Verify the exact installed Compose Multiplatform and Material 3 versions, targets, artifacts, and source sets before naming an API.
3. Share product behavior, semantic presentation models, resources, and portable UI where they truly change together. Keep platform integration behind narrow platform-owned seams.
4. Beauty cannot come at the cost of comprehension, accessibility, state honesty, or unhappy-path behavior.
5. Prefer a small coherent system of semantic tokens, reusable components, and explicit layout policies over per-screen styling.

## Portable evidence method

This skill has no required plugin, documentation index, helper skill, or vendor-specific tool. It must work with ordinary file inspection, repository search, the project's build tool, and any available way to read official web documentation.

Use local evidence first:

1. inspect `settings.gradle` or `settings.gradle.kts`, module build files, version catalogs, lockfiles, and source-set directories;
2. record exact declared and resolved versions, targets, artifacts, and source-set placement;
3. search local source, dependency caches, generated API references, and existing imports when available;
4. run a focused dependency report, compilation, or test for the intended target when the task permits it.

Use official documentation for current intent and supported target claims. Any browser, search tool, HTTP client, or supplied documentation snapshot is acceptable. A third-party documentation index may help discovery when available, but it is never required and is never sole proof.

If the environment has no network access:

- use the installed artifact and repository as current local truth;
- label recency-dependent claims `[local-only]`;
- do not claim that a version, API, or recommendation is the latest;
- provide the exact official URL that should be refreshed later when known.

Optional environment-specific helper skills may accelerate stack discovery, source-set analysis, navigation review, or platform review. The workflow below remains complete without them.

## Choose the task mode

- **Design-only:** no repository is available. Produce a product and implementation proposal, label every stack and owner statement as assumed, and separate product questions from design decisions.
- **Read-only audit:** inspect only the scoped authority needed to understand the target surface. Do not edit. Distinguish source findings from runtime observations and recommend checks without claiming they ran.
- **Implementation:** follow the complete workflow, use failing owner-level tests for correctness changes, and complete the repository's focused and final gates.
- **Visual translation:** when given Figma, a screenshot, or another reference, extract hierarchy, rhythm, component semantics, interaction, and brand intent. Do not copy pixels blindly or assume the reference covers state, accessibility, resize, or target behavior.

Use evidence labels when the distinction matters:

- `[assumed]`: design-only or unresolved input;
- `[source-inspected]`: supported by files or documentation;
- `[compiled]`: proved by the named compilation;
- `[automated-test]`: proved by the named test;
- `[observed]`: manually seen in a named target, window, input mode, or assistive technology.

## Workflow

### 1. Establish local authority

For repository work:

1. Prove the repository and worktree identity.
2. Read every applicable `AGENTS.md` from root to the files in scope.
3. Inspect the dirty tree and preserve unrelated user-owned work.
4. Locate:
   - build files, version catalogs, targets, and source-set topology;
   - the theme, token, component, icon, typography, and resource owners;
   - navigation, window-size, state, copy, analytics, and accessibility owners;
   - product vocabulary and brand guidance;
   - previews, screenshot tests, UI tests, pure policy tests, and final repo gates.
5. Reuse the existing owner when one exists. Do not create a parallel theme, breakpoint table, component library, or state vocabulary.
6. Ask one explicit audit question: does this surface consume the established layout policy, or is its fixed behavior intentional and documented?

For a read-only audit, stop discovery when these scoped owners are proved. Do not traverse unrelated targets, modules, or test systems merely to complete a checklist.

### 2. Fingerprint the implementation surface

Record:

- Kotlin, Compose Multiplatform, Material 3, and adaptive library versions;
- actual targets, not aspirational targets;
- available artifacts in each source set;
- windowing, input, navigation, resource, and testing APIs already in use;
- local minimum target sizes, breakpoints, density rules, and reduced-motion policy;
- target-specific accessibility tooling.

If a recommended API is absent from the installed artifacts, choose one of three honest outcomes:

1. implement the behavior with stable portable primitives;
2. place the behavior behind an existing platform seam;
3. propose a dependency upgrade separately, with migration and target evidence.

Never invent a symbol, silently add a dependency, or imply that Android availability means `commonMain` availability.

When sources conflict:

1. the repository's canonical owners decide product and architecture ownership;
2. the resolved installed artifact plus focused compilation decide whether code is currently available;
3. official documentation for the exact installed version explains intended support;
4. current official documentation informs an upgrade proposal, not current availability;
5. design guidance and roadmap announcements inform direction, not library symbols.

If conflict remains, report it instead of silently choosing the newest-looking source.

Record this receipt for every version-sensitive recommendation:

```text
Kotlin version:
Compose Multiplatform version:
Material 3 artifact and version:
Targets and source set:
Local proof:
Official source URL:
Source version scope:
Retrieved on: YYYY-MM-DD, or local-only
Conflict and resolution:
```

### 3. Write the UI contract

For a new or substantially redesigned surface, state:

- **User job:** what the person is trying to finish.
- **Visual thesis:** one sentence describing hierarchy, density, tone, and the intended emotional quality.
- **Content hierarchy:** primary content, supporting content, primary action, secondary actions, and what stays quiet.
- **Component decisions:** why each Material or product component fits the interaction.
- **Adaptive strategy:** what reveals, divides, resizes, repositions, or swaps as the available window changes.
- **State matrix:** loading, empty, content, partial, stale, offline, blocked, error, disabled, success, and destructive states that can actually occur.
- **Input matrix:** touch, keyboard, pointer, focus traversal, screen reader, and platform back or escape behavior.
- **Ownership:** which facts belong in shared code and which integrations remain platform-owned.

Do not begin with decoration. Begin with the user job, content order, state truth, and action clarity.

### 4. Load only the relevant references

| Need | Read |
|---|---|
| Material principles, expressive restraint, layout, spacing, RTL, elevation, icons | [material3-foundations.md](references/material3-foundations.md) |
| Semantic colors, typography, shapes, theme architecture, contrast | [theming-and-design-system.md](references/theming-and-design-system.md) |
| Choosing buttons, fields, navigation, containers, feedback, and other components | [compose-material3-components.md](references/compose-material3-components.md) |
| Window classes, canonical layouts, panes, navigation adaptation, resize behavior | [adaptive-layouts-and-navigation.md](references/adaptive-layouts-and-navigation.md) |
| Semantics, focus, keyboard, pointer, screen readers, target sizes, platform testing | [accessibility-and-input.md](references/accessibility-and-input.md) |
| Interaction states, progress, feedback, reduced motion, transitions, unhappy paths | [state-feedback-and-motion.md](references/state-feedback-and-motion.md) |
| Source sets, target differences, resources, testing, and API portability | [kmp-target-parity.md](references/kmp-target-parity.md) |
| Visual, behavioral, adaptive, accessibility, and evidence review | [visual-qa-checklist.md](references/visual-qa-checklist.md) |
| Live source map, dated platform facts, and recency procedure | [sources-and-recency.md](references/sources-and-recency.md) |

Fast paths:

- Greenfield screen: foundations, theming, components, adaptive, accessibility, state, target parity, then QA.
- Focused visual audit: foundations plus only the implicated theming, component, adaptive, accessibility, or state references, then QA.
- Component or theme work: theming, components, accessibility, and state.
- Cross-target parity: target parity, adaptive, and accessibility.

### 5. Design the system before the screen

Use this dependency direction:

```text
product intent
  -> semantic app tokens
  -> product components and Material component configuration
  -> screen composition
  -> platform integration
```

- Map raw palette and dimensions into purpose-named tokens.
- Configure the existing `MaterialTheme` owner rather than nesting local themes around individual screens.
- Reuse one implementation per rendered concept.
- Add a reusable component only when multiple call sites should change for the same product reason.
- Keep similar-looking components separate when their semantics or change drivers differ.
- Prefer standard Material components when they express the behavior. Custom components inherit the full state, focus, semantics, keyboard, pointer, target-size, contrast, and test obligations.
- Use one or two visually expressive moments to establish identity. Keep common controls and repeated flows quiet and predictable.

### 6. Implement from structure to finish

Work in this order:

1. semantic layout and reading order;
2. state and event wiring;
3. adaptive placement and window behavior;
4. keyboard, pointer, touch, focus, and semantics;
5. theme roles, typography, shape, and elevation;
6. feedback and motion;
7. previews, target tests, and visual polish.

For correctness or regressions, add the smallest owner-level failing test first. Keep unknown data validation at its serialization boundary. Do not put business or navigation truth inside rendering code to make a screen easier to draw.

### 7. Validate the unhappy paths

Exercise at least the states and environments the feature can encounter:

- minimum supported window and a width on both sides of each active breakpoint;
- resized desktop windows while state is active;
- long text, text scaling, localized strings, RTL, and bidirectional content;
- keyboard-only and pointer-only operation;
- screen reader labels, roles, state descriptions, focus order, and live feedback;
- dark theme, light theme, high contrast when supported, and non-color state cues;
- loading, empty, offline, partial, permission or connection blockers, retry, cancellation, destructive actions, and success;
- reduced motion and interrupted animation;
- target-specific rendering, input, resource, and accessibility behavior.

Use the repository's focused checks while iterating and its final gate before declaring completion. If visual testing infrastructure is absent, provide an honest manual evidence receipt and identify the missing automated proof.

Semantics tests prove the semantics tree and portable interactions. They do not prove real screen-reader output, native accessibility mapping, platform focus behavior, or target packaging.

## Output contract

For plans, implementations, and audits, report:

1. **Goal and local authority:** user job, product owner files, theme owner, and relevant constraints.
2. **Verified stack:** versions, targets, source sets, and artifact availability.
3. **Design direction:** visual thesis, hierarchy, components, tokens, and expressive moment.
4. **Adaptive and input behavior:** window strategy, navigation, touch, keyboard, pointer, and focus.
5. **State and accessibility matrix:** normal and unhappy paths with semantic behavior.
6. **Ownership plan:** shared implementation, platform seams, and reused abstractions.
7. **Validation plan and evidence:** planned checks first, then separately list tests, previews, window sizes, targets, themes, and manual checks actually completed with evidence labels.
8. **Unresolved assumptions:** label design guidance, verified APIs, and platform-specific proposals distinctly.

Do not claim visual parity, accessibility, target support, or production readiness without the corresponding evidence.

## Quality bar

A strong result:

- has an obvious first read and primary action;
- uses spacing, type, color, shape, and motion as one system;
- feels like the product, not a Material catalog;
- remains coherent when resized, translated, empty, loading, or blocked;
- exposes every state through more than color alone;
- makes focus, keyboard, pointer, and screen reader behavior deliberate;
- keeps shared and platform ownership understandable to a new engineer;
- is cheap to change or remove because it extends existing owners instead of forking them.
