# Version V1.1

**Product / Model:** שחר הפקות AI · V1.1  
**Date:** 2026-08-19

## What's in this release
- Russian locale for the whole site (home, search, lessons, glossary)
- Language switcher: עברית / English / العربية / हिन्दी / Русский
- Model name **שחר הפקות AI · V1.1** on titles, meta, quizzes, and inner pages
- Version bump V1.0 → V1.1

## Technical changes
| File | Change |
|------|--------|
| `index-ru.html`, `search-ru.html`, `pages/*-ru.html`, `ru/index.html` | New Russian pages |
| `style.css` / `script.js` | Roboto + LTR for `lang=ru`; quiz/search Russian |
| `.github/workflows/pages.yml` | Publish `*-ru.html` and `/ru/` |
| All HTML | `data-version`, titles, `application-name`, `data-model` → V1.1 |
