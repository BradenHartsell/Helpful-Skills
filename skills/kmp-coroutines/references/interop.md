# Callback and foreign async interop

This capsule owns coroutine-side callback adaptation. Use `$native-swift-current` for Swift and Objective-C export, and `$ktor3-client` for transport streams.

## Boundary contract

At every callback, Promise, listener, or C boundary define:

- one-shot or multi-shot
- callback thread
- registration owner
- cancellation direction
- exactly-once or repeated delivery
- late callback behavior
- error shape
- release action

## One-shot callback

Use `suspendCancellableCoroutine` when one completion produces one result.

Requirements:

- register before returning
- resume exactly once
- unregister or cancel platform work from `invokeOnCancellation`
- tolerate a callback racing with cancellation
- use the required dispatcher only for the section that needs it

Do not check `isActive` and assume that prevents all resume races. Use the continuation contract and idempotent cleanup.

## Multi-shot callback

Use `callbackFlow`.

Requirements:

- register inside the builder
- `trySend` and handle failure or closure
- define buffering and overflow
- use `awaitClose` to unregister
- make cleanup idempotent
- decide whether source completion closes the flow
- avoid retaining the collector through the platform callback after close

## Promise and Java future interop

Preserve cancellation in both directions when the platform primitive supports it. If it cannot cancel, stop delivery and release the subscriber while documenting that underlying work may continue.

JavaScript remains event-loop based unless workers or another parallel facility are used. Do not block it.

## C interop

Stable references and callback function pointers need explicit release. Pair allocation and disposal in one owned adapter. Test a callback after close and ensure it cannot touch released state.

## Review checklist

- Adapter has one owner.
- Cancel and close are idempotent.
- Late callback is safe.
- Resume happens once.
- Buffer policy is explicit.
- Callback thread is not assumed.
- Foreign resource is released.
- Test covers callback before, during, and after cancellation.
