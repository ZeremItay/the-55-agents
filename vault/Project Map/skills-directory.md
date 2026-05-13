# `.claude/skills/` — קטלוג סקילים

## Overview

תיקיית הסקילים מאוכלסת בשלוש קבוצות: **Superpowers** (מתודולוגיית עבודה של Claude), **Obsidian** (תמיכה ב-vault), ו-**Project-Custom Skills** (סקילים שנכתבו ספציפית לפרויקט). כל סקיל הוא תת-תיקייה עם `SKILL.md` במרכזה, ולעיתים סקריפטים וקבצי משנה. **משויך:** משותף לכל הצוות; [[reuven]] מחליט מתי להפעיל מה.

## תת-תיקיות (כל אחת היא סקיל)

**Superpowers (מתודולוגיה):**
- `brainstorming/` — חובה לפני יצירה
- `dispatching-parallel-agents/` — הפעלת agents במקביל
- `executing-plans/` — ביצוע תוכניות עם checkpoints
- `finishing-a-development-branch/` — סגירת branch
- `receiving-code-review/` — קבלת ביקורת
- `requesting-code-review/` — בקשת ביקורת
- `subagent-driven-development/` — ביצוע תוכניות בסשן הנוכחי
- `systematic-debugging/` — דיבאג שיטתי
- `test-driven-development/` — TDD
- `using-git-worktrees/` — בידוד workspaces
- `using-superpowers/` — מבוא למערכת
- `verification-before-completion/` — אימות לפני הצהרת סיום
- `writing-plans/` — כתיבת תוכניות
- `writing-skills/` — יצירת סקילים חדשים

**Obsidian (תמיכה ב-vault):**
- `obsidian-vault-workflow/` — **הסקיל החובה** — קריאה/כתיבה ל-vault בכל משימה
- `obsidian-markdown/` — תחביר Obsidian (wikilinks, callouts, frontmatter)
- `obsidian-bases/` — יצירת `.base` files

**Project-Custom Skills:**
- `gpt-image-gen/` — מעטפת לקריאת OpenAI Images API (`gpt-image-2`) ליצירת תמונות עבור [[yuval]]. כולל `scripts/decode_b64.py` כ-fallback ל-jq. דורש `OPENAI_API_KEY` ב-[[environment-config|.env]].

## Open Questions

- האם להוסיף סקיל מותאם לפרויקט (`five-agents-workflow`?) שייעט את שילוב הסקילים האחרים?
- חלק מהסקילים גלובליים (מותקנים ברמת המשתמש) מופיעים גם בפרויקט — האם להסיר כפילות?

## Session Log

### 2026-05-13 — תיעוד ראשוני וקטלוג מלא [planned]
- **What was done:** נספרו ותועדו 17 סקילים. הקבוצה מחולקת בבירור ל-Superpowers ו-Obsidian.
- **Decisions:** כל הסקילים הנוכחיים נשמרים — לא מסירים שום סקיל לפני שמתברר שהוא יוצר התנגשות.
- **Notes / Caveats:** הקטלוג כאן יישבר כשיתווסף/יוסר סקיל — יש לעדכן עם כל שינוי תחת `.claude/skills/`.
- **Related:** [[claude-directory]], [[vault-directory]], [[reuven]]

### 2026-05-13 — סקיל פרויקטי ראשון: `gpt-image-gen` [shipped]
- **What was done:** נוצרה קבוצה חדשה "Project-Custom Skills" בקטלוג. נכתב `gpt-image-gen/SKILL.md` (מעטפת ל-OpenAI Images API עם `gpt-image-2`) ו-`gpt-image-gen/scripts/decode_b64.py` (python fallback ל-jq).
- **Decisions:** הסקיל הוא דוקומנטציה + scripts ולא wrapper אוטומטי — Yuval מבצע Bash ישירות לפי ההוראות. החלטה זמנית; אם בעתיד נרצה פחות boilerplate נכתוב script אחד שמקבל פרמטרים.
- **Notes / Caveats:** הסקיל מופיע ב-`Available skills` של Claude Code אחרי הכתיבה — אומת בסשן הנוכחי.
- **Related:** [[yuval]], [[environment-config]], [[yuval-and-gpt-image-gen]]
