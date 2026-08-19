# -*- coding: utf-8 -*-
"""Generate ai-tools-hi.html and glossary-hi.html from English sources."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"

FONT = '''    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>body { direction: ltr; font-family: 'Noto Sans Devanagari', sans-serif; }</style>'''

NAV = '''            <ul class="nav-links">
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
            </form>'''

FOOTER = '''            <p class="site-version" aria-label="version">B0.14 · שחר הפקות AI · के लिए निर्मित: COMBE</p>
            <p>© 2026 एआई सीखना – Sam Shahar</p>
            <p class="footer-contact">फ़ोन: <a href="tel:+972522603831">+972522603831</a> | ईमेल: <a href="mailto:shaharprod@gmail.com">shaharprod@gmail.com</a></p>'''

def shell(html, slug, title, breadcrumb):
    html = re.sub(r'<html lang="en"[^>]*>', '<html lang="hi" dir="ltr" data-version="B0.14">', html, 1)
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Heebo[^"]*" rel="stylesheet">\s*<style>body \{ direction: ltr; \}</style>',
        FONT, html, 1)
    html = html.replace('Built for: COMBE', 'के लिए निर्मित: COMBE')
    html = html.replace('../index-en.html', '../index-hi.html')
    html = re.sub(
        r'<span class="logo-text">.*?</span>\s*<span class="logo-byline">.*?</span>\s*<span class="logo-dedication">',
        '<span class="logo-text">एआई सीखना</span>\n                        <span class="logo-byline">שחר הפקות AI · B0.14</span>\n                        <span class="logo-dedication">',
        html, 1, flags=re.S)
    html = re.sub(r'<ul class="nav-links">.*?</form>', NAV, html, 1, flags=re.S)
    html = re.sub(
        r'<nav class="lang-switcher" aria-label="Language">.*?</nav>',
        f'''<nav class="lang-switcher" aria-label="भाषा चुनें">
                <a href="{slug}.html" hreflang="he" lang="he">עברית</a>
                <a href="{slug}-en.html" hreflang="en" lang="en">English</a>
                <a href="{slug}-ar.html" hreflang="ar" lang="ar">العربية</a>
                <span class="lang-active" aria-current="page">हिन्दी</span>
            </nav>''',
        html, 1, flags=re.S)
    html = html.replace('aria-label="Menu"', 'aria-label="मेनू"')
    html = html.replace('alt="Logo"', 'alt="लोगो"')
    html = re.sub(r'<title>.*?</title>',
                  f'<title>{title} | एआई सीखना · שחר הפקות AI · B0.14 · के लिए निर्मित: COMBE</title>', html, 1)
    html = re.sub(
        r'<div class="breadcrumb"><a href="../index-hi.html">Home</a> / <span>.*?</span></div>',
        f'<div class="breadcrumb"><a href="../index-hi.html">होम</a> / <span>{breadcrumb}</span></div>', html, 1)
    html = re.sub(r'<p class="site-version"[^>]*>.*?</p>\s*<p>©.*?</p>\s*<p class="footer-contact">.*?</p>', FOOTER, html, 1, flags=re.S)
    for p in ['intro-to-ai','ai-history','machine-learning','ai-daily-life','ai-tools','prompt-engineering','ai-ethics','ai-future','glossary']:
        html = html.replace(f'{p}-en.html', f'{p}-hi.html')
    return html

# Load translations from companion module
from hi_trans_data import TRANS  # noqa: E402

def apply_trans(html):
    for en, hi in sorted(TRANS.items(), key=lambda x: -len(x[0])):
        html = html.replace(en, hi)
    return html

def build(slug, title, breadcrumb):
    src = (PAGES / f"{slug}-en.html").read_text(encoding="utf-8")
    out = apply_trans(shell(src, slug, title, breadcrumb))
    (PAGES / f"{slug}-hi.html").write_text(out, encoding="utf-8")
    remaining = sum(1 for s in ['Home</a>', 'Lessons', 'Check answers', 'What is', 'Reading time'] if s in out)
    print(f"Wrote {slug}-hi.html ({len(out)} chars, {remaining} English markers left)")

if __name__ == "__main__":
    build("ai-tools", "व्यावहारिक उपकरण", "व्यावहारिक उपकरण")
    build("glossary", "शब्दावली", "शब्दावली")
