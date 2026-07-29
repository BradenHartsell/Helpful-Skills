#!/usr/bin/env python3
"""Advisory scanner for KMP source-set boundary risks."""

import argparse
import re
from pathlib import Path

PLATFORM_IMPORT = re.compile(r"(?m)^import\s+(?:android\.|androidx\.|platform\.|java\.awt\.|javax\.swing\.)")
PATTERNS = {
    "expect declaration, justify language-level coupling": r"(?m)^\s*expect\s+",
    "manual dependsOn, inspect hierarchy": r"\.dependsOn\s*\(",
    "platform type in common API": r"\b(?:Context|Activity|UIViewController|NSURL|PendingIntent)\b",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    for path in args.root.rglob("*"):
        if not path.is_file() or path.suffix not in {".kt", ".kts"}:
            continue
        if any(part in {".git", ".gradle", "build"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "commonMain" in path.parts:
            for match in PLATFORM_IMPORT.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path}:{line}: platform import in commonMain")
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text):
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path}:{line}: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
