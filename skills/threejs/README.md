# Three.js 3D Experience Engineering

**Skill ID:** `threejs`

**Compiled:** 2026-07-28
**Knowledge snapshot:** Three.js official documentation and manual, with version-sensitive guidance clearly marked

Build, improve, debug, and review browser-based 3D experiences with Three.js. This skill turns a broad 3D request into a practical plan for rendering, interaction, visual quality, and performance without assuming a particular product, repository, agent platform, or third-party tool.

## What it helps with

- scene, renderer, camera, resize, color, and render-loop setup;
- choosing and validating WebGL versus WebGPU rendering;
- geometry, materials, textures, lighting, shadows, and art direction;
- glTF, Draco, KTX2, and other asset-loading workflows;
- animation, picking, interaction, controls, and responsive input;
- custom shaders, post-processing, performance, memory cleanup, and debugging.

## Use it when

Use this skill for requests such as:

- "Build a polished product viewer with Three.js."
- "Why is this glTF model slow or missing textures?"
- "Add picking and hover feedback to this scene."
- "Port this renderer from legacy Three.js imports."
- "Decide whether this experience should use WebGL or WebGPU."

It is intentionally general-purpose. It does not require Context7, a browser connector, an MCP server, a specific editor, or network access.

## Install or load

Copy the complete `threejs` directory into your agent's skills folder, or configure the agent to read [`SKILL.md`](SKILL.md) directly. Keep [`references/`](references/) beside it because the operational guide links to those files.

If your agent supports named invocation, use `threejs`.

## How the skill works

`SKILL.md` is the working entrypoint. It begins with an implementation and quality workflow, then routes only to the reference area needed for the task. The source map explains how to handle changing APIs and how to work honestly when the network is unavailable.

The skill asks the agent to inspect the installed Three.js version and current imports before making version-sensitive claims. In particular, WebGPU, TSL, color management, loaders, decoder artifacts, and post-processing should be checked against the project version or current official sources rather than assumed from memory.

## Package contents

| File or directory | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | Main workflow, renderer gate, quality checklist, and reference routing |
| [`references/fundamentals.md`](references/fundamentals.md) | Scene setup, cameras, rendering, transforms, and responsive rendering |
| [`references/geometry.md`](references/geometry.md) | Geometry, BufferGeometry, instancing, and mesh construction |
| [`references/materials.md`](references/materials.md) | Materials, color, transparency, physical rendering, and selection guidance |
| [`references/textures.md`](references/textures.md) | Texture loading, color spaces, UVs, filtering, and optimization |
| [`references/lighting.md`](references/lighting.md) | Lights, shadows, environment lighting, and visual composition |
| [`references/loaders.md`](references/loaders.md) | glTF, Draco, KTX2, asset pipelines, and disposal |
| [`references/animation.md`](references/animation.md) | Mixers, clips, blending, timing, and procedural motion |
| [`references/interaction.md`](references/interaction.md) | Raycasting, input, selection, controls, and accessibility considerations |
| [`references/shaders.md`](references/shaders.md) | ShaderMaterial, uniforms, GLSL, and shader debugging |
| [`references/postprocessing.md`](references/postprocessing.md) | Effects, render targets, composition, and performance tradeoffs |
| [`references/sources-and-recency.md`](references/sources-and-recency.md) | Official source map, retrieval policy, release receipt, and offline behavior |

## Limits and honest behavior

This skill provides a disciplined approach, not a guarantee that an API exists in every Three.js release or that every device supports a rendering backend. It does not assume WebGPU availability, a CDN, hosted decoder assets, a specific bundler, or identical performance across browsers and hardware.

When current documentation or network access is unavailable, the skill uses local package files, lockfiles, imports, builds, tests, and runtime evidence. It labels those conclusions as local-only and avoids presenting them as universal or current.

## Validation performed

- checked the operational entrypoint with the skill validator;
- verified all internal package links and catalog structure with the repository validator;
- refreshed version-sensitive renderer, loader, and WebGPU guidance against official Three.js documentation on 2026-07-28;
- scanned the published package for project-specific identifiers;
- confirmed the public package contains no required third-party connector or service dependency.

## License and notice

This package is original instructional material published under the repository's [MIT License](../../LICENSE). Three.js is an independent open-source project; names and linked documentation remain the property of their respective owners. See the repository [NOTICE](../../NOTICE.md).
