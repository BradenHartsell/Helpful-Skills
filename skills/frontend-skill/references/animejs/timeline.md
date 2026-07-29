# Timeline Reference

Synchronize animations, timers, and callbacks into orchestrated sequences.

## Creation

```js
import { createTimeline } from 'animejs';
const tl = createTimeline(parameters);
```

## Adding Content

### `add()` - New animations
```js
tl.add(targets, animationParameters, position);
```
Allows tween value composition with the timeline's existing children.

### `add()` - Timers
```js
tl.add(timerParameters, position);
```

### `sync()` - Existing instances
```js
tl.sync(animationOrTimerOrTimeline, position);
```
Composition handled at creation time; won't affect existing children.

### `call()` - Callback at position
```js
tl.call(callback, position);
```

### `label()` - Named marker
```js
tl.label('myLabel', position);
```

### `set()` - Set properties at point
```js
tl.set(targets, properties, position);
```

### `remove()` - Remove animations
```js
tl.remove(animation);
```

## Position Syntax

| Type | Example | Description |
|------|---------|-------------|
| Absolute | `100` | At exactly 100ms |
| Addition | `'+=100'` | 100ms after the last element |
| Subtraction | `'-=100'` | 100ms before the last element end |
| Multiplier | `'*=.5'` | Half of total element duration |
| Previous end | `'<'` | End position of previous element |
| Previous start | `'<<'` | Start position of previous element |
| Combined | `'<<+=250'` | 250ms after the previous element's start |
| Label | `'My Label'` | At named label position |
| Stagger | `stagger(10)` | Stagger elements by 10ms |

**Default:** If no position is defined, child is placed at the **end** of the timeline.

**Pitfall:** A bare number is absolute time, not a delay.

## Playback Settings

| Setting | Default | Notes |
|---------|---------|-------|
| `defaults` | - | Applied to all child animations. `from`/`to` not allowed |
| `delay` | `0` | Delay before entire timeline begins |
| `loop` | `0` | 0=once, true/infinity=infinite |
| `loopDelay` | `0` | Delay between loop iterations |
| `alternate` | `false` | Reverse each iteration |
| `reversed` | `false` | Initial direction reversed |
| `autoplay` | `true` | false=manual, onScroll()=scroll-triggered |
| `frameRate` | `240` | Capped to monitor refresh rate |
| `playbackRate` | `1` | Speed multiplier. 0=won't play |
| `playbackEase` | `null` | Easing applied to entire timeline playback |

## Callbacks

| Callback | Fires When |
|----------|-----------|
| `onBegin` | Timeline begins |
| `onComplete` | Timeline completes |
| `onBeforeUpdate` | Before each update |
| `onUpdate` | On each update |
| `onRender` | When timeline renders |
| `onLoop` | When timeline loops |
| `onPause` | When paused |
| `then()` | Promise resolves on completion |

## Methods

| Method | Purpose |
|--------|---------|
| `play()` | Start playing |
| `pause()` | Pause |
| `resume()` | Resume from paused state |
| `restart()` | Restart from beginning |
| `reset()` | Reset to initial state |
| `reverse()` | Play in reverse |
| `alternate()` | Toggle direction |
| `complete()` | Jump to end |
| `cancel()` | Cancel playback |
| `revert()` | Revert to initial state |
| `seek(time)` | Seek to specific time |
| `stretch(duration)` | Stretch/modify duration |
| `refresh()` | Refresh timeline state |
| `init()` | Initialize the timeline |

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | String/Number | Identifier |
| `labels` | Object | Map of label positions |
| `currentTime` | Number | Global current time (ms) |
| `iterationCurrentTime` | Number | Current iteration time (ms) |
| `deltaTime` | Number | Time between frames (ms) |
| `progress` | Number | Overall progress 0-1 |
| `iterationProgress` | Number | Current iteration progress 0-1 |
| `currentIteration` | Number | Iteration count |
| `duration` | Number | Total duration (ms) |
| `speed` | Number | Speed multiplier |
| `fps` | Number | Frame rate |
| `paused` | Boolean | Paused state |
| `began` | Boolean | Whether started |
| `completed` | Boolean | Whether completed |
| `reversed` | Boolean | Reversed state |
| `backwards` | Boolean | Currently playing backwards (read-only) |

## Examples

### Sequential with overlap
```js
const tl = createTimeline({ defaults: { ease: 'outExpo', duration: 750 } });
tl.add('.box1', { x: 250 })
  .add('.box2', { x: 250 }, '-=500')  // overlap by 500ms
  .add('.box3', { x: 250 }, '+=200'); // gap of 200ms
```

### With labels and stagger
```js
tl.label('start')
  .add('.circle', { x: '15rem' }, 500)
  .add('.square', { x: '15rem' }, 'start')
  .add('.items', { x: '15rem', delay: stagger(80) }, '<');
```

### Syncing external animations
```js
const tlA = createTimeline().add('.a', { x: 250, duration: 2000 });
const tlMain = createTimeline()
  .sync(tlA)
  .sync(tlB, '-=2000');
```

### Mixed child loops
```js
const tl = createTimeline({ loop: true, loopDelay: 1000 });
tl.add('.a', { x: 200, duration: 500 })
  .add('.b', { y: 100, duration: 800, loop: 2 }) // child loops within timeline
  .add('.c', { scale: 1.5, duration: 300 });
```

## Gotchas

- `delay` applies to the **entire timeline**, not individual children
- `playbackEase` applies to overall progress; children retain their own easing
- `autoplay` is **overridden to `false`** when an animation is added to a timeline
- `add()` enables tween composition with existing children; `sync()` does not
- `playbackRate` of `0` effectively pauses (same as `pause()`)
- Use `utils.sync()` when updating `speed` dynamically for proper synchronization
