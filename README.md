# Helpful Skills

A growing collection of portable, evidence-aware agent skills for practical software and product work.

Each skill lives in its own directory under [`skills/`](skills/). Its instructions, optional agent metadata, reference material, and user documentation stay together so the repository can grow without turning the root into a collection of unrelated files.

## Skill catalog

| Skill | ID | What it covers | Compiled |
|---|---|---|---|
| [Kotlin Multiplatform Material 3 UI/UX Design and Engineering](skills/kmp-material3-ui-ux/) | `kmp-material3-ui-ux` | Product UI design, Material 3 systems, adaptive Compose layouts, accessibility, input, state, motion, KMP target parity, and visual QA | 2026-07-28 |
| [Kotlin Current Engineering Skill Family](skills/kotlin-current/) | `kotlin-current` | Evidence-based Kotlin stack discovery and routing across nine specialist engineering skills | 2026-07-28 |
| [Kotlin Build Toolchain Current](skills/kotlin-build-toolchain-current/) | `kotlin-build-toolchain-current` | Kotlin, Gradle, AGP, Compose compiler, KSP2, JVM toolchains, and compatibility migrations | 2026-07-28 |
| [Kotlin Multiplatform Coroutines Engineering](skills/kmp-coroutines/) | `kmp-coroutines` | Coroutine ownership, cancellation, failures, dispatchers, Flow, channels, interop, and testing | 2026-07-28 |
| [Android Platform Current](skills/android-platform-current/) | `android-platform-current` | Target-gated Android behavior, background execution, UI system contracts, Billing, and release proof | 2026-07-28 |
| [Ktor 3 Multiplatform Client Engineering](skills/ktor3-client/) | `ktor3-client` | Ktor engines, HTTP, streaming, retry, timeout, cancellation, ownership, and migration | 2026-07-28 |
| [Compose Runtime and Navigation Engineering](skills/compose-runtime-navigation/) | `compose-runtime-navigation` | Compose state, effects, lifecycle, recomposition, restoration, insets, and Navigation 2 or 3 | 2026-07-28 |
| [Kotlin Serialization and Wire Contracts](skills/serialization-wire-contracts/) | `serialization-wire-contracts` | JSON semantics, time, identifiers, precision, schema evolution, and cross-language fixtures | 2026-07-28 |
| [Kotlin Multiplatform Source-Set Boundaries](skills/kmp-source-set-boundaries/) | `kmp-source-set-boundaries` | Common versus platform ownership, source-set hierarchy, dependencies, expect and actual, and AndroidX KMP | 2026-07-28 |
| [Kotlin K2 Analysis Tooling](skills/k2-analysis-tooling/) | `k2-analysis-tooling` | Analysis API, project models, KSP2, reachability, static analysis, and compiler integrations | 2026-07-28 |
| [Kotlin Native and Swift Interoperability](skills/native-swift-current/) | `native-swift-current` | Objective-C and Swift export, async bridges, memory ownership, SPM, and Apple packaging | 2026-07-28 |
| [Three.js 3D Experience Engineering](skills/threejs/) | `threejs` | Browser 3D rendering, scene design, interaction, assets, shaders, performance, and version-aware Three.js guidance | 2026-07-28 |

## Using a skill

Agent products discover skills in different ways. The portable path is:

1. Open the skill directory.
2. Read its `README.md` for scope and installation options.
3. Copy the complete directory into your agent's skills location, or point the agent directly to `SKILL.md`.
4. Keep the `references/` directory beside `SKILL.md` because the skill uses relative links.

If your agent supports named skill invocation, use the identifier declared in the `SKILL.md` frontmatter.

## Repository structure

```text
Helpful-Skills/
  README.md
  LICENSE
  NOTICE.md
  CONTRIBUTING.md
  scripts/
    validate_catalog.py
  skills/
    skill-name/
      README.md
      SKILL.md
      agents/
      references/
```

Not every skill needs every optional directory. Each package should remain self-contained, clearly dated, and usable without a specific proprietary plugin unless its documentation says otherwise.

## Quality standards

Published skills should:

- define a precise trigger and scope;
- keep one complete operational entrypoint in `SKILL.md`;
- use progressive references instead of one unbounded instruction file;
- separate local evidence, verified APIs, current official guidance, and proposals;
- degrade honestly when tools or network access are unavailable;
- include a compilation or research date;
- state what was actually validated;
- avoid secrets, private data, copied proprietary material, and invented APIs.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for package structure, documentation, validation, source, and licensing expectations.

## Validate the catalog

Run the dependency-free catalog validator before publishing:

```bash
python scripts/validate_catalog.py
```

It checks skill placement, required files, frontmatter names, compilation dates, root catalog entries, unfinished template markers, and internal Markdown links.

## License and notices

Original repository content is available under the [MIT License](LICENSE). Third-party names and linked materials remain the property of their respective owners. See [NOTICE.md](NOTICE.md) for the non-affiliation and third-party content notice.
