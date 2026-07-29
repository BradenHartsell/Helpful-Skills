# Sources and recency

## Contents

- Source priority
- Material 3 sources
- Compose Multiplatform sources
- Current snapshot
- Refresh procedure

## Source priority

Use sources in this order:

1. repository build files, design docs, and canonical owners for the product's actual state;
2. official JetBrains Compose Multiplatform documentation for cross-target APIs;
3. official Android Developers documentation for Android-specific Compose and Material APIs;
4. official Material Design guidance for design intent and component behavior;
5. resolved artifact source, generated API references, and official release notes when documentation is ambiguous.

Do not use a design-site announcement as proof that a KMP symbol exists. Do not use an API reference as proof that a product should adopt the visual pattern. The installed artifact plus focused compilation proves code availability; official version-specific documentation explains intended support.

## Material 3 sources

Official Material pages captured through live browser research on 2026-07-28:

- [Material Design 3 home](https://m3.material.io/)
- [Material 3 Expressive introduction](https://m3.material.io/blog/building-with-m3-expressive)
- [Material Android is Compose-first](https://m3.material.io/blog/material-is-compose-first)
- [Accessibility foundations](https://m3.material.io/foundations/overview/principles)
- [Design tokens](https://m3.material.io/foundations/design-tokens/overview)
- [Layout overview](https://m3.material.io/foundations/layout/layout-overview/overview)
- [Breakpoints](https://m3.material.io/foundations/layout/breakpoints/overview)
- [Adaptive design](https://m3.material.io/foundations/layout/layout-overview/adaptive-design)
- [Canonical layout examples](https://m3.material.io/foundations/layout/canonical-examples/overview)
- [Spacing](https://m3.material.io/foundations/layout/understanding-layout/spacing)
- [Bidirectionality and RTL](https://m3.material.io/foundations/layout/bidirectionality-rtl)
- [Color system](https://m3.material.io/styles/color/system/overview)
- [Color roles](https://m3.material.io/styles/color/roles)
- [Dynamic color](https://m3.material.io/styles/color/dynamic/choosing-a-source)
- [Typography](https://m3.material.io/styles/typography/overview)
- [Applying type](https://m3.material.io/styles/typography/applying-type)
- [Shape](https://m3.material.io/styles/shape/overview-principles)
- [Motion](https://m3.material.io/styles/motion/overview/how-it-works)
- [Transitions](https://m3.material.io/styles/motion/transitions/transition-patterns)
- [Interaction states](https://m3.material.io/foundations/interaction/states/state-layers)
- [Elevation](https://m3.material.io/styles/elevation/overview)
- [Icons](https://m3.material.io/styles/icons/overview)
- [Material components](https://m3.material.io/components)

Component overview and accessibility pages were reviewed for buttons, button groups, FABs, icon buttons, date and time pickers, loading and progress, navigation bars and rails, sheets, app bars, badges, cards, carousels, checkboxes, chips, dialogs, dividers, lists, menus, radio buttons, snackbars, switches, tabs, text fields, toolbars, and tooltips.

## Compose Multiplatform sources

Official JetBrains pages captured through live browser research on 2026-07-28:

- [Compose Multiplatform documentation](https://kotlinlang.org/docs/multiplatform/compose-multiplatform.html)
- [Compose Multiplatform compatibility and versions](https://kotlinlang.org/docs/multiplatform/compose-compatibility-and-versioning.html)
- [Platform-specific APIs](https://kotlinlang.org/docs/multiplatform/compose-platform-specifics.html)
- [Android-only APIs](https://kotlinlang.org/docs/multiplatform/compose-android-only-components.html)
- [Multiplatform resources](https://kotlinlang.org/docs/multiplatform/compose-multiplatform-resources.html)
- [Compose Multiplatform UI testing](https://kotlinlang.org/docs/multiplatform/compose-test.html)
- [Accessibility support](https://kotlinlang.org/docs/multiplatform/compose-accessibility.html)
- [iOS accessibility](https://kotlinlang.org/docs/multiplatform/compose-ios-accessibility.html)
- [Desktop accessibility](https://kotlinlang.org/docs/multiplatform/compose-desktop-accessibility.html)
- [JetBrains Compose Multiplatform releases](https://github.com/JetBrains/compose-multiplatform/releases)
- [JetBrains Compose Multiplatform repository](https://github.com/JetBrains/compose-multiplatform)

## Current snapshot

This snapshot explains why the skill is strict about recency:

- Material Design 3 remains the current Material system. Material 3 Expressive expands, rather than replaces, Material 3.
- Material announced an Android Compose-first direction in May 2026. That announcement concerns Android library direction and does not make every expressive API available in shared KMP code.
- Official JetBrains documentation viewed during research described stable Compose Multiplatform 1.11.1 and newer alpha work.
- In the stable 1.11.1 documentation, the listed AndroidX `material3-adaptive` and `material3-window-size-class` APIs remained Android-only rather than available from `commonMain`.
- Newer release material described separate JetBrains-published multiplatform adaptive work, which needs its own artifact and target check.
- Compose Multiplatform releases can trail Jetpack Compose, so similarly named versions and components need exact artifact proof.

These statements will age. Refresh them before making a current availability claim.

## Refresh procedure

When using this skill for implementation:

1. read settings, module builds, version catalogs, lockfiles, and target declarations;
2. record the exact Kotlin, Compose Multiplatform, Material artifact, target, and source-set facts;
3. inspect locally resolved artifacts and existing imports;
4. read the current official JetBrains API or guide page through any available browser or HTTP tool;
5. for Android-only behavior, read the current official Android Developers page;
6. check the Material page for design intent;
7. search the repository for existing usage and owners;
8. compile or test the intended target when the task permits it;
9. check each cited URL for both a successful response and the expected rendered page, since a single-page app can return a friendly not-found page with HTTP 200;
10. record the source URL, version scope, retrieval date, local proof, and any conflict.

If current official documentation cannot be reached, use the installed artifact and repository as local truth, label recency-dependent claims `[local-only]`, keep the recommendation provider-neutral, and identify what needs a later refresh. Do not make the whole skill unusable merely because one documentation service or network capability is absent.
