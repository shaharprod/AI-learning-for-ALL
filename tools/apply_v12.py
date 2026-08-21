# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_NAMES = {
    "VERSION-V1.0.md", "VERSION-V1.1.md",
    "VERSION-B0.15.md", "VERSION-B0.14.md", "VERSION-B0.13.md", "VERSION-B0.12.md",
}
SKIP_PARTS = {".git", ".snapshots"}
SUFFIXES = {".html", ".js", ".md", ".css", ".yml"}


def main():
    n = 0
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.name in SKIP_NAMES:
            continue
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        if p.suffix.lower() not in SUFFIXES:
            continue
        text = p.read_text(encoding="utf-8")
        if "V1.1" not in text:
            continue
        p.write_text(text.replace("V1.1", "V1.2"), encoding="utf-8")
        n += 1
        print(p.relative_to(ROOT))
    print("updated", n)


if __name__ == "__main__":
    main()
