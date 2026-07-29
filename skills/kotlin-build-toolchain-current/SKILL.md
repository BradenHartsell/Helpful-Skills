---
name: kotlin-build-toolchain-current
description: Design, migrate, debug, and validate the current Kotlin, Gradle, Android Gradle Plugin, Kotlin Multiplatform, Compose compiler, KSP2, and JVM toolchain contract. Use for build files, version catalogs, convention plugins, plugin conflicts, source-set configuration, configuration cache, compiler options, dependency upgrades, AGP 9 built-in Kotlin, or unexplained Kotlin build failures.
---

# Kotlin Build Toolchain Current

**Compiled knowledge:** 2026-07-28

Treat the build as one compatibility contract. Never upgrade or repair one version in isolation.

## Preflight

Use `$kotlin-current` first. Inspect wrapper, settings, catalogs, root and affected module build files, convention plugins, `gradle.properties`, and manifests.

Write:

```text
Kotlin:
Gradle:
AGP:
module kind:
Android-KMP plugin:
Compose compiler plugin:
KSP:
Java and JVM toolchain:
compileSdk / targetSdk / minSdk:
configuration cache:
unknown computed values:
```

Read [compatibility-contract.md](references/compatibility-contract.md). Refresh official compatibility tables for the detected versions.

## Classify every module

Do not apply one Android recipe to all modules:

| Module | Expected build ownership |
|---|---|
| Android app on AGP 9 | AGP built-in Kotlin, unless legacy mode is deliberately enabled |
| Android-only library on AGP 9 | AGP built-in Kotlin |
| KMP library with Android target on AGP 9 | KMP plugin plus `com.android.kotlin.multiplatform.library` |
| JVM or non-Android KMP | Kotlin JVM or KMP plugin, no AGP assumptions |
| Convention plugin | Lazy, typed configuration of consumers |

Read [migration-rules.md](references/migration-rules.md) before editing plugin blocks.

## Core rules

1. Use the repository wrapper.
2. Prove Kotlin, Gradle, AGP, Compose, and KSP compatibility from current official documentation.
3. Use typed `compilerOptions` at the highest sensible level. Do not add `kotlinOptions`.
4. With Kotlin 2.x Compose, use `org.jetbrains.kotlin.plugin.compose` at the Kotlin version and configure `composeCompiler {}`.
5. On AGP 9, do not reflexively apply `org.jetbrains.kotlin.android` to modules using built-in Kotlin.
6. For KMP Android libraries, use the dedicated Android-KMP library plugin where the current AGP contract requires it.
7. With KSP2 in KMP, add processors to each required target configuration. Do not add a catch-all `ksp(...)`.
8. Configure JVM toolchains centrally and keep Java and Kotlin bytecode targets compatible.
9. Use Providers, task registration, and lazy configuration in custom build logic.
10. Keep repository declarations centralized. Avoid adding repositories in subprojects.
11. Prefer version catalogs and existing convention plugins over scattered literals.
12. Treat warnings about deprecated build APIs as migration signals, not cosmetic noise.

## Stale-pattern denylist

Investigate and usually reject:

- `kotlinOptions {}`.
- `composeOptions { kotlinCompilerExtensionVersion = ... }` on current Kotlin 2.x Compose builds.
- `org.jetbrains.kotlin.android` added to an AGP 9 built-in Kotlin module.
- `com.android.library` used as the KMP Android library integration after migration to the dedicated plugin.
- Global KMP `ksp(...)`.
- KSP1 assumptions with current Kotlin or AGP.
- `afterEvaluate`, eager `tasks.create`, eager `.get()`, and configuration-time task execution.
- `jcenter()`.
- Dynamic versions, unpinned snapshots, or copied compatibility tables.
- Changing Gradle JVM args to hide a lifecycle or configuration bug.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_kotlin_build.py <repository-root>
```

Every hit is advisory and must be classified by module type and installed version.
If Python is unavailable, apply the denylist manually and record that the
advisory scanner was not run.

## Validate

1. Run discovery again after build edits.
2. Run configuration and project-model tasks.
3. Compile every affected target.
4. Run affected tests and lint.
5. Run one representative task twice with configuration cache enabled.
6. Inspect dependency and plugin resolution for duplicates and conflicts.
7. If publishing, validate metadata and consumer compilation.
8. Record unsupported IDE, JDK, Xcode, and target combinations.

Do not call a build migration safe because one Android debug variant compiles.

## Source routing

- Current snapshot and primary sources: [sources.md](references/sources.md)
- Compatibility and module classification: [compatibility-contract.md](references/compatibility-contract.md)
- AGP 9, Compose, compiler options, KSP2, and Gradle migration: [migration-rules.md](references/migration-rules.md)
