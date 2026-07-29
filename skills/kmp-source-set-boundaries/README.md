# Kotlin Multiplatform Source-Set Boundaries

**Skill ID:** `kmp-source-set-boundaries`

**Compiled:** 2026-07-28

Design, audit, and validate Kotlin Multiplatform source-set ownership, target
hierarchies, dependencies, platform abstractions, expect and actual
declarations, and AndroidX KMP adoption.

Use it when deciding what belongs in common code, adding targets, sharing
libraries, fixing target compilation, or preventing platform APIs and lifecycle
policy from leaking into portable code.

Start with [`kotlin-current`](../kotlin-current/) to map modules and targets.
The package includes ownership, hierarchy, dependency, and AndroidX KMP
guidance.

The audit script is optional. Portability requires compilation and behavior
proof across every affected target, not only Android and JVM desktop.

Original instructions are available under the repository
[MIT License](../../LICENSE).
