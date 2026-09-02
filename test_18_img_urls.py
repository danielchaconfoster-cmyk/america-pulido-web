import requests

prod_urls = [
    "https://www.americapulidospa.cl/img/productos/prod_sacabocado_35mm.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_resina_premium.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_resina_seco.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_ranurador_114mm.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_masilla_dermax.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_piedra_conica.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_rodillo_diamantado.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_base_pulir_reforzada.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_corte_segmentado.jpg",
    "https://www.americapulidospa.cl/img/productos/prod_panete.jpg",
    "https://www.americapulidospa.cl/img/madera-brillo.jpg",
    "https://www.americapulidospa.cl/img/calidad-brillo.jpg",
    "https://www.americapulidospa.cl/img/hormigon-industrial.jpg",
    "https://www.americapulidospa.cl/img/baldosa-comercial.jpg",
    "https://www.americapulidospa.cl/img/hero-servicios.jpg",
    "https://www.americapulidospa.cl/img/antes-despues.jpg",
    "https://www.americapulidospa.cl/img/foto-real-comercial.jpg",
    "https://www.americapulidospa.cl/img/logo-showcase.jpg"
]

for url in prod_urls:
    try:
        res = requests.head(url, timeout=5)
        print(f"{url} -> Status: {res.status_code}")
    except Exception as e:
        print(f"{url} -> Error: {e}")
