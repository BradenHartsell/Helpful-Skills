---
name: kmp-source-set-boundaries
description: Design, audit, and validate Kotlin Multiplatform source-set ownership, target hierarchies, dependencies, platform abstractions, expect and actual declarations, and AndroidX KMP adoption. Use when deciding what belongs in commonMain versus platform source sets, adding targets, sharing AndroidX libraries, fixing target compilation, or preventing platform APIs and lifecycle policy from leaking into shared code.
---

# KMP Source-Set Boundaries

**Compiled knowledge:** 2026-07-28

Share product truth and deterministic behavior. Keep OS authority and platform lifecycle at the platform boundary.

## Preflight

Use `$kotlin-current`. Draw:

```text
modules:
targets:
default hierarchy template:
manual dependsOn edges:
common source sets:
intermediate source sets:
platform source sets:
platform composition roots:
portable libraries:
expect/actual declarations:
generated sources:
```

Read [ownership-model.md](references/ownership-model.md), [hierarchy-and-dependencies.md](references/hierarchy-and-dependencies.md), and [androidx-kmp.md](references/androidx-kmp.md).

## Placement decision

Place code in `commonMain` only when:

- its semantics are genuinely portable
- dependencies exist on every target in that source set
- lifecycle and threading assumptions are expressed in portable terms
- tests can prove deterministic behavior

Keep platform-owned:

- permissions, intents, notifications, WorkManager, FCM, Play Billing, Keystore
- platform UI lifecycle and system integration
- Apple frameworks, keychain, push, and application lifecycle
- desktop tray, window, filesystem integration
- browser DOM and service-worker behavior

Use a small interface or data contract from common code. Supply the implementation from the platform composition root.

## `expect` and `actual`

Prefer ordinary interfaces and dependency injection when they express a service capability. Use `expect`/`actual` for declarations whose identity must be platform-specific and language-level matching is beneficial.

Expected classes remain a heavier, evolving surface. Prefer interfaces and factory functions unless exact class identity is necessary.

## Stale-pattern denylist

Investigate:

- Android or Apple imports under `commonMain`.
- A common abstraction that exposes `Context`, `Activity`, `UIViewController`, `NSURL`, or platform exceptions.
- `expect`/`actual` used for a normal injectable service.
- Manual `dependsOn` that disables or fights the default hierarchy template.
- Dependency added to a source set unsupported by one target.
- Common code choosing platform dispatcher, database path, notification channel, or permission UX.
- Entire platform shells moved shared only to maximize line sharing.
- Platform callback ownership hidden behind an unowned singleton.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_kmp_boundaries.py <repository-root>
```

If Python is unavailable, apply the ownership and portability denylist
manually and record that the advisory scanner was not run.

## Validate

1. Compile every affected source set and target.
2. Run common tests and platform implementation tests.
3. Verify dependency variants and metadata publication.
4. Test missing or unsupported platform capability.
5. Confirm platform owners can cancel and dispose implementations.
6. Verify no platform type leaks through public common APIs.
7. If changing hierarchy, inspect all source-set dependency edges.

Do not call a boundary portable because Android and JVM desktop both compile.
