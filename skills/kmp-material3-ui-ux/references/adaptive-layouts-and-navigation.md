# Adaptive layouts and navigation

## Contents

- Design for windows
- Adaptive transformations
- Canonical layouts
- Pane strategy
- Navigation adaptation
- Insets, posture, and safe regions
- Implementation ownership
- Resize and boundary testing

## Design for windows

Base layout decisions on the available window, not a device category. Desktop windows resize freely, mobile apps can enter split-screen, and foldable posture can change while the user is working.

Start from the smallest useful composition:

1. preserve the primary task and primary action;
2. reveal supporting content as space permits;
3. keep destination and selection state stable;
4. avoid empty width by adding useful hierarchy, not by stretching text and controls;
5. preserve a readable measure and clear focus order.

Reuse the repository's canonical breakpoint or window policy. Material's default five-class width table is documented in [material3-foundations.md](material3-foundations.md), but it must not become a second truth source.

## Adaptive transformations

At each relevant boundary, make an explicit choice:

| Transformation | Meaning | Example |
|---|---|---|
| Reveal | show useful content previously hidden | expose a preview or supporting action |
| Divide | split content into simultaneous regions | list and selected detail panes |
| Resize | change dimensions without changing role | wider search field or content column |
| Reposition | move a component to a better location | action moves from bottom bar to app bar |
| Swap | replace with a functionally equivalent presentation | navigation bar becomes navigation rail |

Swaps must preserve semantics, destination order, selection, action meaning, and accessibility. Do not swap merely to make two screenshots look different.

Other useful adaptation strategies:

- **show or hide:** expose optional controls or supporting content;
- **levitate:** move a component above content when overlap is useful;
- **reflow:** rearrange content while preserving reading order;
- **presentation change:** keep the same action or state with a size-appropriate component.

## Canonical layouts

### Feed

Use for a stream or collection where the next item matters more than persistent selection.

- compact: one readable column;
- wider: multiple balanced columns or a wider central feed with supporting regions;
- avoid masonry layouts when reading order or keyboard traversal becomes ambiguous.

### List-detail

Use when a collection and the selected item form one workflow.

- compact: list and detail usually occupy separate navigation states;
- expanded: list and detail can appear together;
- extra-wide: add a supporting pane only when it helps the current item.

Selection is product state. Do not recreate it independently inside each size-specific branch. Define what happens when the selected item disappears, becomes unavailable, or is filtered out.

### Supporting pane

Use when secondary content assists the main task but is not the main destination, such as context, properties, help, or activity.

- keep the primary pane visually dominant;
- allow dismissal or collapse when appropriate;
- restore focus sensibly when the pane closes;
- do not turn unrelated content into a permanent third column just because space exists.

## Pane strategy

Material guidance commonly recommends:

Use this table only when the repository has no existing pane policy. Content minimums, reading measure, and target ergonomics decide the actual behavior.

| Window context | Typical pane count |
|---|---:|
| Compact | 1 |
| Medium | 1, or 2 for low-density content |
| Expanded and large | 2 |
| Extra large | up to 3 |

This is a design starting point. The content's minimum useful width, reading measure, density, and product workflow decide the real policy.

For each pane define:

- purpose and semantic heading;
- minimum useful size;
- preferred and maximum size;
- resize behavior;
- scrolling owner;
- selection and back behavior;
- focus entry and restoration;
- loading, empty, and error behavior;
- whether it remains mounted when hidden.

Avoid nested independent scrolling unless the relationship is clear and keyboard users can move between regions predictably.

## Navigation adaptation

Use stable top-level destination identity across presentations:

| Available space | Common presentation |
|---|---|
| Compact | navigation bar or contained drawer |
| Medium | compact rail or navigation bar based on content |
| Expanded | navigation rail, expanded rail, or persistent drawer |
| Large and extra large | rail or drawer plus multi-pane content |

The exact choice belongs to the product navigation owner.

Rules:

- preserve destination order and labels;
- preserve the selected destination across resize;
- do not create separate navigation stacks per window class;
- keep three to five destinations for a compact navigation bar;
- keep three to seven primary destinations for a rail;
- use tabs for peer categories within a destination, not unrelated app areas;
- expose overflow destinations through one predictable route;
- keep the primary action distinct from navigation;
- verify back, escape, window close, and deep-link behavior through the runtime owner.

Current expressive Material guidance includes expanded and collapsible navigation presentations. Verify artifact and target availability before choosing a named Compose API.

## Insets, posture, and safe regions

Treat insets as input to layout, not a fixed padding constant.

- Respect safe drawing regions and platform system UI.
- Avoid placing essential controls behind cutouts, hinges, rounded window corners, or draggable title regions.
- Let immersive or edge-to-edge imagery extend only when foreground contrast and input remain safe.
- On foldables, treat a separating hinge as a real boundary.
- On desktop, account for window decorations and minimum resize dimensions.
- On iOS, verify software keyboard and safe-area behavior on device or simulator.

Use platform-specific APIs only at the integration boundary. Keep the product rule, such as which pane may move around a hinge, in shared policy when it is truly shared.

## Implementation ownership

Prefer:

- one state owner;
- one destination model;
- one semantic layout policy;
- size-specific rendering that consumes the same state;
- stable component keys and preserved scroll or selection state where the product expects it;
- a project-owned breakpoint function with pure tests.

Portable primitives such as constraint-aware composition can implement many adaptive behaviors. Verify the exact API in the installed version. Do not add an adaptive library solely to obtain a component name when the existing project policy already handles the behavior clearly.

When a platform lacks a shared artifact:

1. keep the design policy platform-neutral;
2. use stable common primitives if practical;
3. otherwise add a narrow platform implementation through the existing source-set boundary;
4. test parity at the behavior level, not pixel identity.

## Resize and boundary testing

For each active breakpoint:

- test just below, exactly at, and just above the boundary;
- resize continuously while content is selected, edited, loading, or showing an error;
- verify no duplicated events, lost selection, reset form, or scroll jump;
- verify focus order after a pane appears, disappears, or repositions;
- verify the primary action remains visible and unique;
- verify long text, large text, and RTL at the narrowest valid pane;
- test portrait and landscape where those configurations are supported;
- test window restoration and minimum size on desktop.

Record the actual widths and targets reviewed. A preview at one representative width is not adaptive proof.
