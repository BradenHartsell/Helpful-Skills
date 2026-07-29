# Navigation generations

## Navigation 2

Recognize:

- `androidx.navigation:navigation-compose`
- `NavHost`
- `NavController`
- route or typed destination graph

Keep graph, controller, state holder, deep link, and back handling coherent.

## Navigation 3

Recognize:

- `androidx.navigation3`
- app-owned list or back stack of navigation keys
- `NavEntry`
- `NavDisplay`
- entry provider

In Navigation 3 the app owns navigation state as data. Mutate one authoritative back stack. Define key serialization and restoration intentionally.

Current snapshot researched 2026-07-28 showed the Navigation 3 1.1 release line. Refresh official release notes for the installed version:

- https://developer.android.com/guide/navigation/navigation-3
- https://developer.android.com/guide/navigation/navigation-3/basics
- https://developer.android.com/jetpack/androidx/releases/navigation3

## Do not mix casually

Migration requires:

- destination identity mapping
- arguments and serialization
- deep-link mapping
- nested navigation
- saved state
- transitions
- predictive back
- tests

Wrap generations at a deliberate boundary during migration. Do not let individual screens choose independently.

## Back behavior

System back, toolbar back, dismiss, and predictive back must operate on the same navigation truth. Test root behavior and unsaved-work policy.
