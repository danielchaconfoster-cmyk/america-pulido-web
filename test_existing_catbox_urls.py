import requests
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

csv_file = Path(r"c:\Users\usuario\Desktop\america-pulido-web\calendario_6_semanas_america_pulido.csv")
content = csv_file.read_text(encoding="utf-8")

urls = re.findall(r'https://files\.catbox\.moe/\w+\.png', content)
print(f"Found {len(urls)} catbox URLs in calendario_6_semanas_america_pulido.csv:")

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
})

working_urls = []
for idx, url in enumerate(urls, 1):
    try:
        res = session.get(url, timeout=10)
        if res.status_code == 200:
            print(f"Post {idx}: {url} -> OK ({len(res.content)} bytes)")
            working_urls.append(url)
        else:
            print(f"Post {idx}: {url} -> Status {res.status_code}")
    except Exception as e:
        print(f"Post {idx}: {url} -> Error: {e}")

print(f"\nWorking URLs: {len(working_urls)}/{len(urls)}")
