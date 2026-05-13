# חן — החוקרת

## Overview

חן היא חוקרת הרשת של הצוות — אחראית על מציאת תוכן רשת איכותי, מחקר רקע, ובדיקת עובדות **לפני** שהצוות מתחיל לכתוב או לעצב. היא משתמשת ב-`WebSearch` ו-`WebFetch` המובנים של Claude Code — **ללא API חיצוני וללא Bash**. שומרת זיכרון חיפושים מתמשך ב-`chen/Memory/searches.md` ובודקת אותו לפני כל חיפוש כדי למנוע עבודה כפולה ב-30 הימים האחרונים (פרט לנושאים דינמיים — חדשות, מחירים, סטטיסטיקות עדכניות). מוגדרת ב-`.claude/agents/chen.md` עם `tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Grep`. הפלט שלה: קובץ ב-`Content/<YYYY-MM-DD>-<slug>.md` עם header (Source/Retrieved/Quality/Original language) וגוף המאמר בשפת המקור. חן היא הסוכן הראשון בזרימה הטיפוסית — [[reuven]] מנתב אליה לפני [[yael]]. **חן לא מפעילה סוכנים אחרים** — היא מדווחת לראובן וזהו.

## Open Questions

- האם הסף של 30 ימים ב-memory check נכון? יכול להיות שלנושאים תכופים (AI, טכנולוגיה) צריך 14 ימים, ולנושאים יציבים (עקרונות עיצוב, תיאוריה) 60-90 ימים.
- אם בעתיד `WebSearch` המובנה לא יספיק (איכות נמוכה ב-niche queries), שווה לבחון הוספת MCP חיפוש (Perplexity, Exa) — אבל לא לפני שיש הוכחת בעיה אמיתית.
- מתי חן צריכה להמליץ "להרחיב את ה-query" מול "להחליף נושא" כשהיא לא מוצאת מקור איכותי?
- אם המאמר ארוך מאוד (10K+ מילים), עד כמה לקצץ ב-Content/? כרגע נקבע "תקציר מקיף", אבל אין מספר ברור.

## Session Log

### 2026-05-13 — קביעת תפקיד והתחלת תיעוד [planned]
- **What was done:** תועד תפקיד חן כסוכן ראשון בזרימה, וההסתמכות שלה על מפתח חיפוש ב-[[environment-config]].
- **Decisions:** חן רצה לפני יעל בזרימה הסטנדרטית — אסור לכתוב לפני שיש בסיס מחקר.
- **Notes / Caveats:** מפתח `TAVILY_API_KEY` נמצא ב-`.env.example` אבל ה-`.env` עדיין מכיל placeholder — נדרש למלא ערך אמיתי לפני המשימה הראשונה של חן.
- **Related:** [[reuven]], [[yael]], [[yuval]], [[environment-config]], [[agents-directory]]

### 2026-05-13 — chen.md נוצר ופועל + pivot מ-Tavily ל-WebSearch מובנה [shipped]
- **What was done:**
  - **`.claude/agents/chen.md`** — קובץ agent חדש. Frontmatter: `name: chen`, `tools: WebSearch, WebFetch, Read, Write, Edit, Glob, Grep` (ללא Bash, ללא Agent), `model: sonnet`. `description` באנגלית עם 3 example blocks (חיפוש טרי, cache hit, נושא דינמי). System prompt בעברית — workflow בן 8 שלבים (intent → memory check → search → filter → fetch → save → log → report), פורמט קובץ ב-`Content/` (Header + body), פורמט memory entry, וגבולות מפורשים על מה שאסור (Bash, Agent, יצירת תמונות, שכתוב, המצאת מקורות).
  - **`chen/Memory/searches.md`** — קובץ זיכרון ראשוני עם header והסבר על הפרוטוקול.
  - **`CLAUDE.md`:** השורה של חן הורחבה עם trigger keywords (עברית: חפש/מצא/מחקר/מאמר על/חדש על/מה קורה עם/מקור על; English: search/find/research/article about/latest on/news on). נוסף סעיף חדש "תהליך תוכן מהאינטרנט" עם 3 תרחישי ניתוב (רק חיפוש / חיפוש+שכתוב / רק שכתוב מקובץ קיים) וכלל decision לראובן. תיקיית `chen/` נוספה לסעיף "מבנה הפרויקט".
  - **`.env.example`:** `TAVILY_API_KEY` הוסר מהקובץ; הוספה הערה שמסבירה שחן משתמשת ב-WebSearch/WebFetch מובנים ולא דורשת מפתח.
  - **[[chen]]:** Overview שוכתב מחדש (built-in tools, memory protocol, אין API חיצוני); Open Questions עודכן (השאלות הישנות על Tavily ופורמט נסגרו, נפתחו שאלות חדשות על סף ה-30 ימים, MCP עתידי, וקיצוץ מאמרים ארוכים); Session Log entry `[shipped]` נוסף.
- **Decisions:**
  - **`WebSearch`/`WebFetch` במקום Tavily/Perplexity** — לפי החלטת המשתמש. היתרון: אין מפתח לתחזק, יכולות built-in של Claude Code, אין חוב תשתית. הוויתור: אולי איכות נמוכה יותר ב-niche queries — נראה אם זה הופך לבעיה ב-production.
  - **לא Bash, לא Agent** — חן stateless מבחינת execution (זיכרון רק דרך הקובץ), לא מפעילה אף אחד. ראובן הוא המתאם היחיד.
  - **זיכרון מתמשך ב-Markdown ולא DB** — `chen/Memory/searches.md` הוא flat file ב-Markdown שחן בודקת עם Grep. מספיק לסקייל הנוכחי, ו-human-readable.
  - **סף 30 ימים** — ברירת מחדל. נושאים דינמיים (חדשות/מחירים/סטטיסטיקות) מקבלים חריג ומתרעננים תמיד.
  - **שפת התוכן בקובץ — שפת המקור** — חן לא מתרגמת, יעל תתרגם בשלב השכתוב במידת הצורך.
  - **פורמט `Content/` עם header** — Source URL, Retrieved date, Quality stars, Original language. מקבילה מאמר עם הקשר ברור.
- **Notes / Caveats:**
  - ה-agent ייטען רק אחרי reload של הסשן. בסשן הנוכחי לא ניתן להפעיל `Agent(subagent_type='chen')`.
  - חן לא יכולה להעביר משימה ישירות ליעל — חייבת להחזיר סיכום לראובן. שמירה על ראובן כמתאם יחיד (אותה ארכיטקטורה של יעל ויובל).
  - אין vision — חן רואה רק טקסט. תמונות במאמר המקורי שלא חולצו ב-WebFetch מסומנות כ-`[תרשים חסר: ...]` בגוף, ומועברות לשיקול דעת של יעל/יובל.
  - `WebSearch` בלי vendor lock-in — אם בעתיד שווה לעבור ל-MCP חיפוש, צריך לעדכן רק את ה-frontmatter של chen.md ואת ה-workflow.
- **Related:** [[chen-agent-creation]], [[reuven]], [[yael]], [[yuval]], [[agents-directory]], [[environment-config]], [[claude-md]]
