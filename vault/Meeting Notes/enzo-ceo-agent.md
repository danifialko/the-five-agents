# Enzo — CEO Agent

## Overview
**Enzo** הוא הסוכן הראשי של הפרויקט — CEO + Orchestrator + Decision Maker + Quality Controller. הוא נקודת הכניסה לכל משימה: מקבל טקסט חופשי, קורא את `CLAUDE.md`, מפרק למשימות־משנה, בוחר ומפעיל סוכנים מתמחים, מבקר את התוצרים שלהם, ומאשר רק תוצאה סופית איכותית. מוגדר ב-`.claude/agents/enzo.md` כ-Claude Code subagent עם YAML frontmatter (`name: enzo`, `model: opus`, ללא `tools` allowlist — מקבל את כל הכלים). הסוכנים המתמחים שתחתיו טרם הוגדרו.

## Open Questions
- אילו סוכנים מתמחים יעבדו תחת Enzo? (research, writer, editor, designer, publisher? — TBD).
- האם `model: opus` הבחירה הנכונה לטווח הארוך, או שעדיף `sonnet` משיקולי עלות אחרי שנראה התנהגות בפועל?
- האם Enzo יזדקק ל-`tools` allowlist מפורש בעתיד, או שהגישה המלאה הכרחית לתפקיד?
- ה-Operating Loop שלו דורש לקרוא את `CLAUDE.md` לפני כל החלטה משמעותית — איך זה יתנהג כש-`CLAUDE.md` יגדל ויהיה כבד? (אולי יידרש פיצול לקבצים נושאיים).

## File reference

### `.claude/agents/enzo.md`
- **What it does:** מגדיר את Enzo כ-Claude Code subagent. YAML frontmatter (`name`, `description`, `model: opus`) + system prompt מלא בעברית.
- **Sections in body:** Role, Operating Loop (9 שלבים), Decision Rules, Quality Control Checklist, Constraints & Guardrails, Personality, Autonomy Level: 5, Proactive Behavior, Output Format.
- **Owner:** project (us).
- **Tracked in git:** yes.

## Session Log

### 2026-05-06 — Enzo defined [shipped]
- **What was done:** יצירת `.claude/agents/enzo.md` עם frontmatter תקין (`name: enzo`, `model: opus`) וגוף מלא בעברית בהתבסס על ה-PRD ועל `agent.md` שהמשתמש סיפק. עדכון `CLAUDE.md` עם סקציית "Agents" ועם status חדש. תיעוד ב-vault.
- **Decisions:**
  - **Model = opus.** ה-PRD מדגיש איכות לפני מהירות, decomposition מדויק, וביקורת איכות קפדנית — התפקיד מצדיק את המודל החזק ביותר.
  - **אין `tools` allowlist.** Enzo צריך את כל הכלים — Read/Glob/Grep להקשר, Task לסוכנים, Edit/Write לאינטגרציה, Bash ל-CLI, TodoWrite לתזמור. allowlist יחתוך לו רגליים.
  - **שפה: עברית** — תואם ל-CLAUDE.md ולשפה שבה המשתמש מנהל את הפרויקט.
  - **`description` בגוף שלישי, "Use when…"** — כדי ש-Claude Code ינתב משימות אליו אוטומטית כשהן מתאימות.
- **Notes / Caveats:** הסוכנים המתמחים טרם קיימים. עד שיוגדרו, Enzo יזהה זאת בריצה ויסמן אותה כ-blocker במקום לבצע עבודה ללא צוות.
- **Related:** [[claude-folder-structure]], [[root-config-files]], [[anthropic-skills-catalog]]

### 2026-05-06 — forlan registered under Enzo [shipped]
- **What was done:** הוספת סקציית "Sub-Agents Under Your Command" ל-`.claude/agents/enzo.md`, עם forlan כסוכן הראשון, trigger keywords בעברית ובאנגלית, ו-definition-of-done. עדכון `CLAUDE.md` (Agents + Skills + Status) כך שכולל גם את forlan ואת הסקיל `gpt-image-gen`.
- **Decisions:** הסקציה ממוקמת אחרי "Role" ולפני "Operating Loop" — Enzo קורא אותה בשלב 5 ("בחירת סוכנים") של ה-loop. גם הוספה הנחיה: אם אין סוכן מתאים — לא מאלתרים.
- **Notes / Caveats:** Open Question לגבי `model: opus` עדיין פתוח. סוכן `forlan` מוגדר כ-`sonnet`.
- **Related:** [[forlan-creative-agent]], [[gpt-image-gen-skill]]

### 2026-05-06 — cavani registered + image-substitution protocol [shipped]
- **What was done:** הוספת cavani לרשימת ה-Sub-Agents ב-`.claude/agents/enzo.md` עם trigger keywords דו-לשוניים, I/O contract, ואיסור על מגע ב-`Content/Ready/`. הוספת סקציה חדשה "Protocol: post-cavani image substitution" עם 5 צעדים מפורשים: Read קובץ output, Grep ל-`{{IMAGE_NEEDED:`, dispatch forlan עם desc, Edit להחלפה ב-`![alt](../forlan/outputs/...)`, `mv` המקור ל-Ready/, append ל-vault, אישור למשתמש. עדכון Status ב-CLAUDE.md.
- **Decisions:**
  - **Enzo אחראי ל-substitution** ולא cavani — cavani הוא LLM-only ואין לו דרך לקרוא ל-API.
  - **Enzo אחראי ל-`mv`** — cavani אין לו Bash; ה-flow של החלפת תמונות הוא מקום טבעי לאחד את שני השלבים (image-sub + move-source).
  - **כשל-forlan ספציפי** משאיר את ה-placeholder ולא עוצר — המאמר עדיין שמיש, וניתן לרגנר לפי בקשת המשתמש.
  - **relative path** `../forlan/outputs/<file>.png` ב-markdown image — מ-`Output/` זו הדרך לציין path נכון.
- **Notes / Caveats:** עומס cognitive על Enzo גדל — הוא עכשיו אחראי על orchestration של שני סוכנים סדרתית (cavani→forlan) + post-processing. אם ה-pipeline יכבד, אולי כדאי skill ייעודי `image-substitution` שיעטוף את הצעדים.
- **Related:** [[cavani-content-agent]], [[forlan-creative-agent]]

### 2026-05-06 — suarez registered [shipped]
- **What was done:** הוספת suarez לרשימת ה-Sub-Agents ב-enzo.md עם trigger keywords דו-לשוניים, memory protocol note, I/O contract, ו-definition of done. עדכון CLAUDE.md (Agents + Repository Layout + Status). תיעוד ב-vault.
- **Decisions:** suarez נוסף **לפני** cavani ב-pipeline הלוגי (suarez → Content/ → cavani → Output/) אך מתועד **אחריו** בסדר ההוספה. Enzo מנתב לפי trigger keywords — אין סדר קשיח, Enzo מחליט לפי הבקשה.
- **Notes / Caveats:** pipeline מלא עכשיו: suarez (מחקר) → Content/ → cavani (שכתוב) → Output/ + IMAGE_NEEDED → Enzo (image-sub דרך forlan) → Output/ סופי → Content/Ready/. ארבעה סוכנים פעילים + skill אחד.
- **Related:** [[suarez-research-agent]], [[cavani-content-agent]]

### 2026-05-08 — first full 5-agent pipeline run (Argentina article) [shipped]
- **What was done:** הפעלה ראשונה של ה-pipeline המלא על משימת תוכן: מאמר על נבחרת ארגנטינה לקראת מונדיאל 2026 + תמונה סימבולית של מסי ב"ריקוד האחרון". סדר הביצוע: (1) שיגור suarez ו-forlan **במקביל** (background) — suarez למחקר, forlan לתמונה; (2) עם חזרת suarez, שיגור cavani עם בריף סגנוני + פויינטר ל-`Content/2026-05-08-argentina-mundial-2026.md`; (3) Enzo החליף `{{IMAGE_NEEDED}}` בתמונה של forlan + העביר את המקור ל-`Content/Ready/`; (4) שיגור valverde לסבב QA מלא (6 קטגוריות). תוצאה: ✅ APPROVED בסבב #1 + תיקון nit קטן (deadline → מועד הגשת).
- **Decisions:**
  - **suarez ו-forlan במקביל.** המחקר והתמונה אינם תלויים זה בזה — חיסכון של ~2 דקות wall-clock.
  - **Enzo כתב את ה-image alt text** במקום cavani. ה-placeholder היה באנגלית (לפי הסטייל-גייד), אבל ה-alt העברי הוא חלק מהאינטגרציה. שגיאה שעשיתי בתחילה: כללתי EM dash ב-alt — זיהיתי ותיקנתי בעצמי לפני שיגור valverde.
  - **cavani's first production run** — ה-style-guide ו-reference samples שנכתבו מוקדם הסשן עבדו. הסוכן לא נכשל ב-`BLOCKED:`, קרא את ה-anchor, חילץ את הדפוסים מהמדגם הקודם של אורוגוואי, וייצר טקסט שעבר QA נקי.
  - **suarez הזהיר במפורש מה לא לכתוב** ("מסי הצהיר רשמית"). cavani כיבד את זה. valverde אימת. שלוש שכבות הגנה.
- **Notes / Caveats:** המסגור "ריקוד אחרון" עבד יפה כי הוא קיים אובייקטיבית באקוסיסטם (Adidas "El Último Tango" + תקשורת + ציטוטי מסי) — לא היה צורך להמציא אותו. אם המסגור היה מבוסס יותר על ספקולציה, הסיכון לטעות סגנונית/עובדתית היה גבוה יותר.
- **Related:** [[suarez-research-agent]], [[cavani-content-agent]], [[forlan-creative-agent]], [[valverde-qa-agent]]

### 2026-05-08 — valverde registered + QA Loop protocol [shipped]
- **What was done:** הוספת valverde לרשימת Sub-Agents ב-enzo.md עם trigger keywords דו-לשוניים ו-auto-trigger note. הוספת סקציית "Protocol: QA Loop" עם 5-step loop logic + escalation לסבב #3 (אסקלציה למשתמש, לא ל-Enzo). עדכון Operating Loop שלב 9 כך ש-valverde חלק אינטגרלי מ"אישור סופי". עדכון CLAUDE.md (Agents + Repository Layout + Status). תיעוד ב-vault.
- **Decisions:**
  - **valverde רץ אוטומטית** — לא דורש trigger מהמשתמש. כל תוצר עובר QA לפני שחרור. זה הסוכן הראשון בפרויקט עם דפוס auto-trigger.
  - **3 סבבים תקרה.** אחרי 3 דחיות — אסקלציה למשתמש (לא ל-Enzo להחליט לבד). מונע loops אינסופיים ושומר על אחריות מפורשת.
  - **valverde לא נוגע בתוצר** — `tools: Read, Glob, Grep, Write` בלבד, בלי Edit. מכוון: אם יוכל לערוך, יתפתה לתקן ולא לדווח, ויתחיל לעקוף את cavani.
  - **לוג בכל סבב.** גם ✅ נרשם ב-`valverde/QA_Reports/`. היסטוריה מלאה לניתוח מגמות עתידי.
  - **Hard rule:** valverde הוא הסוכן היחיד שמורשה לדחות תוצר. בלי ✅ שלו (או אישור משתמש מפורש בסבב 3) — אין שחרור.
- **Notes / Caveats:** עומס נוסף על Enzo — עכשיו אחראי על loop ניהול עד 3 סבבים בין cavani ל-valverde. אם זה יכבד, יישקל skill ייעודי `qa-loop-orchestration`. valverde לא יכול לקרוא ל-cavani ישירות (Claude Code לא מאפשר sub-agent → sub-agent), ולכן כל ה-loop logic יושב ב-Enzo. ה-style-guide של cavani עדיין חסר — valverde יסמן זאת כ-⚠️ ולא יכשיל על זה לבד.
- **Related:** [[valverde-qa-agent]], [[cavani-content-agent]]
