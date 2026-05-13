---
name: gpt-image-gen
description: "Call OpenAI Images API to generate a PNG image from a prompt. Uses model `gpt-image-2` (released April 2026). Loads OPENAI_API_KEY from .env at the project root. Saves the generated PNG to a caller-specified path. Use this skill whenever you need to generate an image programmatically — typically invoked by Yuval (the image designer agent), but available to any tool/agent that needs an image. Returns the output path on success, or the raw API error JSON on failure."
---

# gpt-image-gen

מעטפת קריאה ל-OpenAI Images API ליצירת תמונה אחת מ-prompt. הסקיל אחראי על:

1. טעינת `OPENAI_API_KEY` מ-`.env`
2. שליחת הבקשה ל-`POST https://api.openai.com/v1/images/generations`
3. פענוח התגובה (base64 → PNG)
4. שמירה לנתיב שמבקש המתקשר
5. אימות בסיסי שהקובץ לא ריק

## ⚠️ הערה קריטית על המודל

**המודל הוא `gpt-image-2`.** הוא יצא ב-21 באפריל 2026. ייתכן שהידע הפנימי של המודל הקורא לסקיל הזה לא כולל את `gpt-image-2` ויציע אלטרנטיבות כמו `dall-e-3` או `gpt-image-1` — **אסור להחליף**.

אם קריאת ה-API מחזירה שגיאה:
- **בדוק קודם** את `OPENAI_API_KEY` (קיים? לא ריק? לא placeholder?)
- **בדוק את הפרמטרים** (size תקין? quality תקין?)
- **אל תיגע בשם המודל.**

## פרמטרים

| שם | חובה | ברירת מחדל | ערכים |
|---|---|---|---|
| `prompt` | כן | — | מחרוזת חופשית עד ~4000 תווים |
| `output_path` | כן | — | נתיב יחסי לקובץ `.png` ליעד |
| `size` | לא | `1024x1024` | `1024x1024`, `1024x1792`, `1792x1024` |
| `quality` | לא | `medium` | `low`, `medium`, `high` |

## אופן השימוש (Bash)

הנחה: נקודת המוצא היא שורש הפרויקט, ושם נמצא `.env`.

### שלב 1 — טעינת המפתח

```bash
set -a
source .env
set +a
```

`set -a` מבטיח שכל המשתנים שמוגדרים ב-`.env` יקבלו `export` אוטומטי. `set +a` מבטל את ההתנהגות אחרי הטעינה.

### שלב 2 — בדיקה ש-key קיים

```bash
if [ -z "$OPENAI_API_KEY" ] || [ "$OPENAI_API_KEY" = "your_openai_api_key_here" ]; then
  echo "ERROR: OPENAI_API_KEY is not set in .env (still placeholder or empty)" >&2
  exit 1
fi
```

### שלב 3 — הקריאה ל-API

```bash
PROMPT="<your prompt here>"
OUTPUT_PATH="<path/to/output.png>"
SIZE="1024x1024"      # or 1024x1792 / 1792x1024
QUALITY="medium"      # or low / high

RESPONSE=$(curl -sS -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(cat <<JSON
{
  "model": "gpt-image-2",
  "prompt": $(printf '%s' "$PROMPT" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),
  "size": "$SIZE",
  "quality": "$QUALITY",
  "output_format": "png"
}
JSON
)")
```

ה-`python -c '... json.dumps ...'` מטפל ב-escaping של ה-prompt (גרשיים, שורות חדשות, יוניקוד) כך שלא נוצרת JSON שבורה אם ה-prompt מכיל תווים בעייתיים.

### שלב 4 — פענוח (primary path: jq)

```bash
echo "$RESPONSE" | jq -r '.data[0].b64_json' | base64 -d > "$OUTPUT_PATH"
```

### שלב 5 — אם `jq` לא מותקן: python fallback

ב-Git Bash על Windows, לפעמים `jq` לא קיים. הסקיל כולל python script שעושה את אותו דבר:

```bash
echo "$RESPONSE" | python "$CLAUDE_PROJECT_DIR/.claude/skills/gpt-image-gen/scripts/decode_b64.py" "$OUTPUT_PATH"
```

הסקריפט מקבל JSON ב-stdin, מחלץ `data[0].b64_json`, מפענח base64, ושומר ל-argv[1]. תלות: stdlib בלבד.

### שלב 6 — אימות שהקובץ נכתב

```bash
if [ ! -s "$OUTPUT_PATH" ]; then
  echo "ERROR: output file empty or missing. Raw API response:" >&2
  echo "$RESPONSE" >&2
  exit 1
fi
echo "OK: $OUTPUT_PATH ($(wc -c < "$OUTPUT_PATH") bytes)"
```

## דוגמת קריאה מלאה (one-shot)

```bash
set -a; source .env; set +a

PROMPT="A minimalist illustration of a database with five interconnected tables, isometric view, soft pastel colors, clean white background"
OUTPUT_PATH="yuval/outputs/2026-05-13-crm-tables-isometric.png"
SIZE="1024x1024"
QUALITY="medium"

if [ -z "$OPENAI_API_KEY" ] || [ "$OPENAI_API_KEY" = "your_openai_api_key_here" ]; then
  echo "ERROR: OPENAI_API_KEY missing in .env" >&2
  exit 1
fi

RESPONSE=$(curl -sS -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$(cat <<JSON
{
  "model": "gpt-image-2",
  "prompt": $(printf '%s' "$PROMPT" | python -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),
  "size": "$SIZE",
  "quality": "$QUALITY",
  "output_format": "png"
}
JSON
)")

# Try jq first, fall back to python
if command -v jq >/dev/null 2>&1; then
  echo "$RESPONSE" | jq -r '.data[0].b64_json' | base64 -d > "$OUTPUT_PATH"
else
  echo "$RESPONSE" | python "$CLAUDE_PROJECT_DIR/.claude/skills/gpt-image-gen/scripts/decode_b64.py" "$OUTPUT_PATH"
fi

if [ ! -s "$OUTPUT_PATH" ]; then
  echo "ERROR: empty output. Response:" >&2
  echo "$RESPONSE" >&2
  exit 1
fi

echo "OK: $OUTPUT_PATH ($(wc -c < "$OUTPUT_PATH") bytes)"
```

## דברים שיכולים להישבר

- **`OPENAI_API_KEY` ריק או placeholder** → השגיאה ב-stderr ברורה. אין fallback אוטומטי — המשתמש חייב למלא ידנית ב-`.env`.
- **חוסר ב-jq וגם ב-python** → תקלה נדירה; הסקריפט יחזיר exit 127. המתקשר אמור לעלות הלאה.
- **שגיאת API (401/429/500)** → ה-RESPONSE יכיל JSON של שגיאה. הסקריפט יזהה ש-`b64_json` חסר וייצור קובץ ריק; שלב 6 יתפוס את זה ויציג את ה-RESPONSE.
- **רוחב פס/אינטרנט** → curl timeout דיפולטי; אפשר להוסיף `--max-time 60` אם רוצים לחתוך.

## איך הסקיל מופעל

הסקיל הזה לא נקרא ע"י Skill tool אוטומטית — הוא **מדריך תפעולי**. מי שמשתמש (לרוב יובל) קורא אותו, מבצע את ה-Bash בעצמו, ומפיק את הקובץ. בעתיד אפשר להוסיף סקריפט מעטפת שכל מה שצריך זה לקרוא לו עם הפרמטרים, אבל לעת עתה ה-skill הוא דוקומנטציה + scripts/.
