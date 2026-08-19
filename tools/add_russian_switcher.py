# -*- coding: utf-8 -*-
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
pat = re.compile(r'(<nav class="lang-switcher"[^>]*>)(.*?)(</nav>)', re.DOTALL)
updated = 0
for p in root.rglob("*.html"):
    if ".git" in p.parts:
        continue
    if p.name.endswith("-ru.html") or p.parent.name == "ru":
        continue
    text = p.read_text(encoding="utf-8")
    if 'hreflang="ru"' in text or ">Русский<" in text:
        continue
    if "lang-switcher" not in text:
        continue
    stem = p.name[:-5]
    for suf in ("-en", "-ar", "-hi"):
        if stem.endswith(suf):
            stem = stem[: -len(suf)]
            break
    href = stem + "-ru.html"
    extra = '                <a href="%s" hreflang="ru" lang="ru">Русский</a>\n            ' % href

    def repl(m):
        inner = m.group(2).rstrip() + "\n"
        return m.group(1) + inner + extra + m.group(3)

    new, n = pat.subn(repl, text, count=1)
    if n:
        p.write_text(new, encoding="utf-8")
        updated += 1
        print(p.relative_to(root))
print("updated", updated)
