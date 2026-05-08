# Cavani — Content Writer Agent

## Overview
**cavani** (קבי) הוא הסוכן השלישי בצוות — content writer/rewriter. LLM-only: tools allowlist `Read, Write, Edit, Glob, Grep` (אכוף ב-frontmatter — אין Bash, WebSearch, או API). הוא מושך מאמרי גלם מ-`Content/`, קורא את `cavani/style-guide.md` (חובה — נכשל בלי) ואת `cavani/reference/`, משכתב בסגנון הבית, ושומר ל-`Output/<name>.md`. כשהוא מזהה צורך בתמונה הוא לא יוצר אותה — מכניס `{{IMAGE_NEEDED: "<desc>"}}` placeholder, ו-Enzo דואג ל-substitution דרך forlan (פרוטוקול מתועד ב-`.claude/agents/enzo.md`). מבנה היברידי: `.claude/agents/cavani.md` (canonical, flat) + `cavani/` workspace בשורש (`style-guide.md`, `reference/`, `agent.md`).

## Open Questions
- `model: sonnet` מספיק לשכתוב, או נצטרך `opus` עבור מאמרים טכניים/ארוכים?
- האם cavani צריך לזכור החלטות סגנון מ-rewrite-ים קודמים? כרגע: לא — כל ריצה עצמאית, קורא את ה-guide מחדש.
- כמה placeholders מקסימום למאמר ארוך? לא מוגדר; מסומן רק כ"רק כשבאמת תורם".
- כיצד להתמודד עם מאמר שדורש מידע חיצוני שאין במקור? cavani חסום מ-WebSearch — Enzo צריך לאסוף מראש ולהזין ל-`Content/`.
- ה-style-guide הראשון מוטה לדומיין ספורט. מתי לפצל לדומיינים נוספים (עסקי, טכני, שיווקי, תרבות), ואיך — סטייל-גייד אחד עם סקציות, או קבצי `style-guide-<domain>.md` נפרדים?

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

### 2026-05-08 — cavani unblocked: style-guide + reference samples [shipped]
- **What was done:** יצירת `cavani/style-guide.md` (5 בלוקים: Voice, Hard Rules, Sentence Rhythm, Hebrew-First, Structure, +bonus image placeholder convention) שמתבסס על feedback_writing_style.md ועל המאמר על אורוגוואי שעבר 6 סבבי QA. אכלוס `cavani/reference/` ב-2 samples (`2026-05-08-uruguay-mundial-2026-hebrew-sample.md` 1,500 מילים, `2026-05-06-uruguay-world-cup-2026-english-sample.md` 600 מילים) + `README.md` שמסביר את הפרוטוקול. עדכון Status ב-`CLAUDE.md`. cavani עכשיו unblocked לבקשות עתידיות.
- **Decisions:**
  - **Bootstrap מראיה אמפירית, לא תיאוריה.** הסגנון שעובד הוא לא דמיון — הוא מאמר אמיתי שהמשתמש כיוון אותו דרך 6 סבבים. החילוץ ממנו מדויק מ-brainstorm מאפס, ומבוסס פחות על השערות שלי.
  - **דומיין יחיד (ספורט) בשלב הראשון.** אם בעתיד יידרש תוכן עסקי/טכני/שיווקי, יוסיפו רפרנסים נושאיים. לא להעמיס מראש.
  - **Hard rules אכופות ע"י valverde.** כל הקווים האדומים (EM dashes, calques, clichés, משפטים ערפיליים, סתירות לוגיות) הם קטגוריות שכבר קיימות ב-valverde — הסטייל-גייד לא מוסיף עומס QA, רק מסביר ל-cavani למה הוא נמדד.
  - **Cross-language sample כולל ניקוי EM dashes.** ה-sample האנגלי המקורי (`Output/2026-05-06-...-en.md`) הכיל EM dash אחד ב"Darwin Problem". הוסר ב-sample כדי לשמור על עקביות עם הסטייל-גייד שאוסר אותם בכל שפה.
  - **README מסביר את הפרוטוקול.** הוספת sample חדש דורשת: (א) המאמר עבר QA אצל valverde; (ב) HTML header עם metadata; (ג) שמירה על קונבנציית שמות; (ד) עדכון הטבלה ב-README; (ה) review משני של valverde.
- **Notes / Caveats:** הסטייל-גייד מוטה לכיוון ספורט-ארוך. ה-sample האנגלי קצר יותר ופחות מפורט מהעברי. אם cavani יידרש לדומיינים אחרים — צריך להוסיף samples ייעודיים. **Smoke test לא נעשה עדיין** — cavani לא הופעל על מאמר גלם אמיתי כדי לוודא שהוא קורא, מתפרשט, וכותב כצפוי. שמירה כ-Open Question לסשן הבא.
- **Related:** [[valverde-qa-agent]], [[enzo-ceo-agent]], [[suarez-research-agent]]
