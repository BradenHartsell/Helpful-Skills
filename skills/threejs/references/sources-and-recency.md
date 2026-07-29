# Three.js sources and recency

## Compiled knowledge snapshot

This skill was refreshed on 2026-07-28. Three.js releases frequently change
renderer, addon, color-management, loader, shader, and WebGPU or TSL details.
Treat this reference as a refresh map, not as proof that an API exists in a
project's installed version.

## Source priority

Use evidence in this order:

1. the project's `package.json`, lockfile, import map, bundler configuration,
   and current source code;
2. the locally resolved `three` package and a focused build or test;
3. official Three.js documentation and examples for the exact installed version
   when available;
4. current official documentation for an upgrade proposal;
5. secondary tutorials only for discovery, never as sole API proof.

When sources disagree, the installed package plus a focused build decides what
code is available today. Official documentation for the installed version
explains intended behavior. Report unresolved conflicts instead of silently
choosing the newest-looking example.

## Official refresh map

- [Three.js documentation](https://threejs.org/docs/)
- [Creating a scene](https://threejs.org/manual/#en/introduction/Creating-a-scene)
- [Color management](https://threejs.org/manual/#en/color-management)
- [WebGLRenderer](https://threejs.org/docs/#api/en/renderers/WebGLRenderer)
- [WebGPURenderer](https://threejs.org/docs/#api/en/renderers/WebGPURenderer)
- [GLTFLoader](https://threejs.org/docs/#examples/en/loaders/GLTFLoader)
- [DRACOLoader](https://threejs.org/docs/#examples/en/loaders/DRACOLoader)
- [KTX2Loader](https://threejs.org/docs/#examples/en/loaders/KTX2Loader)
- [Disposing resources](https://threejs.org/manual/#en/cleanup)
- [ShaderMaterial](https://threejs.org/docs/#api/en/materials/ShaderMaterial)

## Release receipt

For a version-sensitive implementation or review, record:

```text
Installed three version:
Renderer: WebGLRenderer or WebGPURenderer:
Addon import path:
Browser support and fallback:
Local proof: build, test, or running scene:
Official source URL:
Source version scope:
Retrieved on: YYYY-MM-DD, or local-only:
Conflict and resolution:
```

## Offline mode

When official documentation is unavailable, inspect the installed package and
existing imports, run the focused local check that is available, and label
recency-sensitive claims `local-only`. Do not claim that a renderer, addon, or
shader API is the latest without current official evidence.
