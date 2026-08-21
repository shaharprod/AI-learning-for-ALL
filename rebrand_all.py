# -*- coding: utf-8 -*-
"""Rebrand COMBE fork to AI-learning-for-ALL / V0.1."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SKIP_DIRS = {".git", "node_modules", "‏‏בסיס קוורק ב"}
SKIP_FILES = {"rebrand_all.py", "rebrand_combe.py"}
EXTENSIONS = {".html", ".md", ".py", ".js", ".txt", ".json", ".yml", ".yaml"}

REPLACEMENTS = [
    # Dedication (longest / most specific first)
    ("נבנה עבור: COMBE", "נבנה עבור כל מי שרוצה ללמוד"),
    ("Built for: COMBE", "Built for anyone who wants to learn"),
    ("بُني لـ: COMBE", "بُني لكل من يريد أن يتعلم"),
    ("के लिए निर्मित: COMBE", "हर किसी के लिए जो सीखना चाहता है"),
    ("Создано для: COMBE", "Создано для всех, кто хочет учиться"),
    ("Built for COMBE.", "Built for anyone who wants to learn."),
    ("<h2>4. COMBE</h2>\n<p>האתר נבנה עבור COMBE. שמות וסימנים של COMBE נשארים בבעלותם.</p>",
     "<h2>4. למי מיועד האתר</h2>\n<p>האתר נבנה עבור כל מי שרוצה ללמוד.</p>"),
    ("<h2>4. COMBE</h2>\n<p>The site was built for COMBE. COMBE names and marks remain theirs.</p>",
     "<h2>4. Who this site is for</h2>\n<p>The site was built for anyone who wants to learn.</p>"),
    ("<h2>3. COMBE والقانون</h2>\n<p>بُني الموقع لـ COMBE.",
     "<h2>3. القانون</h2>\n<p>بُني الموقع لكل من يريد أن يتعلم."),
    ("<h2>3. COMBE</h2>\n<p>साइट COMBE के लिए बनी है।",
     "<h2>3. यह साइट किसके लिए है</h2>\n<p>साइट हर किसी के लिए बनी है जो सीखना चाहता है।"),
    ("<h2>3. COMBE и право</h2>\n<p>Сайт создан для COMBE.",
     "<h2>3. Право</h2>\n<p>Сайт создан для всех, кто хочет учиться."),
    ("האתר נבנה עבור COMBE.", "האתר נבנה עבור כל מי שרוצה ללמוד."),
    ("COMBE के लिए निर्मित।", "हर किसी के लिए जो सीखना चाहता है।"),
    ("بُني لـ COMBE.", "بُني لكل من يريد أن يتعلم."),
    ("Создано для COMBE.", "Создано для всех, кто хочет учиться."),
    # Logo / site name
    ("<span class=\"logo-text\">לימוד בינה מלאכותית AI</span>",
     "<span class=\"logo-text\">AI-learning-for-ALL</span>"),
    ("<span class=\"logo-text\">AI Learning</span>",
     "<span class=\"logo-text\">AI-learning-for-ALL</span>"),
    ("<span class=\"logo-text\">تعلّم الذكاء الاصطناعي</span>",
     "<span class=\"logo-text\">AI-learning-for-ALL</span>"),
    ("<span class=\"logo-text\">एआई सीखना</span>",
     "<span class=\"logo-text\">AI-learning-for-ALL</span>"),
    ("<span class=\"logo-text\">Обучение ИИ</span>",
     "<span class=\"logo-text\">AI-learning-for-ALL</span>"),
    ('"logo": "לימוד בינה מלאכותית AI"', '"logo": "AI-learning-for-ALL"'),
    ('"logo": "AI Learning"', '"logo": "AI-learning-for-ALL"'),
    ('"logo": "تعلّم الذكاء الاصطناعي"', '"logo": "AI-learning-for-ALL"'),
    ('"logo": "एआई सीखना"', '"logo": "AI-learning-for-ALL"'),
    ('"logo": "Обучение ИИ"', '"logo": "AI-learning-for-ALL"'),
    ("אתר ללימוד בינה מלאכותית AI", "AI-learning-for-ALL"),
    # Title site-name fragments (keep lesson titles)
    (" | AI Learning ·", " | AI-learning-for-ALL ·"),
    (" | تعلّم الذكاء الاصطناعي ·", " | AI-learning-for-ALL ·"),
    (" | एआई सीखना ·", " | AI-learning-for-ALL ·"),
    (" | Обучение ИИ ·", " | AI-learning-for-ALL ·"),
    ("«AI Learning»", "«AI-learning-for-ALL»"),
    # Repo / URLs
    ("AI-learning-for-COMBE", "AI-learning-for-ALL"),
    # Version bump for this fork
    ("V1.2", "V0.1"),
]


def main():
    count = 0
    leftover = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        if path.name in SKIP_FILES:
            continue
        if path.name.startswith("VERSION-V1") or path.name.startswith("VERSION-B"):
            continue
        if path.name.startswith("apply_v1") or path.name.startswith("apply_b"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8", newline="\n")
            count += 1
            print(path.relative_to(ROOT))
        if "COMBE" in text and path.name not in {"rebrand_combe.py"}:
            leftover.append(str(path.relative_to(ROOT)))
    print("Updated %s files" % count)
    print("Leftover COMBE in:")
    for p in leftover:
        print(" ", p)


if __name__ == "__main__":
    main()
