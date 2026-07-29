# Client architecture

## Ownership

An `HttpClient` owns engine resources and installed plugins. Usually it is application, session, or service-client scoped. Close it when that owner ends.

Avoid:

- per-request clients
- global mutable singleton clients without a close contract
- an authentication client that recursively uses its own refresh plugin
- reconnect jobs that outlive the client or session

## Built-ins before custom infrastructure

Check:

- `URLBuilder` and request URL DSL
- `ContentNegotiation`
- `HttpTimeout`
- `HttpRequestRetry`
- `Auth`
- `WebSockets`
- SSE
- response validation
- logging with redaction

If custom behavior remains, document the unmet product requirement.

## Failure taxonomy

Map explicitly:

```text
transport unavailable
TLS or proxy failure
timeout
caller cancellation
HTTP response status
protocol violation
decode or schema failure
domain rejection
```

Cancellation is not failure. Do not retry it.

## Retry

Require:

- method and operation safety
- attempt cap
- exponential backoff and jitter where appropriate
- server hint handling
- deadline interaction
- observability
- cancellation

An idempotency key can make a server operation safer, but only if the server implements it correctly.

## Streaming and reconnect

Give reader and writer tasks a parent. Choose:

- connection state
- replay or resubscribe token
- backoff
- authentication refresh
- duplicate suppression
- terminal states
- owner stop

Persist durable intent if the operation must survive process death. A socket scope is not durable storage.
