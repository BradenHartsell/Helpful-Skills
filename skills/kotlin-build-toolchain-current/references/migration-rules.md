# Migration rules

## Compiler options

Use typed `compilerOptions`:

```kotlin
kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
        freeCompilerArgs.add("-X...")
    }
}
```

Set common defaults high in the hierarchy. Override only where a compilation or task truly differs. Compare Java toolchain and Kotlin bytecode target.

## Compose compiler

For Kotlin 2.x:

```kotlin
plugins {
    id("org.jetbrains.kotlin.plugin.compose") version kotlinVersion
}
```

Use `composeCompiler {}` for supported options. Do not carry an independent old compiler-extension version forward.

## AGP 9 built-in Kotlin

Read the official migration page for the exact AGP line. Check:

- whether built-in Kotlin is active
- whether a temporary legacy opt-out exists
- whether the module is Android-only or KMP
- source-set layout changes
- plugin or DSL conflicts
- kapt and KSP compatibility

Do not remove `org.jetbrains.kotlin.android` repo-wide. Classify each module first.

## Android-KMP library plugin

The dedicated plugin has one Android library variant and a KMP-owned DSL. Check current guidance for:

- host and device tests, which may be disabled by default
- Java source support, which may require opt-in
- Android resources
- publishing
- unsupported top-level Android DSL blocks

## KSP2

In KMP:

```kotlin
dependencies {
    add("kspAndroid", processor)
    add("kspJvm", processor)
}
```

Add only targets that require generated output. Confirm generated source wiring and task names. Do not use KSP as a whole-program analyzer.

## Gradle 9

Check the exact Gradle upgrade guide. Common migration themes include:

- removed legacy APIs
- stricter task and property validation
- lazy configuration
- repository cleanup such as removed `jcenter()`
- configuration-cache compatibility

Do not use an old migration example without matching its source and destination majors.
