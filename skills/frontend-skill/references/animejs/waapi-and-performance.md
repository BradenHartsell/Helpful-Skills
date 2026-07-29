# WAAPI and Performance Reference

## WAAPI Overview

`waapi.animate()` leverages the native Web Animations API for hardware-accelerated animations.

**Size:** ~3KB gzip (vs ~10KB for standard `animate()`)

```js
import { waapi } from 'animejs';
const anim = waapi.animate(targets, parameters);
```

## When to Use WAAPI vs JS

### Use `waapi.animate()` when:
- Animating transforms (`translate`, `rotate`, `scale`) and `opacity`
- Bundle size is critical
- Need smooth animations when CPU is busy (runs off main thread)
- Simple entrance/exit animations
- Hardware acceleration matters (mobile, battery)

### Use `animate()` (JS) when:
- 500+ simultaneous targets (JS handles scale better)
- Animating JS objects, Canvas, WebGL, WebGPU
- SVG path morphing, DOM attributes, CSS variables
- Complex timeline orchestration with advanced callbacks
- Need `onRender`, `onBeforeUpdate`, `deltaTime`, per-animation `frameRate`
- Need `playbackEase` across keyframes

## Hardware-Accelerated Properties

### Fully supported (all major browsers):
- `opacity`
- `transform` (and individual `translate`, `scale`, `rotate`)

### Partially supported (some browsers):
- `clip-path`
- `filter`

### Properties that trigger reflow (avoid animating):
- `top`, `left`, `right`, `bottom`
- `width`, `height`
- `margin`, `padding`
- `border-width`

## Safari Hardware Acceleration Gotcha

Safari (desktop and mobile) will NOT trigger hardware acceleration if the animation uses:
- Custom `'linear()'` easing
- All JavaScript easing functions passed to `waapi.animate()`
- Parametric eases like `'out(3)'`, `'in(3)'`, `'inOut(3)'`

**Workaround:** Use string-based cubic-bezier eases:
```js
// Won't hardware-accelerate in Safari
waapi.animate(el, { x: 200, ease: 'out(3)' });

// Works with hardware acceleration in Safari
waapi.animate(el, { x: 200, ease: 'cubic-bezier(0, 0, .58, 1)' });
```

## WAAPI Improvements over Native

| Feature | Description |
|---------|-------------|
| Sensible defaults | Pre-configured default values |
| Multi-targets | Animate multiple elements simultaneously |
| Default units | Automatic unit assignment |
| Function-based values | Dynamic values via functions |
| Individual CSS transforms | Separate translate, rotate, scale |
| Individual property parameters | Per-property configuration |
| Spring and custom easings | Advanced easing including spring physics |
| ScrollObserver integration | `autoplay: onScroll()` |
| Scope integration | Works with `createScope` |

## API Differences: Anime.js WAAPI vs Native

| Feature | Anime.js `waapi.animate()` | Native `element.animate()` |
|---------|--------------------------|---------------------------|
| Targets | Selector string `'.square'` | DOM element |
| Parameters | Single combined object | Two separate objects |
| Position | `x: 100, y: 50` (separate) | `translate: '100px 50px'` |
| Loop count | `loop: 3` (3 additional plays) | `iterations: 4` (total) |
| Direction | `alternate: true` | `direction: 'alternate'` |
| Easing | `ease: 'out'` | `easing: 'ease-out'` |
| Completion | Callbacks / promises | `finished` promise |

**Loop semantics gotcha:** `loop: 3` = 4 total plays (1 + 3 repeats), vs native `iterations: 4`.

## `waapi.convertEase()`

Converts any JS easing function to a WAAPI-compatible `linear()` string.

```js
import { waapi, spring } from 'animejs';
const mySpring = spring({ stiffness: 12 });
const linearEasing = waapi.convertEase(mySpring.ease);
```

Use with native `element.animate()`:
```js
$el.animate(
  { translate: '17rem' },
  { easing: waapi.convertEase(springs[i].ease), duration: springs[i].duration, fill: 'forwards' }
);
```

## WAAPI-Specific Features

### `persist` (v4.2.0+)
WAAPI animations are auto-canceled on completion by default. Use `persist: true` to keep them active:
```js
waapi.animate(el, { x: 250, persist: true });
```
Scroll-controlled WAAPI animations auto-enable `persist`.

## Performance Best Practices

### DO:
- Animate `translateX/Y`, `scale`, `opacity` (GPU-accelerated)
- Batch similar animations: one `animate()` call for multiple targets
- Use `will-change: transform, opacity` for complex animations (remove when done)
- Set `autoplay: false` for scroll-controlled animations
- Use `waapi.animate()` for simple transform/opacity
- Consider `engine.frameRate` to cap FPS on low-end devices
- Use `composition: 'none'` for better performance with many targets

### AVOID:
- Animating layout properties (`top`, `left`, `width`, `height`, `margin`, `padding`)
- Animating 1000+ elements simultaneously
- Passing JS easing functions to `waapi.animate()` (defeats HW acceleration)
- Creating new animation instances on every render/frame (reuse existing)
- Overusing `will-change` (memory cost)

## Engine Configuration

```js
import { engine } from 'animejs';

engine.frameRate = 60;                    // cap global FPS
engine.speed = 0.5;                       // global slow-mo
engine.precision = 4;                     // decimal places for string values
engine.pauseOnDocumentHidden = true;      // pause on tab hidden (default)
engine.timeUnit = 'ms';                   // 'ms' or 's'
```

### Manual tick (WebGL/Canvas integration)
```js
engine.useDefaultMainLoop = false;

function render() {
  engine.update();              // manually tick anime.js
  renderer.render(scene, camera); // render your scene
}
renderer.setAnimationLoop(render);
```

### Runtime mutation
```js
// Change FPS/speed at runtime (wrap in utils.sync for proper timing)
utils.sync(() => animation.speed = 0.5);
utils.sync(() => engine.fps = 30);
```

## Performance Comparison Summary

| Aspect | WAAPI | JS Engine |
|--------|-------|-----------|
| Thread | Off main thread (compositor) | Main thread (rAF) |
| CPU impact | Smooth when CPU busy | Janky when CPU busy |
| Power | Lower consumption | Higher consumption |
| Properties | Limited set | Any animatable property |
| Safari easing | No HW accel with custom eases | N/A |
| Large targets | Weaker | Better for >500 |
| Bundle size | 3KB | 10KB |
