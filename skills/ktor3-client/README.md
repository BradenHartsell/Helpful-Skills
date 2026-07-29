# Ktor 3 Multiplatform Client Engineering

**Skill ID:** `ktor3-client`

**Compiled:** 2026-07-28

Design, migrate, debug, and test Ktor 3 clients across Kotlin Multiplatform
targets.

Use it for engine selection, requests, typed URLs, authentication, retries,
timeouts, cancellation, WebSockets, server-sent events, streaming, TLS,
proxies, reconnect state machines, MockEngine tests, and Ktor 2 to 3 migration.

Start with [`kotlin-current`](../kotlin-current/) to detect versions and
targets. The references separate client ownership, engine capability, and
testing evidence so JVM MockEngine success is never mistaken for multiplatform
transport proof.

The audit script is optional. Real engine behavior still requires at least one
focused test on each materially different target engine.

Original instructions are available under the repository
[MIT License](../../LICENSE).
