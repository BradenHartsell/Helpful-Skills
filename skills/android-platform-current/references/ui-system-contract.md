# UI and system contract

## Edge-to-edge

Handle:

- status and navigation bars
- display cutouts
- gesture navigation
- keyboard insets
- large screens and multi-window
- transient system bars

Apply insets at the boundary that consumes them. Avoid padding the entire tree repeatedly. Test bars with light and dark content.

## Predictive back

The system back gesture is part of app navigation state. Determine whether the app uses:

- Navigation 2
- Navigation 3
- a custom back stack
- platform fragments or activities

Do not maintain a second hidden back stack in an effect or callback. Test canceled and completed predictive gestures when the API is used.

## State restoration

Process death can remove every in-memory object. Save:

- navigation identity
- small UI reconstruction keys
- durable work IDs

Do not save large models, coroutine scopes, clients, or repositories in a Bundle or saveable-state registry.

## Permissions

Model:

- not requested
- granted
- denied
- denied with rationale
- permanently denied or settings-required
- revoked while app is inactive
- partial or selected access

Permission state belongs at the platform boundary. Business policy consumes a capability, not an assumed boolean.

## Official sources

- https://developer.android.com/develop/ui/compose/layouts/insets
- https://developer.android.com/develop/ui/views/layout/edge-to-edge
- https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture
- https://developer.android.com/topic/libraries/architecture/saving-states
- https://developer.android.com/training/permissions/requesting
