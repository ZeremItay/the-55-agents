# Chen — Agent Creation

## Overview

יצירת ה-sub-agent השלישי בצוות: **חן**, חוקרת הרשת. שלושה רכיבים שמתחברים יחד:

1. **Sub-agent `chen`** — קובץ `.claude/agents/chen.md` עם `tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Grep` (ללא Bash, ללא Agent). System prompt בעברית בן 8 שלבים: intent → memory check → search → filter → fetch → save → log → report.
2. **זיכרון חיפושים** — `chen/Memory/searches.md`, flat Markdown file. חן בודקת אותו עם Grep לפני כל חיפוש כדי למנוע עבודה כפולה ב-30 הימים האחרונים (פרט לנושאים דינמיים).
3. **CLAUDE.md** — חן נוספה לרשימת הצוות עם trigger keywords. סעיף חדש "תהליך תוכן מהאינטרנט" מגדיר 3 תרחישי ניתוב לראובן (רק חיפוש / חיפוש+שכתוב / רק שכתוב מקובץ קיים).

**שינוי ארכיטקטוני חשוב:** מעבר מ-Tavily/Perplexity ל-`WebSearch`/`WebFetch` המובנים של Claude Code. ה-spec הקודם של חן ([[chen]], [[environment-config]]) הניח שימוש ב-API חיצוני ו-`TAVILY_API_KEY`. המעבר מבטל את התלות, מפשט את הסטאק, ולא דורש מפתח. הסיכון: אולי איכות נמוכה יותר ב-niche queries.

הזרימה הסטנדרטית עכשיו: ראובן → חן (מקור) → יעל (שכתוב) → יובל (תמונות) → שילוב ב-`Output/`. ראובן הוא המתאם היחיד — חן לא קוראת לסוכנים אחרים.

## Open Questions

- **סף 30 ימים ב-memory check** — האם זה הסף הנכון לכל הנושאים? נושאים דינמיים מתרעננים תמיד, אבל אולי שווה להבדיל גם בין "טכנולוגיה תכופה" ל"תיאוריה יציבה".
- **איכות `WebSearch` מובנה ב-niche queries** — נראה ב-production האם יש פער מול Tavily/Perplexity. אם כן — אפשר להוסיף MCP חיפוש בעתיד בלי לשנות את הארכיטקטורה.
- **קיצוץ מאמרים ארוכים** (10K+ מילים) — כרגע נכתב "תקציר מקיף" כברירת מחדל. כדאי לקבוע מספר מילים מקסימלי ב-`Content/` כדי שיעל לא תקבל context-bomb.
- **שאלת הדיווח הקצר** — חן מחזירה 3 שדות: filename + 1-2 משפטים + לינק. האם יעל זקוקה ל-summary של התוכן עצמו או שזה כפילות?

## Session Log

### 2026-05-13 — יצירת chen.md + memory + CLAUDE.md update [shipped]
- **What was done:**
  - **`.claude/agents/chen.md`** — קובץ agent חדש (~150 שורות). Frontmatter עם `tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Grep`, `model: sonnet`, ו-3 example blocks (חיפוש טרי / cache hit / נושא דינמי). System prompt בעברית עם workflow מובנה בן 8 שלבים, פורמט קובץ ב-`Content/` (Header + body), פורמט memory entry, וגבולות מפורשים (אין Bash, אין Agent, לא להמציא, לא לשכתב).
  - **`chen/Memory/searches.md`** — קובץ זיכרון ראשוני עם header והסבר על הפרוטוקול.
  - **`CLAUDE.md`** — השורה של חן הורחבה: triggers בעברית (חפש/מצא/מחקר/מאמר על/חדש על/מה קורה עם/מקור על) ובאנגלית (search/find/research/article about/latest on/news on), הפניה לקובץ ה-agent, והערה על כלים מותרים. תיקיית `chen/` נוספה לסעיף "מבנה הפרויקט". סעיף חדש "תהליך תוכן מהאינטרנט" עם 3 תרחישים וכלל decision לראובן (חיפוש בלבד / חיפוש+שכתוב / שכתוב ישיר).
  - **`.env.example`** — הוסר `TAVILY_API_KEY` (כולל comment); הוספה הערה שמסבירה שחן משתמשת ב-WebSearch/WebFetch מובנים.
  - **vault topic files עודכנו:**
    - [[chen]] — Overview שוכתב מחדש (built-in tools במקום Tavily); Open Questions עודכן (שאלות ישנות נסגרו, חדשות נפתחו); Session Log entry `[shipped]`.
    - [[agents-directory]] — Overview עודכן ש-chen.md פעיל; Open Question של tools של חן נסגרה; Session Log entry `[shipped]`.
    - [[environment-config]] — `TAVILY_API_KEY` הוסר מ-Overview; Session Log entry `[shipped]` על ההסרה.
- **Decisions:**
  - **`WebSearch`/`WebFetch` במקום Tavily/Perplexity** — לפי החלטת המשתמש. היתרון: אין מפתח לתחזק, אין חוב תשתית, חיפוש זמין כברירת מחדל בכל סשן Claude Code. החיסרון: ייתכן פער איכות ב-niche queries — נמתין לראיה מ-production.
  - **`tools` ב-frontmatter ולא רק בהוראות** — אכיפה ברמת המערכת. ניסיון של חן להפעיל Bash בעתיד יחזיר InputValidationError. אותו pattern של [[yael]] ו-[[yuval]].
  - **זיכרון חיפושים ב-Markdown ולא DB** — `chen/Memory/searches.md` הוא flat file ש-Grep מספיק לסקייל הנוכחי. יתרון: human-readable, ראובן יכול לקרוא ידנית, ניתן לחיפוש פשוט.
  - **סף 30 ימים** + **חריג לנושאים דינמיים** — חדשות/מחירים/סטטיסטיקות מתרעננים תמיד גם אם יש hit. שאר הנושאים יקבלו cache hit עד 30 יום.
  - **שפת התוכן בקובץ — שפת המקור** — חן לא מתרגמת. יעל תתרגם בשלב השכתוב במידת הצורך. שמירה על נאמנות למקור.
  - **פורמט header** — Source URL, Retrieved date, Quality stars (⭐ 1-5), Original language. מבנה אחיד שיעל יכולה לפרסר אם צריך.
  - **דיווח מינימלי** — חן מחזירה רק filename + 1-2 משפטים + לינק. לא מציפה את ראובן ב-summary שכבר נמצא בקובץ.
  - **חן לא קוראת ליעל ישירות** — שמירה על ראובן כמתאם יחיד. אותה ארכיטקטורה של [[yael]] ו-[[yuval]] — אף סוכן לא יכול להפעיל אחרים.
  - **3 תרחישי ניתוב ב-CLAUDE.md** — חיפוש בלבד עוצר אחרי חן; חיפוש+שכתוב ממשיך אוטומטית; שכתוב מקובץ קיים (`Content/<file>.md` ספציפי) מדלג על חן.
- **Notes / Caveats:**
  - ה-agent ייטען רק אחרי reload של הסשן. בסשן הנוכחי לא ניתן להפעיל `Agent(subagent_type='chen')` — תיבדק בסשן הבא.
  - לא בוצעה קריאת `WebSearch` אמיתית כחלק מהסשן — רק יצירת ה-agent ותשתית. ראובן יזמן את חן במשימה הבאה.
  - שלושת ה-agents (יעל, יובל, חן) כעת פעילים. ראובן הוא היחיד שמוגדר ב-`CLAUDE.md` ולא כ-agent ייעודי — שאלה פתוחה ב-[[agents-directory]].
  - `Content/מאמר CRM.txt` הקיים מקודם לא עוקב אחרי convention החדש (`<YYYY-MM-DD>-<slug>.md`) — לא נגעתי בו, יישאר legacy. חיפושים עתידיים של חן יצרו קבצים בפורמט החדש.
- **Related:** [[chen]], [[yael]], [[yuval]], [[reuven]], [[agents-directory]], [[environment-config]], [[claude-md]], [[yael-agent-creation]], [[yuval-and-gpt-image-gen]]
