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

## Agents

- `.claude/agents/enzo.md` — **Enzo**, ה-CEO. נקודת הכניסה הראשית למשימות. מתזמר את הצוות, מבצע בקרת איכות, ומאשר את התוצר הסופי.

סוכני המומחים שתחת Enzo טרם הוגדרו ויתווספו בהמשך.

## Status

שלב נוכחי: scaffolding + Enzo (CEO) מוגדר; סוכני המומחים בהמתנה.
פרטים נוספים (ארכיטקטורה, פקודות build/test, הגדרות סוכנים נוספות) יתווספו לקובץ הזה ככל שהפרויקט יתקדם.
