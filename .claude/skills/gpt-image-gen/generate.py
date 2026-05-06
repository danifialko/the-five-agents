import os, json, base64, urllib.request, urllib.error, sys

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
    body = urllib.request.urlopen(req, timeout=180).read()
except urllib.error.HTTPError as e:
    sys.stderr.write(f"HTTP {e.code}\n")
    sys.stderr.write(e.read().decode() + "\n")
    sys.exit(1)

resp = json.loads(body)
if "data" not in resp or not resp["data"]:
    sys.stderr.write(f"No data in response: {resp}\n")
    sys.exit(1)

with open(OUTPUT, "wb") as f:
    f.write(base64.b64decode(resp["data"][0]["b64_json"]))

print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")
