# Compose Runtime and Navigation Engineering

**Skill ID:** `compose-runtime-navigation`

**Compiled:** 2026-07-28

Design, review, debug, and test Jetpack Compose and Compose Multiplatform state,
effects, lifecycle collection, recomposition, saveable state, list identity,
edge-to-edge behavior, and navigation.

Use it for duplicate collectors, stale effects, state loss, recomposition bugs,
back-stack design, screen lifetime, UI tests, Navigation 2, Navigation 3, or
custom navigation systems.

Start with [`kotlin-current`](../kotlin-current/) and add
[`kmp-coroutines`](../kmp-coroutines/) when underlying async ownership is also
involved.

The audit script is optional. Compilation alone cannot prove composition
lifetime, restoration, predictive back, or target-specific lifecycle behavior.

Original instructions are available under the repository
[MIT License](../../LICENSE).
