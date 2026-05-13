# Plugin: skill-creator (project scope)

## Overview

תקנת ה-plugin `skill-creator@claude-plugins-official` (מ-marketplace `anthropics/claude-plugins-official`) בהיקף **project** עבור `the-five-agents`. ההתקנה רושמת `enabledPlugins` בקובץ `.claude/settings.json` בתוך הריפו, כך ששיתוף/clone של הפרויקט מפעיל את ה-plugin אוטומטית לכל מי שעובד בו. מקור הסקיל המקורי: https://github.com/anthropics/skills/tree/main/skills/skill-creator, מוגש דרך ה-marketplace הרשמי.

## Open Questions

- האם להוסיף עוד plugins ב-project scope (למשל `frontend-design`, `context7`) כדי שכל הצוות יקבל אותם בלי תלות בהתקנה גלובלית?
- ה-plugin גם מותקן ב-user scope וגם ב-project scope — האם זה גורם לקונפליקט, או ש-Claude Code פשוט מציג סקיל אחד? (נראה ב-`Available skills`: כפילות `skill-creator:skill-creator` ו-`anthropic-skills:skill-creator`.)

## Session Log

### 2026-05-13 — התקנת skill-creator ב-project scope [shipped]
- **What was done:**
  - אומת ש-marketplace `claude-plugins-official` כבר רשום (`anthropics/claude-plugins-official`).
  - הורץ `claude plugin install skill-creator@claude-plugins-official --scope project` → הצליח.
  - נוצר `.claude/settings.json` עם `{ "enabledPlugins": { "skill-creator@claude-plugins-official": true } }`.
  - אומת ב-`claude plugin list --json` ש-scope=project ו-projectPath תואם ל-`C:\Users\zerem\Desktop\workspace\the-five-agents`.
- **Decisions:**
  - לא נדרשו fallback-ים (שלבים 2-3 בהוראת המשתמש) — שלב 1 הצליח ישירות.
  - בוצע commit ל-`.claude/settings.json` בלבד כדי לשמר את מצב ההתקנה בפרויקט; קבצים ישנים שלא קומיטו (vault/, .obsidian/, .claude/skills/) נשארו בחוץ כי הם שייכים לסשנים קודמים שלא נסגרו.
- **Notes / Caveats:**
  - ה-plugin כבר היה מותקן ב-project scope מתאריך 2026-05-06; הרצת הפקודה מחדש היא idempotent ועדכנה את חותמת הזמן.
  - ה-metadata האמיתי של ההתקנה יושב גלובלית ב-`~/.claude/plugins/installed_plugins.json` (לפי `projectPath`); רק ה-`enabledPlugins` יושב ב-repo.
  - יש כפילות גלויה ב-`Available skills` (גם תחת `skill-creator:`, גם תחת `anthropic-skills:`) — שתי הגרסאות מצביעות לאותו מקור marketplace, אבל זה ראוי למעקב.
- **Related:** [[skills-directory]], [[claude-directory]], [[vault-bootstrap]], [[reuven]]
