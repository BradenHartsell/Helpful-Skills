# Fixture corpus

## Minimum corpus

1. Pure Kotlin JVM library.
2. Android app with manifests, resources, lint, Compose, DI, and serialization.
3. KMP library with JVM, Android, Apple, and JS or Wasm targets.
4. Convention-plugin build with version catalog.
5. Generated-code project using KSP2.
6. Reflection and service-loader project.
7. Public API library with binary consumers.

## Golden expectations

Each fixture lists:

- declarations that must be reachable
- declarations intentionally unused
- uncertain dynamic references
- selected variants and source sets
- expected evidence path

## Upgrade gate

On every Kotlin minor:

- compile integration
- run complete corpus
- compare findings
- measure time and memory
- inspect Analysis API release notes
- update exact-version adapter

Do not accept a net finding-count change without classifying it.
