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
