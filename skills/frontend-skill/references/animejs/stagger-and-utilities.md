# Stagger and Utilities Reference

## Stagger

Creates sequential effects by distributing values across targets. Returns a function-based value.

```js
import { stagger } from 'animejs';
const fn = stagger(value, parameters);
```

### Value Types

```js
// Numerical (fixed increment per target)
delay: stagger(100)                    // +100ms per target
x: stagger('5.75rem')                  // +5.75rem per target

// Range (evenly distributed between endpoints)
y: stagger(['-2.75rem', '2.75rem'])   // first=-2.75rem, last=2.75rem
delay: stagger([0, 500])               // delays from 0ms to 500ms
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `start` | Number/String | Starting value before distribution |
| `from` | Number / `'center'` / `'first'` / `'last'` / `'random'` | Stagger origin |
| `reversed` | Boolean | Reverse stagger order |
| `ease` | String/Function | Easing for distribution |
| `grid` | `[cols, rows]` | Grid for 2D spatial staggering |
| `axis` | `'x'` / `'y'` | Which axis for grid staggering |
| `modifier` | Function | Custom value modifier |
| `total` | Number | Total duration for stagger |
| `jitter` | Number / [Number, Number] / null | Random offset per value (v4.5+) |
| `seed` | Boolean / Number / false | Reproducible jitter |

### Jitter (v4.5+)

```js
delay: stagger(100, { jitter: 100, seed: 42 })
// jitter: 100 -> random offset in [-100, +100]
// jitter: [50, 200] -> ramps from first to farthest target
// seed: 42 -> reproducible
// seed: true -> seeds with 0
// seed: false -> random each run (default)
```

### Usage Patterns

```js
// Time staggering (delay/duration)
animate('.item', {
  x: '17rem',
  delay: stagger(100),
  duration: stagger(200, { start: 500 }),
});

// Value staggering (properties)
animate('.square', {
  y: stagger(['-2.75rem', '2.75rem']),
  rotate: { from: stagger('-.125turn') },
});

// Grid staggering from center
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, { grid: [14, 5], from: 'center', axis: 'x' }),
});

// Timeline position staggering
const tl = createTimeline();
tl.add('.item', { x: 250 }, stagger(100));
// Note: callbacks on staggered timeline animations fire per target
```

---

## Utilities

### `$()` - Query selector
```js
const targets = utils.$('.selector'); // Returns Array
// Within scope, uses scope root instead of document
```

### `get()` - Get property value
```js
utils.get(el, 'x');           // '11.22px' (string with unit)
utils.get(el, 'x', false);    // 11.22 (number)
utils.get(el, 'x', 'rem');    // '0.70rem' (converted)
```

### `set()` - Set without animation
```js
const setter = utils.set('.square', {
  borderRadius: '50%',
  scale: stagger(.1, { start: .25 }),
});
setter.revert(); // undo
```
**Gotcha:** For repeated updates, use `createAnimatable()` instead for better performance. Won't work for attributes not already on the element.

### `remove()` - Remove from active animations
```js
utils.remove(targets);                          // from all animations
utils.remove(targets, animation, 'x');          // from specific instance/property
```

### `sync()` - Execute in sync with engine
```js
utils.sync(() => animation.speed = 0.5);
```
Use for event-driven property changes to ensure correct frame timing.

### `keepTime()` - Recreate preserving time (v4.1+)
```js
const tracked = utils.keepTime(() => animate(el, { x: 250, duration: 800 }));
tracked(); // returns animation, preserves currentTime
```

### `cleanInlineStyles()` - Remove inline styles from instance
```js
animate('.el', { x: '17rem', onComplete: utils.cleanInlineStyles });
```
Only removes styles added by that specific instance.

### Random functions
```js
utils.random(0, 100)                    // random number 0-100
utils.random(0, 1, 3)                   // 0.123 (3 decimals)
utils.randomPick([1, 2, 3])             // random array element
utils.randomPick('ABCD')               // random character
utils.shuffle(array)                    // shuffle in place (mutates!)
utils.createSeededRandom(42)            // seeded RNG function
const seeded = utils.createSeededRandom(42);
seeded(0, 100);                         // reproducible sequence
```

### Chain-able Utility Functions

Call without the value parameter to get a chain-able function. Great as `modifier` in animations.

**Supported:** `round()`, `clamp()`, `snap()`, `wrap()`, `mapRange()`, `lerp()`, `roundPad()`, `padStart()`, `padEnd()`, `degToRad()`, `radToDeg()`

```js
// Create chain-able
const fn = utils.clamp(0, 100).round(2).padStart(6, '0');
fn(125);    // '000100' (clamped, rounded, padded)
fn(75.25);  // '075.25'

// As modifier
animate('.value', {
  innerHTML: 1000,
  modifier: utils.wrap(0, 10).roundPad(3).padStart(6, '0'),
  ease: 'linear',
});
```

### Individual function reference

#### `round(value, decimalLength)` / `round(decimalLength)`
```js
utils.round(72.7523, 2);      // 72.75
utils.round(2)(72.7523);      // 72.75 (chain-able)
```

#### `clamp(value, min, max)` / `clamp(min, max)`
```js
utils.clamp(120, 0, 100);     // 100
utils.clamp(0, 100)(120);     // 100 (chain-able)
```

#### `snap(value, increment)` / `snap(increment)`
```js
utils.snap(94, 10);           // 90
utils.snap(30, [0, 50, 100]); // 50 (closest from array)
utils.snap(10)(94);           // 90 (chain-able)
```

#### `wrap(value, min, max)` / `wrap(min, max)`
```js
utils.wrap(105, 0, 100);      // 5
utils.wrap(-15, 0, 100);      // 85
utils.wrap(0, 100)(105);      // 5 (chain-able)
```

#### `mapRange(value, fromLow, fromHigh, toLow, toHigh)` / `mapRange(fromLow, fromHigh, toLow, toHigh)`
```js
utils.mapRange(45, 0, 100, 0, 200);  // 90
// Does NOT clamp! Chain with .clamp() to constrain
const safe = utils.mapRange(0, 100, 0, 1).clamp(0, 1);
```

#### `lerp(start, end, progress)` / `lerp(start, end)`
```js
utils.lerp(0, 100, 0.5);      // 50
utils.lerp(0, 100)(0.75);     // 75 (chain-able)
// Progress values outside 0-1 are clamped
```

#### `damp(start, end, deltaTime, amount)`
Frame-rate independent lerp. Takes deltaTime in ms.
```js
utils.damp(0, 100, 8, 0.5);   // 50
utils.damp(0, 100, 8, 1);     // 100
// Use in timer onUpdate for smooth following
```

#### `roundPad(value, decimalLength)` / `roundPad(decimalLength)`
Returns **String** (for display). Pads with zeros.
```js
utils.roundPad(2)(90.12345);  // '90.12'
utils.roundPad(2)(120);       // '120.00'
```

#### `padStart(value, totalLength, padString)` / `padStart(totalLength, padString)`
```js
utils.padStart(5, '0')('123');  // '00123'
utils.padStart(5, '0')(78);     // '00078'
```

#### `padEnd(value, totalLength, padString)` / `padEnd(totalLength, padString)`
```js
utils.padEnd(5, '0')('123');    // '12300'
utils.padEnd(5, '0')(78);       // '78000'
```

#### `degToRad(degrees)` / `degToRad()`
```js
utils.degToRad(360);          // 6.283...
utils.degToRad().round(2)(180); // 3.14 (chain-able)
```

#### `radToDeg(radians)` / `radToDeg()`
```js
utils.radToDeg(Math.PI);      // 180
utils.radToDeg().round(2)(Math.PI / 7); // 25.71 (chain-able)
```
