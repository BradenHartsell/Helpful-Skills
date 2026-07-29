# KMP target parity and API availability

## Contents

- Portability gate
- Source-set ownership
- Platform differences
- Resources and fonts
- Testing strategy
- Dated compatibility snapshot
- Implementation checklist

## Portability gate

Before recommending a Compose API:

1. read the project's exact version catalog and build files;
2. identify the target and source set where the code will live;
3. confirm the artifact is declared for that source set;
4. check the exact API in current official JetBrains or Android documentation;
5. inspect existing repository usage and locally resolved artifacts;
6. compile the smallest affected target.

Classify every nontrivial recommendation:

- **Design guidance:** a behavior or visual principle independent of a library symbol.
- **Verified shared API:** present in the installed common artifact and intended for all relevant targets.
- **Verified target API:** present only on a named target or platform source set.
- **Proposal:** requires a dependency, version, or architecture change and has not been implemented.

Never present a proposal as current code.

## Source-set ownership

Good shared candidates:

- semantic state and event models;
- product copy and resource keys;
- token roles and portable theme configuration;
- pure layout policy;
- portable Material components;
- validation and display formatting when truly cross-platform;
- accessibility meaning that should be consistent.

Good platform candidates:

- system bars, windows, title bars, menus, notifications, and permissions;
- native navigation or view-controller integration;
- platform back and lifecycle adapters;
- accessibility service setup;
- safe-area, keyboard, and system setting signals;
- file pickers, drag and drop, clipboard, and pointer integration;
- APIs absent from the common artifact.

Do not add `expect` and `actual` for code that can be shared directly. Do not force platform integration into `commonMain` through generic callbacks that hide ownership. Before changing topology, trace the source-set dependency graph, artifact availability, platform composition root, and every affected target.

## Platform differences

### Android

- Jetpack Compose APIs may appear before they reach Compose Multiplatform.
- Material adaptive and window-size artifacts can have different common availability from Android.
- Edge-to-edge, predictive back, IME behavior, and system UI require Android-specific proof.
- Test the supported Android API range, not only the newest emulator.

### iOS

- The software keyboard and safe-area model differ from Android.
- Native presentation and back behavior require UIKit integration.
- VoiceOver consumes Compose semantics through native accessibility objects.
- Full Keyboard Access and AssistiveTouch add non-touch input paths.
- High-contrast theme switching currently needs explicit product colors and an iOS platform signal.
- Validate font rendering, text input, selection, and scrolling on a device or simulator.

### Desktop

- Mouse and keyboard are primary input paths; multitouch assumptions often do not apply.
- Windows resize continuously and may restore to unexpected dimensions.
- Native menus, context menus, file dialogs, popups, and window decoration differ by OS.
- Text rasterization and line breaks are not pixel-identical across operating systems.
- Desktop hot reload helps iteration but does not prove final behavior.
- Windows screen-reader support requires Java Access Bridge and packaging configuration.

### Web

- Raw resources can load asynchronously.
- Browser zoom, focus, DOM semantics, pointer hover, and URL navigation matter.
- Wasm and browser compatibility depend on the exact Compose release.
- Test supported browsers directly.

## Resources and fonts

Compose Multiplatform resources can share images, fonts, strings, and other assets through generated accessors.

- Keep user-facing strings in the canonical resource or copy owner.
- Verify locale fallback and pluralization.
- Bundle fonts only with appropriate licensing and target support.
- Provide fallback families because rendering and glyph coverage vary.
- Check missing glyphs, variable-font axes, tabular figures, and line-height on every target.
- Optimize large images and avoid decoding them at full resolution when only a small rendition is displayed.
- Do not assume large raw resources support the same streaming behavior on every target.

## Testing strategy

Use layered proof:

1. pure tests for layout, breakpoint, content, and state policies;
2. common Compose UI tests for semantics and portable interaction where supported;
3. target UI or integration tests for platform behavior;
4. screenshot or visual regression tests where the repository owns stable baselines;
5. manual assistive-technology and interaction checks for gaps automation cannot prove.

Compose Multiplatform provides common UI testing concepts such as `runComposeUiTest`, but availability and experimental status depend on version. Desktop has target-specific JUnit support. Verify the actual dependencies before adding tests.

Headless rendering is useful for deterministic checks but cannot replace real font, window, accessibility, and input behavior.

## Dated compatibility snapshot

The live research for this skill was performed on 2026-07-28.

Official JetBrains documentation for Compose Multiplatform 1.11.1 listed Android, iOS, desktop, and web support, with Material 3 available multiplatform. It also listed several Android-only APIs and artifacts, including Material adaptive and Material window-size-class support that was not yet available from `commonMain` in that stable release.

More precisely, the AndroidX `material3-adaptive` and `material3-window-size-class` APIs listed in that 1.11.1 guide were not available from `commonMain`. Newer release material described separate JetBrains-published multiplatform adaptive work. Verify the exact artifact coordinates and target matrix rather than generalizing the older AndroidX limitation to every adaptive library.

Material's Android roadmap separately described Compose-first development and upcoming expressive stabilization.

These facts illustrate the portability gap. They are not a substitute for refreshing the exact version in the current repository. Compose Multiplatform can trail Jetpack Compose releases, and current availability may change.

Read [sources-and-recency.md](sources-and-recency.md) before making a current-version claim.

## Implementation checklist

- [ ] Repository and target identity proved
- [ ] Exact Kotlin, Compose, Material, and plugin versions recorded
- [ ] Artifact available in the intended source set
- [ ] Existing owner and pattern inspected
- [ ] Design guidance separated from implementation API
- [ ] Shared state and platform integration ownership explicit
- [ ] No invented API or undeclared dependency
- [ ] Resources and fonts tested on intended targets
- [ ] Target-specific input and accessibility behavior tested
- [ ] Focused compilation and tests passed
- [ ] Unverified targets or visual differences reported honestly
