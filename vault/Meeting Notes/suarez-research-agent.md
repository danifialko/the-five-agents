# Suarez — Web Research Agent

## Overview
**suarez** הוא סוכן המחקר של הצוות — אחראי על מציאת תוכן אמיתי ועדכני מהרשת. Tools: `WebSearch, WebFetch, Read, Write, Edit, Glob, Grep` (ללא Bash, ללא API חיצוני). מקבל נושא/מילות מפתח מ-Enzo, בודק פרוטוקול זיכרון (`suarez/Memory/searches.md`) למניעת חיפוש כפול ב-30 יום, מבצע WebSearch + WebFetch, מסנן למקור האיכותי ביותר, ושומר ל-`Content/<YYYY-MM-DD>-<slug>.md` — הקלט הישיר של cavani. מבנה היברידי: `.claude/agents/suarez.md` (canonical) + `suarez/` workspace (`Memory/searches.md`, `agent.md`). הוא **לא** שוכתב, לא עורך סגנון, לא יוצר תמונות — רק מחקר ומידע מאומת ממקורות אמיתיים.

## Open Questions
- איזו רמת סיכום ב-`Content/<slug>.md`? כרגע: תמלול/סיכום נאמן לתוכן המקורי. האם cavani מעדיף bullet points, ציטוטים ישירים, או פרוזה?
- מה עושים כשאין מקור אמין? כרגע: suarez מדווח "לא מצאתי" ועוצר — Enzo מחליט.
- 30-day threshold לזיכרון — מספיק? לנושאים דינמיים (AI, שוק הון, חדשות) זה הרבה. אולי threshold לפי `topic_type` (static/dynamic)?
- האם `searches.md` יכבד ויקשה על grep לאורך זמן? כדאי לשקול rotation/archiving אחרי N רשומות.

## Session Log

### 2026-05-06 — Suarez defined [shipped]
- **What was done:** יצירת `.claude/agents/suarez.md` (frontmatter עם tools allowlist `WebSearch, WebFetch, Read, Write, Edit, Glob, Grep`, `model: sonnet`, בody מלא). יצירת `suarez/{agent.md, Memory/searches.md}`. עדכון `.claude/agents/enzo.md` — הוספת suarez לרשימת ה-Sub-Agents עם trigger keywords + memory protocol note + definition of done. עדכון `CLAUDE.md` (Agents + Repository Layout + Status). תיעוד ב-vault.
- **Decisions:**
  - **Memory protocol ב-searches.md** — Grep לפני כל חיפוש, 30-day threshold, בדיקה אם הנושא דינמי. מונע חיפושים כפולים וחוסך tokens.
  - **פורמט `Content/<date>-<slug>.md`** — אותה מוסכמה כמו ב-forlan outputs; sortable, קריא, חסין-collision.
  - **"אפס הזיות" כ-quality bar** — כל עובדה חייבת להגיע ממקור מאומת. עדיף "לא מצאתי" על מידע שאינו ניתן לאימות.
  - **`model: sonnet`** — WebSearch/WebFetch לא דורשים opus; עלות vs. איכות מצדיקה sonnet.
  - **suarez לא שוכתב** — הפרדת תחומים נקייה: suarez = raw content, cavani = styled content.
- **Notes / Caveats:** `suarez/Memory/searches.md` נוצר עם header ופורמט רשומה לדוגמה — ריק לחיפושים. ה-30-day threshold הוא הנחה; יתכן שנצטרך לכוונן לפי סוג הנושא.
- **Related:** [[cavani-content-agent]], [[enzo-ceo-agent]], [[claude-folder-structure]]
