# Cavani Style Guide & Reference Samples — Meta-Check Round 2

**Date:** 2026-05-08 19:00
**Reviewer:** valverde
**Scope:** `cavani/style-guide.md`, `cavani/reference/*.md`, `cavani/reference/README.md` (with cross-check on `cavani/agent.md`)
**Round:** #2 (final pre-commit)
**Verdict:** APPROVED FOR USE

---

## 1. EM Dash Compliance

Tool: `Grep` for `—` (U+2014) recursively across `cavani/`.

Result: 1 match, exactly as expected.

| File | Line | Context | Status |
|---|---|---|---|
| `cavani/style-guide.md` | 14 | `### בלי EM dashes (—) בכלל` | Legitimate illustration of the forbidden character (accepted in round #1). |

All other prose, all reference HTML headers, and `cavani/reference/README.md` are clean.

Bonus checks (not strictly required by spec, performed for safety):
- `cavani/agent.md`: 0 EM dashes. Confirmed clean per round-1 bonus fix.
- Adjacent dash characters (`–` en dash, `‒` figure dash, `―` horizontal bar): 0 occurrences anywhere in `cavani/`. No one tried to substitute a near-look-alike.

EM dash rule: **PASS.**

## 2. Bold-Name Convention

**Style-guide section ה (Structure), line 69** now contains:

> **הדגשה (bold) לשמות שחקנים בסקציות סקירת סגל.** הדפוס הסטנדרטי: בפסקה שמתארת מספר שחקנים, השם המלא של כל שחקן בהופעה הראשונה ב-`**bold**`. דוגמה: `**פדריקו ואלברדה** הוא הליבה. ריאל מדריד, 71 הופעות בנבחרת, אחד משחקני הביניים הטובים בעולם כרגע.` בשאר המאמר (טקסט נראטיבי, לא רשימה) לא להדגיש שמות.

Cross-check against the Hebrew sample (`2026-05-08-uruguay-mundial-2026-hebrew-sample.md`):

| Section | Player | Pattern in sample |
|---|---|---|
| `## הסגל` (line 59) | פדריקו ואלברדה | `**פדריקו ואלברדה** הוא הליבה.` — first appearance, bold, full name. Matches. |
| `## הסגל` (line 61) | חוסה מריה ז'ימנס | `**חוסה מריה ז'ימנס** (אטלטיקו מדריד...)` — bold. Matches. |
| `## הסגל` (line 61) | רונאלד אראוחו | `**רונאלד אראוחו** (ברצלונה) לצידו` — bold. Matches. |
| `## הסגל` (line 63) | מתיאס אוליברה | `**מתיאס אוליברה** (נאפולי)` — bold. Matches. |
| `## הסגל` (line 63) | רודריגו בנטנקור | `**רודריגו בנטנקור** (טוטנהאם)` — bold. Matches. |
| `## הסגל` (line 65) | דארווין נונייס | `ועל החוד, **דארווין נונייס**.` — bold. Matches. |
| `## רוח רפאים: סוארס חוזר?` and later sections | סוארס, נונייס (re-mention), ואלברדה (re-mention), ביאלסה, גיאן, מסי, בנזמה | All un-bolded. Matches the "narrative text — no bolding" rule. |

The rule as written ("בפסקה שמתארת מספר שחקנים, השם המלא של כל שחקן בהופעה הראשונה") perfectly matches the sample's behavior. There is no contradiction with any earlier rule.

Bold-name convention: **PASS.**

## 3. Other Gaps Inspected

I went looking for things that could trip cavani after activation. Found none.

- **Section ה consistency:** the new bold-name bullet sits at the end of section ה (Structure). It does not conflict with the "פתיחה ב-2-3 משפטים", "כותרות סקציה קצרות", "סגירה שחוזרת לפתיחה", or "מקור בתחתית" bullets. It's an additive structural rule.
- **Cross-section consistency:** no rule in section א (Voice & Tone), ב (Hard Rules), ג (Sentence Rhythm), or ד (Hebrew-First) touches bold/markdown emphasis. No collision possible.
- **Image placeholder convention** (section ו) intact, format `{{IMAGE_NEEDED: "..."}}` matches what `agent.md` and the Enzo orchestration spec expect.
- **Reference samples** are still the proven approved versions: Hebrew has the 6 QA-rounds pedigree noted in HTML header; English has the cross-language register note explicitly mentioning the EM-dash cleanup.
- **README.md table** still accurately lists both samples with correct word counts and QA rounds.
- **No stray TODOs, FIXMEs, or placeholder text** anywhere in the three files.
- **Hebrew RTL/LTR mixing:** numbers, English club names, and Spanish phrases (MLS, El Proceso, AFC) appear inline as the Hebrew-First rule allows. Sample handles this naturally.
- **Quotation marks** in style-guide use straight `"..."` consistently (no smart-quote drift).

## 4. Internal Consistency Re-Verification

Re-read sections א through ו end to end. No rule contradicts another. The bold-name addition is the only structural change since round 1 and it lives in its own bullet at the end of section ה, where it belongs.

---

## Verdict

**APPROVED FOR USE.**

All round-1 issues confirmed fixed. No new issues found. The style-guide and reference samples are unblocked.

cavani can be activated.
