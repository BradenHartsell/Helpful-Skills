# Validation matrix

Choose proof from the actual affected boundary.

| Change | Minimum proof | Unhappy-path proof |
|---|---|---|
| Build plugin or version | configuration and affected compile tasks | clean configuration-cache run and incompatible-module check |
| Coroutine ownership | affected tests on materially different targets | cancellation, child failure, owner destruction, late callback |
| Android platform | unit plus device or emulator behavior | denied permission, process death, background start, target-gated path |
| Ktor client | MockEngine plus at least one real engine path | timeout, cancellation, retry exhaustion, malformed body, disconnect |
| Compose | UI test and recomposition-sensitive test | duplicate entry, disposal, restoration, rapid navigation |
| Wire contract | Kotlin and TypeScript golden fixtures | missing, null, unknown enum, old persisted payload, precision boundary |
| KMP boundary | compile every affected source set | wrong-target dependency and platform implementation absence |
| Analysis tooling | multi-repository fixture corpus | reflection, generated code, manifest entry, variant-only source |
| Native/Swift | framework export and Swift compile | cancellation, exception, lifetime release, background-to-main hop |

## Gradle proof

Prefer the repository's wrapper and existing tasks. Useful evidence includes:

```text
gradlew projects
gradlew tasks
gradlew <affected compile tasks>
gradlew <affected test tasks>
gradlew lint
gradlew --configuration-cache <representative task>
```

Do not guess task names. Discover them from the project.

## Cross-target proof

Compilation on JVM does not prove:

- Apple framework export
- JS event-loop behavior
- Android manifest or lifecycle behavior
- Native dispatcher availability
- serialization compatibility with TypeScript

Name every target not exercised.
