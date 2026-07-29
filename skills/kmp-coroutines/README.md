# Kotlin Multiplatform Coroutines Engineering

**Skill ID:** `kmp-coroutines`

**Compiled:** 2026-07-28

Design, review, debug, and test coroutine systems across Kotlin Multiplatform
targets. The skill treats failures as ownership, lifetime, cancellation,
failure-policy, stream-semantics, and platform-capability problems before
treating them as syntax problems.

Use it for scopes, jobs, dispatchers, structured concurrency, supervision,
Flow, StateFlow, SharedFlow, Channel, callback adapters, races, leaks, hangs,
UI freezes, dropped events, and virtual-time testing.

Start with [`kotlin-current`](../kotlin-current/) for repository discovery.
Detailed references cover architecture, cancellation, failures, streams,
platforms, interop, debugging, testing, reusable patterns, and a failure
catalog.

The audit script is optional. Without Python, apply the same ownership and
stale-pattern review manually. Platform readiness still requires compilation
and unhappy-path testing on materially different targets.

Original instructions are available under the repository
[MIT License](../../LICENSE).
