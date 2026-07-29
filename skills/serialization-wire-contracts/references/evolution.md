# Schema evolution

## Network evolution

Backward compatible additions usually require:

- old client can ignore new fields
- new client can tolerate missing fields
- enum evolution has an explicit policy
- discriminator evolution has a migration path

Do not assume a default value means the same thing as an omitted field.

## Persisted evolution

Persisted schemas need:

- explicit schema version
- deterministic migrations
- transactional replacement where supported
- backup or recovery policy
- downgrade policy
- fixture for every supported old version

Never enable lenient JSON and call that a persistence migration.

## Golden fixture layout

Recommended:

```text
contracts/
  schema/
  fixtures/
    valid/
    missing/
    null/
    unknown/
    legacy/
  kotlin-tests/
  typescript-tests/
```

Each fixture should name the behavior it proves, not only the DTO type.

## Contract change receipt

```text
field:
old semantics:
new semantics:
old client behavior:
new client with old server:
persistence impact:
fixtures:
rollout order:
rollback:
```
