# Yuval Agent + gpt-image-gen Skill + Yael IMAGE_NEEDED

## Overview

הוספת צד הוויזואל למערכת הצוות. שלושה רכיבים שמתחברים יחד:

1. **סקיל פרויקטי `gpt-image-gen`** — מעטפת ל-OpenAI Images API עם המודל `gpt-image-2` (יצא ב-21.04.2026). מספק curl + Python fallback לפענוח base64, טעינת `OPENAI_API_KEY` מ-`.env`, ואימות פלט.
2. **Sub-agent `yuval`** — מעצב התמונות. כלים: Read, Write, Bash, Glob. workflow בן 8 שלבים: scan reference → build prompt → slug → call skill → save `.txt` sibling → verify → report.
3. **עדכון Yael** — protocol של `{{IMAGE_NEEDED: "..."}}` placeholders ב-MD/HTML, סיכום ממוספר לראובן.

ראובן (אני) מתאם בין יעל ויובל: יעל מסמנת איפה תמונה, יובל מייצר, אני משלב ל-`Output/`.

**שינוי ארכיטקטוני:** מעבר מ-Nano Banana (Gemini) ל-OpenAI gpt-image-2 — החלפה מלאה לפי החלטת משתמש. `GEMINI_API_KEY` נשאר ב-`.env` כי הסקיל הגלובלי `nano-banana` עדיין יכול להזדקק לו, אבל לא בשימוש בפרויקט.

## Open Questions

- **מילוי `OPENAI_API_KEY` ב-`.env`:** עדיין placeholder. עד שהמשתמש ממלא ידנית — לא ניתן להריץ קריאה אמיתית.
- **vision לסריקת reference:** יובל לא יכול "לראות" קבצי PNG ב-`yuval/reference/`. נדרש או (א) דורש מהמשתמש לכתוב תיאור סגנון ב-`reference/style.md`, או (ב) להוסיף בעתיד מודל vision ל-flow.
- **שילוב אוטומטי במקום ידני:** כרגע ראובן מבצע את ההחלפה של placeholders ביד. בעתיד יכול להיות slash command `/finalize-article` שעושה את כל ה-pipeline.
- **`quality: high` benchmark:** מתי שווה את העלות הגבוהה? צריך לבנות 3 דוגמאות (low/medium/high) על אותו prompt ולהשוות.

## Session Log

### 2026-05-13 — הוספת yuval, gpt-image-gen, ו-IMAGE_NEEDED protocol ל-yael [shipped]
- **What was done:**
  - **Skill חדש** ב-`.claude/skills/gpt-image-gen/`: `SKILL.md` (יותר מ-130 שורות — frontmatter, אזהרת מודל, חתימת API, jq/python fallback, וריפיקציה, דוגמת קריאה מלאה) + `scripts/decode_b64.py` (~30 שורות, stdlib בלבד).
  - **Agent חדש** ב-`.claude/agents/yuval.md`: frontmatter עם `tools: Read, Write, Bash, Glob`, 3 example blocks ב-description. System prompt בעברית עם workflow בן 8 שלבים, הוראות slug אוטומטי, וכלל מפורש שלא להחליף את שם המודל גם בשגיאה.
  - **Yael עודכן** — שלב 3.5 חדש (זיהוי מקומות לתמונה והוספת `{{IMAGE_NEEDED: "..."}}` placeholders); שלב 5 (סיכום) הורחב לרשימה ממוספרת של ה-placeholders לראובן; סעיף "גבולות" עודכן.
  - **CLAUDE.md הורחב** — יובל ברשימת הצוות עם triggers; סעיף חדש "תהליך מאמר עם תמונות" (5 שלבים); סעיף "מבנה הפרויקט" עודכן עם `yuval/`, `Output/images/`, ו-`.claude/skills/gpt-image-gen/`.
  - **`.env.example` עודכן** — comment של `OPENAI_API_KEY` שינוי מ"אופציונלי" ל"נדרש לסקיל gpt-image-gen".
  - **תיקיות עבודה:** `yuval/reference/.gitkeep`, `yuval/outputs/.gitkeep`, `Output/images/.gitkeep`.
  - **5 vault topic files עודכנו** — [[yuval]] (החלפה ארכיטקטונית של backend תמונות, Session Log חדש), [[yael]] (Session Log חדש על IMAGE_NEEDED), [[agents-directory]] (yuval.md נוסף, Open Question של tools של יובל נסגרה), [[skills-directory]] (קטגוריה חדשה Project-Custom Skills + Session Log), [[environment-config]] (OPENAI_API_KEY עיקרי, Gemini deprecated לפרויקט).
- **Decisions:**
  - **`gpt-image-2` בדיוק** — הוראה מפורשת בקובץ הסקיל ובסיסטם prompt של יובל לא להחליף ל-`dall-e-3`/`gpt-image-1` גם אם יש שגיאה. הסיבה: המודל יצא 21.04.2026, אחרי ה-knowledge cutoff של ינואר 2026. ההנחה ש"שם מודל לא תקף" היא טעות.
  - **סקיל נפרד ולא curl ישיר ב-Yuval prompt** — מפריד "איך לקרוא ל-API" מ"מה לבקש". יותר maintainable, ניתן לשימוש חוזר.
  - **Python fallback ל-jq** — Git Bash על Windows לעתים קרובות חסר jq. Python כמעט תמיד זמין. סקריפט קצר ב-stdlib בלבד.
  - **Bash ליובל, לא Edit** — יובל יוצר קבצים חדשים בלבד, לא משנה קיימים. צמצום אכוף ברמת frontmatter.
  - **slug אוטומטי מה-prompt** — מינימום חיכוך. יובל מסנן 3-5 מילים, lowercase, hyphens, מתרגם לאנגלית אם בעברית.
  - **העתקה ל-`Output/images/` ולא קישור ישיר ל-`yuval/outputs/`** — התוצר ב-`Output/` עצמאי. ניתן לשלוח את התיקייה כיחידה אחת.
  - **Yael מסמנת בלבד, יובל מייצר בלבד, ראובן משלב.** הפרדת אחריות מוחלטת — קל לדבג ולשנות כל חלק בנפרד.
- **Notes / Caveats:**
  - הסקיל אומת — מופיע ב-Claude Code Available Skills בסשן הנוכחי.
  - ה-agent של יובל ייטען רק בסשן הבא (אחרי reload). בסשן הנוכחי לא ניתן לבצע `Agent(subagent_type='yuval')`.
  - לא בוצעה קריאת API אמיתית — `OPENAI_API_KEY` placeholder + עלות אמיתית.
  - הפלט `yael.md` עודכן ב-EDIT (לא Write) כדי לשמר את כל החלקים שלא נגעו בהם.
- **Related:** [[yuval]], [[yael]], [[agents-directory]], [[skills-directory]], [[environment-config]], [[claude-md]], [[yael-agent-creation]], [[plugin-skill-creator-install]]
