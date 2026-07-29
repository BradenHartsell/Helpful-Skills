# JSON policy

## Important defaults

Refresh against the installed kotlinx.serialization version.

Current 1.11 snapshot:

- `encodeDefaults` defaults to false.
- `ignoreUnknownKeys` defaults to false.
- `explicitNulls` defaults to true.
- class discriminator defaults to a configured property name unless changed.
- `coerceInputValues` can replace some invalid or unknown values with defaults or nulls.

These are protocol semantics.

## Missing and null

Define separately:

```text
field missing
field present with null
field present with default value
```

`explicitNulls = false` can make encode and decode behavior asymmetric. Test round trips, especially nullable properties without a default.

## Enums

Do not serialize ordinals. For forward compatibility choose deliberately:

- reject unknown values
- map to an explicit `Unknown(raw)` domain representation through a custom serializer
- preserve raw wire strings

`ignoreUnknownKeys` does not solve unknown enum values.

## Polymorphism

Pin:

- discriminator property
- serialized subtype names
- unknown subtype behavior
- collision policy when a model property has the same name

Do not use class names as an accidental stable protocol.

## Security

Limit input size at the transport boundary. Do not place raw secrets, tokens, payment data, or full user payloads in serialization exceptions or logs. Current libraries can add richer debug details, which must remain a deliberate non-production choice.

Primary sources:

- https://github.com/Kotlin/kotlinx.serialization
- https://kotlinlang.org/api/kotlinx.serialization/
- https://github.com/Kotlin/kotlinx.serialization/releases
