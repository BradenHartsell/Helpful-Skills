# Target-gated Android behavior

## Required workflow

1. Read `compileSdk`, `targetSdk`, and `minSdk`.
2. Read behavior changes for every target jump being crossed.
3. Read behavior changes that affect all apps on the OS versions being tested.
4. Read current Play submission and availability requirements.
5. Map each applicable change to code, manifest, tests, and release evidence.

Do not infer current policy from the previous release.

## Current snapshot

Researched 2026-07-28:

- Google Play states that from 2026-08-31, new apps and updates generally must target Android 16, API 36, with form-factor exceptions.
- Existing-app availability has a separate threshold.
- Android 15 targeting API 35 enforces edge-to-edge for many app surfaces.
- Android 16 targeting API 36 removes the older edge-to-edge opt-out path.
- Android 17 API 37 has its own target-gated behavior page.

Refresh:

- https://developer.android.com/google/play/requirements/target-sdk
- https://developer.android.com/about/versions/15/behavior-changes-15
- https://developer.android.com/about/versions/16/behavior-changes-16
- https://developer.android.com/about/versions/17/behavior-changes-17

## Receipt

For each gate:

```text
gate:
applies because:
affected code or manifest:
expected behavior:
test:
release implication:
official source and retrieval date:
```
