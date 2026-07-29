# Flow, state, shared streams, and channels

## Contents

- Choose the stream type
- Cold Flow
- Flow context
- Backpressure and latest-value semantics
- StateFlow
- SharedFlow
- Sharing cold flows
- CallbackFlow
- Channels
- Completion and failure
- Stream checklist

## Choose the stream type

| Need | Use |
|---|---|
| One result | Suspending function |
| Repeat computation per collector | Cold `Flow` |
| Current observable state | `StateFlow` |
| Broadcast values with replay or buffer policy | `SharedFlow` |
| Point-to-point queue or work distribution | `Channel` |
| One-shot callback bridge | `suspendCancellableCoroutine` |
| Multi-shot callback bridge | `callbackFlow` |

Do not choose by familiarity. State, events, and queues have different loss, replay, completion, and ownership semantics.

## Cold Flow

A cold Flow starts for each collector. Operators are lazy until a terminal operator runs.

By default:

- Emission and collection are sequential.
- The flow preserves context.
- The collector controls cancellation.
- Completion and exceptions are part of the stream.

Do not call `withContext` around `emit` inside `flow {}`. Use `flowOn` to move upstream work:

```kotlin
fun indexes(): Flow<Index> =
    flow {
        emit(blockingIndexRead())
    }.flowOn(blockingDispatcher)
```

`flowOn` changes upstream context and preserves downstream collector context. It may introduce buffering and an extra coroutine across a dispatcher change.

Use `channelFlow` only when concurrent emission is required.

## Flow context

Intermediate operators normally execute in the collector's context unless an upstream `flowOn` changes it.

Keep context changes close to the implementation that requires them. Avoid multiple `flowOn` calls without a clear pipeline map.

`launchIn(scope)` is a terminal operator. The provided scope owns collection and must be the correct lifetime.

## Backpressure and latest-value semantics

Choose based on product behavior:

- Default sequential Flow: producer suspends behind consumer.
- `buffer(capacity)`: producer and consumer can overlap.
- `conflate()`: slow collector skips intermediate values and receives the latest.
- `collectLatest`: new value cancels the prior collector action.
- `mapLatest` and `flatMapLatest`: new input cancels prior transform or inner flow.
- `debounce`: waits for quiet time and may omit rapidly changing values.
- `sample`: emits the latest value periodically.

Cancellation of previous work is safe only if the work is cancellation-cooperative and has correct cleanup.

Do not use conflation for commands, payments, writes, or any event that must be processed exactly once.

## StateFlow

`StateFlow`:

- Is hot.
- Always has a current value.
- Never completes normally.
- Replays one current value.
- Uses equality-based conflation.
- Is thread-safe.

Expose a read-only view:

```kotlin
private val _state = MutableStateFlow(ScreenState())
val state: StateFlow<ScreenState> = _state.asStateFlow()
```

Use atomic updates:

```kotlin
_state.update { current ->
    current.copy(items = current.items + item)
}
```

Avoid:

- In-place mutation of a value.
- Values with broken `equals`.
- Using StateFlow for transient commands.
- Expecting collectors to see every intermediate update.
- Calling `toList()` without a bound because collection never completes.

If failure or completion matters, encode it in the state model.

## SharedFlow

Define these before creating a SharedFlow:

- Replay count.
- Extra buffer capacity.
- Buffer overflow policy.
- Behavior with zero subscribers.
- Required delivery guarantee.
- Owner scope and shutdown behavior.

An unbuffered `MutableSharedFlow()` has no replay. Subscriber timing matters.

Buffer overflow configuration only applies when a subscriber is too slow. With no subscribers, only replay values are retained and emitters do not suspend for absent subscribers.

Do not use `tryEmit` without handling its Boolean result when loss matters.

Expose `asSharedFlow()` rather than the mutable instance.

## Sharing cold flows

`stateIn` and `shareIn` launch a sharing coroutine in the supplied scope. The scope is therefore an ownership decision.

Choose `SharingStarted`:

- `Eagerly`: upstream starts immediately and may run without subscribers.
- `Lazily`: starts with the first subscriber and stays active until owner cancellation.
- `WhileSubscribed`: starts and stops based on subscriber count.

For `WhileSubscribed`, choose:

- Stop timeout, often used to bridge brief lifecycle gaps.
- Replay expiration, which controls how long cached values survive after stop.

Handle upstream failure before sharing:

```kotlin
val state =
    repository.observe()
        .map<ResultState> { ResultState.Ready(it) }
        .catch { failure ->
            if (failure is CancellationException) throw failure
            emit(ResultState.Failed(failure))
        }
        .stateIn(
            scope = ownerScope,
            started = SharingStarted.WhileSubscribed(stopTimeout),
            initialValue = ResultState.Loading,
        )
```

The sharing coroutine's upstream completion does not complete subscribers. Materialize completion if it matters.

## CallbackFlow

Use `callbackFlow` for multi-shot callbacks:

```kotlin
fun observeSensor(): Flow<Reading> = callbackFlow {
    val listener = SensorListener { reading ->
        trySend(reading).onFailure {
            // Record or handle delivery failure if required.
        }
    }

    sensor.register(listener)

    awaitClose {
        sensor.unregister(listener)
    }
}
```

Verify:

- Registration is thread-safe.
- Unregistration can race with callback delivery.
- `trySend` failure is handled according to product semantics.
- Buffer policy matches burst behavior.
- Late callbacks cannot access released resources.
- `awaitClose` runs on cancellation and normal closure.

Use `close(cause)` for terminal callback failure when appropriate.

## Channels

Channels model communication, not observable state.

Default `Channel()` capacity is rendezvous. Sender and receiver meet unless buffering is configured.

Choose:

- Rendezvous for strict handoff.
- Bounded buffer for controlled producer lead.
- Conflated for latest-only signals.
- Unlimited only with a proven memory bound elsewhere.

Define who closes the channel. Usually the producer owns close.

When consuming a channel, decide whether failure should cancel the consumer, close the channel, or be materialized.

Prefer Flow operators over hand-built channel pipelines when a declarative stream is sufficient.

## Completion and failure

- Cold Flow completes or fails.
- StateFlow and SharedFlow do not complete by themselves.
- Channel can close normally or with a cause.
- `catch` sees upstream exceptions, not downstream collector failures.
- `onCompletion` observes completion cause and can distinguish success from failure.
- Cancellation must stay cancellation.

## Stream checklist

- The type matches state, event, or queue semantics.
- Owner scope for hot flows is explicit.
- Replay and zero-subscriber behavior are documented.
- Buffer and overflow policies are intentional.
- Cancellation of latest-style work is safe.
- State updates are immutable and atomic.
- Callback registration always has cleanup.
- Hot-flow tests never wait for natural completion.
- Failure and completion are represented where the consumer needs them.
