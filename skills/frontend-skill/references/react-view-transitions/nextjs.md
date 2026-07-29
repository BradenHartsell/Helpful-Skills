# View Transitions in Next.js

## Setup

`<ViewTransition>` works out of the box for `startTransition`/`Suspense` updates. To also animate `<Link>` navigations:

```js
// next.config.js
const nextConfig = {
  experimental: { viewTransition: true },
};
module.exports = nextConfig;
```

This enables deeper Next.js integration with React View Transitions. Any VT with `default="auto"` may fire on link navigation, so use `default="none"` to prevent competing animations.

Next.js 16 App Router releases manage a React Canary line internally. Do not
change React channels independently only to unlock this feature. Verify the
installed Next.js and React versions, App Router scope, and the experimental
configuration before implementation.

---

## Next.js Implementation Additions

When following `implementation.md`, apply these additions:

**After Step 2:** Enable the experimental flag above.

**Step 4:** Use `transitionTypes` on `<Link>` only when the installed types and
runtime expose it. See "The `transitionTypes` Prop" below.

**After Step 6:** For same-route dynamic segments such as
`/collection/[slug]`, use the `key` + `name` + `share` pattern. See Same-Route
Dynamic Segment Transitions below.

---

## Layout-Level ViewTransition

**Do NOT add a layout-level VT wrapping `{children}` if pages have their own VTs.** Nested VTs never fire enter/exit when inside a parent VT. Page-level enter/exit will silently not work. Remove the layout VT entirely.

A bare `<ViewTransition>` in layout works only if pages have **no** VTs of their own.

**Layouts persist across navigations.** `enter`/`exit` only fire on initial mount, not on route changes. Do not use type-keyed maps in layouts.

---

## The `transitionTypes` Prop on `next/link`

No wrapper component needed, works in Server Components:

```tsx
<Link href="/products/1" transitionTypes={['transition-to-detail']}>View Product</Link>
```

Replaces the manual pattern of `onNavigate` + `startTransition` + `addTransitionType` + `router.push()`. Reserve manual `startTransition` for non-link interactions (buttons, forms).

**Availability:** Next.js 16.2 documents `transitionTypes` for App Router
`<Link>` navigation. The feature still depends on experimental View Transition
integration, and Pages Router links ignore it. Confirm the installed
`next/link` declarations and focused runtime behavior. If it is unavailable,
use a verified programmatic navigation path or omit transition typing.

---

## Programmatic Navigation

```tsx
'use client';

import { useRouter } from 'next/navigation';
import { startTransition, addTransitionType } from 'react';

function handleNavigate(href: string) {
  const router = useRouter();
  startTransition(() => {
    addTransitionType('nav-forward');
    router.push(href);
  });
}
```

---

## Server-Side Filtering with `router.replace`

For search/sort/filter that re-renders on the server (via URL params), use `startTransition` + `router.replace`. VTs activate because the state update is inside `startTransition`:

```tsx
'use client';

import { useRouter } from 'next/navigation';
import { startTransition } from 'react';

function handleSort(sort: string) {
  const router = useRouter();
  startTransition(() => {
    router.replace(`?sort=${sort}`);
  });
}
```

List items wrapped in `<ViewTransition key={item.id}>` will animate reorder. This is the server-component alternative to the client-side `useDeferredValue` pattern in `patterns.md`.

---

## Two-Layer Pattern (Directional + Suspense)

Directional slides + Suspense reveals coexist because they fire at different moments. Place the directional VT in the **page component** (not layout):

```tsx
<ViewTransition
  enter={{ "nav-forward": "slide-from-right", default: "none" }}
  exit={{ "nav-forward": "slide-to-left", default: "none" }}
  default="none"
>
  <div>
    <Suspense fallback={<ViewTransition exit="slide-down"><Skeleton /></ViewTransition>}>
      <ViewTransition enter="slide-up" default="none"><Content /></ViewTransition>
    </Suspense>
  </div>
</ViewTransition>
```

---

## `loading.tsx` as Suspense Boundary

Next.js `loading.tsx` is an implicit `<Suspense>` boundary. Wrap the skeleton in `<ViewTransition exit="...">` in `loading.tsx`, and the content in `<ViewTransition enter="..." default="none">` in the page:

```tsx
// loading.tsx
<ViewTransition exit="slide-down"><PhotoGridSkeleton /></ViewTransition>

// page.tsx
<ViewTransition enter="slide-up" default="none"><PhotoGrid photos={photos} /></ViewTransition>
```

Same rules as explicit `<Suspense>`: use simple string props (not type maps) since Suspense reveals fire without transition types.

---

## Shared Elements Across Routes

```tsx
// List page
{products.map((product) => (
  <Link key={product.id} href={`/products/${product.id}`} transitionTypes={['nav-forward']}>
    <ViewTransition name={`product-${product.id}`}>
      <Image src={product.image} alt={product.name} width={400} height={300} />
    </ViewTransition>
  </Link>
))}

// Detail page with the same name
<ViewTransition name={`product-${product.id}`}>
  <Image src={product.image} alt={product.name} width={800} height={600} />
</ViewTransition>
```

---

## Same-Route Dynamic Segment Transitions

When navigating between dynamic segments of the same route such as
`/collection/[slug]`, the page stays mounted, so enter/exit never fire. Use
`key` + `name` + `share`:

```tsx
<Suspense fallback={<Skeleton />}>
  <ViewTransition key={slug} name={`collection-${slug}`} share="auto" default="none">
    <Content slug={slug} />
  </ViewTransition>
</Suspense>
```

- `key={slug}` forces unmount/remount on change
- `name` + `share="auto"` creates a shared element crossfade
- VT inside `<Suspense>` (without keying Suspense) keeps old content visible during loading

---

## Server Components

- `<ViewTransition>` works in both Server and Client Components
- In a compatible Next.js App Router release, `<Link transitionTypes>` works in Server Components without `'use client'`
- `addTransitionType` and `startTransition` for programmatic nav require Client Components
