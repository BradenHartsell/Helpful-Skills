#!/usr/bin/env python3
"""Advisory scanner for Kotlin coroutine ownership and behavior risks."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "GlobalScope": r"\bGlobalScope\b",
    "detached Job in child context": r"\+\s*(?:Supervisor)?Job\s*\(",
    "broad Throwable catch": r"catch\s*\(\s*\w+\s*:\s*Throwable\s*\)",
    "runBlocking in production path": r"\brunBlocking\s*\{",
    "hardcoded IO dispatcher": r"\bDispatchers\.IO\b",
    "Main dispatcher, verify target artifact": r"\bDispatchers\.Main\b",
    "launching repository API, inspect ownership": r"(?i)class\s+\w*Repository[\s\S]{0,1600}?\blaunch\s*\{",
    "async result, verify await": r"\basync\s*\{",
    "non-cancellable block, bound cleanup": r"withContext\s*\(\s*NonCancellable\s*\)",
    "non-atomic state read-modify-write": r"\.value\s*=\s*\w*\.value\.(?:copy|plus)|\.value\s*=\s*\.value",
    "limitedParallelism is not a mutex": r"\.limitedParallelism\s*\(\s*1\s*\)",
    "legacy Native freezing": r"\.(?:freeze|ensureNeverFrozen)\s*\(",
    "obsolete native-mt artifact": r"kotlinx-coroutines-core-native-mt",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--max-per-rule", type=int, default=20)
    args = parser.parse_args()
    counts = {label: 0 for label in PATTERNS}
    for path in args.root.rglob("*"):
        if not path.is_file() or path.suffix not in {".kt", ".kts", ".toml"}:
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
