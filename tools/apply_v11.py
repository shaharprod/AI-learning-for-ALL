# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_NAMES = {"VERSION-V1.0.md", "VERSION-B0.15.md", "VERSION-B0.14.md", "VERSION-B0.13.md", "VERSION-B0.12.md"}
SKIP_PARTS = {".git", ".snapshots"}
SUFFIXES = {".html", ".js", ".md", ".css", ".yml"}


def main():
    updated = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        if p.name in SKIP_NAMES:
            continue
        if p.suffix.lower() not in SUFFIXES:
            continue
        text = p.read_text(encoding="utf-8")
        if "V1.0" not in text:
            continue
        p.write_text(text.replace("V1.0", "V1.1"), encoding="utf-8")
        updated.append(p.relative_to(ROOT))
    print("Updated %d files" % len(updated))
    for rel in updated:
        print(rel)


if __name__ == "__main__":
    main()
