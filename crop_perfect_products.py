import fitz, os, shutil
from PIL import Image

doc = fitz.open('America.pdf')
out_dir = 'img/productos'
pub_dir = 'public/img/productos'
os.makedirs(out_dir, exist_ok=True)
os.makedirs(pub_dir, exist_ok=True)

# Render pages at 300 DPI
scale = 300.0 / 72.0
mat = fitz.Matrix(scale, scale)

pages_img = []
for pno, page in enumerate(doc):
    pix = page.get_pixmap(matrix=mat)
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    pages_img.append(img)

# Exact bounding boxes in PDF points (72 dpi)
items = [
    # (Filename_key, page_no (0-based), [x0, y0, x1, y1])
    ("prod_resina_seco", 0, [75.8, 493.1, 405.8, 823.1]),
    ("prod_resina_premium", 0, [99.6, 892.7, 230.8, 1024.0]),
    ("prod_resina_humedo", 0, [92.6, 1170.8, 280.1, 1311.1]),
    ("prod_sacabocado_35mm", 0, [445.0, 829.3, 703.0, 1087.3]),
    
    ("prod_desbaste", 1, [140.7, 61.0, 382.2, 302.5]),
    ("prod_disco_pulidor", 1, [112.1, 298.2, 269.6, 508.2]),
    ("prod_piedra_conica", 1, [84.6, 600.2, 329.1, 844.7]),
    ("prod_disco_silicio", 1, [471.8, 303.3, 705.1, 614.5]),
    ("prod_trompo_resina", 1, [109.0, 899.1, 264.3, 1054.4]),
    ("prod_corte_segmentado", 1, [453.8, 899.8, 713.3, 1143.6]),
    ("prod_corte_continuo", 1, [118.5, 1192.5, 273.8, 1360.5]),
    
    ("prod_panete", 2, [140.7, 20.5, 382.2, 343.0]),
    ("prod_rodillo_diamantado", 2, [73.0, 243.9, 303.3, 551.4]),
    ("prod_masilla_dermax", 2, [455.3, 347.4, 721.5, 608.4]),
    ("prod_base_pulir_reforzada", 2, [82.9, 647.2, 311.6, 818.2]),
    ("prod_base_pulir_flexible", 2, [99.1, 816.8, 300.9, 1086.1])
]

for key, pno, bbox in items:
    # Add a tiny padding margin around the box
    pad = 2.0
    x0 = max(0, int((bbox[0] - pad) * scale))
    y0 = max(0, int((bbox[1] - pad) * scale))
    x1 = min(pages_img[pno].width, int((bbox[2] + pad) * scale))
    y1 = min(pages_img[pno].height, int((bbox[3] + pad) * scale))
    
    cropped = pages_img[pno].crop((x0, y0, x1, y1))
    
    fname_jpg = f"{out_dir}/{key}.jpg"
    fname_png = f"{out_dir}/{key}.png"
    
    cropped.save(fname_jpg, "JPEG", quality=98)
    cropped.save(fname_png, "PNG")
    
    # Also sync to public/img/productos
    shutil.copy(fname_jpg, f"{pub_dir}/{key}.jpg")
    shutil.copy(fname_png, f"{pub_dir}/{key}.png")
    
    print(f"Cropped and saved {key}: {cropped.size}")

print("\nALL 16 PRODUCTS CROP COMPLETE AND SYNCED TO PUBLIC!")
