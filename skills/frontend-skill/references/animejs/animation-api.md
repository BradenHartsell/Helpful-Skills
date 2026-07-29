# Animation API Reference

Complete API for `animate()` and `waapi.animate()`.

## Imports

```js
import { animate } from 'animejs';           // or 'animejs/animation'
import { waapi } from 'animejs';              // or 'animejs/waapi'
```

## Signature

```js
const animation = animate(targets, parameters);
const animation = waapi.animate(targets, parameters);
```

- `targets`: CSS Selector, DOM Element, JS Object, or Array of targets
- `parameters`: Object containing animatable properties, tween parameters, playback settings, callbacks
- Returns: `JSAnimation` or `WAAPIAnimation`

## Target Types

| Type | Example |
|------|---------|
| CSS Selector | `'.square'` |
| DOM Element | `$element` |
| JS Object | `{ x: 0, y: 0 }` |
| Array | `['.el1', $el2, { x: 0 }]` (mix of types) |

## Animatable Properties

| Category | Examples |
|----------|---------|
| CSS Properties | `opacity`, `backgroundColor`, `width`, `height` |
| CSS Transforms | `translateX`, `translateY`, `scale`, `rotate`, `x`, `y` |
| CSS Variables | `--custom-property` |
| JS Object Properties | Any numeric property |
| HTML Attributes | `data-*`, `value` |
| SVG Attributes | `cx`, `cy`, `r`, `points` |

## Tween Value Types

| Type | Example | Notes |
|------|---------|-------|
| Numerical | `100` | Standard numbers |
| Unit conversion | `'6rem'` | CSS unit transformations |
| Relative | `'+=.25'` / `'-=10'` | Relative to current value |
| Color | `'#ff0000'` | Auto-interpolated |
| Color function | `'rgb(255, 0, 0)'` | CSS color function |
| CSS variable | `'var(--my-var)'` | Custom property reference |
| Function-based | `$el => $el.dataset.y` | Dynamic per-target values |

## Tween Parameters

Can be global (all properties) or local (per-property via object).

### `to` (required if no `from`)
```js
x: { to: 100 }           // animate to 100
x: { to: '16rem' }       // with unit
x: { to: [0, 100] }      // [from, to] shorthand
```

### `from` (required if no `to`)
```js
opacity: { from: 0.5 }   // from 0.5 to current value
```

### `delay`
- Default: `0`
- Accepts: Number >= 0 or function-based value

### `duration`
- Default: `1000`
- Accepts: Number >= 0 or function-based value
- `0` = instant completion, clamped to `1e12` (~32 years)

### `ease`
- Default: `'out(2)'`
- Accepts: easing string, easing function, or function-based value

### `composition`
- Default: `'replace'` (or `'none'` if >= 1000 targets in JS version)
- Options: `'replace'` (0), `'none'` (1), `'blend'` (2)

| Mode | Description |
|------|-------------|
| `'replace'` | Replace and cancel running animation on same target+property |
| `'none'` | Don't replace; previous continues. Better performance |
| `'blend'` | Additive, blending values. Only forward, no keyframes/colors/loop/reverse |

### `modifier`
- Accepts: `Function(value)` returning Number
- String units preserved automatically
- Most `utils.*` functions work as modifiers

```js
modifier: utils.round(0)              // round to 0 decimals
modifier: v => v % 17                 // modulo
modifier: utils.clamp(0, 100).round(2) // chain-able
```

## Keyframes

### Property Value Keyframes (single property)
```js
// Array of values
animate('.box', { x: [0, 100, 200], duration: 3000 });

// Array of objects with per-keyframe settings
animate('.box', {
  x: [{ to: 100, ease: 'inQuad' }, { to: 200, ease: 'outQuad' }],
  duration: 3000,
});
```

### Animation Keyframes (multiple properties)
```js
// Duration-based (split evenly)
animate('.box', {
  keyframes: [
    { x: 100, y: 100 },
    { x: 200, y: 200 },
  ],
  duration: 3000,
});

// Percentage-based
animate('.box', {
  keyframes: {
    '0%': { x: 0, y: 0 },
    '50%': { x: 100, y: 100 },
    '100%': { x: 200, y: 200 },
  },
  duration: 3000,
});
```

## Playback Settings

| Setting | Default | Notes |
|---------|---------|-------|
| `delay` | `0` | Global delay for all tweens |
| `duration` | `1000` | Global duration |
| `loop` | `0` | 0=once, true/infinity=infinite, N=N repeats |
| `loopDelay` | `0` | Delay between loops (not before first) |
| `alternate` | `false` | Reverse each iteration (needs loop > 0) |
| `reversed` | `false` | Initial direction reversed |
| `autoplay` | `true` | false=manual, onScroll()=scroll-triggered |
| `frameRate` | `240` | JS only. Per-animation FPS, capped to monitor |
| `playbackRate` | `1` | Speed multiplier. 0=won't play |
| `playbackEase` | `null` | JS only. Easing across entire playback |
| `persist` | `false` | WAAPI only. Keeps animation active after completion |

### `playbackEase` vs `ease`
```
ease (per keyframe):    0 --ease-> A --ease-> B --ease-> C
playbackEase (global):  0 ------ease----------> A -> B -> C
```

## Callbacks

All receive the animation instance (`self`) as first argument.

| Callback | JS | Fires When |
|----------|-----|-----------|
| `onBegin` | Y | Animation begins (after delay) |
| `onComplete` | - | All iterations finished |
| `onBeforeUpdate` | Y | Before tween values update, every frame |
| `onUpdate` | Y | Every frame at specified frameRate |
| `onRender` | Y | When rendered to screen (NOT during delay/loopDelay) |
| `onLoop` | Y | Each iteration completes |
| `onPause` | - | Paused, cancelled, reverted, replaced, or targets removed |
| `then()` | - | Promise resolves on completion |

**Key distinctions:**
- `onUpdate` fires every frame regardless of rendering
- `onRender` fires only when actual screen rendering occurs
- `onPause` fires automatically on cancel/revert/replacement/target removal

## Methods

All chainable (return the animation instance).

| Method | Purpose |
|--------|---------|
| `play()` | Start/resume forward (always forward, even if reversed) |
| `pause()` | Pause |
| `resume()` | Resume from paused state (current direction) |
| `restart()` | Restart from beginning |
| `reverse()` | Reverse direction |
| `alternate()` | Toggle forward/reverse |
| `complete()` | Jump to end |
| `cancel()` | Cancel playback |
| `revert()` | Revert to initial state |
| `reset(softReset)` | Pause + reset state. softReset=true = no visual render |
| `seek(time, muteCallbacks)` | Set currentTime (ms). muteCallbacks suppresses callbacks |
| `stretch(duration)` | Change total duration, recalculates proportionally. stretch(0) normalizes all to 0 |
| `refresh()` | JS only. Re-compute function-based values |

## Properties

| Property | JS | Type | Get/Set | Description |
|----------|-----|------|---------|-------------|
| `id` | Y | String/Number | Both | Identifier |
| `targets` | - | Array | Get | Current targets |
| `currentTime` | - | Number | Both | Global current time (ms) |
| `iterationCurrentTime` | Y | Number | Both | Current iteration time (ms) |
| `deltaTime` | Y | Number | Get | Time between frames (ms) |
| `progress` | - | Number | Both | Overall progress 0-1 |
| `iterationProgress` | Y | Number | Both | Current iteration progress 0-1 |
| `currentIteration` | Y | Number | Both | Iteration count |
| `duration` | - | Number | Get | Total duration (ms) |
| `speed` | - | Number | Both | Speed multiplier |
| `fps` | Y | Number | Both | Frame rate |
| `paused` | - | Boolean | Both | Paused state |
| `began` | Y | Boolean | Both | Whether started |
| `completed` | - | Boolean | Both | Whether completed |
| `reversed` | Y | Boolean | Both | Reversed state |
| `backwards` | Y | Boolean | Get | Currently playing backwards |

## Global defaults

```js
import { engine } from 'animejs';
engine.defaults.duration = 500;
engine.defaults.ease = 'inOutCirc';
engine.defaults.composition = 'blend';
engine.defaults.loopDelay = 500;
engine.defaults.onBegin = self => console.log(self.id);
```

Configurable: `playbackEase`, `playbackRate`, `frameRate`, `loop`, `reversed`, `alternate`, `autoplay`, `duration`, `delay`, `composition`, `ease`, `loopDelay`, `modifier`, and all callbacks.
