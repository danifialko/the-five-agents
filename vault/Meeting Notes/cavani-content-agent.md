# Cavani — Content Writer Agent

## Overview
**cavani** (קבי) הוא הסוכן השלישי בצוות — content writer/rewriter. LLM-only: tools allowlist `Read, Write, Edit, Glob, Grep` (אכוף ב-frontmatter — אין Bash, WebSearch, או API). הוא מושך מאמרי גלם מ-`Content/`, קורא את `cavani/style-guide.md` (חובה — נכשל בלי) ואת `cavani/reference/`, משכתב בסגנון הבית, ושומר ל-`Output/<name>.md`. כשהוא מזהה צורך בתמונה הוא לא יוצר אותה — מכניס `{{IMAGE_NEEDED: "<desc>"}}` placeholder, ו-Enzo דואג ל-substitution דרך forlan (פרוטוקול מתועד ב-`.claude/agents/enzo.md`). מבנה היברידי: `.claude/agents/cavani.md` (canonical, flat) + `cavani/` workspace בשורש (`style-guide.md`, `reference/`, `agent.md`).

## Open Questions
- מי כותב את `cavani/style-guide.md` הראשון? המשתמש אמר "אצור בנפרד" — עד אז cavani יחזיר hard-fail.
- `model: sonnet` מספיק לשכתוב, או נצטרך `opus` עבור מאמרים טכניים/ארוכים?
- האם cavani צריך לזכור החלטות סגנון מ-rewrite-ים קודמים? כרגע: לא — כל ריצה עצמאית, קורא את ה-guide מחדש.
- כמה placeholders מקסימום למאמר ארוך? לא מוגדר; מסומן רק כ"רק כשבאמת תורם".
- כיצד להתמודד עם מאמר שדורש מידע חיצוני שאין במקור? cavani חסום מ-WebSearch — Enzo צריך לאסוף מראש ולהזין ל-`Content/`.

## Session Log

### 2026-05-06 — Cavani defined [shipped]
- **What was done:** יצירת `.claude/agents/cavani.md` עם frontmatter שכולל **tools allowlist מפורש** (`Read, Write, Edit, Glob, Grep`, `model: sonnet`) ובody מלא בעברית בלשון זכר. יצירת `cavani/{agent.md, reference/.gitkeep}` ותיקיות שורש `Content/`, `Content/Ready/`, `Output/` עם `.gitkeep`. עדכון `.claude/agents/enzo.md` — הוספת cavani לרשימת ה-Sub-Agents עם trigger keywords דו-לשוניים, וסקציה חדשה "Protocol: post-cavani image substitution" (Grep ל-IMAGE_NEEDED → dispatch forlan לכל אחד → Edit להחלפה ב-`![alt](../forlan/outputs/...)` → `mv` המקור ל-Ready/). עדכון `CLAUDE.md` (Repository Layout + Agents + Status). תיעוד ב-vault.
- **Decisions:**
  - **Tools allowlist נאכף ב-frontmatter** — לא רק בהוראה למודל. אם cavani ינסה Bash/WebSearch, ה-harness עצמו יחסום.
  - **Hard fail על style-guide חסר.** סוכן סגנון בלי עוגן = המצאות. עדיף לעצור ולחייב את המשתמש ליצור.
  - **המקור עובר ע"י Enzo, לא cavani.** ל-cavani אין Bash; הימנעות מ-tombstones מלאכותיים שומרת איזולציה נקייה. נקודת אינטגרציה ב-Enzo כבר קיימת (image substitution) — מקום טבעי ל-`mv`.
  - **`model: sonnet`** — שכתוב לא דורש את היכולת המקסימלית; opus שמור ל-Enzo.
  - **`{{IMAGE_NEEDED: "<desc>"}}`** — placeholder באנגלית, על שורה משלו, כדי שיהיה קל ל-Grep.
  - **Trigger keywords דו-לשוניים** ב-description (HE + EN).
- **Notes / Caveats:** `cavani/style-guide.md` עדיין לא קיים — המשתמש מתכוון להוסיפו בנפרד. עד אז cavani יחזיר `BLOCKED: Missing or empty cavani/style-guide.md` על כל בקשת שכתוב. גם `cavani/reference/` ריקה — האפקט: שכתוב יסתמך רק על ה-guide.
- **Related:** [[forlan-creative-agent]], [[gpt-image-gen-skill]], [[enzo-ceo-agent]], [[claude-folder-structure]]
