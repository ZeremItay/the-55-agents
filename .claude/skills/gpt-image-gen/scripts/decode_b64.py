#!/usr/bin/env python3
"""
Read an OpenAI Images API response from stdin, extract data[0].b64_json,
decode it, and write the resulting PNG to argv[1].

Usage:
    cat response.json | python decode_b64.py out.png
    echo "$RESPONSE" | python decode_b64.py path/to/out.png

Exit codes:
    0 — success
    1 — bad JSON or missing b64_json field (response printed to stderr)
    2 — wrong arguments
"""
import base64
import json
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: decode_b64.py <output_path>", file=sys.stderr)
        return 2

    output_path = sys.argv[1]
    raw = sys.stdin.read()

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"ERROR: response is not valid JSON ({exc})", file=sys.stderr)
        print(raw, file=sys.stderr)
        return 1

    try:
        b64 = payload["data"][0]["b64_json"]
    except (KeyError, IndexError, TypeError):
        print("ERROR: response missing data[0].b64_json", file=sys.stderr)
        print(json.dumps(payload, indent=2, ensure_ascii=False), file=sys.stderr)
        return 1

    with open(output_path, "wb") as fh:
        fh.write(base64.b64decode(b64))

    return 0


if __name__ == "__main__":
    sys.exit(main())
