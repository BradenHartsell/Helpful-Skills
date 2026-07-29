# State and effects

## State ownership

| State | Owner |
|---|---|
| transient drawing or interaction detail | composable |
| screen UI state | screen state holder or ViewModel |
| navigation identity | navigation owner |
| durable business state | repository or durable store |
| application/session state | application or session owner |

Do not duplicate writable truth across layers.

## Effect selection

| Need | API |
|---|---|
| suspend while this keyed composition exists | `LaunchedEffect` |
| launch from an event while composition exists | `rememberCoroutineScope` |
| register and unregister external resource | `DisposableEffect` |
| publish Compose state outward after successful composition | `SideEffect` |
| transform non-Compose observable into state | `produceState` or platform integration |
| derive cheap state from other snapshot state | `derivedStateOf` when it reduces meaningful invalidations |
| read latest callback without restart | `rememberUpdatedState` |

Effects should bridge Compose to an external system. Do not use them to simulate an ordinary calculation.

## Keys

For each effect ask:

- Which value change must cancel and restart this work?
- Which changing value should be observed without restart?
- Does the key have stable equality?
- Is the work actually owned by composition?

## Stability and recomposition

- Prefer immutable UI models.
- Avoid unstable containers crossing hot composable boundaries.
- Do not add equality or stability annotations without satisfying their contract.
- Measure before introducing memoization.
- Use stable item keys for identity.

## Saveable state

Save minimal reconstruction keys. Restore from durable owners. Test size and serialization limits.

Primary sources:

- https://developer.android.com/develop/ui/compose/state
- https://developer.android.com/develop/ui/compose/side-effects
- https://developer.android.com/develop/ui/compose/lifecycle
- https://developer.android.com/develop/ui/compose/performance/stability
- https://developer.android.com/develop/ui/compose/state-saving
- https://kotlinlang.org/docs/multiplatform/compose-lifecycle.html
