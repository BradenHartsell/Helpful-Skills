# Kotlin Build Toolchain Current

**Skill ID:** `kotlin-build-toolchain-current`

**Compiled:** 2026-07-28

Design, migrate, debug, and validate Kotlin, Gradle, Android Gradle Plugin,
Compose compiler, KSP2, and JVM toolchains as one compatibility contract.

Use this skill for build files, version catalogs, convention plugins, source
sets, configuration cache, compiler options, dependency upgrades, AGP built-in
Kotlin, Android-KMP modules, or unexplained build failures.

Start with the [`kotlin-current`](../kotlin-current/) router when the repository
stack is not already known. The bundled audit script is advisory and optional;
the complete manual workflow remains in [`SKILL.md`](SKILL.md).

The package includes current-source guidance for compatibility, module
classification, migration rules, Compose, KSP2, AGP, and Gradle. It does not
assume a documentation connector or network access.

Validation covers structural checks, script execution, links, portability, and
the family routing fixtures. Real migration proof still requires affected
configuration, compilation, tests, lint, and cache behavior.

Original instructions are available under the repository
[MIT License](../../LICENSE).
