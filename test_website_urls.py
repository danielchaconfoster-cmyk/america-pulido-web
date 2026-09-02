import requests

test_url = "https://www.americapulidospa.cl/img/servicios/2.png"
try:
    res = requests.get(test_url, timeout=5)
    print(f"Website URL: {test_url} -> Status: {res.status_code}, Length: {len(res.content)}")
except Exception as e:
    print(f"Error fetching website URL: {e}")
