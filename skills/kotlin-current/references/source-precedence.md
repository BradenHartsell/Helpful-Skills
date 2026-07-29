# Source precedence and refresh policy

## Precedence

When sources disagree, use this order:

1. Installed dependency metadata and build model.
2. Current API reference for the installed version.
3. Current official release notes and tagged source.
4. Current platform behavior and policy documentation.
5. Current migration documentation.
6. Current concept guides and samples.
7. Older guides, blog posts, copied snippets, and model recall.

Do not combine contradictory statements. Record the conflict and narrow the claim.

## Current snapshot

This skill family was researched on 2026-07-28. Snapshot values are routing hints only:

- Kotlin documentation showed 2.4.x examples and K2-only current guidance.
- Kotlin Gradle configuration uses `compilerOptions`, not `kotlinOptions`.
- AGP 9 uses built-in Kotlin for Android modules and a dedicated Android-KMP library plugin for KMP Android libraries.
- KSP current documentation describes KSP2 and target-specific KMP configurations.
- kotlinx.coroutines current release line was 1.11.x.
- Ktor documentation current release line was 3.5.x.
- Compose Multiplatform documentation current release line was 1.11.x.
- kotlinx.serialization current release line was 1.11.x.
- Google Play announced an API 36 target requirement for new apps and updates from 2026-08-31, with form-factor exceptions.

Refresh these facts. Do not treat them as a version recommendation.

## Official source map

### Kotlin and KMP

- https://kotlinlang.org/docs/home.html
- https://kotlinlang.org/docs/whatsnew24.html
- https://kotlinlang.org/docs/gradle-configure-project.html
- https://kotlinlang.org/docs/gradle-compiler-options.html
- https://kotlinlang.org/docs/multiplatform/kmp-overview.html
- https://kotlinlang.org/docs/multiplatform/multiplatform-hierarchy.html

### Android and build

- https://developer.android.com/build
- https://developer.android.com/build/migrate-to-built-in-kotlin
- https://developer.android.com/kotlin/multiplatform/plugin
- https://developer.android.com/about/versions
- https://developer.android.com/google/play/requirements/target-sdk

### Libraries

- https://kotlinlang.org/api/kotlinx.coroutines/
- https://ktor.io/docs/
- https://kotlinlang.org/docs/multiplatform/compose-multiplatform.html
- https://github.com/Kotlin/kotlinx.serialization
- https://github.com/Kotlin/kotlinx-datetime
- https://kotlinlang.org/docs/ksp-overview.html

### Tooling and Native

- https://kotlin.github.io/analysis-api/
- https://kotlinlang.org/docs/k2-compiler-migration-guide.html
- https://kotlinlang.org/docs/native-overview.html
- https://kotlinlang.org/docs/native-swift-export.html

## Refresh receipt

Record:

```text
source:
retrieved:
applies to:
installed version:
claim:
stability:
conflicts:
```
