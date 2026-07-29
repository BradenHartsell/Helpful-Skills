# Tooling layer selection

## Gradle model

Use it to answer:

- which modules exist
- which plugins and variants apply
- source directories and generated directories
- target compilations
- dependencies and friend paths
- tasks and artifact outputs

Do not parse Gradle scripts as the authoritative project model when convention plugins or computed values matter.

## Analysis API

Use it for semantic source questions:

- declaration and reference targets
- types
- scopes
- call resolution
- diagnostics

It is the supported direction for K2-aware IDE analysis. Standalone command-line support remains less stable than the IDE use case and must be pinned and tested.

## KSP2

Use for compile-time processors that inspect symbols and generate code. Configure KMP targets explicitly. KSP is not a general repository graph, build model, or resource analyzer.

## Android lint

Use or integrate it when Android resources, manifests, UAST checks, or Android-specific build variants are central.

## Compiler plugins

Official Kotlin guidance calls custom compiler plugins a last resort because the API is unstable. Frontend extensions from K1 require K2/FIR migration. Pin exact Kotlin and maintain a compatibility matrix.

Primary sources:

- https://kotlin.github.io/analysis-api/
- https://kotlin.github.io/analysis-api/migrating-from-k1.html
- https://kotlinlang.org/docs/ksp-overview.html
- https://kotlinlang.org/docs/compiler-plugins-overview.html
- https://kotlinlang.org/docs/k2-compiler-migration-guide.html
- https://docs.gradle.org/current/userguide/tooling_api.html
