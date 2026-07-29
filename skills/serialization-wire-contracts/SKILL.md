---
name: serialization-wire-contracts
description: Design, migrate, audit, and prove Kotlin serialization, time, network, and persisted wire contracts, especially between Kotlin Multiplatform and TypeScript. Use for kotlinx.serialization, JSON configuration, DTOs, nullability, defaults, enums, polymorphism, Instant, duration, identifiers, numeric precision, schema evolution, migrations, or cross-language golden fixtures.
---

# Serialization and Wire Contracts

**Compiled knowledge:** 2026-07-28

A compiling DTO is not proof of a compatible wire contract. Define semantics field by field and prove both directions.

## Preflight

Use `$kotlin-current`. Identify:

```text
kotlinx.serialization:
kotlinx-datetime:
Kotlin version:
JSON configuration:
TypeScript validator or schema:
network DTOs:
persisted DTOs:
timestamp and duration policy:
polymorphism:
unknown-field policy:
migration owners:
```

Read [json-policy.md](references/json-policy.md), [time-and-identifiers.md](references/time-and-identifiers.md), and [evolution.md](references/evolution.md).

## Separate models

Distinguish:

- wire DTO
- persisted record
- domain model
- UI model

Do not reuse one class across boundaries when their compatibility rules differ. Map explicitly and validate at the boundary.

## Define the JSON contract

For every field specify:

- required, optional, or defaulted
- missing versus explicit `null`
- encoded default behavior
- unknown-key behavior
- enum unknown-value behavior
- number range and precision
- string normalization
- discriminator and subtype evolution
- timestamp, timezone, and duration representation
- backward and forward compatibility window

Treat `Json` options as protocol decisions, not style preferences.

## Cross-language proof

Maintain canonical fixtures:

```text
TypeScript encode -> Kotlin decode -> Kotlin re-encode
Kotlin encode -> TypeScript decode -> TypeScript re-encode
old persisted payload -> current Kotlin migration -> current representation
```

Compare semantic JSON where key ordering is irrelevant. Preserve exact strings where canonicalization, signatures, or hashes require it.

## Stale-pattern denylist

Investigate:

- Old `kotlinx.datetime.Instant` or `Clock` assumptions after migration to stdlib time.
- `explicitNulls = false` without testing decode asymmetry.
- `ignoreUnknownKeys = true` treated as enum evolution.
- `coerceInputValues = true` hiding an unknown enum or invalid value.
- `encodeDefaults` changed without a server and persistence migration.
- Ordinal enum serialization.
- `Double` for money, large identifiers, or integers beyond JavaScript safe precision.
- Local date-time used as an instant.
- Duration encoded in an undocumented unit.
- One DTO reused for network and durable storage.
- Debug exception payloads leaking secrets or raw user content.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_wire_contracts.py <repository-root>
```

If Python is unavailable, apply the wire-contract denylist manually and record
that the advisory scanner was not run.

## Validate

Test:

- missing, null, default, empty, and zero
- unknown key and unknown enum
- old and future subtype discriminator
- timestamp before epoch, fractional precision, offset, and timezone boundary
- duration zero, negative if valid, fractional, and overflow
- JavaScript safe-integer boundary
- malformed and oversized input
- persisted data from every supported schema version
- redacted decode errors in production logs

Do not call the contract stable until Kotlin and TypeScript fixtures agree.
