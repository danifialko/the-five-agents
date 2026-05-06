---
name: gpt-image-gen
description: Generate images via OpenAI Images API (gpt-image-2). Use when an agent needs to produce a PNG from a text prompt — wraps the HTTP call, decodes the base64 response, and writes the file to disk. Requires OPENAI_API_KEY in .env.
---

# gpt-image-gen — OpenAI Images API Wrapper

מעטפת מינימלית סביב `POST https://api.openai.com/v1/images/generations`. כל סוכן בפרויקט שצריך לייצר תמונה משתמש בסקיל הזה ולא קורא ל-API ישירות.

## Inputs

- `PROMPT` (str, חובה) — תיאור מילולי של התמונה הרצויה (מומלץ באנגלית).
- `OUTPUT` (str, חובה) — נתיב יעד מלא, חייב להסתיים ב-`.png`.
- `SIZE` (str, אופציונלי) — `1024x1024` (default), `1024x1536`, `1536x1024`.
- `QUALITY` (str, אופציונלי) — `low` / `medium` (default) / `high`.

## Loading the API key

המפתח חייב להיות זמין כ-`OPENAI_API_KEY` ב-environment. ב-Git Bash:

```bash
set -a; source .env; set +a
```

ב-Python: `os.environ['OPENAI_API_KEY']` (אחרי `set -a; source .env; set +a` או `python-dotenv`).

**אסור** לכלול את המפתח ב-prompt, ב-log, או בקובץ הפלט.

## Recommended path — PowerShell (Windows)

ב-Windows אין tipically `python`/`jq` ב-PATH, אבל PowerShell תמיד זמין ויש לו JSON + base64 מובנים. **זה הנתיב הראשי בפרויקט הזה.**

```powershell
$envFile = Get-Content .env | Where-Object { $_ -match '^OPENAI_API_KEY=' }
$key = ($envFile -split '=', 2)[1].Trim()
$prompt = (Get-Content $env:PROMPT_FILE -Raw).Trim()   # or assign $prompt directly
$out = $env:OUTPUT
$body = @{
  model="gpt-image-2"; prompt=$prompt; size="1024x1024";
  quality="medium"; output_format="png"
} | ConvertTo-Json -Compress
$bytes = [System.Text.Encoding]::UTF8.GetBytes($body)   # critical for non-ASCII

$resp = Invoke-RestMethod `
  -Uri "https://api.openai.com/v1/images/generations" `
  -Method Post `
  -Headers @{Authorization="Bearer $key"} `
  -ContentType "application/json; charset=utf-8" `
  -Body $bytes -TimeoutSec 240

$abs = (Resolve-Path .).Path + "\" + $out.Replace('/','\')
[IO.File]::WriteAllBytes($abs, [Convert]::FromBase64String($resp.data[0].b64_json))
Write-Output ("wrote " + $out + " (" + (Get-Item $out).Length + " bytes)")
```

**חשוב — UTF-8 encoding לגוף הבקשה.** בלי זה ה-API מחזיר 400 (`unicode decode error`).

על שגיאת `400 invalid_json` או `moderation_blocked` — קרא את `$_.ErrorDetails.Message` (לא רק `$_.Exception.Message`) כדי לראות את גוף השגיאה האמיתי מ-OpenAI.

## How to call — bash + jq (אופציונלי — רק אם jq זמין)

```bash
set -a; source .env; set +a

curl -sS -X POST "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"gpt-image-2\",
    \"prompt\": \"$PROMPT\",
    \"size\": \"$SIZE\",
    \"quality\": \"$QUALITY\",
    \"output_format\": \"png\"
  }" | jq -r '.data[0].b64_json' | base64 --decode > "$OUTPUT"
```

## How to call — Python fallback (אם python מותקן)

```python
import os, json, base64, urllib.request, sys

PROMPT  = os.environ["PROMPT"]
OUTPUT  = os.environ["OUTPUT"]
SIZE    = os.environ.get("SIZE", "1024x1024")
QUALITY = os.environ.get("QUALITY", "medium")

payload = json.dumps({
    "model": "gpt-image-2",
    "prompt": PROMPT,
    "size": SIZE,
    "quality": QUALITY,
    "output_format": "png",
}).encode()

req = urllib.request.Request(
    "https://api.openai.com/v1/images/generations",
    data=payload,
    headers={
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    },
)

try:
    body = urllib.request.urlopen(req, timeout=120).read()
except urllib.error.HTTPError as e:
    sys.stderr.write(e.read().decode())
    raise

resp = json.loads(body)
if "data" not in resp or not resp["data"]:
    raise RuntimeError(f"No data in response: {resp}")

with open(OUTPUT, "wb") as f:
    f.write(base64.b64decode(resp["data"][0]["b64_json"]))

print(f"wrote {OUTPUT}")
```

הפעלה:

```bash
set -a; source .env; set +a
PROMPT="a calm tabby cat sitting on a windowsill, soft morning light" \
OUTPUT="forlan/outputs/2026-05-06-cat.png" \
python .claude/skills/gpt-image-gen/generate.py
```

(אם הפייתון מועתק ישירות לתוך Bash — אותו הדבר עם `python -c "..."`.)

## Verification

אחרי הריצה, בלי יוצא מן הכלל:

```bash
test -s "$OUTPUT" && echo "OK $(stat -c%s "$OUTPUT") bytes" || { echo "FAIL: $OUTPUT missing or empty"; exit 1; }
```

## Errors

- אם תגובת ה-API לא מכילה `data[0].b64_json` — דווח את `error.message` המלא ועצור. אל תייצר קובץ ריק.
- אם `OPENAI_API_KEY` לא קיים — עצור עם הודעה ברורה. אל תנסה לקרוא ל-API ללא מפתח.
- אם המפתח לא תקף (401) — דווח למשתמש; אל תרגנר.
- **`moderation_blocked` (400)** — ה-prompt נדחה ע"י safety filter. רכך ניסוח (החלף "terrified"→"surprised", "panicked"→"playful", וכו'), נסה שוב פעם אחת. אם נחסם פעמיים — דווח למשתמש.
- **`invalid_json` עם "unicode decode error"** — שכחת UTF-8 encoding לגוף הבקשה. השתמש ב-`[System.Text.Encoding]::UTF8.GetBytes($body)` לפני שליחה.

## Rate limits / retries

הסקיל הזה לא מבצע retry אוטומטי. אם תקבל 429 — חזור למשתמש; אל תכניס loops.
