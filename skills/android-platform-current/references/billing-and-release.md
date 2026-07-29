# Billing, Firebase, and release

## Play Billing

Refresh the exact major's integration guide and release notes:

- https://developer.android.com/google/play/billing/integrate
- https://developer.android.com/google/play/billing/release-notes

Require:

- one owned connection lifecycle
- product-detail refresh
- pending purchase support
- acknowledgement or consumption
- server-side verification where value or entitlement matters
- idempotent entitlement application
- recovery after disconnect
- handling already-owned and unavailable products
- test purchases and current Play test configuration

Do not grant durable entitlement solely from a client callback.

## Firebase Kotlin modules

Firebase stopped releasing separate KTX modules in July 2025 and removed them from Firebase BoM 34. Use Kotlin APIs from main modules for current builds.

Source:

- https://firebase.google.com/docs/android/kotlin-migration

Audit dependency aliases and transitive artifacts, not only imports.

## Release checklist

- Current target API requirement checked on release date.
- `compileSdk`, `targetSdk`, and dependency support aligned.
- Release manifest inspected after merge.
- App links and signing verified.
- Billing version and declarations current.
- Data safety and permission disclosures reviewed.
- Background work and foreground-service types reviewed.
- Obfuscation, mapping, symbol, and native debug artifacts generated.
- Upgrade path tested from a production version.
- Device or emulator tests cover current target gates.
