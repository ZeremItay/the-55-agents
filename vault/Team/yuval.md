# יובל — מעצב התמונות

## Overview

יובל אחראי על הצד הוויזואלי — תמונות, גרפיקה, אילוסטרציות, thumbnails, ובאנרים שמלווים תוכן. **מוגדר כ-sub-agent ב-`.claude/agents/yuval.md` החל מ-2026-05-13**, עם כלים מצומצמים: Read, Write, Bash, Glob (Bash נדרש לקריאת ה-API; אין Edit כי לא משנה קבצים קיימים, אין Grep). **שינוי ארכיטקטוני (2026-05-13):** עבר משימוש ב-Nano Banana (Gemini) ל-OpenAI `gpt-image-2` דרך הסקיל הפרויקטי [[skills-directory|gpt-image-gen]]. דורש `OPENAI_API_KEY` ב-[[environment-config]] (כבר קיים, אך כ-placeholder). יובל מקבל את הבריף לרוב **אחרי** ש-[[yael]] השלימה את הטקסט, כשהיא מסמנת `{{IMAGE_NEEDED: ...}}` placeholders שראובן ממיר לקריאות אינדיבידואליות ל-יובל.

## Open Questions

- האם להוסיף יכולת image-to-image (איטרציה על תמונה קיימת) לסקיל `gpt-image-gen`? כרגע — קריאה אחת = קובץ חדש, ה-`.txt` הסמוך הוא ה-source.
- כשמשתמש מוסיף תמונות PNG ל-`yuval/reference/` — איך יובל "מבין" את הסגנון בלי vision? בינתיים: רק קבצי `.md`/`.txt` עם תיאור סגנוני קוראים. תמונות עצמן רק נספרות.
- מתי `quality: high` שווה את העלות הגבוהה? צריך benchmark של תוצאות לפני הקפיצה.

## Session Log

### 2026-05-13 — קביעת תפקיד והתחלת תיעוד [planned]
- **What was done:** תועד תפקיד יובל כמעצב, וההסתמכות שלו על `GEMINI_API_KEY` מ-[[environment-config]].
- **Decisions:** יובל יישאר במורד-הזרם של יעל כברירת-מחדל — קופי לפני ויזואל.
- **Notes / Caveats:** הסקיל `nano-banana` מותקן בפרופיל המשתמש (לא בפרויקט) — לא צריך התקנה חוזרת.
- **Related:** [[reuven]], [[yael]], [[chen]], [[environment-config]], [[agents-directory]]

### 2026-05-13 — יצירת sub-agent + מעבר ל-OpenAI gpt-image-2 [shipped]
- **What was done:**
  - נכתב `.claude/agents/yuval.md` עם YAML frontmatter (tools: Read, Write, Bash, Glob; model: sonnet) ו-system prompt בעברית. ה-description כולל 3 example blocks.
  - **שינוי ארכיטקטוני:** יובל לא משתמש יותר ב-Nano Banana (Gemini). במקום זה — סקיל פרויקטי חדש [[skills-directory|gpt-image-gen]] שמפעיל את OpenAI `gpt-image-2`. ה-Gemini skill הגלובלי נשאר זמין אבל לא בשימוש.
  - Workflow מובנה ב-8 שלבים: סריקת reference → בניית prompt באנגלית → slug אוטומטי → קריאה לסקיל → שמירת sibling `.txt` → אימות → דיווח לראובן.
  - תיקיות עבודה: `yuval/reference/`, `yuval/outputs/`, ו-`Output/images/` (לתוצר המשולב של ראובן).
  - עודכן [[claude-md]] עם יובל ברשימת הצוות, trigger keywords, ותהליך מאמר-עם-תמונות.
- **Decisions:**
  - **`gpt-image-2` בדיוק** — לא להחליף ל-`dall-e-3` או `gpt-image-1` גם אם מודל פנימי מציע. המודל יצא ב-21.04.2026 ואינו בידע פנימי של ינואר-2026.
  - **סקיל נפרד** ולא curl ישיר ב-system prompt — מפריד "איך לקרוא ל-API" מ"מה לבקש". הסקיל ניתן לשימוש חוזר.
  - **Bash כן, Edit לא** — יובל מייצר קבצים חדשים בלבד, לא משנה קיימים. צמצום אכוף ברמת המערכת.
  - **אנגלית ב-prompt** — גם אם הבקשה בעברית. ה-image model מבין טוב יותר אנגלית. יובל מתרגם.
  - **קריאה אחת = קובץ אחד.** אם צריך 3 תמונות, ראובן מזמן את יובל 3 פעמים — לא מנסים לעשות הכל בקריאה אחת.
- **Notes / Caveats:**
  - `OPENAI_API_KEY` ב-`.env` עדיין placeholder — לא ניתן להריץ קריאת API אמיתית עד שהמשתמש ימלא ידנית.
  - אין vision: יובל לא יכול לקרוא קובצי PNG ב-`yuval/reference/` ולהסיק סגנון. רק `.md`/`.txt` עם תיאור סגנוני קוראים.
  - הסקיל לא רץ דרך Skill tool אוטומטית — הוא דוקומנטציה + scripts. יובל מבצע Bash ידנית לפי ההוראות. בעתיד אפשר לעטוף בסקריפט wrapper.
- **Related:** [[yael]], [[reuven]], [[claude-md]], [[environment-config]], [[skills-directory]], [[agents-directory]], [[yuval-and-gpt-image-gen]]
