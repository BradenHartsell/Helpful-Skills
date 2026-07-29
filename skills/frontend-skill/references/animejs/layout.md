# Layout (FLIP) Reference

**Since:** v4.3.0

Automatically animates between two HTML layout states (FLIP: First, Last, Invert, Play). Enables smooth animation of properties that are normally hard to animate (CSS `display`, flex direction, grid settings, DOM order, etc.).

## Creation

```js
import { createLayout } from 'animejs';
// or: import { createLayout } from 'animejs/layout';

const layout = createLayout(root, parameters);
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `root` | CSS selector / DOM element | Target container |
| `parameters` | Object (optional) | Layout settings + States parameters |

## Methods

### `layout.record()`
Captures current layout state as the "before" snapshot. Call before making DOM/layout changes.
```js
layout.record();
// Make your DOM changes here
layout.animate();
```

### `layout.animate(parameters?)`
Compares last `record()` with current DOM measurements and animates changes.
- Optional parameters override default timing/easing
- Returns: Timeline (supports `.then()`)

### `layout.update(callback, parameters?)`
One-call helper: `record()` + DOM mutation callback + `animate()`.
```js
layout.update(({ root }) => {
  root.dataset.grid = (currentGrid + 1) % 4 + 1;
}, {
  duration: 1000,
  delay: stagger(150),
});
```
**Gotcha:** May not work in all frameworks. Use manual `record()`/`animate()` combo if issues arise.

### `layout.revert()`
Completes all running layout animations instantly, reverts DOM to actual current state.

## Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `children` | `'*'` | Elements to track (selector, element, NodeList, Array) |
| `delay` | `0` | Number or Function (supports `stagger()`) |
| `duration` | `350` | Number or Function (supports `stagger()`) |
| `ease` | `'inOut(3.5)'` | Easing function/string |
| `properties` | `['opacity', 'fontSize', 'color', 'backgroundColor', 'borderRadius', 'border', 'filter', 'clipPath']` | Additional CSS properties to measure and animate. Position/dimensions always handled internally. |

## States Parameters

Properties applied during specific transition phases:

### `enterFrom`
Default: `{ opacity: 0 }`
Initial properties for elements entering (becoming visible from `display:none`, `visibility:hidden`, or newly added to DOM).

### `leaveTo`
Default: `{ opacity: 0 }`
Final properties for elements leaving (becoming hidden).

### `swapAt`
Default: `{ opacity: 0, ease: 'inOut(1.75)' }`
Mid-transition properties for non-animated children. Interpolates to these at 50%, then back to computed state.

**CRITICAL GOTCHA:** `enterFrom`, `leaveTo`, and `swapAt` do NOT support CSS transform shorthands (`scale`, `rotate`, `x`, `y`). Use full `transform` strings:
```js
// BAD
enterFrom: { scale: 0 }
// GOOD
enterFrom: { transform: 'scale(0)' }
```

## Properties (AutoLayout instance)

| Property | Description |
|----------|-------------|
| `params` | Configuration object |
| `root` | Resolved root HTMLElement |
| `children` | Selector(s) for tracked elements |
| `properties` | Set of CSS property names being interpolated |
| `oldState` | Previous measurements (LayoutSnapshot) |
| `newState` | Latest measurements (LayoutSnapshot) |
| `timeline` | Timeline from last `.animate()` / `.update()` |
| `animating` | Nodes animated in latest `.animate()` |
| `swapping` | Nodes swapped in latest `.animate()` |
| `entering` | Nodes entering in latest `.animate()` |
| `leaving` | Nodes leaving in latest `.animate()` |

`entering`, `leaving`, `swapping` arrays are cleared and repopulated on every `.animate()` call.

## `data-layout-id` Attribute

Enables animation between elements in different parts of the DOM without cloning/moving.

```js
$itemA1.dataset.layoutId = "item-A";
$itemA2.dataset.layoutId = "item-A";
$itemA2.classList.add('is-hidden');

layout.update(({ root }) => {
  $itemA1.classList.toggle('is-hidden');
  $itemA2.classList.toggle('is-hidden');
});
```

## Common Gotchas

1. **Unexpected fading of elements:** Descendants of `children` targets that aren't targets themselves swap at 50% and may fade to opacity 0. **Fix:** Add to `children` selector, or set `swapAt: { opacity: 1 }`.

2. **Root element position "jumps":** Root position is never animated. Root dimensions CAN be animated. **Fix:** Use parent element as root.

3. **Text jumping during transition:** Animating `fontSize` alongside `width`/`height` causes reflow (especially Firefox). **Fix:** Use `white-space: nowrap`.

4. **Transform shorthands don't work in state params:** Use `transform: 'scale(0)'` not `{ scale: 0 }`.

5. **SVG elements are NOT animated:** Only HTML elements are tracked.

6. **Inline text elements not moving:** Elements adjacent to text nodes are excluded. **Fix:** Wrap text in `<span>` tags.

## Example

```js
import { createLayout, stagger } from 'animejs';

const layout = createLayout('.layout-container', {
  children: '.card',
  duration: 400,
  ease: 'inOut(3.5)',
  enterFrom: { opacity: 0, transform: 'scale(0.8)' },
  leaveTo: { opacity: 0, transform: 'scale(1.2)' },
});

let i = 0;
function animateLayout() {
  layout.update(({ root }) => {
    root.dataset.grid = (++i % 4) + 1;
  }, {
    duration: 1000,
    delay: stagger(150),
    onComplete: () => animateLayout(),
  });
}
animateLayout();
```
