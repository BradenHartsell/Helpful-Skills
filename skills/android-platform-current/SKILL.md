---
name: android-platform-current
description: Design, audit, migrate, and validate Android behavior against the repository's exact compileSdk, targetSdk, minSdk, manifest, dependency versions, and current Google Play requirements. Use for background work, WorkManager, foreground services, notifications, FCM, Play Billing, deep links, exact alarms, edge-to-edge, window insets, predictive back, permissions, process death, or Android release readiness.
---

# Android Platform Current

**Compiled knowledge:** 2026-07-28

The first input is `targetSdk`, not a remembered Android recipe.

## Establish the platform contract

Use `$kotlin-current` and inspect the Android app module, manifest merge inputs, dependencies, and release configuration.

Record:

```text
compileSdk:
targetSdk:
minSdk:
application module:
distribution channel:
foreground service types:
permissions:
manifest components and exported state:
Firebase BoM and modules:
Play Billing:
edge-to-edge implementation:
back implementation:
background-work owners:
```

Refresh current Android behavior changes and Play requirements. Read [target-gates.md](references/target-gates.md).

## Route by work type

Read:

- [background-and-components.md](references/background-and-components.md) for WorkManager, jobs, services, alarms, notifications, FCM, deep links, and background launches.
- [ui-system-contract.md](references/ui-system-contract.md) for edge-to-edge, insets, predictive back, permissions, and process recreation.
- [billing-and-release.md](references/billing-and-release.md) for Billing, Firebase dependency migration, Play policy, and release proof.

Use `$compose-runtime-navigation` as well when system back or insets cross a Compose navigation boundary.

## Core rules

1. Separate app lifecycle, process lifetime, scheduled work, and user-visible ongoing work.
2. Prefer WorkManager for deferrable guaranteed work. Do not use it as an exact timer.
3. Use a foreground service only for current permitted user-visible work and declare the correct type and permissions.
4. Model permission denial, revocation, and limited access as normal states.
5. Use exact alarms only when the product requirement meets current platform and policy rules.
6. Use direct notification `PendingIntent` destinations. Avoid notification trampolines.
7. Treat process death as ordinary. Persist durable inputs and make work idempotent.
8. Handle edge-to-edge with actual insets. Never hardcode status or navigation bar sizes.
9. Integrate predictive back with the navigation generation already present.
10. Use Firebase Kotlin APIs from main modules. Do not introduce removed `-ktx` artifacts.
11. Treat Billing acknowledgements, pending purchases, reconnects, and server verification as owned state machines.
12. Recheck Play target requirements immediately before a release.

## Stale-pattern denylist

Investigate:

- Generic background `Service` for deferrable work.
- Background foreground-service starts without a documented exemption.
- Missing foreground-service type or permission.
- `AlarmManager` used for ordinary periodic sync.
- Exact alarms without permission and policy analysis.
- Notification permission assumed granted.
- Notification trampoline through a receiver or service.
- Fixed system-bar padding.
- Back interception that bypasses the app's navigation state.
- `firebase-*-ktx` dependencies in a current Firebase BoM.
- A Billing example copied from an older major.
- Release readiness claimed without current target API and policy evidence.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_android_platform.py <repository-root>
```

If Python is unavailable, apply the target-gated denylist manually and record
that the advisory scanner was not run.

## Validate the unhappy paths

- Fresh install, upgrade, permission denial, permission revocation.
- Cold start from a notification or deep link.
- Process death and restoration.
- Offline start, network loss, retry, duplicate delivery.
- Background execution under current restrictions.
- Gesture and three-button navigation.
- Status bars, navigation bars, cutouts, keyboard, large screens.
- Purchase pending, canceled, already owned, disconnected, and acknowledged.
- Release build, manifest merger, lint, emulator or device behavior, and current Play policy.

Name the OS versions and target-gated paths not exercised.
