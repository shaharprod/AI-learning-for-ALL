import re
from pathlib import Path
html = Path("pages/glossary-en.html").read_text(encoding="utf-8")
for m in re.finditer(r'<h3 id="[^"]+">([^<]+)</h3>\s*<p>([^<]+)</p>', html):
    print(repr(m.group(1)))
    print(repr(m.group(2)[:80]))
    print("---")
