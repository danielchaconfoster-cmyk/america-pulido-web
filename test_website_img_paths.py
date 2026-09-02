import requests

urls = [
    "https://www.americapulidospa.cl/img/hero-servicios.jpg",
    "https://www.americapulidospa.cl/img/madera-brillo.jpg",
    "https://www.americapulidospa.cl/img/calidad-brillo.jpg",
    "https://www.americapulidospa.cl/img/servicios/2.png"
]

for url in urls:
    try:
        res = requests.get(url, timeout=5)
        print(f"{url} -> Status: {res.status_code}, Length: {len(res.content)}")
    except Exception as e:
        print(f"{url} -> Error: {e}")
