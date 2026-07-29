# Events and Scroll Reference

## Events Module

```js
import { events } from 'animejs';        // events.onScroll()
import { onScroll } from 'animejs';       // direct
import { onScroll } from 'animejs/events'; // standalone
```

## `onScroll(parameters)`

Creates ScrollObserver instances that bind animation playback to scroll behavior. Pass as the `autoplay` value.

```js
import { animate, onScroll } from 'animejs';

animate('.reveal', {
  x: '15rem',
  duration: 2000,
  autoplay: onScroll({ container, debug: true })
});
```

### Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `container` | CSS selector / HTMLElement | - | Scroll container |
| `target` | CSS selector / HTMLElement | - | Element to observe |
| `debug` | Boolean | false | Debug visualization |
| `axis` | `'x'` / `'y'` | `'y'` | Scroll axis |
| `repeat` | Boolean | - | Whether animation repeats |
| `enter` | String / Object / Number | `'end start'` | Enter threshold |
| `leave` | String / Object / Number | `'start end'` | Leave threshold |
| `sync` | Boolean / Number | false | Sync mode |

### Thresholds (`enter` / `leave`)

Determine when actions trigger based on target position within container.

**Object syntax:**
```js
enter: { target: 'top', container: 'bottom' }
leave: { target: 'bottom', container: 'top' }
```

**Container value string:**
```js
enter: 'bottom'   // target defaults to 'start' for enter
leave: 'top'      // target defaults to 'end' for leave
```

**Shorthand string:** `'containerPosition targetPosition'`
```js
enter: 'bottom top'   // bottom of container meets top of target
leave: 'top bottom'   // top of container meets bottom of target
```

**Relative offsets:**
```js
enter: 'bottom-=50 top'   // 50px before bottom of container
leave: 'top+=60 bottom'   // 60px after top of container
```

### Sync Modes

| Value | Behavior |
|-------|----------|
| `false` (default) | Animation triggers on enter/leave thresholds |
| `true` | Playback progress tied directly to scroll position |
| `Number (0-1)` | Smoothed synchronization (e.g., 0.5 = half speed smoothing) |
| `1` | Eased synchronization |

### Callbacks

| Callback | Fires When |
|----------|-----------|
| `onEnter` | Target enters viewport |
| `onEnterForward` | Entering while scrolling forward |
| `onEnterBackward` | Entering while scrolling backward |
| `onLeave` | Target leaves viewport |
| `onLeaveForward` | Leaving while scrolling forward |
| `onLeaveBackward` | Leaving while scrolling backward |
| `onUpdate` | On scroll updates |
| `onSyncComplete` | When sync animation completes |
| `onResize` | On viewport/container resize |

### Methods

#### `scrollObserver.link(animation)`
Connects an animation/timer/timeline to the ScrollObserver. Only one object can be linked at a time.

#### `scrollObserver.refresh()`
Updates bounding values and re-computes function-based values (`repeat`, `axis`, `enter`, `leave`).
No need to call on container size change (handled internally).

#### `scrollObserver.revert()`
Disables observer, removes all EventListeners and debug elements.
```js
animate('.square', {
  autoplay: onScroll({
    sync: 1,
    onSyncComplete: self => self.revert()  // auto-cleanup
  })
});
```

### Properties

| Property | Get/Set | Description |
|----------|---------|-------------|
| `id` | get | Unique identifier |
| `container` | get | Scroll container |
| `target` | get | Target element |
| `linked` | get | Linked animation/timer/timeline |
| `repeat` | get | Whether observer repeats |
| `horizontal` | get | Horizontal scroll |
| `enter` | get | Enter threshold |
| `leave` | get/set | Leave threshold (only settable property) |
| `sync` | get | Sync enabled |
| `velocity` | get | Current scroll velocity |
| `backward` | get | Scrolling backward |
| `scroll` | get | Current scroll position |
| `progress` | get | Progress 0 to 1 |
| `completed` | get | Observation completed |
| `began` | get | Observation began |
| `isInView` | get | Element currently in view |
| `offset` | get | Offset of observed element |
| `distance` | get | Scroll distance |

## Usage Patterns

### Threshold-triggered (play on enter)
```js
animate('.reveal', {
  opacity: [0, 1],
  y: [50, 0],
  duration: 800,
  ease: 'out(3)',
  autoplay: onScroll({
    target: '.reveal',
    enter: 'bottom top',  // when bottom of viewport meets top of element
  })
});
```

### Scroll-synced (progress tied to scroll)
```js
animate('.progress-bar', {
  scaleX: 1,
  duration: 1000,
  autoplay: onScroll({
    target: '.progress-section',
    sync: 1,
  })
});
```

### Timeline on scroll
```js
createTimeline({
  alternate: true,
  loop: true,
  autoplay: onScroll({ target: '.section', container, debug: true })
})
.add('.a', { x: '9rem' })
.add('.b', { x: '9rem' })
.add('.c', { x: '9rem' });
```

### Timer on scroll
```js
createTimer({
  duration: 2000,
  alternate: true,
  loop: true,
  onUpdate: self => { $timer.innerHTML = self.iterationCurrentTime; },
  autoplay: onScroll({ target: $timer.parentNode, container })
});
```

## Manual Scroll Control (Legacy)

For cases where onScroll() doesn't fit:
```js
const animation = animate('.scroll-element', {
  y: [100, 0],
  opacity: [0, 1],
  autoplay: false
});

window.addEventListener('scroll', () => {
  const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  animation.seek(animation.duration * scrollPercent);
});
```

**Note:** The v4 `onScroll()` ScrollObserver is more performant than manual scroll listeners. Use built-in API whenever possible.
