# יעל — כותבת התוכן

## Overview

יעל היא הכותבת של הצוות — אחראית על ניסוח, עריכה וכתיבה של טקסטים. היא מקבלת בריפים מ-[[reuven|ראובן]] בדרך כלל אחרי ש-[[chen|חן]] השלימה מחקר רקע. **מוגדרת כ-sub-agent ב-`.claude/agents/yael.md` החל מ-2026-05-13**, עם כלי קריאה/כתיבה בלבד (Read, Write, Edit, Glob, Grep) — בלי Bash, WebSearch או יצירת תמונות. ה-workflow הקבוע שלה: שולפת מאמר מ-`Content/`, טוענת סגנון מ-`yael/style-guide.md` ומ-`yael/reference/` אם קיימים, ומפיקה שני תוצרים ל-`Output/` (Markdown + HTML מעוצב RTL).

## Open Questions

- ה-`yael/style-guide.md` עדיין לא נוצר — בזמן שזה ככה יעל תפעל לפי ההוראות בקובץ ה-agent עצמו בלבד. המשתמש יכתוב אותו בנפרד.
- ה-`yael/reference/` עדיין ריקה — צריך לאסוף 2-3 מאמרים אמיתיים בסגנון הרצוי לפני שהפלט יהיה תואם.
- מה הפלטפורמות הסטנדרטיות שיעל כותבת אליהן (ניוזלטר? סושיאל? בלוג?) — דורש [[Brand Guidelines/_index|Brand Guidelines]] שעדיין לא קיים.

## Session Log

### 2026-05-13 — קביעת תפקיד והתחלת תיעוד [planned]
- **What was done:** תועד תפקיד יעל ככותבת — היא במורד-זרם של [[chen]] ובמעלה-זרם של [[yuval]].
- **Decisions:** עד שיוגדר agent ייעודי, כל בקשת כתיבה מנותבת ל-Claude עם הסקיל `itay-zerem-writing` כשרלוונטי.
- **Notes / Caveats:** אין כרגע בריפים פעילים ב-[[Content Briefs/_index|Content Briefs]] — תיק זה ימולא תוכן אמיתי כשתעלה משימת כתיבה ראשונה.
- **Related:** [[reuven]], [[chen]], [[yuval]], [[claude-md]], [[agents-directory]]

### 2026-05-13 — יצירת sub-agent מלא ב-`.claude/agents/yael.md` [shipped]
- **What was done:**
  - נכתב קובץ ה-agent עם YAML frontmatter: `name: yael`, `tools: Read, Write, Edit, Glob, Grep`, `model: sonnet`, `description` באנגלית עם 3 `<example>` blocks המכסים שכתוב, סיכום ותרגום.
  - גוף ה-system prompt בעברית — Workflow בן 5 שלבים, כללים נוקשים (הסרת CTAs/קישורים, שמירת מותגים בתוך הסיפור), גבולות מפורשים (אסור WebSearch/יצירת תמונות/Agent/Bash).
  - נוצרו תיקיות עבודה: `Content/`, `Output/`, `yael/reference/` — כל אחת עם `.gitkeep`.
  - עודכן [[claude-md]] בשורש: שורת יעל מקבלת trigger keywords בעברית ובאנגלית.
- **Decisions:**
  - **System prompt בעברית** (החלטת משתמש) — מתואם לרוח ה-CLAUDE.md ולתפקיד הכתיבה. ה-`description` ב-frontmatter נשאר אנגלית כי ה-routing model של Claude Code עובד טוב יותר עליה.
  - **`yael/style-guide.md` לא ייצור בסשן זה** (החלטת משתמש) — ה-agent מוגדר לבדוק קיום בעזרת Glob ולפעול לפי ברירת מחדל אם הקובץ חסר, במקום לקרוס.
  - **HTML output חובה מעוצב RTL** — `<html lang="he" dir="rtl">`, CSS inline עם פונט עברי, max-width 720px, line-height 1.7. הקפדה זו ב-system prompt מבטיחה אחידות גם בלי style-guide.
- **Notes / Caveats:**
  - יעל **לא** יכולה להפעיל סוכנים אחרים — אין לה כלי Agent. כל המלצה להעביר משימה ל-[[chen]] (אימות עובדות) או [[yuval]] (ויזואל) חייבת לעבור דרך הסיכום ל-[[reuven]] בסוף כל ריצה.
  - הכפילות בין הסקיל `itay-zerem-writing` (גלובלי) לבין ה-agent הזה (פרויקטי) לא מוכרעת — `itay-zerem-writing` הוא קול ספציפי לאיתי, יעל היא תפקיד כללי בצוות. ראובן יחליט במשימה ספציפית האם להפעיל את הסקיל בנוסף.
  - ה-routing מ-ראובן ליעל מתבסס על trigger keywords ב-CLAUDE.md — אם ראובן לא מזהה — יש לבקש במפורש "תעבירי ליעל".
- **Related:** [[reuven]], [[chen]], [[yuval]], [[claude-md]], [[agents-directory]], [[yael-agent-creation]]
