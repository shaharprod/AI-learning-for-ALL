# -*- coding: utf-8 -*-
"""Build ai-tools-hi.html and glossary-hi.html from English sources."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"

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

FOOTER_HI = """            <p class="site-version" aria-label="version">B0.14 · שחר הפקות AI · हर किसी के लिए जो सीखना चाहता है</p>
            <p>© 2026 एआई सीखना – Sam Shahar</p>
            <p class="footer-contact">फ़ोन: <a href="tel:+972522603831">+972522603831</a> | ईमेल: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>"""

HEAD_STYLE = """    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>body { direction: ltr; font-family: 'Noto Sans Devanagari', sans-serif; }</style>"""

def apply_chrome(html: str, slug: str, title_hi: str, breadcrumb_hi: str) -> str:
    html = re.sub(r'<html lang="en"[^>]*>', '<html lang="hi" dir="ltr" data-version="B0.14">', html, count=1)
    html = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Heebo[^"]*" rel="stylesheet">\s*<style>body \{ direction: ltr; \}</style>',
                  HEAD_STYLE, html, count=1)
    html = html.replace('AI Learning', 'एआई सीखना')
    html = html.replace('Built for anyone who wants to learn', 'हर किसी के लिए जो सीखना चाहता है')
    html = html.replace('../index-en.html', '../index-hi.html')
    html = html.replace(f'{slug}-en.html', f'{slug}-hi.html')
    html = re.sub(r'<span class="logo-text">.*?</span>\s*<span class="logo-byline">.*?</span>',
                  '<span class="logo-text">AI-learning-for-ALL</span>\n                        <span class="logo-byline">שחר הפקות AI · B0.14</span>',
                  html, count=1, flags=re.S)
    html = re.sub(r'<ul class="nav-links">.*?</form>', NAV_HI, html, count=1, flags=re.S)
    # lang switcher
    html = re.sub(
        rf'<nav class="lang-switcher" aria-label="Language">.*?</nav>',
        f'''<nav class="lang-switcher" aria-label="भाषा चुनें">
                <a href="{slug}.html" hreflang="he" lang="he">עברית</a>
                <a href="{slug}-en.html" hreflang="en" lang="en">English</a>
                <a href="{slug}-ar.html" hreflang="ar" lang="ar">العربية</a>
                <span class="lang-active" aria-current="page">हिन्दी</span>
            </nav>''',
        html, count=1, flags=re.S)
    html = html.replace('aria-label="Menu"', 'aria-label="मेनू"')
    html = html.replace('alt="Logo"', 'alt="लोगो"')
    html = re.sub(r'<p class="site-version"[^>]*>.*?</p>\s*<p>©.*?</p>\s*<p class="footer-contact">.*?</p>',
                  FOOTER_HI, html, count=1, flags=re.S)
    html = re.sub(r'<title>.*?</title>', f'<title>{title_hi} | AI-learning-for-ALL · שחר הפקות AI · B0.14 · हर किसी के लिए जो सीखना चाहता है</title>', html, count=1)
    html = re.sub(r'<div class="breadcrumb"><a href="../index-hi.html">Home</a> / <span>.*?</span></div>',
                  f'<div class="breadcrumb"><a href="../index-hi.html">होम</a> / <span>{breadcrumb_hi}</span></div>', html, count=1)
    return html

# Load translation pairs from external file if present, else use embedded
TRANS = {}

def load_translations():
    global TRANS
    # Embedded critical UI + content replacements for ai-tools and glossary
    pairs = open(PAGES / "_hi_translations.txt", encoding="utf-8").read().split("\n---\n")
    for block in pairs:
        if "=>" in block:
            en, hi = block.split("=>", 1)
            TRANS[en.strip()] = hi.strip()

def translate_text(html: str) -> str:
    for en, hi in sorted(TRANS.items(), key=lambda x: -len(x[0])):
        html = html.replace(en, hi)
    return html

def build(slug: str, title_hi: str, breadcrumb_hi: str):
    src = (PAGES / f"{slug}-en.html").read_text(encoding="utf-8")
    out = apply_chrome(src, slug, title_hi, breadcrumb_hi)
    out = translate_text(out)
    (PAGES / f"{slug}-hi.html").write_text(out, encoding="utf-8")
    print(f"Wrote {slug}-hi.html")

if __name__ == "__main__":
    load_translations()
    build("ai-tools", "व्यावहारिक उपकरण", "व्यावहारिक उपकरण")
    build("glossary", "शब्दावली", "शब्दावली")
    print("Done.")
