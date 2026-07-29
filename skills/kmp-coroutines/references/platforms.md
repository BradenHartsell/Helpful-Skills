# Dispatcher and platform behavior

## Contents

- Portable dependency setup
- Dispatcher provider
- Dispatcher selection
- Android
- JVM desktop
- Darwin Native
- Other Native
- JavaScript and Wasm/JS
- Wasm/WASI
- Version-sensitive cautions
- Platform checklist

## Portable dependency setup

Declare the base multiplatform dependency in `commonMain`:

```kotlin
kotlin {
    sourceSets {
        commonMain.dependencies {
            implementation(libs.kotlinx.coroutines.core)
        }
        commonTest.dependencies {
            implementation(libs.kotlinx.coroutines.test)
        }
    }
}
```

Add platform Main-dispatcher artifacts only to source sets or runtime configurations that need them:

- Android: `kotlinx-coroutines-android`.
- Swing desktop: `kotlinx-coroutines-swing`.
- JavaFX desktop: `kotlinx-coroutines-javafx`.
- Darwin Native: Main is included by core.

Do not declare platform-suffixed core artifacts manually in a normal KMP project. Gradle metadata selects the target artifact.

## Dispatcher provider

Use a small portable contract that names intent:

```kotlin
data class AppDispatchers(
    val main: CoroutineDispatcher,
    val cpu: CoroutineDispatcher,
    val blockingIo: CoroutineDispatcher,
)
```

If a target has no meaningful Main or blocking-I/O dispatcher, do not fake the capability silently. Provide a target-appropriate implementation or redesign the portable contract.

Prefer semantic names such as `database`, `fileIo`, or `imageDecode` when limits differ.

## Dispatcher selection

| Work | Preferred policy |
|---|---|
| UI mutation | Main dispatcher supplied by the platform |
| CPU-heavy pure computation | Default-like dispatcher, often with bounded parallelism |
| Blocking file, socket, or database call | IO-like dispatcher on threaded targets |
| Non-blocking suspending client call | Preserve caller context unless the library requires otherwise |
| Serial access to an external resource | `limitedParallelism(1)` or a dedicated owner, depending on invariants |
| Shared-state invariant across suspension | `Mutex` or state ownership |

`limitedParallelism(n)` limits simultaneous execution, not the number of logical coroutines and not access across suspension. Use `Mutex` or `Semaphore` for concurrency protocols.

Prefer `Dispatchers.IO.limitedParallelism(n)` or `Dispatchers.Default.limitedParallelism(n)` over creating a thread pool. `newFixedThreadPoolContext` is delicate, owns native resources, and must be closed.

Do not use `Dispatchers.Unconfined` in application code. It resumes wherever the suspending function resumes and makes thread assumptions fragile.

## Android

- `Dispatchers.Main` requires `kotlinx-coroutines-android`.
- `viewModelScope` and Lifecycle scopes use Main.
- Inject worker dispatchers so unit tests can replace them.
- Keep suspend functions main-safe.
- Use WorkManager or another durable platform owner for work that must survive process or UI lifetime. A coroutine scope alone does not make work durable.
- Treat Android callbacks and Activity results as lifecycle-bound resources.

Do not move all repository calls to IO. Ktor, Room suspend APIs, and other non-blocking APIs may already be main-safe. Verify the specific library.

## JVM desktop

- `Dispatchers.Main` requires a runtime Main provider.
- Compose Multiplatform Lifecycle and ViewModel scopes use `Dispatchers.Main.immediate`.
- For Swing, add `kotlinx-coroutines-swing`.
- For JavaFX, add `kotlinx-coroutines-javafx`.
- Do not block the AWT Event Dispatch Thread or JavaFX Application Thread.
- Close custom executor-backed dispatchers at application shutdown.
- Avoid `runBlocking` from UI event handlers.

A successful common test does not prove the packaged desktop runtime includes the Main-dispatcher provider.

## Darwin Native

- `Dispatchers.Main` is backed by Darwin's main queue.
- `Dispatchers.Default` is backed by a Darwin global queue in current kotlinx.coroutines source.
- `Dispatchers.IO` is available on Native in current 1.11 API and source.
- Kotlin/Native uses a shared heap and modern GC. Do not add freezing-era patterns.
- Swift or Objective-C completion handlers may run off main. Hop to the required actor or dispatcher explicitly.
- Use autorelease pools around long interop loops that create temporary Objective-C objects.

Do not assume a Kotlin suspend function called from Swift begins on Main. Current Swift export uses Default unless Kotlin switches context.

## Other Native

Current kotlinx.coroutines 1.11 API and source report `Dispatchers.Main` as unavailable on non-Darwin Native targets.

- Inject a dispatcher appropriate to the target.
- Keep UI assumptions out of common code.
- Treat access to Main as a capability that may fail.
- Use current target support documentation before adding a native target.
- Avoid hand-created worker pools unless a separate pool is necessary and its lifecycle is owned.

## JavaScript and Wasm/JS

- `Dispatchers.Main` is equivalent to Default with immediate support.
- Execution normally shares the JavaScript event loop.
- Switching between Main and Default does not create CPU parallelism.
- Never run blocking loops or blocking I/O on the event loop.
- Break CPU work into cooperative chunks or use a platform worker abstraction where supported.
- Promise integrations moved to the `web` target in kotlinx.coroutines 1.11.
- Wasm/JS Promise interop has `JsAny` type constraints in current releases.
- Unhandled coroutine exceptions that cannot propagate are reported to the JavaScript runtime in 1.11.

Design cancellation across Promise boundaries explicitly. A Promise API may not cancel its underlying work merely because a Kotlin waiter is cancelled.

## Wasm/WASI

- Do not assume browser APIs, DOM lifecycle, Swing, Android Main, or Darwin queues.
- Verify the exact kotlinx.coroutines and Kotlin target support for each API.
- Keep timers, file access, networking, and process behavior behind target implementations.
- Run the target's tests. JVM tests do not prove WASI scheduling.

## Version-sensitive cautions

- Legacy Native memory-manager guidance is obsolete. The legacy manager was removed in Kotlin 1.9.20.
- Do not use `native-mt` coroutine artifacts.
- An older Native migration guide says Main uses a standalone Worker on non-Darwin targets. Current 1.11 API and source say Main is missing there. Follow the current API and installed source.
- Coroutine test APIs before 1.6 differ substantially. Current code should use `runTest`, `TestScope`, `TestCoroutineScheduler`, and current test dispatchers.
- In 1.11, using `CoroutineDispatcher` as a coroutine-context key is deprecated. Use `ContinuationInterceptor`.
- Experimental and preview APIs can change. Check annotations on the installed version.

## Platform checklist

- Base dependency is in `commonMain`.
- Each UI runtime has the right Main provider.
- No portable path assumes `Dispatchers.Main` exists everywhere.
- No JS or Wasm path blocks the event loop.
- No Swift callback assumes Main.
- No freezing or `native-mt` workaround remains.
- Blocking, CPU, and UI dispatchers are distinct by intent.
- Custom dispatchers have an owner and close path.
- Every materially different target has a test or an explicit proof gap.
