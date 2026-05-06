# gpt-image-gen Skill

## Overview
`gpt-image-gen` הוא הסקיל היחיד בפרויקט שעוטף את OpenAI Images API (`POST /v1/images/generations`, מודל `gpt-image-2`). מוגדר ב-`.claude/skills/gpt-image-gen/SKILL.md` עם YAML frontmatter (`name`, `description`). הסקיל מקבל `PROMPT`, `OUTPUT`, ואופציונלית `SIZE` / `QUALITY`, מבצע את הקריאה (bash+jq או Python fallback ל-Git Bash), מפענח base64, וכותב PNG ל-disk. דורש `OPENAI_API_KEY` ב-`.env`. כל יצירת תמונה בפרויקט חייבת לעבור דרכו — סוכנים לא קוראים ל-API ישירות.

## Open Questions
- האם להוסיף retry אוטומטי על 429 (rate limit), או להשאיר את ההחלטה לסוכן הקורא? (כרגע: אין retry.)
- האם לתמוך גם ב-`gpt-image-1` כ-fallback אם `gpt-image-2` לא זמין באזור?
- האם לאפשר `quality=high` כברירת מחדל לסוכן `forlan` לפי סוג הבקשה (hero shot vs thumbnail)?
- jq לא מותקן ב-Git Bash על חלק מהמכונות — האם להפוך את ה-Python fallback לדרך הראשית?

## Session Log

### 2026-05-06 — Skill created [shipped]
- **What was done:** יצירת `.claude/skills/gpt-image-gen/SKILL.md` עם frontmatter, שתי דרכי הפעלה (bash+jq ו-Python urllib fallback), הוראות `set -a; source .env`, סעיף verification (`test -s`), וטיפול בשגיאות (401, חוסר `data`, 429). הוספת `OPENAI_API_KEY` ל-`.env.example` (ה-`.env` עצמו כבר הכיל את המפתח).
- **Decisions:**
  - **שני נתיבי הפעלה.** jq לא תמיד זמין ב-Git Bash על Windows → Python urllib fallback ללא תלויות חיצוניות הוא תמיד עובד.
  - **אין retry פנימי.** הסקיל פשוט; ההחלטה אם לרגנר נשארת לסוכן הקורא (forlan).
  - **מודל `gpt-image-2`** כברירת מחדל לפי בקשת המשתמש.
  - **Verification חובה** — `test -s` לפני שמדווחים הצלחה. כך לא מקבלים PNG ריק כתוצאה של שגיאת API.
- **Notes / Caveats:** הסקיל לא מטפל ב-rate-limits. אסור להחזיר את `OPENAI_API_KEY` בדיווח/log — מצוין מפורשות בסקיל.
- **Related:** [[forlan-creative-agent]], [[claude-folder-structure]], [[root-config-files]]
