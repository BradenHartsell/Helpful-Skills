# Scope Reference

Scope enables media query reactivity, custom root elements, shared defaults, batch reversion, and component-based workflows.

## Creation

```js
import { createScope } from 'animejs';
// or: import { createScope } from 'animejs/scope';

const scope = createScope(parameters);
```

## Parameters

### `root`
CSS Selector or DOM Element. Default: `document`.

Limits all DOM queries within the scope to descendants of the root element.

```js
createScope({ root: '.container' })
.add(() => {
  animate('.box', { x: 250 }); // Only .box inside .container
});
```

### `defaults`
Object of default parameters applied to all Timer, Animation, and Timeline created within the scope.

Configurable: `playbackEase`, `playbackRate`, `frameRate`, `loop`, `reversed`, `alternate`, `autoplay`, `duration`, `delay`, `composition`, `ease`, `loopDelay`, `modifier`, and all callbacks (`onBegin`, `onUpdate`, `onRender`, `onLoop`, `onComplete`).

```js
createScope({
  root: $row,
  defaults: { ease: 'out(3)', duration: 600 },
}).add(() => {
  animate('.box', { x: 250 }); // inherits ease and duration
});
```

### `mediaQueries`
Object where keys are custom names and values are CSS media query strings.

```js
createScope({
  mediaQueries: {
    isSmall: '(max-width: 768px)',
    isMedium: '(min-width: 769px) and (max-width: 1024px)',
    isLarge: '(min-width: 1025px)',
    reduceMotion: '(prefers-reduced-motion)',
  }
}).add(self => {
  const { isSmall, isMedium, isLarge, reduceMotion } = self.matches;
  animate('.box', {
    x: isSmall ? 100 : 250,
    duration: reduceMotion ? 0 : 800,
  });
});
```

Scope automatically reverts and rebuilds when any media query match state changes.

## Methods

### `add(constructor)` - Add constructor
Re-runs automatically on media query changes. Can return a cleanup function.
```js
scope.add(self => {
  const { isSmall } = self.matches;
  animate('.box', { x: isSmall ? 100 : 250 });

  // Optional cleanup (runs on revert or media query change)
  return () => {
    // Manual cleanup for event listeners, DOM changes, etc.
    // Anime.js instances auto-cleanup
  };
});
```

### `add(name, method)` - Register named method
Accessible via `scope.methods.name`. Retains scope context.
```js
scope.add(self => {
  self.add('playAnim', (value) => {
    animate('.box', { x: value, ease: 'out(4)' });
  });
});

// Call from outside
scope.methods.playAnim(250);
```

### `addOnce(constructor)` - Run only once (v4.1+)
Constructor runs once. Animations NOT reverted between media query changes.
**Cannot be conditional** (wrapping in `if` breaks tracking).
```js
// BAD
if (scope.matches.small) {
  scope.addOnce(() => { animate(target, params) });
}
// GOOD
scope.addOnce(() => { animate(target, params) });
```

### `keepTime(constructor)` - Recreate preserving time (v4.1+)
Recreates instance between media query changes while preserving currentTime.
**Cannot be conditional.**
```js
scope.add(self => {
  self.keepTime(() => createTimeline().add('.circle', {
    x: self.matches.isSmall ? [-30, 30] : [-70, 70],
    loop: true, alternate: true,
  }, stagger(100)).init());
});
```

### `revert()` - Revert everything
Auto-reverts all tracked instances. Calls cleanup functions.

### `refresh()` - Revert + rebuild
Reverts scope, re-executes all constructors. Custom properties persist across refreshes.

## Properties

| Property | Description |
|----------|-------------|
| `data` | Store variables; cleared on revert |
| `defaults` | Default parameters for this scope |
| `root` | Root element for DOM operations |
| `constructors` | Constructor functions |
| `revertConstructors` | Revert constructor functions |
| `revertibles` | All revertible objects (animations, draggables, scroll observers, nested scopes) |
| `methods` | Registered methods |
| `matches` | Current media query match results (booleans) |
| `mediaQueryLists` | MediaQueryList objects |

## Auto-tracking

All anime.js instances created inside a constructor are **automatically tracked**:
- Animations (`animate()`)
- Timers (`createTimer()`)
- Timelines (`createTimeline()`)
- Animatables (`createAnimatable()`)
- Draggables (`createDraggable()`)
- Scroll observers (`onScroll()`)
- Nested scopes (`createScope()`)

**Event listeners and manual DOM manipulations require explicit cleanup** in the returned function.

## React Pattern

```js
import { animate, createScope, spring } from 'animejs';
import { useEffect, useRef } from 'react';

function Component() {
  const root = useRef(null);
  const scope = useRef(null);

  useEffect(() => {
    scope.current = createScope({ root }).add(self => {
      animate('.box', { x: 250, ease: spring({ bounce: 0.3 }) });

      self.add('playAnim', (value) => {
        animate('.box', { x: value });
      });
    });

    return () => scope.current.revert(); // CRITICAL
  }, []);

  return <div ref={root}><div className="box" /></div>;
}
```

## Gotchas

- Anime.js instances auto-track; event listeners need manual cleanup
- `addOnce()` and `keepTime()` CANNOT be conditional
- `refresh()` = revert + rebuild; custom scope properties persist
- Multiple scopes can be reverted independently
- `root` is essential for component frameworks (prevents cross-component selector leakage)
- `data` is cleared on revert (use for temporary state only)
- Always handle `prefers-reduced-motion` for accessibility
