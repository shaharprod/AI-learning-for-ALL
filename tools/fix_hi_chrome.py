# -*- coding: utf-8 -*-
"""Apply Hindi chrome + URL fixes from EN lesson pages. Content still needs translation."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

LESSONS = [
    "machine-learning",
    "ai-daily-life",
    "ai-ethics",
    "ai-future",
    "ai-tools",
    "glossary",
    "prompt-engineering",
]

NAV_HI = """            <ul class="nav-links">
                <li><a href="../index-hi.html">होम</a></li>
                <li class="dropdown">
                    <a href="../index-hi.html#topics" class="dropdown-toggle">पाठ ▾</a>
                    <ul class="dropdown-menu">
                        <li><a href="intro-to-ai-hi.html">1. एआई का परिचय</a></li>
                        <li><a href="ai-history-hi.html">2. एआई का इतिहास</a></li>
                        <li><a href="machine-learning-hi.html">3. मशीन लर्निंग</a></li>
                        <li><a href="ai-daily-life-hi.html">4. रोज़मर्रा की ज़िंदगी में एआई</a></li>
                        <li><a href="ai-tools-hi.html">5. व्यावहारिक उपकरण</a></li>
                        <li><a href="prompt-engineering-hi.html">6. प्रॉम्प्ट इंजीनियरिंग</a></li>
                        <li><a href="ai-ethics-hi.html">7. एआई नैतिकता</a></li>
                        <li><a href="ai-future-hi.html">8. एआई का भविष्य</a></li>
                        <li><a href="glossary-hi.html">9. शब्दावली</a></li>
                    </ul>
                </li>
                <li><a href="glossary-hi.html">शब्दावली</a></li>
                <li><a href="ai-tools-hi.html">उपकरण</a></li>
                <li><a href="../index-hi.html#about">परिचय</a></li>
            </ul>
            <form class="nav-search" id="site-search" role="search">
                <input type="search" name="q" placeholder="खोजें..." aria-label="खोजें" />
                <button type="submit" aria-label="खोजें">🔍</button>
            </form>"""

HEAD_STYLE = """    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>body { direction: ltr; font-family: 'Noto Sans Devanagari', sans-serif; }</style>"""

LOGO_INNER = """                    <span class="logo-stack">
                        <span class="logo-text">एआई सीखना</span>
                        <span class="logo-byline">שחר הפקות AI · B0.14</span>
                        <span class="logo-dedication">के लिए निर्मित: COMBE</span>
                    </span>"""

DEDICATION_SUFFIX = " · के लिए निर्मित: COMBE"


def lang_switcher(slug: str) -> str:
    return f"""            <nav class="lang-switcher" aria-label="भाषा चुनें">
                <a href="{slug}.html" hreflang="he" lang="he">עברית</a>
                <a href="{slug}-en.html" hreflang="en" lang="en">English</a>
                <a href="{slug}-ar.html" hreflang="ar" lang="ar">العربية</a>
                <span class="lang-active" aria-current="page">हिन्दी</span>
            </nav>"""


def fix_chrome(content: str, slug: str) -> str:
    content = content.replace('lang="en"', 'lang="hi"')
    content = content.replace("Built for: COMBE", "के लिए निर्मित: COMBE")
    content = re.sub(r'href="../index-en\.html"', 'href="../index-hi.html"', content)
    content = re.sub(rf'href="{slug}-en\.html"', f'href="{slug}-hi.html"', content)
    content = re.sub(r'href="([a-z-]+)-en\.html"', r'href="\1-hi.html"', content)
    content = re.sub(r'<span class="lang-active" aria-current="page">English</span>', '<span class="lang-active" aria-current="page">हिन्दी</span>', content)
    content = re.sub(r'aria-label="Language"', 'aria-label="भाषा चुनें"', content)
    content = re.sub(r'aria-label="Menu"', 'aria-label="मेनू"', content)
    content = re.sub(r'alt="Logo"', 'alt="लोगो"', content)
    if "Noto Sans Devanagari" not in content:
        content = content.replace(
            '<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap" rel="stylesheet">',
            HEAD_STYLE,
        )
        content = content.replace("<style>body { direction: ltr; }</style>", "")
    content = re.sub(
        r'<span class="logo-stack">.*?</span>\s*</a>',
        LOGO_INNER + "\n                </a>",
        content,
        count=1,
        flags=re.S,
    )
    content = re.sub(
        r'<ul class="nav-links">.*?<button type="button" class="mobile-menu-btn"',
        NAV_HI + "\n            " + lang_switcher(slug) + "\n            <button type=\"button\" class=\"mobile-menu-btn\"",
        content,
        count=1,
        flags=re.S,
    )
    if DEDICATION_SUFFIX not in content.split("</title>")[0]:
        content = content.replace(" · B0.14</title>", f" · B0.14{DEDICATION_SUFFIX}</title>", 1)
    content = re.sub(
        r'<p class="site-version"[^>]*>[^<]*</p>',
        '<p class="site-version" aria-label="version">B0.14 · שחר הפקות AI · के लिए निर्मित: COMBE</p>',
        content,
    )
    return content


def main():
    for slug in LESSONS:
        en = PAGES / f"{slug}-en.html"
        hi = PAGES / f"{slug}-hi.html"
        if not en.exists():
            continue
        c = fix_chrome(en.read_text(encoding="utf-8"), slug)
        hi.write_text(c, encoding="utf-8")
        print("chrome", hi.name)


if __name__ == "__main__":
    main()
