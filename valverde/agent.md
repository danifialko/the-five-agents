# valverde — Workspace

לסוכן הקנוני ראה `.claude/agents/valverde.md`.
תיקייה זו היא workspace בלבד.

## תיקיות

- `QA_Reports/` — דוחות QA היסטוריים. valverde כותב לכאן דוח לכל בדיקה (לכל מאמר, לכל סבב). הדוחות נשמרים בפורמט `<YYYY-MM-DD-HHMM>-<slug>.md`.

## תזכורת על valverde

- read-mostly: Read, Glob, Grep, Write בלבד
- לא נוגע בתוצרים (Output/) — רק קורא ושופט
- כותב רק ל-`QA_Reports/`
- מחזיר ל-Enzo: ✅ מאושר / ❌ דורש תיקון + path לדוח
- הסוכן היחיד שמורשה לדחות תוצר
