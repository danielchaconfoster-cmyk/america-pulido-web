import requests

urls = [
    "https://files.catbox.moe/oxieec.png",
    "https://files.catbox.moe/kgr9wz.png",
    "https://files.catbox.moe/1zcs2a.png"
]

for url in urls:
    try:
        res = requests.head(url, timeout=5)
        print(f"{url} -> Status: {res.status_code}, Content-Type: {res.headers.get('content-type')}")
    except Exception as e:
        print(f"{url} -> Error: {e}")
