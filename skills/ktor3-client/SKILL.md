---
name: ktor3-client
description: Design, migrate, debug, and test Ktor 3 clients across Kotlin Multiplatform targets. Use for HttpClient setup, engine selection, requests, URLs, content negotiation, authentication, retries, timeouts, cancellation, WebSockets, SSE, streaming, TLS, proxies, reconnect state machines, MockEngine tests, or Ktor 2 to 3 migration.
---

# Ktor 3 Client

**Compiled knowledge:** 2026-07-28

Start from target capabilities and transport requirements. "Ktor supports it" does not mean every engine supports it.

## Preflight

Use `$kotlin-current`. Record:

```text
Ktor version:
targets:
engine per target:
HTTP version requirement:
WebSocket / SSE / streaming:
proxy and TLS:
timeout policy:
retry policy:
authentication:
serialization:
client owner:
connection owner:
```

Read [engine-capabilities.md](references/engine-capabilities.md) and refresh the current engine table for the installed Ktor version.

Use `$kmp-coroutines` when client, socket, or reconnect lifetime is part of the issue. Use `$serialization-wire-contracts` when payload semantics are part of it.

## Design the client boundary

1. Give `HttpClient` an explicit owner and close boundary.
2. Install plugins once in the owned client or a deliberate per-service client.
3. Use typed URL construction and request builders.
4. Keep authentication refresh single-flight and cancellation-aware.
5. Separate transport failures, protocol failures, HTTP status failures, decode failures, and domain rejections.
6. Retry only idempotent or explicitly safe operations.
7. Bound attempts and backoff. Respect cancellation.
8. Make timeout layers intentional: connect, request, socket, and product deadline are different.
9. Treat WebSocket and SSE reconnect as an application state machine only when built-in primitives do not satisfy product semantics.
10. Do not make a second hidden networking framework around Ktor.

Read [client-architecture.md](references/client-architecture.md).

## Ktor 2 to 3 migration

Use the official migration guide for the actual source version. Ktor 3 moved low-level I/O toward `kotlinx-io` and renamed or changed several lower-level surfaces. Search source, tests, custom plugins, and adapters for legacy types.

Do not mechanically rename APIs before proving behavioral equivalence, especially around body channels, streaming, and plugins.

## Stale-pattern denylist

Investigate:

- Assuming engine feature parity.
- Manual URL concatenation or percent encoding.
- A retry loop outside Ktor that retries every method and status.
- `while (true)` reconnect in a detached scope.
- Wrapping requests in arbitrary delay/timeouts while ignoring `HttpTimeout`.
- Creating a new client per request.
- Swallowing `CancellationException`.
- Consuming response bodies twice.
- Treating any non-2xx response as a network failure.
- Trusting MockEngine as proof of an engine-specific TLS, proxy, timeout, or streaming behavior.
- Ktor 2 imports or low-level channel types in a Ktor 3 build.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_ktor_client.py <repository-root>
```

If Python is unavailable, apply the client and engine denylist manually and
record that the advisory scanner was not run.

## Validate

Read [testing.md](references/testing.md). Test:

- URL and query encoding.
- Headers and authentication refresh.
- Success, every mapped status class, malformed payload, empty body.
- Connect, request, and socket timeout paths.
- Caller cancellation and owner closure.
- Retry exhaustion, non-idempotent no-retry, and server retry hints.
- Disconnect and reconnect without duplicate collectors or writers.
- Backpressure and slow consumers for streams.
- At least one real target engine for engine-specific behavior.

Do not declare cross-platform readiness from JVM MockEngine tests.
