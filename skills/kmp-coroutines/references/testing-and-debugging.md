# Testing, debugging, and observability

## Contents

- Test architecture
- runTest
- Test dispatchers
- Virtual time
- Long-lived work
- Flow tests
- Cancellation and failure tests
- Multiplatform test details
- Debugging
- Observability
- Proof checklist

## Test architecture

Inject every dispatcher or scope that affects scheduling. In a test:

- Use one `TestCoroutineScheduler`.
- Create all `TestDispatcher` instances from that scheduler.
- Keep real Main, Default, and IO out of deterministic unit tests.
- Use platform integration tests for actual threading behavior.

Test APIs, not implementation delays. Prefer a method that returns a result, `Job`, `Deferred`, or observable state over an unobservable fire-and-forget start.

## runTest

Use:

```kotlin
@Test
fun loads_state() = runTest {
    // Arrange, act, assert.
}
```

`runTest`:

- Creates a `TestScope`.
- Uses a test dispatcher.
- Skips delays on its scheduler.
- Reports uncaught child failures.
- Has a default whole-test timeout of 60 seconds in current kotlinx.coroutines.
- Waits for child work and scheduled work it controls.

Real dispatchers do not use virtual time. A `delay` inside `withContext(Dispatchers.Default)` consumes real time.

Do not nest `runTest`.

## Test dispatchers

`StandardTestDispatcher`:

- Queues new work.
- Resembles production scheduling more closely.
- Requires `runCurrent`, `advanceTimeBy`, `advanceUntilIdle`, `yield`, `join`, or another suspension to let queued work run.
- Is the default for `runTest`.

`UnconfinedTestDispatcher`:

- Enters top-level child coroutines eagerly.
- Can simplify state tests.
- Does not model production scheduling.
- Is a poor choice for concurrency-order assertions.

If multiple dispatchers are required:

```kotlin
@Test
fun coordinates_dispatchers() = runTest {
    val cpu = StandardTestDispatcher(testScheduler, "cpu")
    val io = StandardTestDispatcher(testScheduler, "io")
    val subject = Subject(cpu = cpu, io = io)

    subject.start()
    advanceUntilIdle()
}
```

## Virtual time

Use:

- `runCurrent()` for tasks scheduled at current virtual time.
- `advanceTimeBy(duration)` to move time forward.
- `advanceUntilIdle()` to drain finite scheduled work.

Avoid `advanceUntilIdle()` when the subject reschedules forever. Use precise advancement or `backgroundScope`.

All test dispatchers must share one scheduler. Class property initialization order can accidentally create multiple schedulers before Main is replaced.

On JVM Android-style unit tests, use a Main dispatcher rule or equivalent setup that calls `Dispatchers.setMain` and `resetMain`.

## Long-lived work

Use `backgroundScope` for work that intentionally never completes:

```kotlin
@Test
fun receives_updates() = runTest {
    val values = mutableListOf<Value>()

    backgroundScope.launch(UnconfinedTestDispatcher(testScheduler)) {
        subject.values.toList(values)
    }

    subject.update(Value.One)
    assertEquals(listOf(Value.Initial, Value.One), values)
}
```

`backgroundScope` is cancelled automatically at test end.

Do not launch an infinite collector as an ordinary child of `runTest` and then wait for natural completion.

## Flow tests

Cold finite Flow:

- Use `first`, `single`, `take(n).toList()`, or `toList()` when it completes.

Hot Flow:

- Assert `StateFlow.value` when intermediate emissions are not the contract.
- Start collection before emitting when subscription timing matters.
- Use a background collector for interleaved emission and assertion.
- Bound collection with `take`, cancellation, or a test helper.

StateFlow is conflated. Tests must not require every intermediate state unless the system contract uses a non-conflated stream.

For `shareIn` and `stateIn` with `WhileSubscribed`, a collector may be required to start upstream. Prove start, stop timeout, replay expiration, and restart behavior.

Third-party test tools such as Turbine can improve ergonomics, but verify their current KMP target support and timeout semantics before using them.

## Cancellation and failure tests

Test at least:

- Cancelling the owner cancels children.
- Cancelling a caller cancels the suspending operation.
- Cancellation unregisters callbacks.
- `CancellationException` is not materialized as failure.
- A child failure cancels siblings under `coroutineScope`.
- A child failure does not cancel independent siblings under supervision.
- Supervised failures are still observed.
- Timeout releases resources.
- Cleanup is bounded and idempotent.
- Late callbacks after cancellation are ignored safely.

Use `CompletableDeferred` or channels as synchronization points instead of real sleeps.

## Multiplatform test details

For common tests, use expression-body return:

```kotlin
@Test
fun common_test() = runTest {
    // ...
}
```

On Kotlin/JS, the `TestResult` from `runTest` must be returned immediately. Do not execute code after it, call it twice, or nest it.

On Native unit tests, do not use an unmocked Main queue when the test launcher does not process it. Replace Main when supported or inject a test dispatcher.

Run target-specific tests for:

- Main-dispatcher availability.
- Swift cancellation and callbacks.
- JS or Wasm event-loop behavior.
- JVM blocking interruption.
- Native memory and interop cleanup.

## Debugging

On JVM:

- Enable `-Dkotlinx.coroutines.debug` to add coroutine identifiers to thread names.
- Add `CoroutineName` to durable scopes and major operations.
- Use IntelliJ coroutine and Flow debuggers.
- Use `kotlinx-coroutines-debug` and `DebugProbes` for JVM tests or services when appropriate.
- Use timeout dumps for hanging tests.

`kotlinx-coroutines-debug` uses JVM instrumentation and is not an Android runtime solution. Avoid accidentally packaging it into Android.

Inspect a hang in this order:

1. Dump the Job tree.
2. Locate non-completing children.
3. Find real dispatchers outside the test scheduler.
4. Find blocking calls on a constrained thread.
5. Find a Flow or Channel waiting for a subscriber, send, receive, or close.
6. Find a `Mutex` held across a call that re-enters the same invariant.

On Native:

- Use Xcode Instruments and Kotlin/Native GC signposts for pause and memory analysis.
- Inspect retained interop objects and stable refs.
- Distinguish retained scopes from GC pause behavior.

## Observability

Name and measure ownership boundaries:

- Coroutine name.
- Owner ID that is safe to log.
- Start, completion, cancellation, and failure.
- Dispatcher or lane when useful.
- Retry attempt and deadline.
- Buffer overflow or dropped-value counts.
- Active subscriber or child counts when diagnosing leaks.

Do not log sensitive payloads merely to debug concurrency.

## Proof checklist

- Common tests pass.
- Materially different target tests pass.
- One scheduler controls deterministic unit tests.
- No real delay is used for ordering.
- Owner cancellation is asserted.
- Failure propagation and supervision are asserted.
- Flow start, stop, replay, and slow-consumer behavior are asserted.
- Callback and native resources are released.
- UI-thread responsiveness or event-loop non-blocking behavior has appropriate proof.
- Any untested platform is named as a proof gap.
