# Version B0.15

**Product / Model:** שחר הפקות AI · B0.15  
**Date:** 2026-08-19

## What's in this release
- Fix fixed header overlapping page content (breadcrumb, h1, search title) on all languages
- Dynamic `--header-offset` CSS variable measured from header height in `script.js`
- Version bump B0.14 → B0.15

## Technical changes
| File | Change |
|------|--------|
| `style.css` | `--header-offset`, `.search-page`, hero padding, `scroll-padding-top` |
| `pages/article.css` | Article padding uses `--header-offset`; removed 44px mobile bug |
| `script.js` | `setHeaderOffset()` on load/resize/fonts/menu toggle |
