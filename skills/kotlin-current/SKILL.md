---
name: kotlin-current
description: Discover the exact Kotlin project stack, produce evidence-backed stack facts, and route work to the smallest current Kotlin capsule. Use at the start of nontrivial Kotlin, Kotlin Multiplatform, Android, Compose, Ktor, kotlinx.serialization, Gradle, KSP, compiler tooling, or Kotlin/Native work, especially after dependency, plugin, targetSdk, source-set, or toolchain changes.
---

# Kotlin Current

**Compiled knowledge:** 2026-07-28

Do not answer from a generic idea of "modern Kotlin." Fingerprint the repository, identify the affected modules, then load only the capsules that own the task.

## Run discovery first

Read all applicable repository instruction files, including `AGENTS.md` when
present, then run:

```text
python <skill-dir>/scripts/discover_stack.py <repository-root> --format markdown
```

Use `--format json` when another tool will consume the result. The script is advisory. Confirm ambiguous or computed values in the referenced Gradle files.

If Python is unavailable, perform the discovery manually with
[stack-facts.md](references/stack-facts.md) and record that the helper was not
run. The workflow must remain usable without the script.

Read [stack-facts.md](references/stack-facts.md) for the evidence schema and invalidation rules. Read [source-precedence.md](references/source-precedence.md) whenever documentation disagrees or the installed version is unclear.

## Establish affected paths

Before loading a capsule:

1. Name the directly affected modules, source sets, manifests, and generated-code paths.
2. Inspect their callers, platform implementations, build plugins, dependency declarations, and tests.
3. Determine whether the issue is local or caused by an ownership or compatibility rule shared across modules.
4. Preserve the repository's architecture unless current platform constraints require a deliberate migration.

## Route to capsules

Load only the matching skill or skills:

| Evidence or task | Required capsule |
|---|---|
| Kotlin, Gradle, AGP, Android-KMP plugin, Compose compiler plugin, KSP, JVM toolchain, build cache | `$kotlin-build-toolchain-current` |
| Scopes, jobs, cancellation, dispatchers, Flow, channels, coroutine tests | `$kmp-coroutines` |
| Android target behavior, WorkManager, services, notifications, FCM, Billing, alarms, back, insets, release requirements | `$android-platform-current` |
| Ktor client, engines, HTTP, WebSocket, SSE, retry, timeout, TLS, proxy | `$ktor3-client` |
| Composition, effects, snapshot state, collection, recomposition, saveable state, Navigation 2 or 3, UI tests | `$compose-runtime-navigation` |
| JSON, serialization, datetime migration, Kotlin and TypeScript DTOs, persisted schemas | `$serialization-wire-contracts` |
| Source-set ownership, targets, hierarchy, `expect`/`actual`, AndroidX KMP, portable interfaces | `$kmp-source-set-boundaries` |
| K2, Analysis API, Gradle project model, KSP2 processors, static analysis, compiler plugins | `$k2-analysis-tooling` |
| Kotlin/Native, Apple frameworks, Objective-C export, Swift export, SPM, coroutine or Flow bridging | `$native-swift-current` |

Load more than one capsule only when the task actually crosses their boundary. For example:

- A duplicate collector caused by a wrong `LaunchedEffect` key requires Compose plus coroutines.
- A Ktor reconnect loop that outlives a session requires Ktor plus coroutines.
- A Room processor failure in a KMP module requires build toolchain plus source-set boundaries.
- A Kotlin and TypeScript timestamp mismatch requires wire contracts, not Native interop.

## Produce immutable stack facts

Before implementation, emit a compact block:

```text
STACK FACTS
fingerprint: <sha256>
affected modules: <paths>
Kotlin: <value + evidence>
Gradle: <value + evidence>
AGP: <value + evidence or not present>
module kind: <Android app | Android library | KMP library | JVM | other>
targets: <detected targets>
targetSdk: <value or unresolved>
relevant libraries: <exact detected versions>
loaded capsules: <names>
unknowns: <items that can change the answer>
```

Do not silently turn unresolved aliases, convention-plugin values, or environment properties into facts.

## Refresh current documentation

Refresh official documentation when:

- The fingerprint is new or changed.
- A relevant version is unknown, dynamic, pre-release, or newer than the capsule's recorded snapshot.
- A task crosses a major-version boundary.
- Android behavior depends on `targetSdk` or a current Play deadline.
- A current API reference conflicts with a guide or migration page.
- The capsule labels a feature Alpha, Beta, experimental, deprecated, or unstable.

Use current official API references, release notes, and source repositories
through whatever documentation access is available. A documentation index such
as Context7 may help with discovery, but it is optional and never a prerequisite
for this skill. Record exact URLs, version scope, and retrieval date in the work
receipt. When offline, use the locally resolved packages and label
recency-sensitive conclusions `local-only`.

## Implement and prove

1. State the compatibility, ownership, and lifecycle assumptions.
2. Make the smallest architecture-consistent change.
3. Exercise the unhappy path, not only compilation.
4. Run the capsule's advisory scanner if applicable.
5. Run affected compilation, unit tests, platform tests, lint, and static checks.
6. Re-run discovery if a build or dependency file changed.
7. Do not declare success from plausible code or a single target's compile.

Read [validation-matrix.md](references/validation-matrix.md) for proof selection.

## Report with evidence boundaries

Separate:

- Detected facts and their files.
- Current official facts and their sources.
- Confirmed defects.
- Architectural causes shared across call sites.
- Changes made.
- Validation run and platforms not exercised.
- Time-sensitive facts that must be refreshed before release.

## Stale-pattern denylist

Never:

- Mix snippets from different Kotlin, Gradle, AGP, KSP, Ktor, Compose, Navigation, or Android generations without proving compatibility.
- Infer an Android behavior without reading `targetSdk`.
- Treat all Ktor engines or KMP targets as capability-equivalent.
- Put Android APIs in `commonMain` because the project is multiplatform.
- Move Compose lifecycle behavior into a generic coroutine abstraction.
- Use KSP as a substitute for a whole-project static-analysis graph.
- Introduce Alpha language or Native export features only because they are new.
- cache stack facts after an invalidating file changes.
