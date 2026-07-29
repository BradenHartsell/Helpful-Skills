# Export modes

## Objective-C export

Traditional Kotlin/Native Apple frameworks expose Objective-C-compatible headers that Swift imports. API shape is constrained by Objective-C interop rules.

Check:

- framework base name and static or dynamic mode
- exported dependencies
- generated header names
- Swift name annotations
- generics and nullability
- exception annotations
- framework search and link settings

## Swift export

Current Kotlin 2.4 documentation describes Swift export as Alpha. It aims for a more direct Swift surface and SPM integration but has limitations and moving compatibility.

Before adopting:

- confirm exact Kotlin version
- read current supported declarations and limitations
- isolate the build configuration
- compile a golden Swift consumer
- pin toolchain and CI environment
- define rollback to Objective-C export if required

Primary sources:

- https://kotlinlang.org/docs/native-objc-interop.html
- https://kotlinlang.org/docs/native-swift-export.html
- https://kotlinlang.org/docs/native-spm.html
- https://kotlinlang.org/docs/native-cocoapods.html

## Do not blend

A type name, async mapping, exception rule, or package setup from one export mode may not apply to the other. Label every example with:

```text
Kotlin version:
export mode:
Apple target:
Swift version:
package integration:
```
