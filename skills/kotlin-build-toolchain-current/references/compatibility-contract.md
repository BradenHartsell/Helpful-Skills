# Compatibility contract

## Resolve, do not assume

Capture:

- Kotlin Gradle plugin and language/API version
- Gradle wrapper and runtime JDK
- AGP and Android Studio compatibility if Android is affected
- module plugin IDs and module kind
- Compose compiler plugin and Compose runtime lines
- KSP plugin and processor versions
- Java toolchain and Kotlin `jvmTarget`
- Android SDK levels
- source-set targets and host-only tasks

Use current official compatibility pages. A version catalog alias is evidence only after resolving the alias.

## Module classification

AGP 9 built-in Kotlin changes Android-only modules. It does not remove the Kotlin Multiplatform plugin from KMP modules. Current Android-KMP guidance uses:

```kotlin
plugins {
    kotlin("multiplatform")
    id("com.android.kotlin.multiplatform.library")
}
```

Do not paste this into an application module. The Android-KMP library plugin is library-oriented and has a different DSL and variant model.

## Compatibility decisions

For an upgrade, produce:

| Surface | Before | After | Official compatibility proof | Migration needed |
|---|---|---|---|---|
| Kotlin | | | | |
| Gradle | | | | |
| AGP | | | | |
| Compose compiler | | | | |
| KSP | | | | |
| JDK | | | | |
| SDK levels | | | | |

Refuse a partial upgrade when the resulting combination is undocumented or explicitly unsupported.

## Configuration cache

Configuration-cache readiness requires:

- no project access during task execution
- no configuration-time reads of task outputs
- serializable task inputs
- provider-backed values
- no hidden environment or filesystem dependency

Validate a representative task twice. The second run should reuse the configuration cache, not merely avoid task work through the build cache.
