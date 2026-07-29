# Background work and components

## Choose the owner

| Need | Typical mechanism |
|---|---|
| Complete while screen is visible | lifecycle-owned coroutine |
| Durable deferrable work | WorkManager |
| User-visible ongoing permitted work | foreground service |
| Exact user-facing time | AlarmManager only after current policy check |
| Push-triggered hint | FCM, followed by valid local handling |

WorkManager is not an exact scheduler. A foreground service is not a general way around background restrictions.

## Durable work

- Persist minimal durable inputs.
- Use unique work policies deliberately.
- Make retries idempotent.
- Classify retryable and terminal failures.
- Bound retries and backoff.
- Observe constraints and stop signals.
- Do not hold process-local scopes as the source of truth.

## Foreground services

Confirm current:

- allowed start context
- declared service type
- manifest permission
- runtime permission or user grant
- notification timing and channel
- stop behavior
- Android-version restrictions

## Notifications and FCM

- Request notification permission where required.
- Model disabled channels.
- Use stable notification IDs and intentional replacement behavior.
- Make tap actions direct and immutable where required.
- Treat FCM delivery as best effort, duplicate-capable, and unordered.
- Fetch durable truth after a push instead of trusting the payload as authority.

## Deep links and background launches

- Validate scheme, host, path, and untrusted parameters.
- Use verified App Links where applicable.
- Test cold, warm, authenticated, unauthenticated, and invalid destinations.
- Do not start activities from background components unless current rules permit it.

## Official sources

- https://developer.android.com/develop/background-work
- https://developer.android.com/develop/background-work/background-tasks/persistent
- https://developer.android.com/develop/background-work/services/fgs
- https://developer.android.com/develop/ui/views/notifications
- https://firebase.google.com/docs/cloud-messaging/android/receive
- https://developer.android.com/training/app-links
