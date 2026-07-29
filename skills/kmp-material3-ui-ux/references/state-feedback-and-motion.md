# State, feedback, and motion

## Contents

- State is part of the design
- Interaction states
- Product state matrix
- Progress and loading
- Feedback component choice
- Motion system
- Transition direction
- Reduced motion
- Interruption and failure

## State is part of the design

A polished happy path with vague loading, failure, or blocked states is not a finished UI.

Distinguish:

- durable product state;
- transient UI state;
- navigation state;
- operation state;
- validation state;
- connectivity or provider state.

Render state owned by the correct layer. Do not create local booleans that compete with a canonical operation or navigation owner.

## Interaction states

Material interaction states include enabled, disabled, hover, focused, pressed, and dragged. Current Material components use state layers based on the component's content color. Preserve the installed component defaults or the repository's canonical component owner. Do not manually recreate dated state-layer opacity values from design guidance.

Material guidance commonly uses a compact visible state layer inside a larger interactive target. Treat exact dimensions as design defaults and follow the repository's canonical component implementation.

Rules:

- focus and pressed states must be visible;
- hover cannot be the only cue;
- disabled controls do not receive focus, hover, or press;
- explain a missing prerequisite in content, not only through a disabled control;
- if a floating primary action is not available in the current context, removing it may be clearer than showing a dead focal point;
- preserve non-color cues for selected, error, and disabled states.

## Product state matrix

Use only states that the feature can actually encounter, but name them before implementation:

| State | Content obligation | Action obligation | Accessibility obligation |
|---|---|---|---|
| Initial | stable structure or immediate content | avoid accidental duplicate start | clear page or region label |
| Loading | identify what is loading | cancel or leave when supported | progress purpose and value if known |
| Empty | explain why and what can happen next | one useful next action | not announced as an error unless it is one |
| Content | clear hierarchy | primary and secondary actions | complete reading and focus order |
| Partial | show available content and missing portion | retry only the failed portion | announce limitation without repeating |
| Stale or offline | distinguish cached from current facts | refresh or continue safely | non-color status and actionable message |
| Blocked | explain exact prerequisite | connect, sign in, provide input, or leave | focus the explanation before action |
| Validation error | preserve input | direct recovery at field and summary | error semantics and useful focus |
| Operation error | preserve recoverable state | retry, cancel, or alternate path | concise announcement and persistent text |
| Disabled | retain context only when useful | no activation | expose disabled state |
| Success | show the result or next stable state | undo or continue when useful | avoid noisy repeated announcements |
| Destructive | identify exact consequence | deliberate confirmation when materially necessary | safe initial focus and explicit labels |

Do not add arbitrary progress steps, delays, confirmation loops, or caps for implementation convenience.

## Progress and loading

Choose feedback from what the system knows:

- determinate progress when completion is measurable and honest;
- indeterminate progress when duration is unknown;
- skeletons when preserving final geometry improves comprehension;
- a localized inline spinner for a bounded control action;
- a full-region loading state only when the whole region is unavailable.

Keep a stable layout. Avoid replacing an entire screen with a centered spinner when navigation, title, cached content, or cancellation can remain available.

Use the same progress style for the same process. Do not let two indicators imply two independent operations when there is only one.

Progress semantics should identify the process and affected content. If a progress track lacks enough contrast, use the component's recommended stop or boundary treatment when supported.

## Feedback component choice

| Need | Prefer |
|---|---|
| Immediate field recovery | inline supporting or error text |
| Non-blocking result or undo | snackbar |
| Persistent page limitation | inline banner or status region using the product component owner |
| Critical bounded decision | dialog |
| Background activity visible in context | persistent activity or status surface |
| Missing prerequisite | explanatory content plus exact next action |
| Destructive material consequence | explicit confirmation only when truly necessary |

Do not use a toast or snackbar for information the user must retain. Do not interrupt with a dialog for routine success.

## Motion system

Motion should preserve cause and effect, hierarchy, and spatial relationship.

Current Material 3 Expressive guidance uses spring-based motion with expressive and standard schemes:

- **spatial motion** changes position, size, rotation, or shape and may overshoot;
- **effects motion** changes opacity or color and should not overshoot;
- speed families are commonly fast, default, and slow;
- default speed should cover most transitions.

Treat these as motion design guidance. Verify whether the installed Compose version exposes named motion-scheme APIs. Stable animation primitives can implement the intended behavior without an unavailable library symbol.

Use expressive motion for:

- a hero transformation;
- a meaningful state transition;
- a strong spatial relationship;
- a rare celebratory moment.

Use standard, quiet motion for repeated navigation, forms, menus, and operational feedback.

## Transition direction

Choose the transition from information architecture:

- top-level destinations: quick fade or platform-consistent transition;
- lateral peer content: lateral movement only when the relationship is clear;
- deeper contextual content: enter and exit that preserve hierarchy;
- modal content: scale, fade, or platform-native presentation;
- expanding detail: motion from the invoking element when it explains origin.

Honor platform back and forward conventions. Avoid conflicting directions between content and navigation chrome.

Avoid jump cuts when continuity matters. A jump cut is acceptable for a pure efficiency action where spatial continuity adds no value.

## Reduced motion

When reduced motion is requested:

- replace large spatial movement with a subtle fade;
- disable parallax;
- disable shape morphs that are decorative;
- remove intense slide and scale;
- keep state changes immediate or short;
- preserve focus and content continuity;
- keep essential progress information.

For carousels, remove parallax and item expansion and keep item dimensions stable.

Reduced motion is a product behavior, not only a shorter duration.

## Interruption and failure

Test animation and operation interruption:

- resize during transition;
- navigate back during loading;
- cancel a drag;
- lose connectivity while saving;
- receive success after the destination closes;
- retry after partial success;
- replace or remove the focused item;
- enable reduced motion while the app is running if the platform supports it.

The UI must converge on canonical state without duplicate actions, lost focus, stale overlays, or an animation that leaves interaction blocked.
