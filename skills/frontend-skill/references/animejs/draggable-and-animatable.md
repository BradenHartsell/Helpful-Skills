# Draggable and Animatable Reference

## Draggable

Adds physics-based drag interactions to DOM elements.

```js
import { createDraggable } from 'animejs';
// or: import { createDraggable } from 'animejs/draggable';

const draggable = createDraggable(target, parameters);
```

### Axes Parameters

Can be global (all axes) or per-axis via object.

```js
createDraggable('.box', {
  x: { snap: 100 },           // per-axis x
  y: { snap: 50 },            // per-axis y
  snap: 56,                   // global snap
  modifier: utils.wrap(-200, 0), // global modifier
});
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `x` | - | Configure x axis (object) |
| `y` | - | Configure y axis (object) |
| `snap` | `0` | Number (round to increment), Array (closest from list), or Function (auto-refreshes on resize) |
| `modifier` | `noop` | Alters axis value (e.g., `utils.wrap(-128, 128)`) |
| `mapTo` | `null` | Maps drag to custom property (`'rotateY'`, `'z'`, etc.) instead of x/y |

#### `snap` examples
```js
snap: 56                    // round to nearest 56
x: { snap: [0, 200] }       // closest from array
snap: () => calculateSnap() // dynamic, auto-refreshes
```

#### `mapTo` examples
```js
createDraggable('.card', {
  x: { mapTo: 'rotateY' },  // x drag controls rotation
  y: { mapTo: 'z' },        // y drag controls depth
});
```

### Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `trigger` | - | Different element to trigger drag |
| `container` | `null` | CSS selector / HTMLElement / `[top,right,bottom,left]` / Function (auto-refreshes) |
| `containerPadding` | `0` | Number / `[t,r,b,l]` / Function |
| `containerFriction` | `0.8` | 0=no friction, 1=can't leave bounds |
| `releaseContainerFriction` | - | Friction after release when out of bounds |
| `releaseMass` | - | Mass for release spring |
| `releaseStiffness` | `80` | Post-release stiffness (no effect if spring passed to releaseEase) |
| `releaseDamping` | `10` | Post-release damping (no effect if spring passed to releaseEase) |
| `velocityMultiplier` | `1` | 0=no velocity, 2=double |
| `minVelocity` | - | Minimum velocity |
| `maxVelocity` | - | Maximum velocity |
| `releaseEase` | `eases.outQuint` | Easing for release. Spring overrides releaseMass/Stiffness/Damping |
| `dragSpeed` | `1` | 0=can't drag, <0=inverted |
| `dragThreshold` | `{mouse:3, touch:7}` | Pixels before drag triggers (v4.2.1+) |
| `scrollThreshold` | `20` | Pixels beyond bounds before auto-scroll |
| `scrollSpeed` | - | Auto-scroll speed |
| `cursor` | `{onHover:'grab', onGrab:'grabbing'}` | Cursor styles. false=disabled. Only on (pointer:fine) |

Many settings accept a Function that auto-refreshes on resize. Manually refresh via `draggable.refresh()`.

### Callbacks

| Callback | Fires When |
|----------|-----------|
| `onGrab` | Element first grabbed |
| `onDrag` | Continuously while dragging |
| `onUpdate` | On every position update |
| `onRelease` | User releases |
| `onSnap` | Element snaps to grid/target |
| `onSettle` | All movement after release finishes |
| `onResize` | Draggable element resized |
| `onAfterResize` | Resize fully completes |

### Methods

| Method | Purpose |
|--------|---------|
| `disable()` | Disable dragging |
| `enable()` | Re-enable |
| `setX(value)` | Set x programmatically |
| `setY(value)` | Set y programmatically |
| `stop()` | Stop current movement |
| `reset()` | Reset to initial state |
| `revert()` | Revert + cleanup |
| `refresh()` | Recalculate bounds/dynamic values |
| `animateInView()` | Animate into view |
| `scrollInView()` | Scroll into view |

### Key Properties

**Position:** `x`, `y`, `progressX`, `progressY`, `destX`, `destY`, `deltaX`, `deltaY`
**Velocity:** `velocity`, `pointerVelocity`, `maxVelocity`, `minVelocity`, `velocityMultiplier`
**Container:** `containerBounds`, `containerFriction`, `containerPadding`, `contained`
**State:** `enabled`, `grabbed`, `dragged`, `released`, `fixed`, `initialized`
**Coordinates:** `coords`, `pointer`, `scroll`, `angle`, `pointerAngle`
**Bounds:** `targetBounds`, `scrollBounds`, `dragArea`, `window`

### Gotchas
- `releaseStiffness`/`releaseDamping` have NO effect if `spring()` passed to `releaseEase`
- `releaseEase` default is `eases.outQuint`; spring's `velocity` is always replaced with actual drag velocity
- `containerFriction: 1` prevents leaving bounds entirely
- Container array format is `[top, right, bottom, left]` (CSS ordering)
- `dragSpeed: 0` prevents dragging; negative inverts
- Use `refresh()` after DOM changes to recalculate

---

## Animatable

Efficiently animates properties for high-frequency updates (cursor events, real-time interactions).

```js
import { createAnimatable } from 'animejs';
// or: import { createAnimatable } from 'animejs/animatable';

const animatable = createAnimatable(targets, parameters);
```

**Use this instead of `animate()` or `utils.set()` when the same properties change frequently.**

### Settings

Global or per-property (via object):

```js
createAnimatable('.follower', {
  x: { unit: 'rem', duration: 400, ease: 'out(4)' },
  y: 500,              // shorthand: duration only
  ease: 'out(2)',      // global
});
```

| Setting | Default | Description |
|-----------|---------|-------------|
| `unit` | - | Per-property CSS unit (`'px'`, `'deg'`, `'rad'`, `'%'`) |
| `duration` | `1000` | Transition duration (ms). 0=immediate set |
| `ease` | `'out(2)'` | Recommend `out` type easings |
| `modifier` | `noop` | Transforms value before application |

### Methods

#### Getters (no arguments)
```js
animatable.x();     // returns Number or Array<Number>
```

#### Setters (with value)
```js
animatable.x(100);                          // animate to 100
animatable.x(100, 250);                     // override duration to 250ms
animatable.x(100, 250, 'out(4)');           // override duration and ease
animatable.x(100).y(200);                   // chain multiple properties
animatable.backgroundColor([164, 255, 79]); // multi-component (RGB)
```
**Returns:** The animatable instance (chainable)

#### `revert()` - Destroy and cleanup
```js
animatable.revert();
```

### Properties

| Property | Description |
|----------|-------------|
| `targets` | Get targets (read-only) |
| `animations` | Get all Animation instances (read-only) |

### Example: Cursor tracking
```js
import { createAnimatable, utils } from 'animejs';

const cursor = createAnimatable('.follower', {
  x: { duration: 400, ease: 'out(3)' },
  y: { duration: 400, ease: 'out(3)' },
});

document.addEventListener('mousemove', e => {
  cursor.x(e.clientX);
  cursor.y(e.clientY);
});

// Cleanup when done
cursor.revert();
```

### Example: Snapped rotation
```js
const PI = Math.PI;
const clock = createAnimatable('.clock', {
  rotate: { unit: 'rad' },
  modifier: utils.snap(PI / 10),  // snap to PI/10 increments
  duration: 0,                     // immediate, no tweening
});
```

### Gotchas
- **Only Number/Array<Number> values** for property functions (use `unit` setting for units)
- `duration: 0` = immediate set without tweening (real-time tracking)
- Setters return the instance for chaining
- Use `revert()` to fully destroy and remove inline styles
- For multi-component properties (RGB), pass `Array<Number>`
