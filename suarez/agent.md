# suarez/ — Workspace Pointer

קובץ זה הוא **pointer לבני אדם בלבד**. Claude Code לא טוען אותו.

## הסוכן הקנוני
`.claude/agents/suarez.md`. Claude Code סורק רק קבצים flat ב-`.claude/agents/`.

## תיקייה זו (`suarez/`)
Workspace של הסוכן:

- `Memory/searches.md` — לוג חיפושים. suarez מבצע `Grep` כאן לפני כל חיפוש חדש כדי לבדוק אם חיפש נושא דומה ב-30 הימים האחרונים.

## זרימת תוכן

```
Enzo → suarez (חיפוש) → Content/<date>-<slug>.md → cavani (שכתוב) → Output/<name>.md → Enzo (image sub) → Output/<name>.md (סופי)
```
