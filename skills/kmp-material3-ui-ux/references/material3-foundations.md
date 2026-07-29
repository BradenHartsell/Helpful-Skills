# Material 3 foundations for KMP

## Contents

- Product-first use of Material
- Expressive design without visual noise
- Tokens and ownership
- Layout and spacing
- Adaptive default window classes
- RTL and bidirectional content
- Elevation and surfaces
- Icons and imagery
- Common failure patterns

## Product-first use of Material

Material 3 supplies principles, roles, components, and interaction guidance. It does not supply the product's information architecture, voice, or distinctive identity.

Use this order:

1. understand the user job and content;
2. preserve the repository's product language and existing behavior owners;
3. choose Material roles and components that make the job legible;
4. use branded tokens and a restrained expressive treatment to make the experience distinctive;
5. prove the result across states, windows, input modes, and targets.

Accessibility guidance is a starting point, not a ceiling. Honor individual needs, learn from actual users when possible, and do not treat a minimum WCAG ratio as proof that a flow is usable.

## Expressive design without visual noise

Material 3 Expressive expands shape, typography, motion, color, and adaptive composition. Treat it as a design vocabulary that can be used independently of whether a named Expressive Compose API exists in the installed KMP version.

Useful tactics:

- vary shape to establish hierarchy or a celebratory moment;
- use richer, nuanced color while preserving semantic role pairing;
- use typography to direct attention;
- contain related content clearly;
- use fluid motion to preserve cause and effect;
- adapt component presentation to the available window;
- choose one or two hero moments per surface.

Restraint matters. If every card, button, heading, and transition asks for attention, the hierarchy disappears. Common controls should usually remain familiar and quiet.

Shape, color, or motion must not carry meaning alone. Pair visual expression with labels, semantics, structure, and state cues.

## Tokens and ownership

Material token layers are useful as an ownership model:

1. **Reference values:** raw palette tones, typefaces, dimensions, and motion parameters.
2. **System tokens:** semantic roles such as primary action, surface container, body text, focus indicator, and destructive action.
3. **Component tokens:** the roles applied to a specific component and state.

Prefer semantic names that explain purpose:

- `surfaceRaised`, not `gray100`;
- `contentCritical`, not `red`;
- `spacingPaneGap`, not `padding24`;
- `shapePrimaryAction`, not `roundedLarge`.

Values can vary by light or dark theme, contrast preference, density, input mode, window class, and locale direction while the semantic name remains stable.

Do not create a screen-local token collection if the concept belongs to the app design system. Do not add a global token for a one-off decorative value with no shared product meaning.

## Layout and spacing

Compose from regions before styling individual elements:

- system and app bars;
- primary navigation;
- primary content;
- secondary or supporting content;
- contextual actions and feedback.

Use the available window, not a device label. A desktop window can be compact. A tablet can be split-screen. A foldable can change posture while the flow remains active.

Material commonly uses an 8 dp base spacing rhythm. Treat that as a starting vocabulary, then follow the repository's established token scale. Use smaller increments only where typography, icons, or compact controls require them.

Prefer:

- parent padding and layout gaps for group rhythm;
- leading and trailing semantics rather than hardcoded left and right;
- consistent alignment lines;
- whitespace before dividers;
- a deliberate maximum readable line length on wide windows;
- stable regions that do not jump when loading resolves.

Avoid:

- unrelated values scattered through composables;
- nested padding that obscures the true layout rule;
- stretching a narrow mobile composition across a large desktop window;
- shrinking touch targets to make dense visuals fit;
- putting every item in a card.

## Adaptive default window classes

Material guidance currently describes five default width classes:

Use this table only when the repository has no existing policy, then validate it against content minimums and target ergonomics.

| Class | Default width range |
|---|---:|
| Compact | less than 600 dp |
| Medium | 600 to 839 dp |
| Expanded | 840 to 1199 dp |
| Large | 1200 to 1599 dp |
| Extra large | 1600 dp and above |

These are dated design defaults, not automatic project policy. Current Material language calls them breakpoints and notes that this succeeds the earlier window-size-class terminology. Reuse an existing repository breakpoint owner. If the product has evidence-backed breakpoints, do not replace them just to match this table.

At a size change, decide what should:

- **reveal:** expose useful content or controls;
- **divide:** place related regions into panes;
- **resize:** adjust dimensions without changing semantics;
- **reposition:** move a component to a more useful location;
- **swap:** replace a component only with a functionally equivalent presentation.

Read [adaptive-layouts-and-navigation.md](adaptive-layouts-and-navigation.md) for full guidance.

## RTL and bidirectional content

Use leading and trailing layout semantics. Mirror directional composition and navigation where appropriate.

Usually mirror:

- back and forward arrows;
- directional chevrons;
- previous and next controls;
- navigation rail placement to the leading edge;
- directional motion.

Usually do not mirror:

- media playback controls;
- clocks;
- circular progress;
- non-directional brand marks;
- text inside images.

Test mixed-direction text, email addresses, URLs, numbers, punctuation, cursor movement, selection, and truncation. Do not assume that mirroring the top-level row proves RTL support.

## Elevation and surfaces

Material 3 uses surface tone and, when useful, shadow to communicate containment and relative level.

- Use a small number of meaningful levels.
- Prefer tonal surface roles for persistent hierarchy.
- Add shadow when physical separation, overlap, or transient placement needs stronger evidence.
- Keep the default component elevation unless product hierarchy provides a reason to change it.
- Do not use elevation as decoration on every container.

Surface container roles progress from lowest through highest. Use them to separate regions without introducing unrelated colors.

## Icons and imagery

Use one icon family consistently. Material Symbols offer variable weight, fill, optical size, and grade, but the installed project may use another canonical set.

- Pair unfamiliar icon actions with visible text.
- Provide a tooltip for compact pointer-driven icon actions.
- Give every actionable icon an accessible action label.
- Use filled and outlined variants consistently when they communicate selected state.
- Keep decorative icons out of the semantics tree.
- Do not use an icon when a short label is clearer.

Imagery and abstract shapes can create a hero moment. Keep decorative treatment away from dense forms, navigation, and repeated operational states where clarity matters most.

## Common failure patterns

- Copying a Material sample instead of designing for the product.
- Treating an Android announcement as a stable shared KMP API.
- Creating a second theme or breakpoint table.
- Hardcoding palette values directly in screens.
- Using cards and shadows for every grouping.
- Using expressive type, shape, and motion everywhere.
- Hiding unavailable actions as disabled controls without explaining the blocker.
- Making disabled controls the only way to communicate a missing prerequisite.
- Mirroring all icons in RTL, including media controls.
- Validating only one ideal window and one ideal data state.
