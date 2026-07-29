---
name: compose-runtime-navigation
description: Design, review, debug, and test Jetpack Compose and Compose Multiplatform runtime behavior, effects, state ownership, lifecycle collection, recomposition, saveable state, list identity, edge-to-edge, and Navigation 2 or Navigation 3. Use for composables, duplicate collectors, stale effects, state loss, recomposition bugs, back-stack design, screen lifecycle, UI tests, or Compose compiler/runtime integration.
---

# Compose Runtime and Navigation

**Compiled knowledge:** 2026-07-28

Correct coroutine code can still be incorrect composition code. Own composition behavior here and use `$kmp-coroutines` only for the underlying async semantics.

## Preflight

Use `$kotlin-current`. Identify:

```text
Compose runtime and plugin versions:
AndroidX or Compose Multiplatform:
targets:
Navigation 2, Navigation 3, custom, or mixed:
screen state owner:
durable state owner:
collection lifecycle:
effect keys:
saveable state:
edge-to-edge owner:
UI test targets:
```

Do not migrate navigation generations as a side effect of an unrelated fix.

## Model state and effects

Read [state-and-effects.md](references/state-and-effects.md).

1. Hoist state to the lowest owner that needs to read or change it.
2. Keep durable business state outside composition.
3. Use immutable observable state. Never rely on mutating an ordinary collection inside snapshot state.
4. Key effects by every input that should restart the work, and no incidental input.
5. Use `rememberUpdatedState` when an effect must see a changing value without restarting.
6. Use `DisposableEffect` for paired registration and cleanup.
7. Use `rememberCoroutineScope` for user events whose lifetime is the current composition.
8. Use `LaunchedEffect` for composition-owned suspending work.
9. Collect with the lifecycle mechanism appropriate to the target and owner.
10. Give lazy-list items stable semantic keys.
11. Save only reconstruction data. Do not save repositories, clients, scopes, or large graphs.

## Navigation generation

Read [navigation.md](references/navigation.md).

- Navigation 2 centers on `NavController` and a navigation graph.
- Navigation 3 makes the app-owned back stack data explicit and renders `NavEntry` values through `NavDisplay`.
- A custom back stack is a third architecture.

Determine the generation from dependencies and code. Do not mix route strings, typed keys, controllers, and entry providers casually.

## Stale-pattern denylist

Investigate:

- `launch` directly in a composable body.
- A collector started on every recomposition.
- `LaunchedEffect(Unit)` that captures changing parameters incorrectly.
- Missing cleanup for listeners or observers.
- `remember` used for state that must survive recreation.
- `rememberSaveable` used for a large model.
- Mutable `ArrayList` or `HashMap` inside state without snapshot-aware observation.
- Index-only lazy-list identity for reorderable items.
- State duplicated in a composable, ViewModel, and navigation entry.
- Navigation 2 and 3 APIs mixed without a migration boundary.
- Fixed system-bar padding.
- `Dispatchers.Main` assumed available on desktop without the platform artifact.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_compose_runtime.py <repository-root>
```

If Python is unavailable, apply the state, effect, navigation, and lifecycle
denylist manually and record that the advisory scanner was not run.

## Validate

Read [testing.md](references/testing.md). Exercise:

- recomposition without duplicate work
- key changes and stale captured values
- disposal and navigation away
- rapid navigation and repeated taps
- process recreation and saveable restoration
- deep link and cold-start back stack
- predictive back, canceled gesture, and completed gesture
- lazy-list reorder and state retention
- lifecycle stop and restart
- insets with keyboard, cutout, gesture, and three-button navigation
- target-specific lifecycle behavior in Compose Multiplatform

Compilation is not proof of correct composition lifetime.
