# Compose testing

## Required proof

- State-holder unit tests for deterministic behavior.
- Compose UI tests for semantics and interaction.
- Recomposition-sensitive tests for duplicate side effects.
- Restoration tests for saved state.
- Navigation tests for stack state and deep links.
- Platform tests for lifecycle and insets.

## Unhappy paths

- Recompose while request is active.
- Change an effect key mid-flight.
- Dispose before callback.
- Navigate forward twice rapidly.
- Press back during transition.
- Recreate process with partial state.
- Restore a destination whose durable entity no longer exists.
- Reorder a lazy list.
- Stop lifecycle while flow emits.
- Open keyboard under edge-to-edge.

## Observability

Count starts, stops, subscriptions, and disposals in tests. A UI assertion alone may miss duplicate background work.

Primary sources:

- https://developer.android.com/develop/ui/compose/testing
- https://developer.android.com/develop/ui/compose/testing-synchronization
- https://kotlinlang.org/docs/multiplatform/compose-test.html
