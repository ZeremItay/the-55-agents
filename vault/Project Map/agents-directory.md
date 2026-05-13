# `.claude/agents/` — הגדרות הסוכנים

## Overview

התיקייה מכילה קובץ `.md` לכל אחד מהסוכנים בצוות ([[yael]], [[yuval]], [[chen]]), עם YAML frontmatter שמגדיר את התפקיד, תיאור (`description`), הכלים המותרים (`tools`), והמודל. **מצב נוכחי (2026-05-13):** `yael.md` ו-`yuval.md` נכתבו ופועלים; `chen.md` עדיין לא נוצר (עד שיתבקש). **משויך:** [[reuven]] אחראי על האדריכלות; כל סוכן יקבל את הקובץ שלו.

## Open Questions

- איזה tools תקבל [[chen]] כשתיווצר? (WebSearch + WebFetch כברירת מחדל, MCP חיפוש לפי הצורך?)
- האם להגדיר את ראובן עצמו כ-agent נפרד או להישאר עם ברירת-המחדל מ-[[claude-md]]?

## Session Log

### 2026-05-13 — תיעוד ראשוני, התיקייה עדיין ריקה [planned]
- **What was done:** תועד התפקיד הצפוי של התיקייה ומה אמור להיכנס אליה.
- **Decisions:** לא יוצרים stub agents כעת — קובץ ייכתב רק כשהדרישות בשלות.
- **Notes / Caveats:** סוכן ייעודי הוא היחיד שניתן להפעיל דרך ה-Agent tool ב-Claude Code — היעדר הקבצים אומר שכרגע "ראובן" מבצע הכל בעצמו.
- **Related:** [[reuven]], [[yael]], [[yuval]], [[chen]], [[claude-directory]], [[claude-md]]

### 2026-05-13 — yael.md נוצר ופועל [shipped]
- **What was done:** נכתב `yael.md` עם `tools: Read, Write, Edit, Glob, Grep` (ללא Bash/WebSearch/Agent), `model: sonnet`, `description` באנגלית עם 3 example blocks. גוף ה-system prompt בעברית, מגדיר workflow בן 5 שלבים ו-HTML output מעוצב RTL.
- **Decisions:** ה-tool restrictions נכתבים ב-frontmatter ולא רק כהוראות בטקסט — כך Claude Code אוכף את הצמצום ברמת המערכת, לא רק על סמך ציות. זה הופך את יעל ל-agent בטוח באמת.
- **Notes / Caveats:** התיקייה עדיין לא מלאה — `yuval.md` ו-`chen.md` לא קיימים. ה-Open Questions עודכן בהתאם — שאלת ה-tools הספציפיים לכל אחד מהם עדיין פתוחה.
- **Related:** [[yael]], [[claude-md]], [[reuven]], [[yael-agent-creation]]

### 2026-05-13 — yuval.md נוצר ופועל [shipped]
- **What was done:** נכתב `yuval.md` עם `tools: Read, Write, Bash, Glob` (Bash נדרש לקריאת API; לא Edit כי לא משנה קבצים קיימים; לא Grep). description עם 3 example blocks (תמונה ללא reference, עם reference, סדרה של תמונות למאמר). System prompt בעברית עם workflow בן 8 שלבים, מסתמך על סקיל `gpt-image-gen` החדש.
- **Decisions:** Yael IMAGE_NEEDED protocol הוסף כדי לחבר בין יעל ליובל. ראובן הוא היחיד שמשלב — שמירה על אחריות יחידה לכל agent.
- **Notes / Caveats:** עדכון ב-Open Questions — נסגרה שאלת tools של יובל. נשארה שאלת tools של חן.
- **Related:** [[yuval]], [[yael]], [[claude-md]], [[reuven]], [[skills-directory]], [[yuval-and-gpt-image-gen]]
