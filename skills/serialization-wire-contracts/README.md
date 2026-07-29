# Kotlin Serialization and Wire Contracts

**Skill ID:** `serialization-wire-contracts`

**Compiled:** 2026-07-28

Design, migrate, audit, and prove Kotlin serialization, time, network, and
persisted wire contracts, especially across Kotlin Multiplatform and
TypeScript.

Use it for JSON configuration, DTOs, nullability, defaults, enums,
polymorphism, timestamps, durations, identifiers, numeric precision, schema
evolution, migrations, and cross-language golden fixtures.

Start with [`kotlin-current`](../kotlin-current/) for exact library versions.
The references separate JSON policy, time and identifier policy, and contract
evolution.

The audit script is optional. Stability requires semantic round trips, old-data
migrations, malformed-input tests, precision boundaries, and redacted error
handling.

Original instructions are available under the repository
[MIT License](../../LICENSE).
