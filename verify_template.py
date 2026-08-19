#!/usr/bin/env python3
import json
with open("/tmp/verify.json") as f:
    data = json.load(f)
print(f"{len(data)} sections loaded:")
for s in data:
    sid = s.get('id', '?')
    title = s.get('settings', {}).get('_title', '?')
    print(f"  - {sid}: {title}")
