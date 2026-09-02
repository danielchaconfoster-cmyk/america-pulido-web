import os, shutil
from PIL import Image, ImageOps

out_dir = 'img/productos'
pub_dir = 'public/img/productos'
os.makedirs(out_dir, exist_ok=True)
os.makedirs(pub_dir, exist_ok=True)

# Map key to raw extracted file
raw_map = {
    "prod_sacabocado_35mm": "img/productos/raw_p1_img5_29.png",
    "prod_resina_premium": "img/productos/raw_p1_img2_26.jpeg",
    "prod_resina_seco": "img/productos/raw_p1_img1_25.jpeg",
    "prod_resina_humedo": "img/productos/raw_p1_img3_27.jpeg",
    "prod_desbaste": "img/productos/raw_p2_img3_52.jpeg",
    "prod_disco_pulidor": "img/productos/raw_p2_img4_53.jpeg",
    "prod_piedra_conica": "img/productos/raw_p2_img2_51.jpeg",
    "prod_disco_silicio": "img/productos/raw_p2_img1_50.jpeg",
    "prod_trompo_resina": "img/productos/raw_p2_img5_58.jpeg",
    "prod_corte_segmentado": "img/productos/raw_p2_img6_59.jpeg",
    "prod_corte_continuo": "img/productos/raw_p2_img7_60.jpeg",
    "prod_panete": "img/productos/raw_p3_img3_93.jpeg",
    "prod_rodillo_diamantado": "img/productos/raw_p3_img1_91.png",
    "prod_masilla_dermax": "img/productos/raw_p3_img5_98.jpeg",
    "prod_base_pulir_reforzada": "img/productos/raw_p3_img2_92.jpeg",
    "prod_base_pulir_flexible": "img/productos/raw_p3_img4_94.jpeg"
}

target_size = (600, 600)
# Dark background matching card image wrap (#141416)
bg_color = (20, 20, 22)

for key, src_path in raw_map.items():
    if not os.path.exists(src_path):
        print(f"ERROR: missing {src_path}")
        continue
    
    img = Image.open(src_path).convert('RGBA')
    
    # Calculate scale to fit inside target_size with 8% padding
    max_w = int(target_size[0] * 0.90)
    max_h = int(target_size[1] * 0.90)
    
    img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    
    # Create canvas
    canvas = Image.new('RGBA', target_size, bg_color + (255,))
    
    # Center image
    offset_x = (target_size[0] - img.width) // 2
    offset_y = (target_size[1] - img.height) // 2
    
    # Paste using alpha channel if transparent
    canvas.paste(img, (offset_x, offset_y), img if img.mode == 'RGBA' else None)
    
    # Save RGB JPG and RGBA PNG
    canvas_rgb = canvas.convert('RGB')
    
    dst_jpg = f"{out_dir}/{key}.jpg"
    dst_png = f"{out_dir}/{key}.png"
    
    canvas_rgb.save(dst_jpg, 'JPEG', quality=95)
    canvas.save(dst_png, 'PNG')
    
    # Copy to public/img/productos
    shutil.copy(dst_jpg, f"{pub_dir}/{key}.jpg")
    shutil.copy(dst_png, f"{pub_dir}/{key}.png")
    
    print(f"Processed {key}: {src_path} -> 600x600 centered photo")

print("\nALL 16 PURE RAW PRODUCT PHOTOS PROCESSED & CENTERED!")
