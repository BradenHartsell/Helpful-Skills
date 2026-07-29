# Analysis API rules

## Sessions and lifetimes

`KaSession` is module-perspective analysis state. Values with Analysis API lifetimes are generally valid only inside the analysis action that produced them.

Do not:

- store `KaSymbol`, `KaType`, or `KaSession` in a long-lived graph
- access them after modification or session exit
- use raw objects as cache keys

Extract stable identifiers and plain immutable facts. Use supported symbol pointers when re-resolution is required, then handle failure to restore.

## PSI and semantics

PSI is syntax. It does not by itself answer resolved target, overload, inferred type, or cross-module meaning. Use Analysis API for semantic claims.

## Module perspective

The same syntax can resolve differently by module, source set, dependencies, or variant. Build the correct `KaModule` view before analyzing.

## Standalone status

Current Analysis API documentation says IntelliJ plugin development is the officially supported primary use case and standalone mode is still under development. Pin dependencies, isolate integration, and run compatibility fixtures on Kotlin updates.

## K1 migration

Replace descriptor and `BindingContext` logic conceptually. Do not build a compatibility wrapper that preserves invalid K1 lifetime assumptions.
