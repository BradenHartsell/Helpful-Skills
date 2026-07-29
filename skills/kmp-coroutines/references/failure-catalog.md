# Coroutine failure catalog

## Contents

- UI and event-loop failures
- Lifetime and leak failures
- Cancellation failures
- Exception failures
- Flow and channel failures
- Test failures
- Platform failures
- Architectural escalation

## UI and event-loop failures

### UI freezes while coroutines are active

Likely causes:

- Blocking call on Main.
- CPU-heavy code before the first suspension.
- Many Main launches doing non-suspending work.
- `runBlocking` on UI thread.
- Synchronous `join`, lock, or callback bridge.
- JS or Wasm event loop blocked by a loop.

Trace:

1. Identify current dispatcher at each expensive section.
2. Inspect the body before its first true suspension.
3. Measure Main or event-loop occupancy.
4. Find implementation boundaries that should move blocking or CPU work.

### Jank despite moving work to Default

Likely causes:

- Too much parallel fan-out.
- State updates causing excessive recomposition.
- Large value copying on Main.
- Dispatcher ping-pong.
- Native GC pressure from interop allocations.

Bound parallelism, batch state changes, and profile before adding more scopes.

## Lifetime and leak failures

### Work continues after navigation or logout

Likely causes:

- Application scope used for screen work.
- `Job()` replaced parent.
- Composition scope stored in a longer-lived object.
- Hot flow shared in a longer-lived scope.
- Callback not unregistered.
- Session owner not closed on identity change.

Trace from launch to the actual parent Job and owner close path.

### Work stops too early

Likely causes:

- Composition or screen scope owns a write that must survive navigation.
- `WhileSubscribed` stops upstream during a brief subscriber gap.
- ViewModel is recreated or cleared.
- Parent failed due to an unrelated child.

Move work only to the smallest owner that satisfies the required lifetime.

### Duplicate work after recomposition

Likely causes:

- Incorrect `LaunchedEffect` key.
- Start called during composition without an effect.
- Multiple collectors each start a cold upstream.
- `shareIn` or `stateIn` missing where one shared upstream is intended.

## Cancellation failures

### Cancel does nothing

Likely causes:

- CPU loop lacks cancellation checks.
- Blocking call is not interruptible.
- External request has no cancellation bridge.
- Parent was detached.
- Code catches and swallows `CancellationException`.

### Cancel appears as an error

Likely causes:

- Broad catch.
- `runCatching` around suspend work.
- Flow `catch` materializes cancellation.
- Logging boundary treats cancellation as failure.

Rethrow cancellation before translating failures.

### Cleanup hangs

Likely causes:

- Unbounded work in `NonCancellable`.
- Cleanup waits for a child that waits for the owner.
- Blocking close on Main.
- Callback unregister never returns.

Make cleanup minimal, idempotent, and bounded.

## Exception failures

### Error disappears

Likely causes:

- `Deferred` never awaited.
- Supervised child failure has no consumer.
- Empty `CoroutineExceptionHandler`.
- Broad catch logs and continues.
- Hot sharing coroutine failed without state materialization.

### One failure cancels unrelated features

Likely causes:

- Unrelated children share a regular Job.
- Application scope lacks a deliberate supervision boundary.
- A long-lived root was modeled as one fail-together operation.

Do not add supervision until product independence is proven.

### Siblings keep running when the whole operation should fail

Likely causes:

- `supervisorScope` used inside an atomic operation.
- Child launched in an external scope.
- Failure converted to a value too early.

## Flow and channel failures

### Flow never emits

Likely causes:

- Cold Flow has no terminal collector.
- `WhileSubscribed` has no subscriber.
- Callback registration did not occur.
- Upstream waits on a channel send or receive.
- Test collector has not been scheduled.

### First event is lost

Likely causes:

- `SharedFlow` replay is zero.
- Emitter runs before subscriber registration.
- `tryEmit` failed.
- Channel consumer was not ready.

Define whether this is state, replayable event, or fire-and-forget event.

### Memory grows under load

Likely causes:

- Unlimited Channel.
- Large SharedFlow replay.
- Slow subscriber plus large buffer.
- Unbounded `flatMapMerge` or child launches.
- Retained collector scope.
- Callback registration leak.

### State appears stale

Likely causes:

- Mutable object changed in place.
- Equal value suppressed by StateFlow.
- Non-atomic read-modify-write lost an update.
- Collector follows composition rather than visible lifecycle.
- Derived state shared in the wrong scope.

### Multiple flow collections run sequentially

Likely cause:

```kotlin
flowA.collect { ... }
flowB.collect { ... }
```

The first non-terminating collection never returns. Launch parallel child collectors inside an owned scope or combine the flows.

## Test failures

### Test hangs at 60 seconds

Likely causes:

- Infinite collector is a normal child.
- Background loop keeps scheduler non-idle.
- Real dispatcher or blocking call.
- Hot Flow collection waits for completion.
- Callback never completes.

Use `backgroundScope`, bounded collection, injected dispatchers, and deterministic synchronization.

### Test passes alone but flakes in suite

Likely causes:

- Global Main replacement not reset.
- Multiple test schedulers.
- Global scope or application singleton retains work.
- Real clock or dispatcher.
- Shared mutable fake.

### `advanceUntilIdle` never returns

Likely cause:

- Work continually schedules more work.

Advance a bounded duration or run the infinite worker in `backgroundScope`.

### Common JS test silently misses failure

Likely cause:

- `runTest` result was not returned immediately.

Use expression-body tests or return `TestResult`.

## Platform failures

### Missing Main dispatcher on desktop

Add the correct Swing or JavaFX runtime artifact and verify the packaged application.

### Missing Main dispatcher on non-Darwin Native

Current API says it is unavailable. Inject a supported dispatcher and remove portable UI assumptions.

### Swift UI update crashes or warns about wrong thread

Completion or Flow value arrived off Main. Hop to `MainActor` in Swift or Main in Kotlin for the UI section.

### Native freezing advice appears in code review

The legacy memory manager is gone. Investigate actual synchronization, ownership, and retention under the modern shared heap.

### JS dispatcher switch does not improve performance

Main and Default share the event loop. Dispatcher switching does not provide CPU parallelism.

## Architectural escalation

Escalate from a local fix to a system change when:

- Many classes create their own scopes.
- Dispatchers are hardcoded across layers.
- Lifecycle ownership differs by platform with no shared contract.
- Every feature invents its own event buffering.
- Cancellation is repeatedly translated into errors.
- Tests require sleeps because APIs do not expose completion.
- One large UI owner launches many unrelated background tasks.

Propose a shared owner hierarchy, dispatcher provider, lifecycle contract, stream semantics, and test scheduler policy instead of patching each symptom.
