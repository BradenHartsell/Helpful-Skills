# Frontend Quality Standards

Apply these standards across projects. Derive brand-specific facts from the active brief and repository; never import branding, product claims, personas, geography, or vocabulary from an unrelated project.

## Reference fidelity

- Inspect interactive references by scrolling, clicking, and testing responsive behavior.
- Do not extrapolate an entire experience from one screenshot, still, or looping clip.
- Borrow principles and interaction models while preserving the active product's identity.
- Treat moodboards as thematic evidence, not literal page layouts.

## Brand and copy

- Preserve specific brand personality instead of defaulting to generic premium SaaS or fashionable AI styling.
- Prefer concrete utility to cinematic abstraction. A headline must explain why the capability matters.
- Remove prototype commentary such as "demo," "concept," or instructions to admire the design unless the page is explicitly an internal prototype.
- Use accent color surgically and consistently.
- Remove arbitrary decorative symbols and effects that do not add meaning, orientation, or recognizable brand value.
- Keep copy warm when appropriate, but never use personality to obscure state, proof, limitations, or consequences.

## Truthful examples

- Keep visible UI state internally consistent.
- If data or files are already present, responses must acknowledge them rather than request them again.
- After submission, clear the input unless retaining it is intentional and clearly communicated.
- Do not display inactive controls as though they work.
- Use coherent scenarios whose source material, actions, timeline, and result agree.
- Clearly distinguish examples from defaults and user-customizable concepts from predefined choices.
- Do not imply capabilities beyond the approved product model.

## Responsive composition

- Design mobile as its own composition, not a compressed desktop.
- Treat tablet and small-laptop widths as a first-class composition. A breakpoint must not combine mobile visibility rules with desktop track sizing or placement.
- Keep safe bands around common device and zoom-equivalent widths. Media queries may evaluate fractional CSS pixels while browser APIs report rounded widths; both adjacent layouts must remain valid if an exact boundary resolves to either side.
- If a breakpoint shows or hides a grid child, assign explicit grid areas, rows, or columns to every affected sibling. Do not let auto-placement move a primary panel into an implicit row or squeeze it into a rail-width track.
- Never introduce unintended horizontal page scrolling.
- Avoid inner scrollbars in bubbles, composers, cards, and primary storytelling panels.
- Keep mobile sections compact enough that the user retains context; eliminate large empty regions and excessive sticky distances.
- Use shared spacing tokens and avoid doubled gaps from adjacent section padding.
- Include fixed headers in hero viewport budgets and anchor offsets.
- Verify real text wraps, line spacing, clipping, and tap-target sizes.
- Maintain accessible contrast over every surface and image.

## Stable mutations

- Keep the outer surface stable while state changes inside it whenever practical.
- Measure every possible state before choosing the layout strategy.
- Prefer normalized subregions, overlapping exclusive panels, local minimum heights, shared layout/FLIP, or measured height transitions.
- Do not fix the entire card to an extreme tallest state if that produces dead space on smaller screens.
- Do not let transient work/loading states collapse and re-expand the final surface.
- Keep controls and the stage's top edge anchored during necessary size changes.
- Make mutation motion brief, interruptible, and compatible with reduced motion.

## Scroll and timing

- Tune scroll thresholds and progress independently for desktop and mobile.
- Trigger each state while its related content is visible and preserve enough dwell time for reading.
- Avoid late desktop transitions and accelerated mobile transitions.
- Base timing on section and viewport geometry rather than one page-wide magic number.
- Let users revisit content; motion must not make required information inaccessible.

## Accessibility

- Meet WCAG contrast and preserve visible focus.
- Use semantic controls, useful accessible names, and logical keyboard order.
- Do not rely on color alone.
- Preserve information when motion is reduced.
- Support zoom, long text, narrow screens, and touch interaction.

## State-matrix QA

- Exercise every tab, selector, disclosure, profile, send/answer action, inspector row, and navigation control.
- Measure layout before, during, and after mutation.
- Test representative phone, tablet/intermediate, and desktop widths; every layout-changing breakpoint at one pixel below and above; a short laptop viewport; a tall tablet viewport; and one 125% or 150% zoom equivalent for dense layouts.
- Record CSS viewport width, document client width, device pixel ratio, and media-query match state at critical boundaries. Screenshot pixel dimensions alone are not breakpoint evidence.
- Visit and measure every below-fold scene, not only the hero or document overflow. Add a repository gate for critical responsive invariants when the codebase supports executable validation.
- Record the primary grid/flex geometry at each layout mode and confirm all visible children occupy the intended tracks without implicit rows, leftover columns, or unexplained dead space.
- Check page overflow, inner overflow, clipping, anchor clearance, focus, contrast, tap size, and readable timing.
- Verify UI copy and displayed artifacts match the current state.
- Recheck prior accepted behavior after each subsequent correction.
