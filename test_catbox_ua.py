import requests
from pathlib import Path

img_path = Path(r"c:\Users\usuario\Desktop\america-pulido-web\img\servicios\2.png")
url = "https://catbox.moe/user/api.php"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

with open(img_path, "rb") as f:
    res = requests.post(url, data={"reqtype": "fileupload"}, files={"fileToUpload": ("2.png", f, "image/png")})

up_url = res.text.strip()
print("Uploaded URL:", up_url)

r2 = requests.get(up_url, headers=headers, timeout=10)
print("Get with UA header status:", r2.status_code, "Length:", len(r2.content))
