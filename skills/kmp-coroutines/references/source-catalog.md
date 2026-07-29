# Coroutine source catalog

Snapshot researched 2026-07-28. The current kotlinx.coroutines release line was 1.11.x. Refresh for the installed version.

## Primary sources

- Guide anchor: https://kotlinlang.org/docs/coroutines-guide.html
- API: https://kotlinlang.org/api/kotlinx.coroutines/
- Repository and README: https://github.com/Kotlin/kotlinx.coroutines
- Releases: https://github.com/Kotlin/kotlinx.coroutines/releases
- KEEP design: https://github.com/Kotlin/KEEP/blob/master/proposals/coroutines.md
- Android best practices: https://developer.android.com/kotlin/coroutines/coroutines-best-practices
- Android testing: https://developer.android.com/kotlin/coroutines/test
- Debugging: https://kotlinlang.org/docs/debug-coroutines-with-idea.html
- Native overview: https://kotlinlang.org/docs/native-overview.html

## Guide coverage

The official coroutine guide routes to:

- basics
- cancellation and timeouts
- composing suspending functions
- context and dispatchers
- asynchronous Flow
- channels
- exception handling and supervision
- shared mutable state and concurrency
- select expressions
- coroutine design KEEP
- UI programming guide

Use current API reference and release notes to resolve old guide conflicts.

## Conflict rule

Current API reference for `Dispatchers.Main` says:

- Android needs the Android dispatcher artifact.
- JVM desktop needs an appropriate UI dispatcher artifact.
- Darwin has a Main implementation.
- JS and Wasm/JS use the event loop where Main is equivalent to Default.
- other Native targets do not have a general Main implementation.

Older Native migration prose has described a broader fallback. Do not blend it with the current API claim. Match the installed version and target.

## Current semantic facts

- `StateFlow` is hot, equality-conflated, thread-safe, and does not complete.
- `MutableStateFlow.update` provides atomic read-modify-write semantics.
- `runTest` uses virtual time only for dispatchers sharing its scheduler.
- `backgroundScope` is for work that intentionally remains active during a test.
- JS tests must return the `runTest` result immediately.
- `limitedParallelism` limits scheduling parallelism but does not provide a mutual-exclusion critical section.
- modern Kotlin/Native no longer uses the legacy freezing memory model.

Verify every version-sensitive statement.
