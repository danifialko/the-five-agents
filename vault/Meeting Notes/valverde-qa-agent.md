# Valverde — QA Agent

## Overview

**valverde** הוא סוכן ה-QA של הפרויקט — הסוכן ה-5 וסוגר הלולאה. read-mostly: `Read, Glob, Grep, Write` (אין Edit, אין Bash, אין API). תפקידו לקרוא תוצרים שיוצאים מ-cavani (אחרי שילוב תמונות), להריץ צ'קליסט מובנה של 5 קטגוריות (רלוונטיות לבריף, סגנון/מיתוג, שלמות מבנית, תמונות, שלמות טכנית), ולכתוב דוח ל-`valverde/QA_Reports/<YYYY-MM-DD-HHMM>-<slug>.md`. מחזיר ל-Enzo החלטה ברורה: ✅ מאושר או ❌ דורש תיקון. הסוכן היחיד שמורשה לדחות תוצר. רץ אוטומטית בסוף כל pipeline תוכן, גם בלי trigger מהמשתמש. מוגדר ב-`.claude/agents/valverde.md` עם `tools: Read, Glob, Grep, Write` ו-`model: sonnet`.

## Open Questions

- האם להוסיף מטריקה אגרגטיבית (% תוצרים שעוברים סבב #1) על בסיס היסטוריה ב-`QA_Reports/`?
- מה לעשות אם `cavani/style-guide.md` עדיין חסר — לאשר ללא בדיקת סגנון (כפי שמוגדר עכשיו ⚠️) או לדחות אוטומטית?
- האם 3 סבבים זה הסף הנכון, או שצריך לאפשר יותר במקרים מורכבים?
- האם valverde צריך לבדוק גם תמונות שנוצרו בנפרד (לא במסגרת מאמר), או רק כשהן embedded במאמר?

## File reference

### `.claude/agents/valverde.md`
- **What it does:** מגדיר את valverde כ-Claude Code subagent עם `tools: Read, Glob, Grep, Write`. YAML frontmatter (`name`, `description` דו-לשוני, `tools` allowlist, `model: sonnet`) + system prompt בעברית.
- **Sections in body:** Role, Working Directories, Workflow (8 שלבים), QA Checklist (5 קטגוריות / 17 סעיפים), פורמט דוח QA, Quality Bar, Constraints, Personality, Output Format לדיווח.
- **Owner:** project (us).
- **Tracked in git:** yes.

### `valverde/agent.md`
- **What it does:** pointer doc לבני אדם — מפנה לסוכן הקנוני ב-`.claude/agents/valverde.md` ומסביר את מבנה ה-workspace.
- **Tracked in git:** yes.

### `valverde/QA_Reports/`
- **What it does:** תיקייה לדוחות QA. valverde כותב דוח לכל בדיקה (לכל מאמר, לכל סבב). פורמט שם קובץ: `<YYYY-MM-DD-HHMM>-<slug>.md`.
- **Tracked in git:** yes (`.gitkeep`).

## Session Log

### 2026-05-08 — image QA category added (visual content) [shipped]
- **What was done:** הרחבת valverde לבדוק גם תוכן ויזואלי. עדכוני `.claude/agents/valverde.md`: (א) הוספת `forlan/outputs/` ל-Working Directories כקריאה בלבד; (ב) Workflow שלב 5 דורש Glob+Read לכל תמונה ב-markdown; (ג) קטגוריה 6 חדשה בצ'קליסט (6 סעיפים: קיום, התאמה לתיאור, שייכות לאומית/מותגית, טקסט/מספרים, לוגואים מסחריים, דמיון לאישים); (ד) Quality Bar עודכן עם פסילות אוטומטיות לתמונה (דגלים זרים, לוגו מקושקש); (ה) Constraints עודכן ש-Read תומך בתמונות וחובה להשתמש בזה. דוח התבנית עודכן עם דוגמת קטגוריה 6.
- **Decisions:**
  - **לא מחליפים את ה-tools allowlist.** Read כבר תומך ב-PNG/JPG; אין צורך ב-tool חדש.
  - **תמונה עם דגלים זרים = ❌ אוטומטי.** זה לא דבר שאפשר לקרוא לו "מינורי".
  - **דמיון לאישים ספציפיים — סף נמרץ:** אם תיאור טוען לדמיון ולא ניתן לזיהוי = ❌. (זה בדיוק מה שהפיל את `2026-05-08-uruguay-legends-montage.png` — סוארס/קבאני זוהו, אבל פרנצ'סקולי/טבארס/ביאלסה לא.)
  - **לא דורשים גישה לאינטרנט לאימות אישים.** valverde שופט לפי הופעה כללית מול ארכיטיפ + הקשר הסעיף. גבול ידוע — אם יש אדם שלא מוכר ב-training set של המודל, ייתכן שהוא יחמיץ.
- **Notes / Caveats:** התקלה שהובילה להרחבה — תמונת `2026-05-08-uruguay-legends-montage.png` כללה דגלי ארגנטינה בקהל ופרצופים שלא דמו לאישים שצוטטו בכותרת. valverde של סבב #2 אישר את המאמר ✅ אבל לא בדק את התמונה. הרחבה זו סוגרת את הפער. ה-Open Question המקורית ("האם valverde צריך לבדוק גם תמונות?") נסגרה.
- **Related:** [[forlan-creative-agent]], [[enzo-ceo-agent]]

### 2026-05-08 — valverde defined + QA Loop integrated [shipped]
- **What was done:** יצירת `.claude/agents/valverde.md` עם frontmatter ו-system prompt מלא בעברית. יצירת workspace `valverde/` עם `agent.md` ו-`QA_Reports/.gitkeep`. עדכון `.claude/agents/enzo.md` עם valverde ב-Sub-Agents (כולל auto-trigger note), פרוטוקול חדש "QA Loop" עם 5-step loop logic ו-3-rounds escalation, ועדכון Operating Loop שלב 9. עדכון `CLAUDE.md` (Agents + Repository Layout + Status). תיעוד ב-vault.
- **Decisions:**
  - **Tools = Read, Glob, Grep, Write בלבד.** read-mostly מכוון. אין Edit כדי שלא יתפתה לתקן בעצמו ולעקוף את cavani. החלוקה החדה (cavani כותב, valverde שופט) שומרת על אחריות נקייה.
  - **דוח לכל סבב, גם אם ✅.** היסטוריה מלאה ב-`QA_Reports/`, לא רק כשלים. מאפשר ניתוח מגמות עתידי.
  - **3 סבבים תקרה.** מעבר לזה אסקלציה למשתמש (לא ל-Enzo להחליט לבד). מונע loops אינסופיים.
  - **valverde הוא bottleneck מכוון.** הסוכן היחיד שמורשה לדחות. בלי ✅ שלו אין שחרור (חוץ מאישור משתמש ידני בסבב 3).
  - **`style-guide.md` חסר → ⚠️, לא ❌.** לא להכשיל תוצר על משהו שעדיין לא נכתב. הקובץ יסומן כ"לא נבדק" ויעלה כ-Open Question בדוח.
  - **Auto-trigger.** valverde רץ אוטומטית בסוף כל pipeline, גם בלי trigger מהמשתמש. הראשון בפרויקט עם דפוס כזה.
- **Notes / Caveats:** עומס נוסף על Enzo — עכשיו אחראי על loop ניהול עד 3 סבבים בין cavani ל-valverde. אם זה יכבד יישקל skill ייעודי `qa-loop-orchestration`. valverde לא יכול לקרוא ל-cavani ישירות — Claude Code לא מאפשר sub-agent → sub-agent, ולכן כל ה-loop logic יושב ב-Enzo.
- **Related:** [[enzo-ceo-agent]], [[cavani-content-agent]], [[forlan-creative-agent]], [[suarez-research-agent]]
