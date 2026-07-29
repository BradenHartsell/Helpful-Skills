# Compose Material 3 component selection

## Contents

- Selection method
- Actions
- Selection controls and chips
- Text and structured input
- Navigation
- Containers and content
- Feedback and transient UI
- Date, time, menus, and tooltips
- Custom component obligations
- Component review questions

## Selection method

Choose a component from interaction semantics, not appearance:

1. What user decision or action does it represent?
2. Is it primary, secondary, optional, destructive, or immediate?
3. Does it navigate, mutate, select, reveal, or report status?
4. Is it persistent, contextual, modal, or transient?
5. How many choices or destinations exist?
6. What must happen for keyboard, pointer, touch, and screen reader users?
7. Does the installed KMP artifact expose the desired component on every target?

Prefer a familiar standard component when it fits. Custom visuals are worthwhile when the product concept is genuinely distinct and the team accepts the full interaction and accessibility obligations.

## Actions

### Buttons

| Component | Use |
|---|---|
| Filled button | highest-emphasis action in a flow |
| Filled tonal button | important action with less visual dominance |
| Elevated button | action that needs separation from a patterned or tonal surface |
| Outlined button | medium-emphasis alternative |
| Text button | low-emphasis, compact, or dialog action |
| Toggle button | an action with an on or selected state |
| Button group | related actions presented together |

Use concise sentence-case labels. Prefer a verb that predicts the result. Keep one dominant action per decision region.

Connected button groups are the current expressive replacement for segmented buttons in some Material guidance. Verify that the exact Compose artifact supports the desired API. A stable segmented control remains valid when it matches local patterns and target support.

### Floating action buttons

Use a FAB or extended FAB only for the most important and frequent action on the current screen. It should not compete with another dominant action.

- Use an unmistakable icon.
- Add text when the action needs explanation.
- Reposition or change presentation adaptively when the screen structure changes.
- Hide an unavailable contextual FAB when showing a disabled floating control would create a dead focal point, but explain any missing prerequisite elsewhere.

### Icon buttons

Use an icon button when a familiar icon communicates the action in limited space.

- Provide an accessible action label.
- Provide a tooltip for pointer and web contexts.
- Keep the interactive target large even when the visible icon is compact.
- Use selected and unselected treatments consistently for toggles.
- Prefer text when the icon is ambiguous.

## Selection controls and chips

| Component | Use |
|---|---|
| Checkbox | zero or more independent choices |
| Radio button | exactly one choice from a visible set |
| Switch | an independent setting that takes effect immediately |
| Segmented or connected control | two to five compact peer choices |
| Assist chip | a contextual action that helps complete a task |
| Filter chip | include or exclude content by a filter |
| Input chip | a user-provided entity, token, or recipient |
| Suggestion chip | a short suggested response or next action |

Make both the control and its visible label interactive. Expose indeterminate checkbox state semantically. Do not use a switch for a choice that requires a separate Save action.

## Text and structured input

### Text fields

- Filled fields create stronger containment and suit short, focused forms.
- Outlined fields reduce visual weight and can work well in longer forms.
- Preserve a visible label when content is entered.
- Use supporting text for persistent guidance and a clear error message for invalid input.
- Label leading and trailing actions.
- Expose error state through semantics and not color alone.
- Avoid fixed height when text can scale or wrap.
- Keep prefix and suffix content meaningful to assistive technology.

For forms, decide:

- validation timing;
- first focus and traversal order;
- keyboard action behavior;
- submission while work is in progress;
- preservation after failure;
- how server and local errors differ;
- where destructive or irreversible choices receive confirmation.

### Date and time

Use date or time pickers when the value must be valid and the visual chooser improves accuracy. Offer keyboard input when faster or when a calendar grid is inaccessible for the task.

Verify locale, first day of week, 12 or 24 hour format, time zone, range limits, and target-specific presentation.

## Navigation

Use destination-count guidance only when the repository has no existing navigation policy. Validate it against the product's information architecture.

| Component | Typical use |
|---|---|
| Navigation bar | three to five stable top-level destinations in compact windows |
| Navigation rail | three to seven stable destinations in medium or wider windows |
| Navigation drawer | larger destination sets, secondary destinations, or account-level areas |
| Tabs | peer categories inside one destination |
| Top app bar | current page context plus one or two essential actions |
| Back, breadcrumbs, or hierarchy affordance | movement within a nested information structure |

Navigation is product and runtime architecture, not just styling. Reuse the existing destination and state owner. Read [adaptive-layouts-and-navigation.md](adaptive-layouts-and-navigation.md), then inspect lifecycle, state restoration, back handling, and window routing before changing behavior.

Do not:

- reorder stable destinations across window classes;
- use tabs for unrelated top-level product areas;
- hide the selected destination label without another clear cue;
- run a navigation bar and toolbar in the same role;
- duplicate navigation state inside a responsive composable.

## Containers and content

### Cards

Use a card for one related unit with a coherent action or reading order. Do not wrap every group in a card. Spacing, headings, tonal surfaces, or dividers may communicate structure with less noise.

### Lists

Keep ordering logical and rows scannable. Align repeated content, keep metadata quiet, make the whole intended row target interactive, and preserve keyboard focus behavior.

### Dividers

Use a divider only when whitespace or surface tone cannot group the regions clearly. Divide meaningful regions, not every item by default.

### Carousels

Use a carousel for visual content whose sequence benefits from horizontal browsing. Provide a "Show all" alternative when a carousel is embedded in a vertically scrolling page. Remove parallax and item expansion for reduced motion.

### Bottom and side sheets

- Bottom sheets suit secondary or contextual content on compact and medium windows.
- Side sheets can keep optional supporting content visible on wider windows.
- Modal variants block the underlying flow and need focus containment, dismissal, and back or escape handling.
- Standard variants coexist with the main content and need clear spatial hierarchy.

### Dialogs

Use a dialog sparingly for one critical decision or bounded task that must interrupt the current flow.

- Give it a clear title.
- Move focus into it and restore focus on dismissal.
- Keep content scrollable when it can grow.
- Avoid placing a multi-screen workflow inside a dialog.
- Use an alert role only for truly urgent content.

## Feedback and transient UI

### Progress

- Use determinate progress when the system can report meaningful completion.
- Use indeterminate progress when duration or completion is unknown.
- Keep the same progress configuration for the same ongoing process.
- Explain what is in progress and which content is affected through semantics.
- Do not use a loading indicator as decoration.

### Snackbar

Use a snackbar for non-blocking feedback related to the current context. Offer a concise action when recovery or undo is useful. Do not put critical decisions or long explanations in a snackbar.

### Badge

Use a badge for a short count or status. Current Material guidance limits badge content to a very short label, commonly no more than four characters including a plus sign. Use a fuller accessible description.

## Date, time, menus, and tooltips

### Menus

Menus hold temporary actions or choices. Keep frequently used actions visible in a toolbar. On pointer platforms, consider a context menu for an established secondary-click interaction, while preserving an accessible visible path.

### Toolbars

Use docked or floating toolbars for persistent actions tied to the current content. Do not show competing toolbars and navigation bars that occupy the same visual role.

### Tooltips

- Plain tooltips label unfamiliar compact actions.
- Rich tooltips can add short supporting information or an action.
- Trigger from hover and focus where supported.
- Keep them visible long enough to read.
- Do not trap focus or place essential information only in a tooltip.

## Custom component obligations

A custom interactive component must define:

- semantic role and accessible name;
- value, selected, expanded, checked, or progress state;
- enabled and disabled behavior;
- hover, focus, press, drag, and pointer cursor behavior where relevant;
- keyboard activation and traversal;
- touch and pointer target;
- visible focus and non-color state cues;
- loading, error, and interruption behavior;
- light, dark, high-contrast, and reduced-motion behavior;
- target support and tests.

If this list is disproportionate to the product value, use the standard component.

## Component review questions

- Does the component's behavior match what users expect from its shape and label?
- Is there one obvious primary action?
- Is selection distinct from navigation and activation?
- Can every action be reached and understood without a pointer?
- Does long text or text scaling break the component?
- Does the component keep state across resize and recomposition?
- Is the API actually present on every intended target?
- Could spacing or hierarchy replace another container, divider, or card?
- Is the custom styling product-specific or merely different?
