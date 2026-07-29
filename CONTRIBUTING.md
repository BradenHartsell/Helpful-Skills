# Contributing to Helpful Skills

Thank you for helping make agent skills clearer, safer, and more useful.

## Package structure

Place each skill in:

```text
skills/<skill-id>/
```

Keep all files required by that skill inside its directory. A typical package contains:

```text
README.md
SKILL.md
agents/
references/
```

Do not place an individual skill's operational files at the repository root.

## Required documentation

Each skill should include:

- a stable lowercase hyphenated skill ID;
- a precise human-facing title;
- a friendly `README.md`;
- a `SKILL.md` with a clear trigger, scope, workflow, output contract, and limitations;
- the date its knowledge or source snapshot was compiled;
- installation or loading guidance that does not assume one agent vendor;
- a source and recency policy for facts that can drift;
- an honest list of validation actually performed.

Add every new skill to the root `README.md` catalog with:

- its human-facing title;
- its stable skill ID;
- a concise description of what it covers;
- its compiled or refreshed date;
- a relative link to the skill directory.

Optional platform metadata must remain optional. The core instructions should degrade gracefully when a plugin, helper skill, documentation index, browser, or network connection is unavailable.

## Quality expectations

Before proposing a skill:

1. test realistic trigger and non-trigger scenarios;
2. forward-test the skill with a fresh agent or clean context;
3. check relative links and referenced files;
4. verify current official source links and retrieval dates;
5. distinguish local evidence, verified API availability, design guidance, and proposals;
6. check that offline or limited-tool behavior remains honest;
7. remove unfinished template text and environment-specific secrets;
8. document known gaps.

Do not claim accessibility, portability, production readiness, or current API support without corresponding evidence.

Run the repository validator:

```bash
python scripts/validate_catalog.py
```

## Third-party material

Links and original summaries are preferred over copied source material.

Before adding external prose, examples, code, screenshots, icons, fonts, binaries, or other assets:

1. identify the original source;
2. confirm that redistribution and modification are allowed;
3. preserve any required attribution or license;
4. avoid implying affiliation, sponsorship, or endorsement;
5. update [NOTICE.md](NOTICE.md) when needed.

Never commit credentials, tokens, private prompts, personal data, proprietary repository content, or private research artifacts.

## Pull requests

Keep each pull request focused on one skill or one coherent catalog improvement. Describe:

- what changed;
- who the skill helps;
- the compiled or refreshed date;
- sources that materially influenced it;
- validation performed;
- known limitations or follow-up work.
