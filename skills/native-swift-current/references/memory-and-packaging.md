# Memory and packaging

## Memory model

Current Kotlin/Native uses the modern memory manager. The old strict freezing model and native-mt coroutine artifact are obsolete.

Investigate real retention:

- long-lived coroutine scopes
- hot flows with subscribers
- callback closures
- stable references used by C interop
- Swift closure captures
- Kotlin facade retained by Swift owner
- framework-level singleton caches

## Close handles

Every multi-shot bridge should return or expose an idempotent close operation. Closing must:

- cancel child work
- unregister callbacks
- release stable references
- stop delivery
- tolerate a late platform callback

## Packaging

Validate:

- debug and release framework
- simulator and device architectures
- XCFramework if used
- exported transitive dependencies
- SPM checksum or local package wiring
- CocoaPods podspec if used
- dSYM and crash symbol upload
- binary size
- clean consumer integration

## Sources

- https://kotlinlang.org/docs/native-memory-manager.html
- https://kotlinlang.org/docs/native-arc-integration.html
- https://kotlinlang.org/docs/native-binary-options.html
- https://kotlinlang.org/docs/multiplatform/compose-swiftui-integration.html
