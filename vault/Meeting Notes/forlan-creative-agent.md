# Forlan — Creative Agent

## Overview
**forlan** (פורלאן) הוא סוכן הקריאייטיב של הפרויקט — אחראי על כל יצירת תמונה ועל **עקביות ויזואלית** בין כל התמונות שמיוצרות. מבנה היברידי: הסוכן הקנוני יושב ב-`.claude/agents/forlan.md` (Claude Code סורק רק קבצים flat ב-`agents/`), ולצידו תיקיית workspace `forlan/` בשורש הפרויקט עם `reference/` (תמונות השראה — input), `outputs/` (תוצרים — `.png` + sibling `.txt` עם הפרומפט), ושני pointer-docs (`agent.md`, `skill.md`) לבני אדם בלבד. ה-workflow: סריקת `reference/` → חילוץ סגנון/פלטה/קומפוזיציה → ניסוח prompt באנגלית שמשלב בקשת המשתמש + סגנון → קריאה ל-skill `gpt-image-gen` → שמירת `.txt` sibling → אימות `size > 0` → דיווח. `model: sonnet`. נקרא ע"י Enzo דרך trigger keywords בעברית ובאנגלית.

## Open Questions
- איך לטפל ב-`reference/` עם תמונות בסגנונות סותרים? (לבחור דומיננטי? לשאול את המשתמש? לקבץ?)
- מה הסף לקבוע "התמונה תואמת לרפרנס"? כרגע נתון לשיקול הסוכן — האם להוסיף checklist מבני?
- האם פורלאן צריך לדעת לערוך תמונה קיימת (variations / edits) או רק לייצר חדשות?
- `model: sonnet` מספיק או שיצירת prompt מסגנון ויזואלי דורשת `opus`?

## Session Log

### 2026-05-06 — Forlan defined [shipped]
- **What was done:** יצירת `.claude/agents/forlan.md` (frontmatter + workflow מלא בעברית), תיקיית workspace `forlan/{reference,outputs}/` עם `.gitkeep`, pointer-docs `forlan/agent.md` + `forlan/skill.md` לבני אדם. עדכון `.claude/agents/enzo.md` עם סקציית "Sub-Agents Under Your Command" שמכילה את forlan + trigger keywords. עדכון `CLAUDE.md` (Agents + Skills + Status). תיעוד ב-vault.
- **Decisions:**
  - **מבנה היברידי.** הסוכן ב-`.claude/agents/forlan.md` (אילוץ של Claude Code) + workspace ב-`forlan/`. הפרדה ברורה: הגדרה vs נכסים.
  - **`model: sonnet`** ולא opus — ניסוח prompt לא דורש את היכולת המקסימלית; שמורים את opus ל-Enzo.
  - **תמיד דרך הסקיל.** הסוכן לא קורא ל-curl ישירות — הסקיל הוא ה-API surface היחיד.
  - **`.txt` sibling חובה.** כל `.png` מלווה בפרומפט המלא ששימש — קריטי לאיטרציה.
  - **שמות קבצים `<YYYY-MM-DD>-<slug>.png`** — sortable, קריא, חסין-conflict.
  - **Trigger keywords דו-לשוניים** ב-`description` של frontmatter כדי ש-Enzo (וגם ניתוב אוטומטי של Claude Code) יזהו את הסוכן הנכון לבקשה בעברית או באנגלית.
- **Notes / Caveats:** `reference/` ריקה כרגע — הסוכן יציין זאת בדיווח. עקביות תיווצר רק כשייכנסו תמונות.
- **Related:** [[gpt-image-gen-skill]], [[enzo-ceo-agent]], [[claude-folder-structure]]

### 2026-05-06 — Identity-preserving generation via /edits [shipped]
- **What was done:** ריצה שנייה: בקשה לתמונה פוטוריאליסטית של "Danie" (קובץ `forlan/reference/danie.jpg`, דיוקן צבעוני) משולב עם שור אמיתי. במקום `/generations` (שלא מקבל reference), הסוכן עבר ל-`/v1/images/edits` עם `image[]=@danie.jpg`. זהות הפנים נשמרה. תוצר: `forlan/outputs/2026-05-06-danie-with-bull.png` (1.6 MB). פרומפט נשמר ב-sibling `.txt`. עודכן ה-workflow של forlan עם החלטת בחירת endpoint (`/edits` כש-reference דורש שימור זהות, `/generations` אחרת).
- **Decisions:**
  - **`/edits` עם `gpt-image-1`** — `gpt-image-2` כרגע generations-only; ה-edits endpoint דורש את הגרסה הקודמת. ההפרש ב-quality מינורי לסוג הבקשה.
  - **multipart דרך curl** — PS 5.1 אין לו `-Form`; curl + multipart הוא הדרך הקלה. ה-JSON response נכתב לקובץ זמני ומפוענח ב-PowerShell.
  - **`-F "prompt=<file"`** — קריאת prompt מקובץ מנטרלת בעיות quoting עם newlines/quotes/punctuation.
- **Notes / Caveats:** הזהות נשמרת היטב כשהרפרנס הוא דיוקן ברור עם תאורה טובה. רפרנסים מוטים/חתוכים יתנו תוצאות פחות אמינות.
- **Related:** [[gpt-image-gen-skill]]
