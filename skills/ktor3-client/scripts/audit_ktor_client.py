#!/usr/bin/env python3
"""Advisory scanner for Ktor client risks."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "HttpClient construction, prove owner and reuse": r"\bHttpClient\s*\(",
    "manual URL string construction": r"https?://[^\"']*\$|URLEncoder|encodeURL",
    "unbounded reconnect loop": r"while\s*\(\s*true\s*\)",
    "manual retry loop": r"repeat\s*\([^)]*\).*?request|retryWhen",
    "timeout wrapper, compare with HttpTimeout": r"\bwithTimeout(?:OrNull)?\s*\(",
    "legacy Ktor 2 I/O surface": r"\bByteReadChannel\b|\bByteWriteChannel\b|response\.content\b",
    "GlobalScope networking": r"\bGlobalScope\b",
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
            for match in re.finditer(pattern, text, re.DOTALL):
                line = text.count("\n", 0, match.start()) + 1
                print(f"{path}:{line}: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
