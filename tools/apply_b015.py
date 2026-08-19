# -*- coding: utf-8 -*-
"""Bump version B0.14 → B0.15 across all site HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_VER = "B0.14"
NEW_VER = "B0.15"


def main():
    updated = []
    for html in ROOT.rglob("*.html"):
        if "בסיס קוורק" in str(html):
            continue
        content = html.read_text(encoding="utf-8")
        if OLD_VER not in content:
            continue
        html.write_text(content.replace(OLD_VER, NEW_VER), encoding="utf-8")
        updated.append(html.relative_to(ROOT))
    print(f"Updated {len(updated)} HTML files to {NEW_VER}")


if __name__ == "__main__":
    main()
