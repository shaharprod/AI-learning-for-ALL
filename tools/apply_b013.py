# -*- coding: utf-8 -*-
"""Apply B0.13 + per-language dedication line across all HTML pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OLD_VER = "B0.12"
NEW_VER = "B0.13"

DEDICATION = {
    "he": "נבנה עבור: COMBE",
    "en": "Built for: COMBE",
    "ar": "بُني لـ: COMBE",
    "hi": "के लिए निर्मित: COMBE",
}

DEDICATION_BLOCK = '''                        <span class="logo-dedication">{text}</span>'''


def detect_lang(path: Path, content: str) -> str:
    name = path.name.lower()
    if name.endswith("-en.html") or path.parent.name == "en":
        return "en"
    if name.endswith("-ar.html") or path.parent.name == "ar":
        return "ar"
    if name.endswith("-hi.html") or path.parent.name == "hi":
        return "hi"
    m = re.search(r'<html[^>]*\slang="([a-z]{2})"', content, re.I)
    if m:
        code = m.group(1).lower()
        if code in DEDICATION:
            return code
    return "he"


def update_html(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    orig = content
    lang = detect_lang(path, content)
    ded = DEDICATION[lang]

    content = content.replace(OLD_VER, NEW_VER)

    # Remove old dedication lines (any language) to allow re-run
    content = re.sub(
        r'\s*<span class="logo-dedication">[^<]*</span>\s*',
        "\n",
        content,
    )

    # Insert dedication after logo-byline
    if 'class="logo-dedication"' not in content and 'class="logo-byline"' in content:
        block = DEDICATION_BLOCK.format(text=ded)
        content = content.replace(
            'class="logo-byline">',
            'class="logo-byline">',
            1,
        )
        content = re.sub(
            r'(<span class="logo-byline">[^<]*</span>)',
            r"\1\n" + block,
            content,
            count=1,
        )

    # Title: append dedication once
    def _title_repl(m):
        t = m.group(1)
        if ded in t:
            return m.group(0)
        return f"<title>{t} · {ded}</title>"

    content = re.sub(r"<title>([^<]*)</title>", _title_repl, content, count=1)

    # Footer site-version
    footer_pat = r'<p class="site-version"[^>]*>[^<]*</p>'
    new_footer = f'<p class="site-version" aria-label="version">{NEW_VER} · שחר הפקות AI · {ded}</p>'
    if re.search(footer_pat, content):
        content = re.sub(footer_pat, new_footer, content)
    elif 'class="footer"' in content and "site-version" not in content:
        content = content.replace(
            '<footer class="footer">\n        <div class="container">',
            f'<footer class="footer">\n        <div class="container">\n            {new_footer}',
            1,
        )

    if content != orig:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    updated = []
    for html in ROOT.rglob("*.html"):
        if "בסיס קוורק" in str(html):
            continue
        if update_html(html):
            updated.append(html.relative_to(ROOT))
    print(f"Updated {len(updated)} HTML files")
    for p in updated[:5]:
        print(" ", p)
    if len(updated) > 5:
        print(f"  ... and {len(updated) - 5} more")


if __name__ == "__main__":
    main()
