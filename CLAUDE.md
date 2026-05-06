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

כל שלוש התיקיות ריקות כרגע ויתמלאו בהמשך.

## Status

שלב נוכחי: scaffolding בלבד. אין עדיין קוד, build, tests, או הגדרות סוכנים.
פרטים נוספים (ארכיטקטורה, פקודות build/test, הגדרות סוכנים) יתווספו לקובץ הזה ככל שהפרויקט יתקדם.
