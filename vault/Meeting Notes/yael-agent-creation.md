# Yael — Agent Creation

## Overview

יצירת ה-sub-agent הראשון בצוות: **יעל**, כותבת התוכן. כללה כתיבת `.claude/agents/yael.md` (flat file עם YAML frontmatter בפורמט Claude Code), הקמת מבנה תיקיות עבודה (`Content/`, `Output/`, `yael/reference/`), עדכון `CLAUDE.md` עם trigger keywords לניתוב אוטומטי, ועדכון שני topic files ב-vault. סגירת ה-Open Question של [[yael]] בנושא tool restrictions: יעל מקבלת Read, Write, Edit, Glob, Grep — בלי Bash, WebSearch או Agent. ה-tool restrictions נאכפים ברמת המערכת ב-frontmatter, לא רק כהוראות טקסטואליות.

## Open Questions

- ה-`yael/style-guide.md` עדיין לא נכתב — בלעדיו יעל פועלת לפי הוראות ברירת מחדל בלבד. מתי יוסיף המשתמש סגנון מובהק?
- ה-`yael/reference/` ריקה — דוגמאות אמיתיות לסגנון הרצוי יקפיצו את איכות הפלט.
- ה-`itay-zerem-writing` הגלובלי vs `.claude/agents/yael` הפרויקטי — מתי כל אחד? ההנחה: יעל היא תפקיד צוותי, הסקיל הוא קול ספציפי לאיתי. ראובן יחליט במשימה.
- האם להפיק stubs דומים ליובל וחן בקרוב, או לחכות שתעלה דרישה אמיתית לכל אחד מהם?

## Session Log

### 2026-05-13 — יצירת ה-agent של יעל [shipped]
- **What was done:**
  - **`.claude/agents/yael.md`** — קובץ agent חדש. Frontmatter: `name: yael`, `tools: Read, Write, Edit, Glob, Grep`, `model: sonnet`. `description` באנגלית עם 3 example blocks (שכתוב, סיכום, תרגום). System prompt בעברית — workflow בן 5 שלבים, כללי הסרת CTAs/קישורים, שמירת מותגים בתוך הסיפור, וגבולות מפורשים על מה שאסור (WebSearch, יצירת תמונות, Agent, Bash).
  - **תיקיות עבודה:** `Content/.gitkeep`, `Output/.gitkeep`, `yael/reference/.gitkeep`.
  - **`CLAUDE.md`:** שורת יעל הורחבה עם trigger keywords בעברית (שכתב/ערוך/נסח מחדש/תרגם/סכם/מאמר/תוכן/פוסט) ובאנגלית (rewrite/edit/rephrase/translate/summarize/article/content/post), והפניה לקובץ ה-agent.
  - **[[yael]]:** Overview עודכן ש-agent קיים; Open Questions עודכן (נסגרה שאלת ה-tools, נפתחו שאלות חדשות על style-guide ו-reference); נוסף Session Log entry `[shipped]`.
  - **[[agents-directory]]:** Overview עודכן ש-yael.md פעיל; Open Questions עודכן (התרכזה בשאלות על חן ויובל); Session Log entry `[shipped]` נוסף.
- **Decisions:**
  - **שפת ה-system prompt עברית, ה-description אנגלית** — מתואם לפי החלטת המשתמש, ובהתאם להבחנה ש-routing model של Claude Code עובד טוב יותר על description אנגלית עם examples, אבל פלט הכתיבה של יעל בעברית.
  - **`tools` ב-frontmatter ולא רק בהוראות** — מבטיח אכיפה ברמת המערכת. ניסיון של יעל להפעיל Bash בעתיד יחזיר InputValidationError, לא יסתמך על ציות עצמי.
  - **לא ייצור `yael/style-guide.md` בסשן הזה** — המשתמש יכתוב בעצמו; ה-system prompt מורה ליעל לבדוק קיום עם Glob ולפעול לפי ברירת מחדל אם הקובץ חסר.
  - **HTML output חייב להיות RTL מעוצב** — נכתב במפורש ב-system prompt כדי שגם בלי style-guide הפלט יהיה אחיד.
  - **Triggers ל-CLAUDE.md רק עבור יעל בשלב זה** — לפי החלטת משתמש; יובל וחן יקבלו את שלהם כשייוצרו.
- **Notes / Caveats:**
  - בעבודה ב-Claude Code, ייתכן ש-Yael לא תופיע כ-subagent_type בסשן הנוכחי — צריך reload session כדי שהיא תיטען. בסשן הבא היא תופיע ב-Agent tool.
  - יעל לא יכולה להעביר משימה ישירות לחן/יובל — היא חייבת להחזיר סיכום לראובן עם המלצה. זו החלטת ארכיטקטורה כדי לשמור על ראובן כמתאם יחיד.
  - הכפילות בין הסקיל `itay-zerem-writing` (גלובלי) ל-agent יעל (פרויקטי) — לא נוצרה התנגשות כי הם בנויים אחרת: סקיל הוא style-guide שניתן להחיל בכל הקשר, agent הוא תפקיד עם workflow. במשימת כתיבה עתידית בקול של איתי, נראה אם ראובן מפעיל את שניהם או רק את אחד.
- **Related:** [[yael]], [[agents-directory]], [[claude-md]], [[claude-directory]], [[skills-directory]], [[reuven]], [[plugin-skill-creator-install]]
