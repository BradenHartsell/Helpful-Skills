# Android Platform Current

**Skill ID:** `android-platform-current`

**Compiled:** 2026-07-28

Design, audit, migrate, and validate Android behavior against the project's
actual compile SDK, target SDK, minimum SDK, manifest, dependency versions, and
current distribution requirements.

Use it for WorkManager, foreground services, notifications, FCM, Play Billing,
deep links, exact alarms, edge-to-edge, insets, predictive back, permissions,
process death, and Android release readiness.

Start with [`kotlin-current`](../kotlin-current/) to establish the stack. The
package routes into background components, target gates, UI system contracts,
Billing, and release proof.

The audit script is optional and has a manual fallback. Time-sensitive Android
and Play requirements must be refreshed immediately before a release.

Original instructions are available under the repository
[MIT License](../../LICENSE).
