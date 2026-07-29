# Kotlin K2 Analysis Tooling

**Skill ID:** `k2-analysis-tooling`

**Compiled:** 2026-07-28

Design, migrate, audit, and test K2-aware developer tooling, static analysis,
dead-code analysis, IntelliJ inspections, Gradle project models, KSP2
processors, and compiler plugins.

Use it for Analysis API, PSI, symbols, reachability, variants, generated code,
reflection heuristics, K1 migration, or compiler integration.

Start with [`kotlin-current`](../kotlin-current/) to identify the exact Kotlin
and project model. The skill chooses the narrowest supported tooling layer and
treats compiler internals as a pinned last resort.

The audit script is optional. Reliable deletion or reachability tooling needs a
multi-project fixture corpus and explicit false-positive measurement.

Original instructions are available under the repository
[MIT License](../../LICENSE).
