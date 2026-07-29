#!/usr/bin/env python3
"""Advisory scanner for stale Kotlin/Native and Swift interop patterns."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "legacy freezing API": r"\.(?:freeze|ensureNeverFrozen)\s*\(",
    "obsolete native-mt artifact": r"kotlinx-coroutines-core-native-mt",
    "Main dispatcher in Native, verify Darwin-only assumption": r"\bDispatchers\.Main\b",
    "Objective-C exception bridge, verify policy": r"@Throws\s*\(",
    "Flow in exported API, require Swift bridge": r"(?m)^\s*(?:public\s+)?(?:fun|val)\s+\w+[^{\n]*\bFlow<",
    "framework export configuration": r"\bbinaries\.framework\b|\bXCFramework\b|\bswiftExport\b",
    "StableRef lifecycle review": r"\bStableRef\b",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--max-per-rule", type=int, default=20)
    args = parser.parse_args()
    counts = {label: 0 for label in PATTERNS}
    for path in args.root.rglob("*"):
        if not path.is_file() or path.suffix not in {".kt", ".kts"}:
            continue
        if any(part in {".git", ".gradle", "build"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text):
                counts[label] += 1
                if counts[label] > args.max_per_rule:
                    continue
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path}:{line}: {label}")
    for label, count in counts.items():
        if count > args.max_per_rule:
            print(f"summary: {label}: {count} total, {count - args.max_per_rule} suppressed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
