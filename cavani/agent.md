# cavani/ — Workspace Pointer

קובץ זה הוא **pointer לבני אדם בלבד**. Claude Code לא טוען אותו.

## הסוכן הקנוני
`.claude/agents/cavani.md`. Claude Code סורק רק קבצים flat ב-`.claude/agents/`, לכן ההגדרה חייבת לשבת שם.

## תיקייה זו (`cavani/`)
Workspace של הסוכן:

- `style-guide.md` — מדריך הסגנון. **חובה**. בלעדיו cavani נכשל מיד עם `BLOCKED: Missing or empty cavani/style-guide.md`.
- `reference/` — דוגמאות לטקסטים שמייצגים את סגנון הבית. cavani קורא הכל בתחילת כל ריצה.

## תיקיות העבודה (בשורש הפרויקט)

- `Content/` — מאמרי גלם ממתינים לשכתוב.
- `Content/Ready/` — מאמרים שטופלו (Enzo מעביר לשם — לא cavani).
- `Output/` — תוצרי cavani (`<name>.md`, יכולים להכיל `{{IMAGE_NEEDED ...}}` placeholders ש-Enzo מחליף).
