import requests
import json
import time
from pathlib import Path

SERVICIOS_DIR = Path(r"c:\Users\usuario\Desktop\america-pulido-web\img\servicios")
CATBOX_URL = "https://catbox.moe/user/api.php"

headers_req = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

uploaded_urls = {}

print("Starting upload of 21 service images to Catbox CDN...")

for idx in range(2, 23):
    img_name = f"{idx}.png"
    img_path = SERVICIOS_DIR / img_name
    
    if not img_path.exists():
        print(f"❌ Missing file: {img_name}")
        continue

    print(f"Uploading {img_name} ({img_path.stat().st_size} bytes)...")
    
    success = False
    for attempt in range(3):
        try:
            with open(img_path, "rb") as f:
                res = requests.post(CATBOX_URL, data={"reqtype": "fileupload"}, files={"fileToUpload": (img_name, f, "image/png")}, timeout=30)
            
            up_url = res.text.strip()
            if up_url.startswith("http"):
                # Verify link
                r_chk = requests.get(up_url, headers=headers_req, timeout=10)
                if r_chk.status_code == 200 and len(r_chk.content) > 1000:
                    uploaded_urls[idx] = up_url
                    print(f"  ✅ {img_name} -> {up_url} (HTTP 200 OK, {len(r_chk.content)} bytes)")
                    success = True
                    break
                else:
                    print(f"  ⚠️ Check failed: Status {r_chk.status_code}")
            else:
                print(f"  ⚠️ Catbox response: {up_url}")
        except Exception as e:
            print(f"  ⚠️ Upload error on attempt {attempt+1}: {e}")
        time.sleep(1)
        
    if not success:
        print(f"❌ Failed to upload {img_name}")

# Save JSON mapping
out_json = Path(r"c:\Users\usuario\Desktop\america-pulido-web\servicios_cdn_urls.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(uploaded_urls, f, indent=2)

print(f"\nCompleted upload: {len(uploaded_urls)}/21 images uploaded successfully. Saved to {out_json}")
