#!/usr/bin/env python3
"""Advisory Kotlin stack fingerprint and capsule router."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


CONFIG_NAMES = {
    "settings.gradle",
    "settings.gradle.kts",
    "build.gradle",
    "build.gradle.kts",
    "gradle.properties",
    "libs.versions.toml",
    "gradle-wrapper.properties",
    "AndroidManifest.xml",
    "Package.swift",
    "Podfile",
    "package.json",
}

VERSION_PATTERNS = {
    "kotlin": r"(?im)^\s*(?:kotlin|kotlin_version|kotlinVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "agp": r"(?im)^\s*(?:agp|agp_version|agpVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "ksp": r"(?im)^\s*(?:ksp|ksp_version|kspVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "ktor": r"(?im)^\s*(?:ktor|ktor_version|ktorVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "coroutines": r"(?im)^\s*(?:coroutines|kotlinx-coroutines|coroutines_version|coroutinesVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "serialization": r"(?im)^\s*(?:serialization|kotlinx-serialization|serialization_version|serializationVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "datetime": r"(?im)^\s*(?:datetime|kotlinx-datetime|datetime_version|datetimeVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "compose": r"(?im)^\s*(?:compose|compose-multiplatform|compose_version|composeVersion)\s*=\s*[\"']?([^\"'\s]+)",
    "firebase_bom": r"(?im)^\s*(?:firebaseBom|firebase-bom|firebase_bom)\s*=\s*[\"']?([^\"'\s]+)",
    "billing": r"(?im)^\s*(?:billing|play-billing|billing_version|billingVersion)\s*=\s*[\"']?([^\"'\s]+)",
}

TARGET_PATTERNS = {
    "android": r"\bandroidTarget\s*\(|\bcom\.android\.(?:application|library)\b|\bcom\.android\.kotlin\.multiplatform\.library\b",
    "jvm": r"(?<!android)\bjvm\s*(?:\(|\{)",
    "ios": r"\bios(?:Arm64|X64|SimulatorArm64|\s*(?:\(|\{))",
    "macos": r"\bmacos(?:Arm64|X64)\s*(?:\(|\{)",
    "linux": r"\blinux(?:Arm64|X64)\s*(?:\(|\{)",
    "mingw": r"\bmingwX64\s*(?:\(|\{)",
    "js": r"\bjs\s*(?:\(|\{)",
    "wasmJs": r"\bwasmJs\s*(?:\(|\{)",
    "wasmWasi": r"\bwasmWasi\s*(?:\(|\{)",
}

ROUTES = {
    "kotlin-build-toolchain-current": (
        "gradle-wrapper.properties",
        "org.jetbrains.kotlin",
        "com.android.",
        "com.google.devtools.ksp",
        "compilerOptions",
        "kotlinOptions",
    ),
    "kmp-coroutines": ("kotlinx-coroutines", "CoroutineScope", "StateFlow", "SharedFlow"),
    "android-platform-current": ("AndroidManifest.xml", "targetSdk", "firebase", "billing"),
    "ktor3-client": ("io.ktor", "ktor-client"),
    "compose-runtime-navigation": ("org.jetbrains.compose", "androidx.compose", "navigation3", "navigation-compose"),
    "serialization-wire-contracts": ("kotlinx-serialization", "kotlinx-datetime", "@Serializable"),
    "kmp-source-set-boundaries": ("multiplatform", "commonMain", "androidMain", "iosMain", "expect "),
    "k2-analysis-tooling": (
        "kotlin-analysis-api",
        "org.jetbrains.kotlin.analysis",
        "SymbolProcessorProvider",
        "CompilerPluginRegistrar",
        "IrGenerationExtension",
    ),
    "native-swift-current": ("swiftExport", "binaries.framework", "XCFramework", "cocoapods"),
}


def collect_files(root: Path) -> list[Path]:
    files: list[Path] = []
    ignored = {".git", ".gradle", "build", "node_modules", ".idea", "out"}
    for path in root.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file() and (
            path.name in CONFIG_NAMES
            or "buildSrc" in path.parts
            or path.suffix == ".versions.toml"
        ):
            files.append(path)
    return sorted(set(files))


def first_match(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    files = collect_files(root)
    digest = hashlib.sha256()
    combined_parts: list[str] = []
    evidence: list[str] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        data = path.read_bytes()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(data)
        digest.update(b"\0")
        evidence.append(rel)
        combined_parts.append(data.decode("utf-8", errors="replace"))
    combined = "\n".join(combined_parts)

    wrapper = first_match(r"distributionUrl=.*gradle-([0-9][^-\\/]+)-", combined)
    versions = {key: first_match(pattern, combined) for key, pattern in VERSION_PATTERNS.items()}
    sdks = {
        key: first_match(rf"(?m)\b{key}\s*(?:=|\()\s*([0-9]+)", combined)
        for key in ("compileSdk", "targetSdk", "minSdk")
    }
    targets = [name for name, pattern in TARGET_PATTERNS.items() if re.search(pattern, combined)]
    routes = [
        capsule
        for capsule, needles in ROUTES.items()
        if any(needle in combined or needle in "\n".join(evidence) for needle in needles)
    ]
    facts = {
        "root": str(root),
        "fingerprint": digest.hexdigest(),
        "evidence_files": evidence,
        "gradle": wrapper,
        "versions": versions,
        "android_sdks": sdks,
        "targets": targets,
        "navigation_generation": {
            "navigation2": bool(re.search(r"navigation-compose|androidx\.navigation(?!3)", combined)),
            "navigation3": "navigation3" in combined,
        },
        "recommended_capsules": routes,
        "warnings": [
            message
            for condition, message in (
                (not files, "No recognized stack files were found."),
                (wrapper is None, "Gradle wrapper version was not resolved."),
                ("libs.versions.toml" in "\n".join(evidence) and not any(versions.values()),
                 "A version catalog exists, but common aliases were not resolved. Inspect it manually."),
                ("buildSrc" in combined and not any("buildSrc" in item for item in evidence),
                 "Build logic may hide computed values."),
            )
            if condition
        ],
    }

    if args.format == "json":
        print(json.dumps(facts, indent=2, sort_keys=True))
        return 0

    print("STACK FACTS")
    print(f"root: {facts['root']}")
    print(f"fingerprint: {facts['fingerprint']}")
    print(f"Gradle: {wrapper or 'unresolved'}")
    for key, value in versions.items():
        if value:
            print(f"{key}: {value}")
    print("Android SDKs: " + ", ".join(f"{k}={v or 'unresolved'}" for k, v in sdks.items()))
    print("targets: " + (", ".join(targets) or "unresolved"))
    print("navigation: " + json.dumps(facts["navigation_generation"], sort_keys=True))
    print("capsules: " + (", ".join(routes) or "manual routing required"))
    print(f"evidence files: {len(evidence)}")
    for warning in facts["warnings"]:
        print(f"warning: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
