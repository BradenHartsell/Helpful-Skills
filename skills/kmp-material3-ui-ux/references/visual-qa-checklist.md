# Visual and behavioral QA checklist

## Contents

- Before implementation
- Composition and hierarchy
- Theme and finish
- Component behavior
- Adaptive review
- Accessibility and input
- State and motion
- Cross-target review
- Evidence receipt

## Before implementation

- [ ] User job and success state are explicit.
- [ ] Local design, theme, component, navigation, state, and copy owners are known.
- [ ] Exact targets and installed artifacts are known.
- [ ] Visual thesis names hierarchy, density, tone, and product character.
- [ ] One or two expressive moments are identified.
- [ ] State, input, and window matrices are written.
- [ ] Existing reusable components were reviewed before adding new ones.

## Composition and hierarchy

- [ ] The first read is obvious within a glance.
- [ ] One action is visually primary in each decision region.
- [ ] Supporting actions remain discoverable without competing.
- [ ] Grouping is created first with order, alignment, whitespace, and surface tone.
- [ ] Cards and dividers appear only when they clarify containment.
- [ ] Reading width remains comfortable on large windows.
- [ ] Dense and sparse states both feel deliberate.
- [ ] Empty space has a compositional purpose.
- [ ] Repeated items align and scan consistently.
- [ ] Destructive actions are separated from routine actions.

## Theme and finish

- [ ] Colors use semantic roles and paired foreground or container roles.
- [ ] Accent color is restrained and hierarchy remains visible in grayscale.
- [ ] Light, dark, and supported high-contrast variants remain coherent.
- [ ] Typography creates a clear ladder without too many weights or styles.
- [ ] Emphasized type is reserved for real emphasis.
- [ ] Long text, large text, and font fallback do not clip.
- [ ] Spacing follows the project token rhythm.
- [ ] Shapes are consistent by role and do not obscure interaction.
- [ ] Elevation explains layering instead of decorating every surface.
- [ ] Icon family, weight, fill, and size remain consistent.
- [ ] Imagery has suitable cropping, contrast, loading, and fallback behavior.

## Component behavior

- [ ] Each component matches the semantic action or choice.
- [ ] Labels predict outcomes and use product language.
- [ ] Selection is distinct from navigation and activation.
- [ ] Standard components are used unless customization earns its obligations.
- [ ] Custom components cover semantics, focus, keyboard, pointer, touch, state, and testing.
- [ ] Forms preserve labels, input, validation, and recovery.
- [ ] Menus, sheets, dialogs, tooltips, and snackbars are used for the correct level of interruption.
- [ ] Progress reports a real process and does not decorate idle content.

## Adaptive review

- [ ] The layout is based on available window space.
- [ ] Existing breakpoints are reused.
- [ ] Behavior is checked just below, at, and above each breakpoint.
- [ ] Primary task and primary action survive every window class.
- [ ] Revealed panes add useful content.
- [ ] Swapped components preserve semantics and state.
- [ ] Destination order and selection remain stable.
- [ ] Resize does not reset forms, selection, scroll, or active work.
- [ ] Focus order remains logical after reflow.
- [ ] Insets, keyboard, title bar, hinge, and safe areas are respected.
- [ ] Minimum supported window remains usable without hidden actions.

## Accessibility and input

- [ ] Every action has an accessible name and role.
- [ ] Selected, checked, expanded, error, disabled, and progress states are exposed.
- [ ] Decorative content is excluded from semantics.
- [ ] Focus is visible and meets contrast needs.
- [ ] Traversal order follows the intended reading and action order.
- [ ] Keyboard activation follows component conventions.
- [ ] Pointer hover has a non-hover path.
- [ ] Essential actions do not depend on gesture precision.
- [ ] Interactive targets follow the project minimum.
- [ ] Text and meaningful non-text contrast meet minimums.
- [ ] State is not communicated through color alone.
- [ ] Large text, localization, RTL, and mixed-direction content were exercised.
- [ ] Target screen readers or accessibility inspectors were used where required.

## State and motion

- [ ] Loading preserves useful structure and cancellation where supported.
- [ ] Empty state explains the situation and next useful action.
- [ ] Offline, partial, stale, blocked, and error states are distinct when they can occur.
- [ ] Retry cannot duplicate completed work.
- [ ] Destructive consequences are exact and confirmations are proportionate.
- [ ] Success reveals the result or stable next state.
- [ ] Hover, focus, press, drag, selection, and disabled states are distinct.
- [ ] Motion explains cause, hierarchy, or spatial relation.
- [ ] Repeated flows use quiet motion.
- [ ] Reduced motion removes parallax, morphs, and large spatial movement.
- [ ] Interrupted animations converge on valid state.

## Cross-target review

- [ ] Shared API availability is proved for every intended target.
- [ ] Platform seams are narrow and owned.
- [ ] Font and text rendering differences do not break layout.
- [ ] Native menus, popups, back behavior, keyboard, and windows follow platform conventions.
- [ ] Resources load correctly on each target.
- [ ] Visual parity is behavioral and semantic, not forced pixel identity.
- [ ] Unsupported or untested targets are reported.

## Evidence receipt

Report only what was actually checked:

```text
Surface:
Targets:
Versions:
Theme variants:
Window sizes and breakpoint edges:
Data and operation states:
Input modes:
Accessibility tools:
Automated tests:
Manual checks:
Known gaps:
```

For screenshot review, capture the same meaningful state at representative widths and themes. Compare hierarchy, clipping, alignment, contrast, focus, and content continuity, not only pixel difference.

If the repository lacks screenshot or Compose UI test infrastructure, do not create a broad test framework as incidental work without local evidence. Add focused pure policy tests where useful, complete manual evidence, and identify the missing automated proof.
