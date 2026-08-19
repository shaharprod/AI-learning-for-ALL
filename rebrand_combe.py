# -*- coding: utf-8 -*-
"""Replace Soho House dedication with COMBE across all project files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REPLACEMENTS = [
    ("נבנה עבור: טל שחר מי - רון", "נבנה עבור: COMBE"),
    ("Built for: Tal Shahar Mei - Ron", "Built for: COMBE"),
    ("بُني لـ: تل شحر مي - رون", "بُني لـ: COMBE"),
    ("के लिए निर्मित: तल शहर मी - रोन", "के लिए निर्मित: COMBE"),
]

SKIP_DIRS = {".git", "בסיס קוורק ב"}
EXTENSIONS = {".html", ".md", ".py", ".js", ".txt", ".json"}


def main():
    count = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if path.name == "rebrand_combe.py":
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            count += 1
            print(path.relative_to(ROOT))
    print(f"Updated {count} files")


if __name__ == "__main__":
    main()
