# Framework Integration Reference

## React

### Core pattern: useEffect + createScope + revert

```jsx
import { animate, createScope, createDraggable, spring, utils } from 'animejs';
import { useEffect, useRef, useState } from 'react';

function App() {
  const root = useRef(null);
  const scope = useRef(null);
  const [rotations, setRotations] = useState(0);

  useEffect(() => {
    scope.current = createScope({ root }).add(self => {
      // All animations scoped to <div ref={root}>
      animate('.logo', {
        scale: [
          { to: 1.25, ease: 'inOut(3)', duration: 200 },
          { to: 1, ease: spring({ bounce: 0.7 }) }
        ],
        loop: true,
        loopDelay: 250,
      });

      createDraggable('.logo', {
        container: [0, 0, 0, 0],
        releaseEase: spring({ bounce: 0.7 })
      });

      // Register methods callable outside useEffect
      self.add('rotateLogo', (i) => {
        animate('.logo', {
          rotate: i * 360,
          ease: 'out(4)',
          duration: 1500,
        });
      });
    });

    return () => scope.current.revert();
  }, []);

  const handleClick = () => {
    setRotations(prev => {
      const newRotations = prev + 1;
      scope.current.methods.rotateLogo(newRotations);
      return newRotations;
    });
  };

  return (
    <div ref={root}>
      <img className="logo" src="/logo.svg" alt="logo" />
      <button onClick={handleClick}>rotations: {rotations}</button>
    </div>
  );
}
```

### Key React concepts

| Concept | Method | Purpose |
|---------|--------|---------|
| Init | `useEffect()` | Initialize animations on mount |
| Scoping | `createScope({ root })` | Scope to DOM element + cleanup |
| External calls | `self.add('name', fn)` | Register callable methods |
| Cleanup | `scope.current.revert()` | Remove all instances on unmount |
| Refs | `useRef(null)` | Store root element and scope |

### React with media queries (responsive + reduced motion)

```jsx
useEffect(() => {
  scope.current = createScope({
    root,
    mediaQueries: {
      isSmall: '(max-width: 768px)',
      reduceMotion: '(prefers-reduced-motion: reduce)',
    },
  }).add(self => {
    const { isSmall, reduceMotion } = self.matches;

    if (reduceMotion) {
      utils.set('.box', { opacity: 1 });
      return;
    }

    animate('.box', {
      x: isSmall ? 100 : 250,
      duration: isSmall ? 400 : 800,
    });
  });

  return () => scope.current.revert();
}, []);
```

### React page transitions

```jsx
import { useEffect, useRef } from 'react';
import { animate, createScope } from 'animejs';
import { useLocation } from 'react-router-dom';

function PageTransition({ children }) {
  const root = useRef(null);
  const scope = useRef(null);
  const location = useLocation();

  useEffect(() => {
    scope.current = createScope({ root }).add(self => {
      self.add('transitionIn', () => {
        animate(root.current, {
          opacity: [0, 1],
          y: [30, 0],
          duration: 500,
          ease: 'outExpo',
        });
      });
    });

    scope.current.methods.transitionIn();
    return () => scope.current.revert();
  }, [location]);

  return <div ref={root}>{children}</div>;
}
```

### React caveat: exit animations

anime.js works **outside React's lifecycle**. Animations are applied after React renders. You cannot easily animate component removal. Options:
- Keep elements in DOM with `opacity: 0` transitions
- Use `react-transition-group` for exit animation lifecycle
- Consider Motion/Framer Motion for AnimatePresence-style exit animations

---

## Vue

### Vue 3 Composition API

```javascript
import { onMounted, onUnmounted, ref } from 'vue';
import { animate, createScope } from 'animejs';

export default {
  setup() {
    const root = ref(null);
    const scope = ref(null);

    onMounted(() => {
      scope.value = createScope({ root: root.value }).add(self => {
        animate('.box', { x: 250, duration: 800 });
      });
    });

    onUnmounted(() => {
      scope.value?.revert();
    });

    return { root };
  }
}
```

### Vue Router page transitions

Use `:css="false"` to skip CSS class binding and use JS hooks:

```vue
<template>
  <router-view v-slot="{ Component }">
    <transition :css="false" @enter="onEnter" @leave="onLeave" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
</template>

<script setup>
import { animate } from 'animejs';

const onEnter = (el, done) => {
  animate(el, {
    opacity: [0, 1],
    y: [50, 0],
    duration: 600,
    ease: 'outExpo',
    onComplete: done,
  });
};

const onLeave = (el, done) => {
  animate(el, {
    opacity: [1, 0],
    y: [0, -50],
    duration: 400,
    ease: 'inExpo',
    onComplete: done,
  });
};
</script>
```

**Critical:** Use `:css="false"` on `<transition>` to tell Vue to skip CSS classes and rely on JS hooks.

---

## Svelte

### Approach 1: `$effect` (mount & reactive animations)

```svelte
<script lang="ts">
  import { animate, text, stagger } from "animejs";
  let el = $state<HTMLElement | null>(null);

  $effect(() => {
    if (el) {
      const { chars } = text.split(el, { chars: true });
      animate(chars, {
        delay: stagger(50),
        y: [30, 0],
        loop: true,
        duration: 300,
        loopDelay: 1000,
        alternate: true,
      });
    }
  });
</script>

<div bind:this={el}>Hello World</div>
```

### Approach 2: Attachments (entrance animations)

```svelte
<script lang="ts">
  import { type Attachment } from "svelte/attachments";
  import { animate } from "animejs";

  const animeAttachment: Attachment = (el) => {
    animate(el, {
      y: [100, 0],
      opacity: [0, 1],
      scale: [0.5, 1],
      duration: 1000,
    });
  };
</script>

<div {@attach animeAttachment}>Content</div>
```

**Limitation:** Attachment return callbacks fire after element removal; cannot use for exit animations.

### Approach 3: Transitions (entrance + exit)

```svelte
<script lang="ts">
  import { animate } from "animejs";
  import type { TransitionConfig } from "svelte/transition";

  function animeTransition(node: HTMLElement, params: { duration?: number }): TransitionConfig {
    const duration = params.duration || 1000;
    const animation = animate(node, {
      opacity: [0, 1],
      x: [100, 0],
      autoplay: false,
      duration,
    });

    return {
      duration,
      tick(t, u) {
        animation.seek(t * duration);
      },
    };
  }
</script>

<li transition:animeTransition={{ duration: 300 }}>Todo item</li>
```

### Svelte approach comparison

| Method | Best For | Exit Animations? |
|--------|----------|------------------|
| `$effect` | Mount animations, state-reactive | No |
| Attachments | Entrance animations on mount | No |
| Transitions | Both entrance and exit | Yes |

---

## SvelteKit

Use `onMount` to ensure DOM is ready:

```svelte
<script lang="ts">
  import { onMount } from 'svelte';
  import { animate } from 'animejs';

  onMount(() => {
    animate('.box', { x: 250 });
  });
</script>
```

## Next.js / SSR

Anime.js v4 is ESM-first and also distributes CommonJS and UMD builds. DOM
animation still belongs in client lifecycle code. If an SSR tool evaluates a
DOM-dependent import on the server, move that code behind the framework's
client boundary or use a conditional dynamic import:

```js
const { animate } = await import('animejs');
```

Or ensure animation runs in `useEffect` / `onMounted` / `onMount` (client-side only).

## Framework-agnostic tips

1. **Always clean up:** `scope.revert()` in React's `useEffect` cleanup, Vue's `onUnmounted`, or Svelte's `$effect` return
2. **Use `createScope({ root })`:** Prevents selectors from affecting elements outside the component
3. **Register methods via `self.add()`:** Enables calling animations from event handlers outside the init lifecycle
4. **Handle reduced motion:** Use `createScope({ mediaQueries: { reduceMotion: '...' } })`
5. **Don't fight the framework:** anime.js manipulates the DOM directly. For React especially, don't animate properties that React also manages (text content, className if React controls it). Animate transforms, opacity, and other properties that don't conflict with React's virtual DOM.
