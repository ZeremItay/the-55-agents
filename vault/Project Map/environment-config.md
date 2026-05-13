# Environment Config — `.env` ו-`.env.example`

## Overview

שני קבצים בשורש הפרויקט מנהלים מפתחות API: `.env.example` הוא תבנית גלויה (תחת git), `.env` הוא הקובץ האמיתי (לא תחת git, מוגן ב-[[gitignore-policy]]). המפתחות הצפויים: `ANTHROPIC_API_KEY` (קריאות ישירות ל-Claude), **`OPENAI_API_KEY` (עיקרי — נדרש לסקיל `gpt-image-gen` שמשתמש ב-`gpt-image-2` ליצירת תמונות עבור [[yuval]])**, `GEMINI_API_KEY` (נשמר עבור הסקיל הגלובלי `nano-banana` — לא בשימוש בפרויקט החל מ-2026-05-13), `TAVILY_API_KEY` (חיפוש ל-[[chen]]). **משויך:** תשתית — שייך לראובן [[reuven]] לוודא שמתאפשר לסוכנים לעבוד.

## Open Questions

- ה-`.env` הנוכחי הוא placeholder בלבד (294 בייטים, אותם ערכי דמה כמו ב-`.env.example`) — יש למלא ערכים אמיתיים לפני שיובל או חן יוכלו לפעול.
- האם צריך מפתח נוסף לפלטפורמת פרסום (LinkedIn / Facebook / Twitter API) עבור [[Publishing Log/_index|Publishing Log]] בעתיד?

## Session Log

### 2026-05-13 — תיעוד ראשוני [planned]
- **What was done:** תועד תפקיד שני הקבצים והקישור בין מפתחות לסוכנים: Gemini→יובל, Tavily→חן, Anthropic→הכל.
- **Decisions:** `.env` נשאר תחת `.gitignore` ולא מוכנס לבאקאפ — מפתחות לעולם לא נכנסים ל-git.
- **Notes / Caveats:** ה-`.env` הנוכחי **לא פעיל** — תוכן ה-placeholder מהווה תזכורת ולא ערך עובד. אסור להריץ הפעלות אמיתיות עד מילוי המפתחות.
- **Related:** [[gitignore-policy]], [[yuval]], [[chen]], [[reuven]]

### 2026-05-13 — מעבר ל-OpenAI: OPENAI_API_KEY הופך למפתח עיקרי לתמונות [shipped]
- **What was done:** עודכן comment ב-`.env.example` ש-`OPENAI_API_KEY` נדרש לסקיל החדש `gpt-image-gen` (מודל `gpt-image-2`). הוסבר ב-Overview ש-`GEMINI_API_KEY` נשאר רשום אבל לא בשימוש בפרויקט (רק עבור הסקיל הגלובלי `nano-banana`, שאינו פעיל אחרי המעבר).
- **Decisions:** לא הוסר `GEMINI_API_KEY` מ-`.env` — סקילים גלובליים עדיין יכולים להזדקק לו, ועלות שמירה אפסית.
- **Notes / Caveats:** ה-`OPENAI_API_KEY` ב-`.env` עדיין placeholder (`your_openai_api_key_here`) — קריאת API אמיתית תיכשל עד מילוי ידני.
- **Related:** [[yuval]], [[skills-directory]], [[yuval-and-gpt-image-gen]]
