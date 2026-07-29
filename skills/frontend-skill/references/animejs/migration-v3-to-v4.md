# Migration: anime.js v3 to v4

v4 is a complete rewrite. This guide covers all breaking changes.

## Import Changes

```diff
- import anime from 'animejs';
+ import { animate } from 'animejs';

- anime({ targets: 'div', translateX: 250 })
+ animate('div', { translateX: 250 })
```

The global `anime` object is gone. `targets` is now the first argument of `animate()`.

No default export. Use named imports:
```js
import { animate, stagger, createTimeline, utils, onScroll,
  createDraggable, createScope, spring, svg, text, createLayout,
  engine, waapi } from 'animejs';
```

## Property Parameter Renames

| v3 | v4 | Notes |
|----|-----|-------|
| `endDelay` | `loopDelay` | Not 1:1. `loopDelay` only delays between loops, not after last iteration |
| `easing` | `ease` | Function names shortened (remove `'ease'` prefix) |
| `value` (object syntax) | `to` | For per-property parameters |
| `round` | `modifier: utils.round(n)` | Takes decimal length, not multiplier |

Default easing changed to `'out(2)'`.

```diff
- easing: 'easeOutQuad',
+ ease: 'outQuad',

- opacity: { value: .5, duration: 250 },
+ opacity: { to: 1, duration: 250 },

- round: 100,
+ modifier: utils.round(2),
```

## Animation Parameter Changes

| v3 | v4 | Notes |
|----|-----|-------|
| `direction: 'reverse'` | `reversed: true` | Split into separate parameters |
| `direction: 'alternate'` | `alternate: true` | |

### Loop behavior change (critical)

```diff
- loop: 1  // v3: 1 iteration total
+ loop: 1  // v4: 1 repeat = 2 iterations total

- loop: 0  // v3: no animation
+ loop: 0  // v4: play once (no repeat)

- loop: true  // v3: infinite
+ loop: true  // v4: infinite (same)
```

## Keyframes

```diff
- opacity: [{ value: .5 }, { value: 1 }, { value: .5 }],
+ opacity: [{ to: .5 }, { to: 1 }, { to: .5 }],
```

## Timeline Changes

```diff
- const tl = anime.timeline({ easing: 'easeOutQuad', duration: 250 }),
+ const tl = createTimeline({ defaults: { ease: 'outQuad', duration: 250 } }),
```

Child `loop` parameter now properly works and can mix with timeline's own loop.

## Playback Control Changes

| v3 | v4 | Notes |
|----|-----|-------|
| `play()` | `play()` | Now always plays forwards, even if reversed |
| `reverse()` | `reverse()` | Now always plays backwards (doesn't toggle) |
| - | `.resume()` | NEW: resumes in previous direction |
| - | `.alternate()` | NEW: plays in opposite direction |

## Callback Renames

All callbacks now use `on` prefix:

| v3 | v4 | Notes |
|----|-----|-------|
| `update` | `onUpdate` | |
| `begin` | `onBegin` | Now called after delay completes (was immediate in v3) |
| `complete` | `onComplete` | |
| `change` | `onRender` | Called when animation values change |
| `loopBegin` + `loopComplete` | `onLoop` | Merged into single callback |
| `changeBegin` / `changeComplete` | **Removed** | |

## Promise API

```diff
- anime({...}).finished.then(() => {})
+ animate(target, options).then(() => {})
```

## SVG Helper Changes

| v3 | v4 |
|----|-----|
| `anime.path()` | `svg.createMotionPath()` |
| `anime.setDashoffset()` | `svg.createDrawable()` |

```diff
- const { x, y, angle } = anime.path(el),
+ const { translateX, translateY, rotate } = svg.createMotionPath(el);

- anime({ targets: 'path', strokeDashoffset: [anime.setDashoffset, 0] });
+ animate(svg.createDrawable('path'), { draw: '0 1' });
```

## Easing Changes

- All easing names lost the `ease` prefix: `easeOutQuad` becomes `outQuad`
- Default easing is now `'out(2)'`

Spring easings are no longer string-based:
```diff
- easing: 'spring(1, 80, 10, 0)',
+ ease: spring({ mass: 1, stiffness: 80, damping: 10, velocity: 0 }),
```

Custom easing functions no longer wrapped:
```diff
- easing: () => t => 1 - Math.sqrt(1 - t * t),
+ ease: t => 1 - Math.sqrt(1 - t * t),
```

## Utility Function Migration

| v3 | v4 |
|----|-----|
| `animation.remove(targets)` | `utils.remove(targets)` |
| `anime.get(target, 'prop')` | `utils.get(target, 'prop')` |
| `anime.set(target, {...})` | `utils.set(target, {...})` |
| `anime.random(50, 100)` | `utils.random(50, 100)` |
| `anime.running` | **Removed** |
| `anime.suspendWhenDocumentHidden` | `engine.pauseOnDocumentHidden` |

## New Features in v4 (no v3 equivalent)

| Feature | Purpose |
|---------|---------|
| `createScope()` | Scoping, media query reactivity, batch cleanup |
| `createDraggable()` | Physics-based drag with bounds and snapping |
| `createAnimatable()` | High-frequency property updates (cursor tracking) |
| `createLayout()` | FLIP layout animations (v4.3+) |
| `onScroll()` | ScrollObserver for scroll-triggered/synced animations |
| `splitText()` | Text splitting into lines/words/chars |
| `scrambleText()` | Scramble-and-reveal text effect (v4.4+) |
| `spring()` | Spring physics easing generator |
| `waapi.animate()` | WAAPI-powered hardware-accelerated animations |
| `engine.update()` | Manual tick for WebGL/canvas integration |
| `utils.sync()` | Execute in sync with engine frame |
| `utils.keepTime()` | Recreate animation preserving time (v4.1+) |
| Chain-able utils | `utils.clamp(0, 100).round(2).padStart(6, '0')` |

## Quick Migration Checklist

1. Change `import anime from 'animejs'` to `import { animate } from 'animejs'`
2. Change `anime({ targets: ... })` to `animate(targets, ...)`
3. Rename `easing` to `ease`, remove `ease` prefix from easing names
4. Rename `value` to `to` in per-property object syntax
5. Rename `round` to `modifier: utils.round(n)`
6. Rename callbacks: `begin` to `onBegin`, `complete` to `onComplete`, `update` to `onUpdate`, `change` to `onRender`, `loopBegin`/`loopComplete` to `onLoop`
7. Update `loop` semantics: v4 `loop: N` = N repeats (N+1 total iterations)
8. Change `.finished.then()` to `.then()`
9. Move SVG helpers: `anime.path()` to `svg.createMotionPath()`, `anime.setDashoffset()` to `svg.createDrawable()`
10. Move utilities: `anime.get/set/random` to `utils.get/set/random`
11. Update spring eases from string to `spring()` function
12. Add `scope.revert()` cleanup in framework lifecycle hooks
