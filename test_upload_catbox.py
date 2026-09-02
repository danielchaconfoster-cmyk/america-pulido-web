import requests
from pathlib import Path

img_path = Path(r"c:\Users\usuario\Desktop\america-pulido-web\img\servicios\2.png")
url = "https://catbox.moe/user/api.php"

with open(img_path, "rb") as f:
    res = requests.post(url, data={"reqtype": "fileupload"}, files={"fileToUpload": ("2.png", f, "image/png")})

print("Status:", res.status_code)
print("Response text:", res.text.strip())

up_url = res.text.strip()
if up_url.startswith("http"):
    r2 = requests.get(up_url)
    print("Download test:", r2.status_code, len(r2.content))
