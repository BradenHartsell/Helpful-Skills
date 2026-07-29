---
name: threejs
description: Build, debug, refactor, and optimize Three.js browser 3D experiences. Use this whenever the user is working on scene setup, WebGL or WebGPU renderer choice, cameras, geometry, materials, textures, lighting, model loading, shaders, post-processing, animation, interaction, or performance. Prefer this umbrella skill over narrower Three.js fragments so decisions stay coordinated across rendering, art direction, interaction, and performance.
---

# Three.js 3D Experience Engineering

Use this as the top-level skill for Three.js work. The goal is to keep the first load small, then pull in only the topic references that match the task.

**Compiled knowledge:** 2026-07-28

## What this skill is for

Use this skill when the user is:

- building a new Three.js scene or application
- debugging a broken scene, loader, camera, shader, or render path
- implementing interactive 3D behavior in the browser
- improving visual quality, performance, or architecture in an existing Three.js project
- combining multiple Three.js concerns in one task, such as loaders plus animation plus lighting

This skill is the orchestrator. Do not start by loading every reference file. Start with the task, decide which domains matter, then read only the relevant references.

## Progressive disclosure workflow

1. Understand the actual user task.
2. Identify the smallest set of Three.js domains involved.
3. Read only the matching reference files from `references/`.
4. Solve the task in an integrated way.
5. Verify that the rendering, interaction, and performance choices still make sense together.

When a task spans several domains, treat them as one system rather than independent snippets. For example, lighting decisions affect materials, loaders affect animation and texture handling, and interaction choices affect camera behavior and performance.

## Reference selection

Read only the files you need:

- `references/fundamentals.md`
  Use for scene setup, cameras, renderer configuration, transforms, resize handling, and core scene graph questions.
- `references/geometry.md`
  Use for built-in geometry, custom `BufferGeometry`, mesh construction, and instancing.
- `references/materials.md`
  Use for PBR materials, basic/phong/standard materials, material tuning, and material performance.
- `references/textures.md`
  Use for texture loading, UVs, cubemaps, texture settings, and image-based environment work.
- `references/lighting.md`
  Use for direct lights, shadows, environment lighting, and lighting tradeoffs.
- `references/loaders.md`
  Use for GLTF/GLB models, texture assets, async loading, loading managers, and asset pipeline issues.
- `references/animation.md`
  Use for `AnimationMixer`, clips, skeletal animation, morph targets, and procedural motion.
- `references/interaction.md`
  Use for raycasting, input handling, selection, object manipulation, controls, and interactive scenes.
- `references/shaders.md`
  Use for GLSL, `ShaderMaterial`, custom effects, uniforms, and material extension.
- `references/postprocessing.md`
  Use for `EffectComposer`, bloom, depth of field, color treatment, and screen-space effects.
- `references/sources-and-recency.md`
  Use before making version-sensitive API claims about renderers, color management, addons, loaders, WebGPU, TSL, or shader APIs.

## Renderer and version gate

Before naming an API or copying an addon import:

1. Inspect the installed `three` version, package manager lockfile, and existing renderer.
2. Use `WebGLRenderer` when broad browser compatibility and established WebGL addons are the priority.
3. Evaluate `WebGPURenderer` and TSL as a deliberate rendering-backend choice. Verify browser support, installed package exports, migration impact, and fallback behavior before adopting them.
4. Prefer current package addon imports such as `three/addons/controls/OrbitControls.js`. Do not copy historical `three/examples/jsm/` paths into new code without verifying the installed package.
5. Treat color management, decoder/transcoder artifacts, and post-processing APIs as version-sensitive. Read `references/sources-and-recency.md` and record the exact version and source date for material changes.

## How to approach common task shapes

### New scene or prototype

Start with `references/fundamentals.md`.
Then pull in only the next domain that matters, usually `geometry`, `materials`, `lighting`, or `interaction`.

Keep the first version structurally correct:

- correct renderer and resize handling
- stable camera setup
- sensible material and light pairing
- clear animation loop ownership

### Art-heavy or look-development work

Start with:

- `references/materials.md`
- `references/lighting.md`
- `references/textures.md`

Add `references/shaders.md` or `references/postprocessing.md` only if the effect genuinely needs them.

Prefer coherent art direction over stacking effects. A clean material-light-texture relationship usually matters more than another post effect.

### Model pipeline or asset integration

Start with:

- `references/loaders.md`
- `references/materials.md`
- `references/textures.md`

Add `references/animation.md` if imported clips or rigs are involved.

Keep an eye on:

- color space correctness
- texture settings
- asset cleanup and disposal
- loader lifecycle and fallback behavior

### Interaction or game-like behavior

Start with:

- `references/interaction.md`
- `references/fundamentals.md`

Then add whichever rendering references are needed. Interactive work usually touches camera decisions, object hierarchy, and update-loop structure at the same time.

### Performance or architecture work

Start with the references that correspond to the bottleneck. Do not read everything by default.

Typical mappings:

- too many objects or draw calls: `geometry`, `materials`
- expensive effects: `postprocessing`, `lighting`, `shaders`
- loader churn or asset bloat: `loaders`, `textures`
- update loop and controls issues: `fundamentals`, `interaction`, `animation`

## Operating principles

- Favor working, coherent scene architecture over isolated snippets.
- Reuse materials, textures, and geometry where repetition exists.
- Keep interaction, camera, and render-loop logic aligned.
- When debugging visuals, verify the full chain: asset import, color space, lighting, material, camera, post.
- When optimizing, fix the dominant cost first rather than doing scattered micro-tuning.

## Output expectations

When answering or implementing:

- explain the relevant Three.js decisions in plain language
- keep code aligned with current Three.js import patterns
- call out tradeoffs when a visually nicer option is materially more expensive
- verify the affected path when practical instead of stopping at a code guess

## When not to over-read

Do not open shader or post-processing references unless the task actually needs custom rendering work.
Do not load all ten references just because the user mentioned Three.js.
The point of this skill is focused depth, not maximal context.
