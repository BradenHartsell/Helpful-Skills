# SVG and Text Reference

## SVG Module

```js
import { svg } from 'animejs';
// or: import { morphTo, createMotionPath, createDrawable } from 'animejs';
// or: import { morphTo, createMotionPath, createDrawable } from 'animejs/svg';
```

### `svg.createDrawable(target)`

Creates Proxy wrappers around SVG elements with a `draw` property for line/path drawing animations.

| Parameter | Type | Description |
|-----------|------|-------------|
| `target` | CSS selector / SVGLineElement / SVGPathElement / SVGPolylineElement / SVGRectElement | Target SVG element(s) |

**Returns:** Array of `Proxy<SVGElement>` with `draw` property

#### `draw` Property
Space-separated string of two values (0 to 1) defining start and end of visible segment:

| Value | Visual |
|-------|--------|
| `'0 1'` | Full line visible |
| `'0 .5'` | First half visible |
| `'.25 .75'` | Middle 50% visible |
| `'.5 1'` | Second half visible |
| `'1 1'` | No line visible |

Also accepts arrays for keyframed animation:
```js
draw: ['0 0', '0 1', '1 1']  // draws then erases
```

#### Usage
```js
import { animate, svg, stagger } from 'animejs';

animate(svg.createDrawable('.line'), {
  draw: ['0 0', '0 1', '1 1'],
  ease: 'inOutQuad',
  duration: 2000,
  delay: stagger(100),
  loop: true,
});
```

**Performance gotcha:** Animating elements with `vector-effect: non-scaling-stroke` is slow because the path's scale factor must be recalculated on every tick.

---

### `svg.createMotionPath(path, offset)`

Creates tween parameters that animate along an SVGPathElement's coordinates and inclination.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `path` | CSS selector / SVGPathElement | - | The SVG path to follow |
| `offset` | Number (0-1) | `0` | Position offset along path |

**Returns:** Object with `translateX`, `translateY`, `rotate` properties. Spread with `...` into `animate()`.

```js
import { animate, svg } from 'animejs';

// Follow a path
animate('.car', {
  ease: 'linear',
  duration: 5000,
  loop: true,
  ...svg.createMotionPath('path')
});

// Combined with line drawing (trace the path while following it)
animate(svg.createDrawable('path'), {
  draw: '0 1',
  ease: 'linear',
  duration: 5000,
  loop: true,
});
```

**Best practices:**
- Use `ease: 'linear'` for constant-speed motion
- Only works with `SVGPathElement` (not polylines/polygons)

---

### `svg.morphTo(shapeTarget, precision)`

Creates a morphing animation by interpolating `d` (path) or `points` (polygon/polyline).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `shapeTarget` | CSS selector / SVGPathElement / SVGPolylineElement / SVGPolygonElement | - | Target shape to morph into |
| `precision` | Number (0-1) | `.33` | Point interpolation density. 0 = no extrapolation |

**Returns:** Array `[startValue, endValue]` for the `d` or `points` property

```js
import { animate, svg, utils } from 'animejs';

animate($path1, {
  points: svg.morphTo($path2),
  ease: 'inOutCirc',
  duration: 500,
});
```

**Gotchas:**
- `precision: 0` means shapes must have compatible point counts
- Morphing works on `points` (polygons/polylines) and `d` (paths)

---

## Text Module

```js
import { text } from 'animejs';
// or: import { splitText, scrambleText } from 'animejs';
// or: import { splitText, scrambleText } from 'animejs/text';
```

### `splitText(target, parameters)`

Splits text into animatable lines, words, and characters.

| Parameter | Type | Description |
|-----------|------|-------------|
| `target` | CSS selector / HTMLElement | Target element containing text |
| `parameters` | Object (optional) | TextSplitter settings |

**Returns:** `TextSplitter` instance (destructure as `{ lines, words, chars }`)

#### Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `lines` | `false` | Split into line elements |
| `words` | `true` | Split into word elements |
| `chars` | `false` | Split into character elements |
| `debug` | `false` | Toggle debug CSS outlines (lines=green, words=red, chars=blue) |
| `includeSpaces` | `false` | Include whitespace within split elements |
| `accessible` | `true` | Create accessible clone for screen readers |

Each of `lines`, `words`, `chars` can be:
- `Boolean` - enable/disable
- `Object` - split parameters (`class`, `wrap`, `clone`)
- `String` - HTML template with `{value}` and `{i}` variables

#### Split Parameters (for object syntax)

| Parameter | Default | Description |
|-----------|---------|-------------|
| `class` | `null` | Custom CSS class for split elements |
| `wrap` | `null` | Extra wrapper with CSS overflow: `'hidden'`, `'clip'`, `'visible'`, `'scroll'`, `'auto'`, `true` (='clip') |
| `clone` | `null` | Clone in direction: `'left'`, `'top'`, `'right'`, `'bottom'`, `'center'`, `true` (='center') |

#### HTML Template
```js
// Custom wrapper
splitText('p', { chars: '<em class="char-{i}">{value}</em>' });

// 3D faces
splitText('p', {
  chars: `<span class="char-3d">
    <em class="face-top">{value}</em>
    <em class="face-front">{value}</em>
    <em class="face-bottom">{value}</em>
  </span>`,
});
```

#### Key behaviors
- Lines split after `document.fonts.ready` fulfills
- Auto re-splits on element resize (when splitting by lines)
- Word splitting uses `Intl.Segmenter` for CJK/Thai/etc., falls back to `String.split()`
- `accessible: true` creates a screen-reader-friendly clone at `split.$target.firstChild`

#### Methods

**`split.revert()`** - Revert to original HTML, remove debug styles, revert all `addEffect()` animations

**`split.addEffect(callback)`** - Register animations/callbacks that survive re-splits
```js
const split = splitText('p', { lines: true });
split.addEffect(({ lines }) => {
  animate(lines, { y: ['50%', '0%'], delay: stagger(200) });
});
// Can also register callbacks with cleanup
split.addEffect(split => {
  split.words.forEach($el => {
    $el.addEventListener('pointerenter', handler);
  });
  return () => split.words.forEach($el => $el.removeEventListener('pointerenter', handler));
});
```

**`split.refresh()`** - Manually re-split after changing properties (`html`, `debug`, `templates`, etc.)

#### Properties

| Property | Type | Description |
|---------|------|-------------|
| `$target` | HTMLElement | Split root element |
| `html` | String | HTML to split (get/set) |
| `debug` | Boolean | Debug styles visible |
| `includeSpaces` | Boolean | Spaces wrapped |
| `accessible` | Boolean | Accessible clone created |
| `lines` | Array | Line elements |
| `words` | Array | Word elements |
| `chars` | Array | Character elements |

#### Critical: addEffect for line splits

**Always use `addEffect()` when splitting by `lines`** because line splitting waits for `document.fonts.ready`. Direct animations will fail if fonts haven't loaded yet.

```js
// BAD - may fail if fonts not loaded
const { lines } = splitText('p', { lines: true });
animate(lines, { y: ['50%', '0%'] }); // lines might be empty!

// GOOD - survives font loading and re-splits
const split = splitText('p', { lines: true });
split.addEffect(({ lines }) => {
  animate(lines, { y: ['50%', '0%'], delay: stagger(200) });
});
```

---

### `scrambleText(parameters)` (v4.4+)

Scramble-and-reveal text effect. Use as function-based value for `innerHTML`.

**Must be applied to `innerHTML`, NOT `textContent`.**

```js
import { animate, scrambleText } from 'animejs';

animate('p', {
  innerHTML: scrambleText({
    text: 'Hello World',
    chars: 'uppercase',
    from: 'center',
    cursor: '_',
  }),
  loop: true,
  loopDelay: 1000,
});
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | String/Function | Original text | Text to transition to |
| `chars` | String/Function | `'a-zA-Z0-9!%#_'` | Scramble character set |
| `override` | Boolean/String | `true` | Starting appearance (true=scramble, false=original, ''=blank, String=custom set) |
| `ease` | Easing | `'linear'` | Easing for reveal wave |
| `cursor` | Boolean/Number/String | `''` | Characters at leading edge of reveal |
| `revealRate` | Number | `60` | Characters revealed per second |
| `revealDelay` | Number/Function | `0` | Delay before reveal starts (ms) |
| `settleRate` | Number | `30` | Times per second each char cycles random glyphs |
| `settleDuration` | Number | `300` | Time each char scrambles before settling (ms) |
| `delay` | Number/Function | `0` | Delay before scramble starts (ms) |
| `duration` | Number/Function | Auto | Override computed duration |
| `perturbation` | Number (0-1) | `0` | Randomness of reveal timing |
| `from` | String/Number | `'auto'` | Where reveal wave starts |
| `reversed` | Boolean | `false` | Reverses reveal order |
| `seed` | Number | `0` | Seed for reproducible scramble |
| `onChange` | Function | - | Fires during scramble on each change |

#### `chars` named presets

| Name | Characters |
|------|------------|
| `'lowercase'` | a-z |
| `'uppercase'` | A-Z |
| `'numbers'` | 0-9 |
| `'symbols'` | `!%#_\|*+=` |
| `'braille'` | Unicode braille block |
| `'blocks'` | Unicode block elements |
| `'shades'` | `░-▓` |

Range syntax: `'a-d'` = `'abcd'`. Literal `-` at start/end.

#### `from` values

| Value | Description |
|-------|-------------|
| `'auto'` | Left when text grows, right when shrinks |
| `'left'` | Reveal from left |
| `'center'` | Reveal from center |
| `'right'` | Reveal from right |
| `'random'` | Random order |
| Number | From specific index |

#### `perturbation`
- `0` = evenly spaced reveals
- `0.5` = moderate random offset
- `1` = maximum offset, characters settle out of order

#### Duration auto-computation
If unset or `0`, duration is auto-calculated from text length, `revealRate`, and `settleDuration`.
