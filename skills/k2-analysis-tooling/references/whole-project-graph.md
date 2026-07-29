# Whole-project reachability graph

## Node classes

- source declarations
- generated declarations
- resources
- manifest components
- Gradle tasks and plugins
- serialization names
- DI bindings
- service-loader entries
- reflection strings
- native or JS exports
- test and benchmark entry points

## Edge classes

- resolved call and reference
- inheritance and override
- expect/actual
- generated-code origin
- resource reference
- manifest registration
- reflection heuristic
- serialization discriminator
- framework convention
- build task consumption

Mark edges exact, inferred, or unknown.

## Root classes

- application and framework entry points
- public library API
- manifest components
- tests, fixtures, and benchmarks under selected policy
- reflection configuration
- exported symbols
- generated registries
- resources referenced by identifier or convention

## Finding policy

An "unused" finding should include:

```text
declaration:
variant and source set:
searched exact edges:
searched dynamic edges:
roots considered:
generated and resource coverage:
confidence:
safe action:
```

Default safe action for heuristic findings is review or suppression, not deletion.
