# Async interop

## Suspend functions

Current Swift export can map suspend functions to Swift async forms, subject to current limitations. Traditional Objective-C export commonly exposes completion-handler forms.

In either case define:

- Kotlin owner scope
- Swift cancellation bridge
- dispatcher or executor
- error mapping
- callback exactly-once behavior
- result lifetime

Do not assume Swift task cancellation automatically cancels arbitrary Kotlin work. Prove the bridge.

## Flow

Choose an explicit bridge:

- callback subscription with a close handle
- a wrapper that exposes `AsyncSequence`
- state snapshot plus observation

Define:

- cold versus hot behavior
- replay
- buffering
- terminal failure
- cancellation from Swift
- deallocation
- main-actor delivery

## Main execution

Darwin provides a Main dispatcher through the relevant coroutine support. Current API documentation says other Native targets do not necessarily have Main. Shared Native code must not assume universal Main availability.

Swift export work may start on Kotlin's default dispatcher unless explicitly switched. UI mutation must satisfy Swift and Apple actor rules.

## Exceptions

Unchecked Kotlin exceptions crossing a native boundary can terminate the process depending on export mode and annotations. Convert expected failures into typed results or declared error bridges. Test unexpected exceptions deliberately.
