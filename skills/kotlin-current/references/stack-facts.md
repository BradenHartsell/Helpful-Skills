# Stack facts

## Purpose

Stack facts are a reproducible receipt, not a hand-maintained project description. They prevent an agent from combining configuration examples from incompatible Kotlin generations.

## Required evidence

Read, when present:

- `gradle/wrapper/gradle-wrapper.properties`
- `settings.gradle.kts` or `settings.gradle`
- `gradle/libs.versions.toml`
- root `build.gradle.kts` or `build.gradle`
- affected module build files
- convention plugin source under `buildSrc` or included builds
- `gradle.properties`
- affected `AndroidManifest.xml`
- package manager files for an adjacent TypeScript contract
- `Package.swift`, CocoaPods files, and Xcode project settings for Apple work

## Fact states

Every fact has one of four states:

| State | Meaning |
|---|---|
| exact | Literal value is visible in evidence |
| resolved alias | Alias maps to one exact literal in the inspected catalog |
| computed | Build logic computes the value and must be confirmed through the Gradle model or task output |
| unresolved | Evidence is absent, dynamic, conflicting, or outside the inspected paths |

Never report a computed or unresolved fact as exact.

## Fingerprint

The discovery script hashes the paths and bytes of relevant configuration files. The hash is an invalidation key, not a security signature.

Invalidate facts after changes to:

- wrapper, settings, catalogs, build files, convention plugins, or `gradle.properties`
- Kotlin, AGP, Compose, KSP, Ktor, coroutines, serialization, datetime, Firebase, Billing, or AndroidX versions
- `compileSdk`, `targetSdk`, `minSdk`, JVM toolchain, source sets, or targets
- manifests that declare components, permissions, deep links, services, providers, or features
- contract fixtures or TypeScript schemas for wire work

## Minimum output

Include:

- repository root and fingerprint
- files hashed
- affected modules and module kinds
- Kotlin, Gradle, AGP, KSP, and Compose plugin facts
- SDK levels and KMP targets
- relevant library versions
- detected navigation generation
- unknowns and conflicts
- capsule routing

## Convention plugins

Values hidden in `buildSrc`, precompiled script plugins, or included builds are common. If a module only applies a convention plugin:

1. Inspect the plugin implementation.
2. Prefer a Gradle model or property-reporting task over regex inference.
3. Record the source path and whether the value is computed.
4. Re-run discovery after the plugin changes.
