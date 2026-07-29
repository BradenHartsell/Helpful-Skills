#!/usr/bin/env python3
"""Advisory Android platform scanner."""

import argparse
import re
from pathlib import Path

PATTERNS = {
    "Firebase KTX artifact": r"firebase-[\w-]+-ktx",
    "fixed system bar size": r"(?:statusBar|navigationBar)(?:Height|Padding)\s*=\s*\d",
    "background Service start": r"\bstartService\s*\(",
    "foreground service start requires context review": r"\bstartForegroundService\s*\(",
    "exact alarm requires policy review": r"\bsetExact(?:AndAllowWhileIdle)?\s*\(",
    "legacy back callback": r"\bonBackPressed\s*\(",
    "manifest component needs exported review": r"<(?:activity|service|receiver|provider)\b",
    "Play Billing usage needs exact-version review": r"BillingClient|com\.android\.billingclient",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    allowed = {".kt", ".kts", ".xml", ".toml", ".gradle"}
    for path in args.root.rglob("*"):
        if not path.is_file() or path.suffix not in allowed:
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
