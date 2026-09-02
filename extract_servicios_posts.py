import csv
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

csv_path = Path(r"c:\Users\usuario\Desktop\america-pulido-web\calendario_6_semanas_america_pulido.csv")

posts = []
with open(csv_path, mode='r', encoding='utf-8-sig') as f: # utf-8-sig removes BOM if present
    reader = csv.reader(f)
    header = next(reader)
    print("Header columns:", header)
    for row in reader:
        if not row or len(row) < 3:
            continue
        datetime_str = row[0].strip()
        text = row[1].strip()
        img_url = row[2].strip()
        platform = row[3].strip() if len(row) > 3 else "Instagram"
        
        parts = datetime_str.split(' ')
        date_part = parts[0]
        time_part = parts[1] if len(parts) > 1 else "20:00:00"
        
        posts.append({
            "date": date_part, # YYYY-MM-DD
            "time": time_part, # HH:MM:SS
            "text": text,
            "img_url": img_url,
            "platform": platform
        })

print(f"Extracted {len(posts)} posts from calendario_6_semanas_america_pulido.csv.")
for idx, p in enumerate(posts, 1):
    first_line = p['text'].split('\n')[0]
    print(f"Post {idx:2d} | Date: {p['date']} | Time: {p['time']} | Title: {first_line[:45]}... | Img: {p['img_url']}")

out_json = Path(r"c:\Users\usuario\Desktop\america-pulido-web\extracted_servicios_posts.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"Saved to {out_json}")
