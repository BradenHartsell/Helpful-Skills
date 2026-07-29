# Coroutine patterns

## Owned long-lived scope

```kotlin
class SessionScope(
    dispatcher: CoroutineDispatcher,
) : Closeable {
    private val job = SupervisorJob()
    val scope = CoroutineScope(job + dispatcher + CoroutineName("session"))

    override fun close() {
        job.cancel()
    }
}
```

Use supervision only when session children are intentionally independent and each reports failure.

## Main-safe suspend implementation

```kotlin
class FileStore(
    private val blocking: CoroutineDispatcher,
) {
    suspend fun read(): ByteArray = withContext(blocking) {
        blockingRead()
    }
}
```

The implementation owns the blocking hop. Callers do not guess.

## Atomic state update

```kotlin
private val _state = MutableStateFlow(State())
val state: StateFlow<State> = _state.asStateFlow()

fun markReady(id: String) {
    _state.update { current -> current.copy(readyIds = current.readyIds + id) }
}
```

## Fail-together parallel work

```kotlin
suspend fun load(): Result = coroutineScope {
    val first = async { loadFirst() }
    val second = async { loadSecond() }
    combine(first.await(), second.await())
}
```

## Supervised independent work

```kotlin
suspend fun refreshIndependentPanels() = supervisorScope {
    launch {
        try {
            refreshA()
        } catch (cancelled: CancellationException) {
            throw cancelled
        } catch (failure: Throwable) {
            reportA(failure)
        }
    }
    launch {
        try {
            refreshB()
        } catch (cancelled: CancellationException) {
            throw cancelled
        } catch (failure: Throwable) {
            reportB(failure)
        }
    }
}
```

Do not use `runCatching` around arbitrary suspending work unless cancellation is rethrown explicitly.

## One scheduler in tests

```kotlin
@Test
fun ownerCancellationStopsWork() = runTest {
    val dispatcher = StandardTestDispatcher(testScheduler)
    val subject = Subject(dispatcher)

    subject.start()
    subject.close()
    advanceUntilIdle()

    assertFalse(subject.isRunning)
}
```

## Hot-flow test

Use `backgroundScope` for collection that should remain active during the test:

```kotlin
val values = mutableListOf<State>()
backgroundScope.launch(UnconfinedTestDispatcher(testScheduler)) {
    subject.state.toList(values)
}
```

Bound expectations and cancel collection through the test owner.
