# Ktor client testing

## Test layers

| Layer | Proves |
|---|---|
| Pure request builder test | URLs, headers, body shape |
| MockEngine | plugin ordering, response mapping, deterministic sequences |
| Local protocol server | actual HTTP and streaming semantics |
| Real target engine | TLS, proxy, cancellation, engine timeout, platform behavior |
| Backend contract test | deployed or representative server compatibility |

MockEngine is necessary but insufficient.

## Deterministic cases

- encoded path segment versus query parameter
- redirect policy
- authentication expiry during concurrent calls
- body decode after non-success response
- empty success body
- response larger than expected
- retry with non-repeatable body
- cancellation during backoff
- client close during an active stream
- reconnect with duplicate event
- slow collector and buffer limit

## Version notes

Review current Ktor changelog for test-engine limitations. A virtual-time coroutine test may not control every engine or plugin clock. If timeout behavior is engine-specific, test that engine.

Primary sources:

- https://ktor.io/docs/client-testing.html
- https://ktor.io/docs/client-timeout.html
- https://ktor.io/docs/client-request-retry.html
- https://ktor.io/docs/migrating-3.html
- https://github.com/ktorio/ktor/releases
