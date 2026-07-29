# Helpful Skills

A growing collection of portable, evidence-aware agent skills for practical software and product work.

Each skill lives in its own directory under [`skills/`](skills/). Its instructions, optional agent metadata, reference material, and user documentation stay together so the repository can grow without turning the root into a collection of unrelated files.

## Skill catalog

| Skill | ID | What it covers | Compiled |
|---|---|---|---|
| [Kotlin Multiplatform Material 3 UI/UX Design and Engineering](skills/kmp-material3-ui-ux/) | `kmp-material3-ui-ux` | Product UI design, Material 3 systems, adaptive Compose layouts, accessibility, input, state, motion, KMP target parity, and visual QA | 2026-07-28 |
| [Frontend Experience Design and Engineering](skills/frontend-skill/) | `frontend-skill` | Product and marketing UI design, responsive systems, accessibility, truthful state, purposeful motion, implementation, and browser validation | 2026-07-28 |
| [Three.js 3D Experience Engineering](skills/threejs/) | `threejs` | Browser 3D rendering, scene design, interaction, assets, shaders, performance, and version-aware Three.js guidance | 2026-07-28 |

## Using a skill

Agent products discover skills in different ways. The portable path is:

1. Open the skill directory.
2. Read its `README.md` for scope and installation options.
3. Copy the complete directory into your agent's skills location, or point the agent directly to `SKILL.md`.
4. Keep the `references/` directory beside `SKILL.md` because the skill uses relative links.

If your agent supports named skill invocation, use the identifier declared in the `SKILL.md` frontmatter.

## Repository structure

```text
Helpful-Skills/
  README.md
  LICENSE
  NOTICE.md
  CONTRIBUTING.md
  scripts/
    validate_catalog.py
  skills/
    skill-name/
      README.md
      SKILL.md
      agents/
      references/
```

Not every skill needs every optional directory. Each package should remain self-contained, clearly dated, and usable without a specific proprietary plugin unless its documentation says otherwise.

## Quality standards

Published skills should:

- define a precise trigger and scope;
- keep one complete operational entrypoint in `SKILL.md`;
- use progressive references instead of one unbounded instruction file;
- separate local evidence, verified APIs, current official guidance, and proposals;
- degrade honestly when tools or network access are unavailable;
- include a compilation or research date;
- state what was actually validated;
- avoid secrets, private data, copied proprietary material, and invented APIs.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for package structure, documentation, validation, source, and licensing expectations.

## Validate the catalog

Run the dependency-free catalog validator before publishing:

```bash
python scripts/validate_catalog.py
```

It checks skill placement, required files, frontmatter names, compilation dates, root catalog entries, unfinished template markers, and internal Markdown links.

## License and notices

Original repository content is available under the [MIT License](LICENSE). Third-party names and linked materials remain the property of their respective owners. See [NOTICE.md](NOTICE.md) for the non-affiliation and third-party content notice.
