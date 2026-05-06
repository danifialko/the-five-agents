# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**the-five-agents** הוא צוות סוכנים ליצירת תוכן.
המבנה הוא של סוכן ראשי ("מנכ"ל") שמנהל ומתזמר צוות של סוכנים מתמחים תחתיו.
המנכ"ל וצוות הסוכנים יוגדרו בהדרגה — כרגע הפרויקט נמצא בשלב הקמה ראשוני, ללא קוד.

## Repository Layout

תחת `.claude/` יושבים ההתאמות הייעודיות לפרויקט:

- `.claude/agents/` — subagents מותאמים לפרויקט
- `.claude/skills/` — skills מותאמים לפרויקט
- `.claude/commands/` — slash commands מותאמים לפרויקט

תיקיות עבודה בשורש (לזרימת תוכן):

- `Content/` — מאמרי גלם הממתינים לשכתוב ע"י cavani
- `Content/Ready/` — מאמרים שטופלו (Enzo מעביר לשם אחרי שילוב תמונות)
- `Output/` — תוצרים משוכתבים של cavani; Enzo מחליף בהם `{{IMAGE_NEEDED}}` placeholders ע"י forlan

## Agents

- `.claude/agents/enzo.md` — **Enzo**, ה-CEO. נקודת הכניסה הראשית למשימות. מתזמר את הצוות, מבצע בקרת איכות, ומאשר את התוצר הסופי.
- `.claude/agents/forlan.md` — **forlan** (פורלאן), סוכן קריאייטיב / יצירת תמונות. נקרא ע"י Enzo כשנדרש ויזואל. משתמש בסקיל `gpt-image-gen` ועובד מול `forlan/reference/` + `forlan/outputs/`.
- `.claude/agents/cavani.md` — **cavani** (קבי), סוכן Content writer/rewriter. LLM-only (Read/Write/Edit/Glob/Grep). משכתב מאמרי גלם מ-`Content/` ל-`Output/` בסגנון `cavani/style-guide.md`. מסמן צורך בתמונה ב-`{{IMAGE_NEEDED}}` placeholders ש-Enzo מחליף ע"י forlan.

סוכני מומחים נוספים תחת Enzo יוגדרו בהמשך.

## Skills

- `.claude/skills/gpt-image-gen/SKILL.md` — מעטפת ל-OpenAI Images API (`gpt-image-2`). דורש `OPENAI_API_KEY` ב-`.env`. כל יצירת תמונה בפרויקט עוברת דרך הסקיל הזה.

## Status

שלב נוכחי: scaffolding + Enzo (CEO) + forlan (creative) + cavani (writer) + skill `gpt-image-gen`; שאר סוכני המומחים בהמתנה.
פרטים נוספים (ארכיטקטורה, פקודות build/test, הגדרות סוכנים נוספות) יתווספו לקובץ הזה ככל שהפרויקט יתקדם.
