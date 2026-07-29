# Hierarchy and dependencies

## Default hierarchy template

Modern KMP creates intermediate source sets for common target families where applicable. Inspect the actual Gradle model.

Manual `dependsOn` edges can disable or conflict with default hierarchy inference. Before adding one:

1. Draw current target compilations.
2. Identify the API or dependency that needs sharing.
3. Check whether the default template already supplies an intermediate source set.
4. Confirm the dependency supports every target in the proposed set.
5. Compile all descendants.

## Dependency placement

Put a dependency in the narrowest source set that owns its semantics. A library publishing a KMP artifact is necessary but not sufficient. Check target support and behavior.

## Target removal or addition

Audit:

- source-set edges
- generated tasks
- tests
- native host availability
- publishing metadata
- consumer variants
- expect/actual completeness
- resources
- cinterop and framework settings

## Primary sources

- https://kotlinlang.org/docs/multiplatform/multiplatform-discover-project.html
- https://kotlinlang.org/docs/multiplatform/multiplatform-hierarchy.html
- https://kotlinlang.org/docs/multiplatform/multiplatform-expect-actual.html
- https://kotlinlang.org/docs/multiplatform/multiplatform-compatibility-guide.html
