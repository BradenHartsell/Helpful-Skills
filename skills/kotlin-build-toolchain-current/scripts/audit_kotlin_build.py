#!/usr/bin/env python3
"""Advisory scanner for stale Kotlin build patterns."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "legacy kotlinOptions": r"\bkotlinOptions\s*\{",
    "independent Compose compiler extension": r"kotlinCompilerExtensionVersion",
    "Kotlin Android plugin needs AGP 9 module classification": r"org\.jetbrains\.kotlin\.android",
    "legacy Android library plugin needs KMP classification": r"com\.android\.library",
    "catch-all KSP configuration": r"(?m)^\s*ksp\s*\(",
    "eager afterEvaluate": r"\bafterEvaluate\s*\{",
    "eager task creation": r"\btasks\.create\s*\(",
    "removed JCenter repository": r"\bjcenter\s*\(",
    "dynamic dependency version": r":[+*](?:[\"'])",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    for path in args.root.rglob("*"):
        if not path.is_file() or path.suffix not in {".kts", ".gradle", ".toml"}:
            continue
        if any(part in {".git", ".gradle", "build"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text):
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path}:{line}: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
