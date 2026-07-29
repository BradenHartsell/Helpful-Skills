#!/usr/bin/env python3
"""Advisory scanner for serialization and wire-contract risks."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "JSON option requires protocol review": r"\b(?:encodeDefaults|explicitNulls|ignoreUnknownKeys|coerceInputValues|classDiscriminator)\s*=",
    "old kotlinx.datetime time type": r"\bkotlinx\.datetime\.(?:Instant|Clock)\b",
    "floating-point field, inspect precision": r"(?m)\b(?:price|amount|money|balance|identifier|id)\w*\s*:\s*(?:Double|Float)\b",
    "numeric identifier, inspect TypeScript precision": r"(?m)\b\w*[Ii]d\s*:\s*(?:Long|ULong)\b",
    "enum ordinal serialization risk": r"\.ordinal\b",
    "manual JSON parsing": r"JSONObject|JsonObject\s*\(|parseToJsonElement",
    "serializable class, verify boundary ownership": r"@Serializable",
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
