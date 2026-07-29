# Ownership model

## Good common code

- DTOs and canonical wire models
- pure reducers and state transitions
- validation and policy
- domain interfaces
- deterministic business rules
- portable repositories when all dependencies and semantics are portable

## Good platform code

- OS permission and capability acquisition
- lifecycle integration
- background execution
- secure storage implementation
- push and billing
- window, notification, clipboard, and file picker integration
- framework and SDK adapters

## Interface pattern

Common code owns the need:

```kotlin
interface SecureTokenStore {
    suspend fun read(): String?
    suspend fun write(value: String?)
}
```

Platform code owns mechanism and lifecycle. The composition root supplies it.

Do not put a platform object in the common interface merely to avoid one adapter.

## Unhappy path

Every platform capability needs a portable failure shape:

- unsupported
- unavailable temporarily
- permission denied
- canceled by user
- invalid platform state
- permanent failure

Do not flatten these into `false` or `null` when product behavior differs.
