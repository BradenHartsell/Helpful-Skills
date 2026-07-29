#!/usr/bin/env python3
"""Advisory scanner for Compose runtime and navigation risks."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "coroutine launch in composable body": r"@Composable[\s\S]{0,1200}?\b(?:scope\.)?launch\s*\{",
    "constant-key effect, inspect captures": r"LaunchedEffect\s*\(\s*(?:Unit|true)\s*\)",
    "listener effect needs cleanup": r"@Composable[\s\S]{0,800}?(?:addListener|registerReceiver|addObserver)\s*\(",
    "large or nontrivial rememberSaveable value": r"rememberSaveable\s*\{",
    "mutable collection as state": r"mutableStateOf\s*\(\s*(?:mutableListOf|arrayListOf|hashMapOf|mutableMapOf)",
    "index item key risk": r"key\s*=\s*\{\s*(?:index|it)\s*\}",
    "Navigation 2 API": r"\bNavController\b|\bNavHost\s*\(",
    "Navigation 3 API": r"\bNavDisplay\s*\(|\bNavEntry\b|androidx\.navigation3",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    for path in args.root.rglob("*.kt"):
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
