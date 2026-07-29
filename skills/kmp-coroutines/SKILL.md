---
name: kmp-coroutines
description: Design, review, debug, and test coroutine systems across Kotlin Multiplatform targets. Use for CoroutineScope, Job, dispatchers, suspend APIs, structured concurrency, cancellation, exception handling, supervision, Flow, StateFlow, SharedFlow, Channel, callback adapters, concurrency control, coroutine tests, hangs, leaks, races, UI freezes, dropped events, stale state, or cross-platform scheduling differences. Use the separate Compose and Native/Swift capsules when composition or export behavior owns the problem.
---

# KMP Coroutines

**Compiled knowledge:** 2026-07-28

Treat coroutine failures first as ownership, lifetime, failure-policy, and platform-capability failures.

## Establish current truth

Use `$kotlin-current` first for nontrivial repository work. Identify:

```text
Kotlin:
kotlinx.coroutines:
targets:
platform coroutine artifacts:
scope owners:
dispatcher providers:
test schedulers:
hot-flow owners:
callback boundaries:
```

Fetch current official documentation for installed library versions. Read [source-catalog.md](references/source-catalog.md) for the researched source map and conflict policy.

Use `$compose-runtime-navigation` when composition, effects, lifecycle collection, or navigation owns the work. Use `$native-swift-current` for Swift or Objective-C export and bridging. Use `$ktor3-client` for transport behavior.

## Build the ownership map

For every coroutine entry point answer:

| Question | Required answer |
|---|---|
| Who owns the work? | operation, screen, ViewModel, session, repository, application, process, request, or test |
| When must it stop? | exact lifecycle event or completion condition |
| Which `Job` is its parent? | trace the actual context, including any replacement `Job()` |
| Where may it execute? | Main, CPU pool, blocking-I/O pool, serial lane, platform callback thread, or event loop |
| How does cancellation arrive? | parent, timeout, consumer loss, callback cleanup, or explicit close |
| What is the failure policy? | fail siblings, isolate, retry, materialize, or terminate owner |
| How is the result represented? | return, Flow, state, event, channel, persisted effect, or callback |
| Which target boundary matters? | Android, JVM desktop, Darwin, other Native, JS, Wasm, or C |

If any answer is unknown, keep investigating.

Read [architecture.md](references/architecture.md), [cancellation-and-failures.md](references/cancellation-and-failures.md), and [platforms.md](references/platforms.md).

## Core rules

1. Prefer a suspending API that completes with its work. Use a scope only when work must outlive the call.
2. Make every long-lived scope owned, named, and canceled at a documented boundary.
3. Preserve the caller's `Job`. Never add `Job()` or `SupervisorJob()` to a child launch to change failure behavior.
4. Use `coroutineScope` for fail-together work. Use `supervisorScope` only when sibling independence is a product rule and every failure has an owner.
5. Never use `GlobalScope` as an escape hatch.
6. Make suspend functions safe for the declared caller. Move blocking work at the implementation boundary.
7. Inject dispatchers or an application dispatcher provider. Keep platform-only dispatchers out of portable code.
8. Rethrow `CancellationException`. Never convert cancellation to generic failure or retry.
9. Keep `NonCancellable` cleanup small and bounded.
10. Expose immutable Flow views and centralize mutation.
11. Use `MutableStateFlow.update` when new state depends on old state.
12. Choose `stateIn` or `shareIn` only after owner scope, start policy, replay, buffer, and error representation are explicit.
13. Use `callbackFlow` for multi-shot callbacks and `suspendCancellableCoroutine` for one-shot callbacks. Release resources on cancellation.
14. Use synchronization that matches the invariant. `limitedParallelism(1)` is not a mutex.
15. Use one `TestCoroutineScheduler` per test and inject all relevant dispatchers.
16. Test cancellation, owner destruction, child failure, slow consumers, no consumers, duplicate starts, and late callbacks.

Read [streams.md](references/streams.md), [interop.md](references/interop.md), and [testing-and-debugging.md](references/testing-and-debugging.md).

## Platform capability matrix

| Target | Main | Blocking work | Critical trap |
|---|---|---|---|
| Android | needs `kotlinx-coroutines-android` | injected blocking-I/O dispatcher | UI owner accidentally owns session or repository work |
| JVM desktop | needs Swing or JavaFX Main provider | injected IO or bounded dispatcher | Main missing at runtime |
| Darwin Native | current support uses Darwin main queue | injected supported dispatcher | exported completion executor is assumed |
| Other Native | current API reports Main unavailable | supported target dispatcher | portable code assumes UI Main |
| JS and Wasm/JS | Main is equivalent to Default event loop | never block the event loop | switching dispatcher is mistaken for parallelism |
| Wasm/WASI | no generic UI Main assumption | target-supported facilities | JVM or browser assumptions leak |

Refresh this table against the installed coroutine version. A migration guide does not override current API reference.

## Flow and event decisions

Use:

- cold `Flow` for per-collector work
- `StateFlow` for current observable state
- `SharedFlow` for broadcast where replay and loss are explicit
- `Channel` for coordinated queue or handoff semantics

Do not model a durable state transition as a lossy event. Do not assume `StateFlow` completes. Do not mutate shared state with `value = value.copy(...)` when concurrent writers can race.

Read [streams.md](references/streams.md).

## Audit and diagnose

When Python is available, run:

```text
python <skill-dir>/scripts/audit_kmp_coroutines.py <repository-root>
```

Scanner hits are leads, not findings. Trace ownership before proposing a fix.
If Python is unavailable, inspect the ownership and stale-pattern rules
manually and record that the advisory scanner was not run.

Use [failure-catalog.md](references/failure-catalog.md):

- UI freeze: blocking call, CPU loop, Main overload, or synchronous join.
- Work after navigation: wrong owner or detached job.
- Unrelated cancellation: parent tree or failure policy mismatch.
- Missing error: un-awaited `async`, supervised child without handler, or broad catch.
- Flow never starts or stops: collection, sharing owner, start policy, or lifecycle mismatch.
- Event disappears: replay, buffer, overflow, subscriber timing, or wrong state/event model.
- Test hangs: infinite hot-flow collection, real dispatcher, foreign scheduler, or uncanceled child.
- Cross-target mismatch: dispatcher, event loop, artifact, or callback cleanup difference.

## Implement and prove

Before editing:

1. Draw owner and job trees.
2. State cancellation and failure semantics.
3. Choose portable contract and platform implementations.
4. Identify the unhappy path at each boundary.

After editing:

1. Compile affected source sets.
2. Run common and materially different target tests.
3. Exercise owner cancellation, failure propagation, slow consumers, and cleanup.
4. Confirm no work remains after owner destruction.
5. Confirm tests use virtual time and controlled dispatchers where intended.
6. Review scanner output and the diff.

Use [patterns.md](references/patterns.md) for copyable templates.

## Stale-pattern denylist

Investigate:

- `GlobalScope`.
- Anonymous application scopes with no close boundary.
- `Job()` or `SupervisorJob()` added inside a child context.
- Broad `catch (Throwable)` around suspending work.
- `runBlocking` in UI, request, or shared library paths.
- Hardcoded `Dispatchers.IO` in `commonMain`.
- `Dispatchers.Main` assumed on every target.
- `launch` hidden in a repository method that should be suspend.
- `async` result never awaited.
- `flowOn` used as a substitute for ownership or synchronization.
- `MutableStateFlow.value = value.copy(...)` with concurrent writers.
- `SharedFlow` used for must-deliver durable actions.
- `limitedParallelism(1)` treated as mutual exclusion.
- `runTest` with separately created schedulers.
- legacy Native freezing or native-mt advice.
