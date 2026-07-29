#!/usr/bin/env python3
"""Advisory scanner for stale or unsafe Kotlin analysis tooling."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "K1 BindingContext API": r"\bBindingContext\b",
    "K1 descriptor API": r"\b(?:DeclarationDescriptor|FunctionDescriptor|ClassDescriptor)\b",
    "compiler internals dependency": r"org\.jetbrains\.kotlin\.(?:fir|resolve|descriptors|backend)",
    "Analysis API symbol storage, inspect lifetime": r"(?:val|var)\s+\w+\s*:\s*Ka(?:Symbol|Type|Session)",
    "catch-all KSP configuration": r"(?m)^\s*ksp\s*\(",
    "automatic deletion from unused finding": r"(?:delete|remove).*unused|unused.*(?:delete|remove)",
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
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text, re.IGNORECASE):
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path}:{line}: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
