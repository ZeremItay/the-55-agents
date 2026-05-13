# `.claude/agents/` — הגדרות הסוכנים

## Overview

התיקייה מכילה קובץ `.md` לכל אחד מהסוכנים בצוות ([[yael]], [[yuval]], [[chen]]), עם YAML frontmatter שמגדיר את התפקיד, תיאור (`description`), הכלים המותרים (`tools`), והמודל. **מצב נוכחי (2026-05-13):** שלושת ה-agents (`yael.md`, `yuval.md`, `chen.md`) נכתבו ופועלים. **משויך:** [[reuven]] אחראי על האדריכלות; כל סוכן מחזיק את הקובץ שלו.

## Open Questions

- האם להגדיר את ראובן עצמו כ-agent נפרד או להישאר עם ברירת-המחדל מ-[[claude-md]]?
- האם להוסיף בעתיד agent רביעי שמתמחה בפרסום (LinkedIn/Twitter/וכו') או להישאר ב-4 (ראובן + יעל + יובל + חן) ולהפעיל את הפרסום כסקיל?

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

### 2026-05-13 — chen.md נוצר ופועל [shipped]
- **What was done:** נכתב `chen.md` עם `tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Grep` (ללא Bash, ללא Agent — נאכף ברמת frontmatter). description עם 3 example blocks (חיפוש טרי, cache hit, נושא דינמי). System prompt בעברית עם workflow בן 8 שלבים (intent → memory check → search → filter → fetch → save → log → report). הפלט שלה: קובץ ב-`Content/<YYYY-MM-DD>-<slug>.md` עם header מובנה (Source/Retrieved/Quality/Original language).
- **Decisions:** **`WebSearch`/`WebFetch` במקום Tavily/Perplexity** — שינוי ארכיטקטוני שמבטל את התלות במפתח API חיצוני. **זיכרון חיפושים ב-Markdown flat file** (`chen/Memory/searches.md`) ולא DB — שמירה על פשטות, human-readable, Grep מהיר מספיק לסקייל הנוכחי. **לא Bash ולא Agent** — חן stateless ב-execution, מדווחת לראובן וזהו.
- **Notes / Caveats:** ה-Open Question של "איזה tools תקבל chen" נסגרה — WebSearch/WebFetch כצפוי. נסגרה גם שאלת ה-API החיצוני (אין כזה). שלושת ה-agents כעת פעילים — ראובן הוא היחיד שאין לו agent ייעודי, רק `CLAUDE.md`.
- **Related:** [[chen]], [[chen-agent-creation]], [[claude-md]], [[reuven]], [[environment-config]]
