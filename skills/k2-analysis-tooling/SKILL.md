---
name: k2-analysis-tooling
description: Design, migrate, audit, and test Kotlin K2-aware developer tooling, static analysis, dead-code analysis, IntelliJ inspections, command-line analyzers, Gradle project models, KSP2 processors, and compiler plugins. Use for Kotlin Analysis API, PSI, symbols, reachability, project graphs, variants, generated code, reflection heuristics, K1 migration, or Kotlin compiler integration.
---

# K2 Analysis Tooling

**Compiled knowledge:** 2026-07-28

Choose the narrowest supported tooling layer. Compiler internals are a last resort and require an exact Kotlin pin.

## Preflight

Use `$kotlin-current`. Record:

```text
tool purpose:
IDE plugin, CLI, build plugin, processor, or compiler plugin:
Kotlin and K2 version:
Gradle and KMP model needs:
source and binary analysis:
variants and source sets:
generated code:
resources and manifests:
reflection and DI:
incremental requirements:
supported repositories:
```

Read [layer-selection.md](references/layer-selection.md), [whole-project-graph.md](references/whole-project-graph.md), and [analysis-api.md](references/analysis-api.md).

## Select the layer

| Need | Preferred layer |
|---|---|
| Modules, variants, source sets, dependencies, tasks | Gradle Tooling API or a purpose-built Gradle model |
| Semantic symbols, references, types, diagnostics | Kotlin Analysis API |
| Compile-time symbol processor for annotated source | KSP2 |
| Android resources and manifest reachability | Android lint/model/resource analysis |
| Transform compiler IR | Compiler plugin only when unavoidable |
| Whole-project unused analysis | Combined project model, Analysis API, resources, generated code, and framework reachability |

Do not choose KSP merely because it exposes symbols. It does not inherently provide a complete whole-project reachability graph.

## Core rules

1. Separate syntactic PSI facts from semantic symbol facts.
2. Build analysis from module and variant perspective.
3. Keep Analysis API objects inside their valid analysis session and lifetime.
4. Never cache symbols or sessions across invalidation boundaries without an approved pointer abstraction.
5. Treat generated source, manifests, resources, serialization, DI, reflection, service loading, tests, and platform entry points as graph roots or heuristic edges.
6. Model certainty. A dynamic reachability edge should prevent a confident deletion.
7. Keep suppressions scoped, documented, and testable.
8. Pin unstable standalone or compiler integrations and run a fixture corpus on every Kotlin minor upgrade.
9. Measure memory, invalidation, and analysis time on real repositories.
10. Prefer findings with evidence paths over unexplained "unused" labels.

## Stale-pattern denylist

Investigate:

- K1 descriptors, `BindingContext`, FE10-only APIs, or old resolution examples.
- Compiler internals used when Analysis API or lint suffices.
- Analysis API symbols stored outside `analyze {}`.
- KSP used as the sole engine for dead-code analysis.
- One source set or one JVM compilation treated as the whole KMP project.
- Generated directories skipped without representing their declarations.
- Reflection, DI, serialization, manifest, and resource entry points ignored.
- A single Kotlin repository fixture used as compatibility proof.
- Auto-deletion from a heuristic finding.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_k2_tooling.py <repository-root>
```

If Python is unavailable, apply the tooling-layer and stale-pattern review
manually and record that the advisory scanner was not run.

## Validate with a corpus

Read [fixture-corpus.md](references/fixture-corpus.md). Include:

- JVM, Android, and KMP repositories
- expect/actual
- multiple variants
- generated source
- Compose previews and navigation destinations
- serialization and DI
- reflection and service loaders
- manifests and resources
- tests and test fixtures
- compiler-version matrix

Score false positives separately from false negatives. For deletion tools, false positives are the critical safety failure.
