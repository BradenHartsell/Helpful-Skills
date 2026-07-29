# Time, duration, identifiers, and numbers

## Time

Modern Kotlin stdlib provides `kotlin.time.Instant` and `Clock`. Recent kotlinx-datetime versions migrated away from their older equivalents. Confirm Kotlin, kotlinx-datetime, and kotlinx.serialization compatibility before migrating.

Choose:

- instant for a point on the global timeline
- local date for a calendar date without time
- local date-time only with an explicit timezone conversion policy
- timezone ID when future civil-time interpretation matters

Network instants should normally use a documented ISO 8601 or epoch representation with explicit precision.

Primary sources:

- https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-instant/
- https://github.com/Kotlin/kotlinx-datetime

## Duration

Document whether duration is:

- ISO 8601 string
- integer milliseconds
- integer nanoseconds
- structured seconds and nanos

Name units in field names when using numeric representations.

## Identifiers

Opaque identifiers should remain strings unless arithmetic is meaningful. Do not parse UUID-like or provider IDs merely for validation unless the protocol requires it.

## Numeric precision

JavaScript exact integer range is smaller than Kotlin `Long`. Encode large counters or identifiers as strings when TypeScript consumers must preserve exactness.

Use decimal minor units or a decimal type for money. Do not use binary floating point for exact monetary contracts.
