# Coroutine architecture

## Contents

- Model work as an ownership tree
- Choose the API shape
- Create and own scopes
- Preserve structured concurrency
- Choose supervision deliberately
- Keep suspend functions main-safe
- Protect shared mutable state
- Review checklist

## Model work as an ownership tree

A coroutine is safe only when its lifetime has an owner. Start with the product lifetime, then map it to a scope:

| Product lifetime | Typical owner |
|---|---|
| One operation | Calling suspend function and `coroutineScope` |
| One composition node | `LaunchedEffect` or `rememberCoroutineScope` |
| One screen or navigation entry | ViewModel or screen lifecycle |
| One authenticated session | Session component with an owned scope |
| One repository subscription | Repository owner or caller collection |
| One application process | Application component with explicit shutdown |
| One server request | Request scope |
| One test | `TestScope` |

The owner must define:

- Creation point.
- Parent `Job`.
- Dispatcher policy.
- Failure policy.
- Cancellation point.
- Cleanup and observability.

A `CoroutineScope` is not merely a place to call `launch`. It is a lifetime capability.

## Choose the API shape

Prefer these shapes in order:

1. `suspend fun`: one operation, one result, caller controls cancellation.
2. `fun observe(): Flow<T>`: repeatable stream, collector controls collection.
3. `StateFlow<T>`: owner-held current state with an initial value.
4. `SharedFlow<T>`: owner-held broadcast stream with explicit replay and buffer semantics.
5. Injected or owned `CoroutineScope`: work deliberately outlives the call.
6. `Channel`: queue, fan-out, fan-in, or point-to-point delivery with explicit close semantics.

Avoid methods that launch hidden work and return `Unit`. If startup must be asynchronous, return `Job` or `Deferred`, expose observable state, or make initialization suspending.

## Create and own scopes

For a durable non-UI owner:

```kotlin
class SessionRuntime(
    parentScope: CoroutineScope,
    dispatcher: CoroutineDispatcher,
) : AutoCloseable {
    private val job = SupervisorJob(parentScope.coroutineContext[Job])
    private val scope = CoroutineScope(
        parentScope.coroutineContext.minusKey(Job) +
            job +
            dispatcher +
            CoroutineName("session-runtime")
    )

    override fun close() {
        job.cancel()
    }
}
```

Use this pattern only when the runtime truly has a distinct lifetime. If the work should finish before a function returns, use `coroutineScope` instead.

Do not write:

```kotlin
scope.launch(Job()) {
    work()
}
```

The new `Job()` replaces the inherited parent job and detaches cancellation. To create a child owner, pass the current parent to `Job(parent)` or `SupervisorJob(parent)` at the owner's construction boundary.

Do not rely on garbage collection to cancel a scope.

## Preserve structured concurrency

Use `coroutineScope` when all children form one operation:

```kotlin
suspend fun loadDashboard(): Dashboard = coroutineScope {
    val account = async { accountRepository.load() }
    val activity = async { activityRepository.load() }
    Dashboard(account.await(), activity.await())
}
```

If either child fails, the operation fails and the sibling is cancelled. The scope waits for all cleanup before returning.

Prefer sequential calls unless concurrency materially reduces latency. `async` has overhead and expands failure timing.

Avoid async-style APIs:

```kotlin
fun loadAsync(): Deferred<Result> = GlobalScope.async { load() }
```

Return a suspending result instead. Let the caller choose concurrency.

## Choose supervision deliberately

Use `supervisorScope` when child independence is required:

```kotlin
suspend fun refreshIndependentTiles(): List<TileResult> = supervisorScope {
    tileSources.map { source ->
        async {
            runCatchingPreservingCancellation { source.refresh() }
        }
    }.awaitAll()
}
```

Supervision does not handle failures. It only changes propagation. Every supervised child must do one of these:

- Return a materialized result.
- Be awaited by an owner that handles failure.
- Be a root-like `launch` with an explicit handler or failure-reporting boundary.

Do not add `SupervisorJob` to silence a crash without defining the new product behavior.

## Keep suspend functions main-safe

A suspending function does not automatically run off the main thread. `suspend` means it may suspend.

The implementation that performs blocking or CPU-heavy work owns the dispatcher switch:

```kotlin
class FileIndex(
    private val blockingDispatcher: CoroutineDispatcher,
) {
    suspend fun readAll(): List<Entry> =
        withContext(blockingDispatcher) {
            blockingFileApi.readAll()
        }
}
```

Do not wrap already non-blocking suspending APIs in `Dispatchers.IO` without a documented reason. Avoid dispatcher ping-pong at call sites.

For CPU-heavy loops:

- Use an injected Default-like dispatcher.
- Add `ensureActive()` or `yield()` at useful boundaries when the loop has no suspending calls.
- Bound parallel fan-out.

For blocking JVM calls that support interruption, consider `runInterruptible` inside the blocking dispatcher.

## Protect shared mutable state

Prefer state ownership and immutable values. When state is shared:

- `MutableStateFlow.update` for atomic read-modify-write.
- `Mutex` for suspending critical sections.
- Kotlin Atomics for simple atomic state.
- Thread confinement when a platform requires one serial owner.
- `Semaphore` for permits, not mutual exclusion of a state invariant.
- `limitedParallelism(1)` only for execution parallelism. It is not a mutex across suspension points.

This is unsafe:

```kotlin
state.value = state.value.copy(count = state.value.count + 1)
```

Use:

```kotlin
state.update { current ->
    current.copy(count = current.count + 1)
}
```

Do not store mutable collections or mutable objects inside `StateFlow`. In-place mutation does not replace the value and may not emit.

## Review checklist

- Every launch has a named owner.
- Every owner has a cancellation point.
- No child replaces its inherited `Job`.
- No hidden application work runs in a composition scope.
- No `GlobalScope` or unowned `CoroutineScope`.
- Suspending APIs preserve caller cancellation.
- Blocking and CPU work switch dispatcher at their implementation boundary.
- Parallelism is bounded.
- Supervision has an explicit failure consumer.
- Shared state updates are atomic or confined.
- Long-lived scope shutdown is tested.
