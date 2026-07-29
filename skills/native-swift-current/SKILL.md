---
name: native-swift-current
description: Design, migrate, debug, and validate Kotlin/Native Apple frameworks, Objective-C export, Swift export, Swift Package Manager integration, coroutine and Flow bridging, exception boundaries, memory ownership, and binary packaging. Use when iOS or macOS interop becomes real, or when Kotlin APIs must be consumed safely from Swift or Objective-C.
---

# Native and Swift Current

**Compiled knowledge:** 2026-07-28

First choose the export generation. Do not merge Objective-C framework guidance, direct Swift export guidance, and old Native memory-manager advice.

## Preflight

Use `$kotlin-current`. Identify:

```text
Kotlin version:
Apple targets:
export mode: Objective-C headers or Swift export
framework kind and name:
SPM, CocoaPods, or manual integration:
public exported API:
suspend and Flow bridge:
exception policy:
thread and dispatcher policy:
ownership and cancellation:
Xcode and Swift versions:
stability level:
```

Read [export-modes.md](references/export-modes.md), [async-interop.md](references/async-interop.md), and [memory-and-packaging.md](references/memory-and-packaging.md).

## Choose a narrow exported API

1. Export stable facades, immutable data, and explicit lifecycle handles.
2. Keep platform SDK types behind Apple implementations unless they are intentionally part of the Swift surface.
3. Map Kotlin exceptions to an explicit Swift error policy.
4. Give async work an owner and cancellation bridge.
5. Deliver UI-facing completion on the required Apple executor.
6. Avoid exporting large generic or framework-internal graphs.
7. Treat Swift export as Alpha when current Kotlin documentation says so.
8. Keep Objective-C export and Swift export build paths separate in documentation and tests.

## Modern Native memory model

The legacy memory manager and its freezing-centric development model are obsolete in current Kotlin/Native. Do not add `freeze()`, `ensureNeverFrozen()`, or `kotlinx-coroutines-native-mt` as a modern fix.

Memory leaks still occur through retained scopes, callbacks, flows, stable references, and Swift or Objective-C ownership cycles.

## Stale-pattern denylist

Investigate:

- Legacy freezing guidance.
- `kotlinx-coroutines-native-mt`.
- Assuming `Dispatchers.Main` exists on every Native target.
- Exported suspend work without cancellation ownership.
- `Flow` exposed as though Swift consumes it natively without a bridge.
- Kotlin exceptions allowed to cross an unprepared boundary.
- Swift callback updating UI from a background executor.
- A framework retained globally with no close contract.
- Alpha Swift export adopted without a version pin and fixture.
- CocoaPods and SPM settings mixed accidentally.

When Python is available, run:

```text
python <skill-dir>/scripts/audit_native_swift.py <repository-root>
```

If Python is unavailable, apply the export, memory, and interop denylist
manually and record that the advisory scanner was not run.

## Validate

- Build every Apple target and configuration.
- Inspect exported header or Swift surface.
- Compile a minimal Swift consumer.
- Test success, cancellation, exception, and deallocation.
- Test background completion followed by UI update.
- Test repeated subscribe and unsubscribe for streams.
- Validate SPM or CocoaPods resolution from a clean consumer.
- Inspect binary size, symbols, dSYMs, and release packaging.

Do not call iOS ready from a Kotlin framework compile alone.
