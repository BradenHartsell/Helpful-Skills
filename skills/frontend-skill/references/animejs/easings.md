# Easings Reference

## Imports

```js
import { eases, cubicBezier, linear, steps, irregular, spring } from 'animejs';
// or via easings object
import { easings } from 'animejs';
```

## Built-in Eases

Specified by name string in the `ease` parameter. v4 names do NOT have the `ease` prefix.

| Type | Variants | Parameters |
|------|----------|------------|
| Linear | `'linear'` | - |
| Power | `'in'`, `'out'`, `'inOut'`, `'outIn'` | `power = 1.675` |
| Quad | `'inQuad'`, `'outQuad'`, `'inOutQuad'`, `'outInQuad'` | - |
| Cubic | `'inCubic'`, `'outCubic'`, `'inOutCubic'`, `'outInCubic'` | - |
| Quart | `'inQuart'`, `'outQuart'`, `'inOutQuart'`, `'outInQuart'` | - |
| Quint | `'inQuint'`, `'outQuint'`, `'inOutQuint'`, `'outInQuint'` | - |
| Sine | `'inSine'`, `'outSine'`, `'inOutSine'`, `'outInSine'` | - |
| Exponential | `'inExpo'`, `'outExpo'`, `'inOutExpo'`, `'outInExpo'` | - |
| Circular | `'inCirc'`, `'outCirc'`, `'inOutCirc'`, `'outInCirc'` | - |
| Bounce | `'inBounce'`, `'outBounce'`, `'inOutBounce'`, `'outInBounce'` | - |
| Back | `'inBack'`, `'outBack'`, `'inOutBack'`, `'outInBack'` | `overshoot = 1.70158` |
| Elastic | `'inElastic'`, `'outElastic'`, `'inOutElastic'`, `'outInElastic'` | `amplitude = 1`, `period = .3` |

### Parameter syntax in strings
```js
ease: 'inOut(3)'                  // power of 3
ease: 'outElastic(.8, 1.2)'       // custom amplitude and period
ease: eases.outElastic(.8, 1.2)   // via eases object
```

## Cubic Bezier

```js
import { cubicBezier } from 'animejs';

// JS
animate(el, { x: 100, ease: cubicBezier(0, 0, 0.58, 1) });

// WAAPI (string-based, Safari HW-acceleration safe)
waapi.animate(el, { x: 100, ease: 'cubic-bezier(0, 0, .58, 1)' });
```

Parameters: `cubicBezier(x1, y1, x2, y2)` where x1/x2 must be 0-1, y1/y2 can be any value (negative = anticipation, >1 = overshoot).

## Linear Easing (v4)

```js
import { linear } from 'animejs';
animate(el, { x: 100, ease: linear(0, '0.5 50%', '0.3 75%', 1) });
// WAAPI: ease: 'linear(0, 0.5 50%, 0.3 75%, 1)'
```

Values outside 0-1 create overshoot. Percentages define timing position.

## Steps

```js
import { steps } from 'animejs';
animate(el, { x: 100, ease: steps(5) });        // 5 steps, change at end
animate(el, { x: 100, ease: steps(5, true) });  // 5 steps, change at start
// WAAPI: ease: 'steps(5)' or 'steps(5, start)'
```

## Irregular (v4)

Randomized linear interpolation between points.

```js
import { irregular } from 'animejs';
animate(el, { x: 100, ease: irregular(10, 1.5) }); // 10 steps, randomness 1.5
```

## Spring Physics

The `spring()` method generates a spring curve easing function with its corresponding duration.

**Critical:** The animation's `duration` is **overridden** by the spring's calculated settling duration.

### Perceived Parameters (SwiftUI model)

```js
import { spring } from 'animejs';
animate(el, { x: 100, ease: spring({ bounce: 0.5, duration: 350 }) });
```

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `bounce` | -1 to 1 | 0.5 | 0-1=bouncy, below 0=over-damped. Keep between -0.5 and 0.5 |
| `duration` | 10-10000 | 628 | Perceived duration in ms |

### Physics Parameters

```js
animate(el, { x: 100, ease: spring({ stiffness: 100, damping: 10, mass: 1, velocity: 0 }) });
```

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `mass` | 1-10000 | 1 | Higher = more inertia, slower |
| `stiffness` | 0-10000 | 100 | Higher = tighter spring, faster response |
| `damping` | 0-10000 | 10 | Higher = less bounce, faster decay |
| `velocity` | -10000 to 10000 | 0 | Initial velocity. Positive = running start |

### Perceived `onComplete`

Only works with JS `animate()`, not `waapi.animate()`.

```js
animate(el, {
  x: 100,
  onComplete: () => console.log('settling duration reached'),
  ease: spring({
    bounce: 0.25,
    duration: 350,
    onComplete: () => console.log('perceived duration reached'),
  })
});
```

### Spring gotchas
- Spring **overrides** animation `duration`
- Keep `bounce` between -0.5 and 0.5 when using perceived parameters
- `spring.onComplete` fires at perceived duration; `animation.onComplete` at settling duration
- Spring works with WAAPI (`waapi.animate`)
- `waapi.convertEase(spring.ease)` converts to WAAPI-compatible linear() string

## Choosing the right easing

| Use case | Easing | Why |
|----------|--------|-----|
| Element entering | `'out(3)'` / `'outExpo'` | Fast start, slow settle |
| Element leaving | `'in(3)'` / `'inExpo'` | Slow start, fast exit |
| State toggle | `'inOut(3)'` / `'inOutQuad'` | Symmetric, balanced |
| Bounce/impact | `spring({ bounce: 0.4 })` | Physics = organic |
| Mechanical/UI | `'inOut(2)'` | Subtle, predictable |
| Playful/emphasis | `'outBack'` / `'outElastic'` | Overshoot = personality |
| Linear/constant speed | `'linear'` | Only for mechanical/progress |
| Stepped/discrete | `steps(5)` | Jump between values |
| Custom curve | `cubicBezier(...)` | Precise control |
