# Kotlin Current Engineering Skill Family

**Router skill ID:** `kotlin-current`

**Compiled and researched locally:** 2026-07-28

This is a coordinated ten-skill system for current Kotlin, Kotlin
Multiplatform, Android, Compose, Ktor, serialization, build tooling, static
analysis, and Apple interop work.

Start with `kotlin-current`. It fingerprints the actual repository and routes
the task to the smallest relevant specialist skill. This prevents agents from
mixing APIs, platform assumptions, or migration advice from incompatible
Kotlin generations.

## Family members

| Skill | Responsibility |
|---|---|
| `kotlin-current` | Stack discovery, evidence, source precedence, routing, and proof selection |
| [`kotlin-build-toolchain-current`](../kotlin-build-toolchain-current/) | Kotlin, Gradle, AGP, Compose compiler, KSP2, and JVM toolchains |
| [`kmp-coroutines`](../kmp-coroutines/) | Ownership, jobs, cancellation, dispatchers, Flow, channels, and tests |
| [`android-platform-current`](../android-platform-current/) | Target-gated Android behavior, background work, Billing, UI system contracts, and release |
| [`ktor3-client`](../ktor3-client/) | Ktor 3 engines, HTTP, streaming, retry, timeout, and client lifetime |
| [`compose-runtime-navigation`](../compose-runtime-navigation/) | State, effects, lifecycle collection, recomposition, and Navigation 2 or 3 |
| [`serialization-wire-contracts`](../serialization-wire-contracts/) | JSON, time, identifiers, Kotlin and TypeScript fixtures, and evolution |
| [`kmp-source-set-boundaries`](../kmp-source-set-boundaries/) | Common versus platform ownership, hierarchy, dependencies, and AndroidX KMP |
| [`k2-analysis-tooling`](../k2-analysis-tooling/) | Gradle models, Analysis API, KSP2, reachability, and compiler tooling |
| [`native-swift-current`](../native-swift-current/) | Objective-C export, Swift export, SPM, async bridges, memory, and packaging |

## Install or load

For full routing, copy all ten sibling skill directories into the same skills
location. An agent may also load one specialist directly when the task is
already narrow.

If Python is available, the router can run:

```text
python <kotlin-current-dir>/scripts/discover_stack.py <repository-root> --format markdown
```

Python is optional. Without it, follow the manual stack-facts workflow in
[`SKILL.md`](SKILL.md) and record that automated discovery was not run.

No Context7, MCP server, documentation connector, hosted service, or particular
agent product is required. Current official documentation is preferred when
available. Offline work uses local packages, build files, types, and focused
proof, with recency-sensitive claims labeled local-only.

## Research basis

The family was built from official Kotlin, kotlinx.coroutines, Kotlin
Multiplatform, Compose Multiplatform, Android, Ktor, kotlinx.serialization,
Kotlin Analysis API, KSP, Kotlin/Native, and Swift export material. Source
precedence and refresh triggers live in
[`references/source-precedence.md`](references/source-precedence.md).

## Validation performed

- all ten skills passed the structural skill validator;
- all ten Python helpers passed `--help` and Python compilation;
- internal Markdown links, template markers, project identifiers, machine
  paths, and forbidden punctuation were checked;
- routing was forward-tested against a synthetic modern KMP fixture;
- discovery was forward-tested against the current `Kotlin/kotlinx.coroutines`
  repository;
- scanner output was bounded to prevent large repositories from flooding
  context;
- source and public operational files were compared by SHA-256.

The synthetic fixture validated discovery and routing, not a complete
application build. Every real use still requires repository-specific compile,
platform, runtime, and unhappy-path proof.

## License and notice

This family is original instructional material published under the repository's
[MIT License](../../LICENSE). Third-party names and linked documentation remain
the property of their respective owners. See the repository
[NOTICE](../../NOTICE.md).
