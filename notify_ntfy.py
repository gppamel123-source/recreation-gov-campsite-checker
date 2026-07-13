import os
import sys

import requests

NTFY_TOPIC = os.environ.get("NTFY_TOPIC") or "gp-mine-yosemite-alert-g1p2"
SUCCESS_EMOJI = "🏕"

def main():
    lines = sys.stdin.readlines()
    hits = [l.strip() for l in lines if SUCCESS_EMOJI in l]
    if hits:
        message = "\n".join(hits)
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=message.encode("utf-8"),
            headers={"Title": "Yosemite campsite available!", "Priority": "urgent"},
        )
        print("Notification sent:", message)
    else:
        print("No campsites available, no notification sent.")

if __name__ == "__main__":
    main()
