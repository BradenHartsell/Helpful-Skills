# Accessibility and input

## Contents

- Accessibility as interaction design
- Semantics
- Labels, roles, and state
- Target size and contrast
- Focus and keyboard
- Pointer, touch, and alternate input
- Text, localization, and RTL
- Platform-specific proof
- Testing matrix

## Accessibility as interaction design

Accessibility is not a final modifier pass. It affects content order, component choice, focus behavior, target size, contrast, motion, error recovery, and platform validation.

Design for:

- screen readers;
- keyboard and D-pad navigation;
- mouse, trackpad, and stylus;
- touch and switch access;
- increased text size;
- reduced motion;
- high contrast;
- color-vision differences;
- localization and bidirectional text.

Material components provide useful defaults, but custom composition, custom gestures, and target-specific integration can remove those defaults.

## Semantics

Compose produces a semantics tree that platform accessibility services and UI tests consume.

Use semantics to expose:

- accessible name;
- role;
- value or state;
- selected, checked, expanded, disabled, error, or progress status;
- available action;
- traversal relationship;
- test identity when the repository uses semantic test tags.

Common Compose concepts include `contentDescription`, `role`, `stateDescription`, and `testTag`. Verify exact APIs and target behavior in the installed version.

Rules:

- prefer visible text as the accessible name when it already labels the control;
- add an action-oriented description to icon-only controls;
- remove purely decorative imagery from the semantics tree;
- merge child semantics only when the combined spoken result is clearer;
- do not hide meaningful nested actions by over-merging;
- define traversal order when visual reflow makes source order unclear;
- keep test tags stable and independent of user-facing copy where local testing conventions permit.

## Labels, roles, and state

An accessible name should predict what activation does.

- Button labels use an action, such as "Save changes".
- Toggle descriptions identify the setting and expose on or off state.
- Navigation items identify the destination and selected state.
- Fields keep a label, not only a placeholder.
- Errors identify the field, the problem, and a recovery path.
- Progress identifies the process and, when possible, its value.
- Badges expose a full spoken meaning rather than only a compact count.

Do not repeat the role inside the label if the platform already announces it. Do not announce implementation terms.

For live changes, use the platform's supported announcement or live-region behavior judiciously. Avoid repeatedly announcing progress or rapidly changing content.

## Target size and contrast

Follow the repository's canonical minimum target rule. When no project rule exists:

- Material commonly uses a 48 dp minimum touch target;
- Apple platform guidance commonly starts from 44 by 44 points;
- a compact visible control can retain a larger invisible hit target;
- pointer density does not remove keyboard, motor, or touch obligations.

Keep separate controls from overlapping hit regions. Make the visible label part of the intended target for checkboxes, radio buttons, switches, and list rows.

Contrast starting points:

| Content | Common minimum |
|---|---:|
| Small text | 4.5:1 |
| Large text | 3:1 |
| Meaningful controls, focus, and non-text boundaries | 3:1 |

Verify the actual rendered combination. Opacity, image backgrounds, elevation, disabled treatment, and dynamic color can change the result.

State must not rely on color alone. Add a label, icon, outline, position, weight, or semantic state.

## Focus and keyboard

Every interactive item needs:

- a visible focus indication with sufficient contrast;
- a logical traversal position;
- keyboard activation appropriate to its role;
- focus restoration after dialogs, sheets, menus, or removed panes;
- no hidden or disabled focus targets;
- no trap except an intentional modal focus scope.

Typical expectations:

| Interaction | Common keys |
|---|---|
| Move through controls | Tab and Shift+Tab |
| Activate button or link | Enter, sometimes Space by role |
| Toggle checkbox or switch | Space |
| Move within radio group, tabs, menu, or rail | Arrow keys |
| Close transient UI | Escape or platform back |
| Invoke default form action | Enter when unambiguous |

Follow platform convention and existing repository behavior. Avoid adding global shortcuts that conflict with text editing or assistive technology.

When adaptive layout reorders content visually, make source and focus order intentional. A visually adjacent pane should not require an unpredictable traversal jump.

## Pointer, touch, and alternate input

Pointer support includes:

- hover state;
- appropriate cursor;
- secondary click where conventional;
- tooltip for unfamiliar icon actions;
- scroll wheel and trackpad behavior;
- drag affordance, threshold, cancellation, and keyboard alternative.

Touch support includes:

- minimum target;
- gesture conflict handling;
- no hover-only information;
- clear pressed feedback;
- cancellation when a gesture leaves the target;
- alternatives to precision gestures.

Do not make swipe, drag, long press, double click, or hover the only way to reach an essential action.

## Text, localization, and RTL

Validate:

- text at 200 percent where the platform supports it;
- system font scaling and custom font fallback;
- long labels, long words, and multi-line actions;
- pluralization and formatted numbers;
- mixed RTL and LTR content;
- URLs, email addresses, phone numbers, dates, and time;
- truncation with an accessible full value;
- input cursor, selection, and keyboard behavior.

Avoid fixed heights around text. Keep touch targets large after wrapping. Underline links so color is not the only differentiator.

Read [material3-foundations.md](material3-foundations.md) for mirroring guidance.

## Platform-specific proof

### Android

Verify TalkBack, keyboard or D-pad navigation, touch target, font scaling, contrast, edge-to-edge placement, and system back behavior on the supported Android version range.

### iOS

Compose Multiplatform maps semantics to native accessibility objects for VoiceOver and XCTest. Verify:

- VoiceOver reading and action order;
- Full Keyboard Access with Tab and Space;
- AssistiveTouch or pointer operation;
- text scaling and safe areas;
- accessibility audit in XCTest where available;
- high-contrast palette switching.

Current JetBrains guidance notes that Material 3 `ColorScheme` does not automatically provide iOS high-contrast colors. A product that supports the iOS Increase Contrast setting needs an explicit palette and platform signal.

### Desktop

Verify keyboard-first operation even when the product is primarily pointer-driven.

- macOS: use Accessibility Inspector and test VoiceOver where relevant.
- Windows: Compose accessibility uses Java Access Bridge, which may be disabled in the development environment. Native packaging also needs the accessibility module configured. Test with NVDA or JAWS when Windows screen-reader support is in scope.
- Validate focus, menus, context menus, window resizing, and platform shortcuts on the actual OS.

### Web

Verify semantic HTML mapping, browser zoom, keyboard order, focus visibility, hover alternatives, screen-reader behavior, and asynchronous resource loading on supported browsers.

## Testing matrix

For every important flow, record evidence for:

| Dimension | Cases |
|---|---|
| Input | touch, pointer, keyboard, D-pad or switch when applicable |
| Perception | light, dark, high contrast, non-color state cue |
| Text | normal, large, localized, RTL, mixed direction |
| Assistive tech | semantics inspection plus target screen reader |
| Motion | normal and reduced |
| Window | minimum, breakpoint boundaries, wide, resized during work |
| State | loading, empty, error, blocked, disabled, success |
| Target | each supported target or an explicit unverified gap |

Portable Compose UI tests can verify semantics and interactions, but they do not replace platform tests. Use target tools such as XCTest accessibility audits, desktop accessibility inspectors, Android accessibility testing, and browser tooling where supported.
