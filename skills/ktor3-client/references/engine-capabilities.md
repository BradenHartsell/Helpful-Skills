# Engine capabilities

Snapshot researched 2026-07-28 from current Ktor 3.5 documentation. Refresh for the installed version.

| Engine | Typical targets | HTTP/2 | WebSocket | Notes |
|---|---|---:|---:|---|
| Apache5 | JVM | yes | no | JVM Apache stack |
| Java | JVM | yes | yes | JDK client |
| Jetty | JVM | yes | no | Check exact Jetty capabilities |
| CIO | JVM, Android, Native, JS, Wasm | no in current table | yes | Broad target coverage is not feature parity |
| Android | Android | no | no | Android platform engine |
| OkHttp | JVM, Android | yes | yes | Engine-specific interceptors and TLS |
| Js | JS | yes | yes | Browser or JS runtime constraints apply |
| Darwin | Apple | yes | yes | NSURLSession-based platform behavior |
| WinHttp | Windows | yes | yes | Windows capabilities apply |
| Curl | Native targets | yes | yes | Native libcurl environment applies |

Confirm:

- engine artifact
- supported target
- HTTP/2
- WebSocket
- SSE behavior
- streaming
- proxy
- TLS customization
- connect timeout
- socket timeout
- cancellation

Primary sources:

- https://ktor.io/docs/client-engines.html
- https://ktor.io/docs/client-supported-platforms.html
- https://api.ktor.io/

Do not use the snapshot table as a substitute for current docs.
