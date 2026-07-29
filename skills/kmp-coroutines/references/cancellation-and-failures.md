# Cancellation, failures, and supervision

## Contents

- Cancellation contract
- Cooperative cancellation
- Catching and translating failures
- Timeout semantics
- Cleanup
- Exception propagation
- Supervision
- Retry
- Failure checklist

## Cancellation contract

Cancellation is a normal control signal represented by `CancellationException`. Preserve it across every layer.

Use a narrow helper when broad failure capture is required:

```kotlin
inline fun <T> runCatchingPreservingCancellation(
    block: () -> T,
): Result<T> =
    try {
        Result.success(block())
    } catch (cancelled: CancellationException) {
        throw cancelled
    } catch (failure: Throwable) {
        Result.failure(failure)
    }
```

Use a suspending variant for suspend lambdas.

Standard `runCatching` catches `Throwable`, including cancellation. Do not use it across suspending work unless cancellation is rethrown.

## Cooperative cancellation

Coroutine cancellation is cooperative.

Suspending functions in kotlinx.coroutines usually check cancellation. Pure CPU loops and blocking calls may not.

For CPU loops:

```kotlin
while (hasMoreWork) {
    currentCoroutineContext().ensureActive()
    processChunk()
}
```

Use `yield()` when fairness and a suspension point are both useful. Do not add it blindly to tight loops without measuring.

For JVM blocking calls that react to interruption:

```kotlin
withContext(blockingDispatcher) {
    runInterruptible {
        blockingClient.read()
    }
}
```

For APIs with their own cancellation token, connect `invokeOnCancellation` to that token.

## Catching and translating failures

Never write a broad catch that turns cancellation into failure:

```kotlin
try {
    repository.sync()
} catch (failure: Exception) {
    state.value = Failed(failure)
}
```

Use:

```kotlin
try {
    repository.sync()
} catch (cancelled: CancellationException) {
    throw cancelled
} catch (failure: Exception) {
    state.value = Failed(failure)
}
```

Flow `catch` is transparent to downstream failures and cancellation when used correctly. It handles upstream exceptions. Do not use it to conceal programmer errors or infinite retry loops.

Materialize expected domain failures as values. Let programming errors and broken invariants fail visibly at an owned boundary.

## Timeout semantics

`withTimeout` cancels its block and throws `TimeoutCancellationException`, a subtype of `CancellationException`.

`withTimeoutOrNull` returns `null`. Use it only when `null` cannot be confused with a valid result.

Timeout is asynchronous relative to the block. A value acquired near the timeout boundary can be lost before it is returned. Acquire resources with structured lifetime and release them in `finally`.

Do not use timeouts as a substitute for:

- Backpressure.
- Proper request cancellation.
- Owner shutdown.
- Bounded retry.
- Server-side deadlines.

When crossing a network or process boundary, propagate the deadline if the protocol supports it.

## Cleanup

Suspending cleanup in a cancelled coroutine needs a small `NonCancellable` region:

```kotlin
try {
    runSession()
} finally {
    withContext(NonCancellable) {
        withTimeout(cleanupTimeout) {
            session.close()
        }
    }
}
```

Use this only when cleanup must suspend. Ordinary non-suspending `finally` code runs during cancellation without `NonCancellable`.

Keep cleanup:

- Idempotent.
- Bounded.
- Minimal.
- Independent of optional business work.

Do not launch new unowned work from `finally`.

## Exception propagation

`launch` and `async` differ:

- A root-like `launch` reports an uncaught exception.
- A root-like `async` captures the exception until `await`.
- Child failures normally cancel their parent, regardless of a child `CoroutineExceptionHandler`.
- `CoroutineExceptionHandler` is a last-resort handler for uncaught root-like failures. It is not a general `try/catch`.

The first failure normally wins. Later failures may be attached as suppressed exceptions on supported platforms.

Parent completion waits for children, including their cleanup.

Inspect every `Deferred` and prove it is awaited or otherwise observed.

## Supervision

`SupervisorJob` and `supervisorScope` stop a child failure from cancelling siblings. Cancellation of the supervisor still cancels children.

Use supervision for independently useful work such as:

- Separate dashboard tiles.
- Independent optional integrations.
- Long-lived service children whose failures are individually restarted or surfaced.

Do not use supervision for:

- Two values required to construct one result.
- Transactions.
- Invariants that require all children to succeed.
- Hiding an exception.

In `supervisorScope`, direct `launch` children behave like root coroutines for exception handling. Direct `async` children still require `await`.

## Retry

Retry only failures that are:

- Classified as transient.
- Idempotent or protected by an idempotency key.
- Bounded by attempts or a deadline.
- Cancelable during backoff.
- Observable.

Never retry `CancellationException`.

For Flow, `retryWhen` sees upstream failures. It does not handle downstream collector failures.

Use jittered backoff for distributed systems. Keep backoff in suspendable delays, not blocking sleeps.

## Failure checklist

- Cancellation is rethrown through every broad catch.
- Callback cancellation unregisters the callback or cancels the underlying work.
- Timeout does not leak an acquired resource.
- Cleanup cannot hang forever.
- Each `async` result is awaited.
- Each supervised child reports or materializes failure.
- Retry is bounded, classified, and cancellation-aware.
- Expected failures are represented in domain state.
- Unexpected failures reach an observable owner boundary.
