import fitz, os
from PIL import Image

doc = fitz.open('America.pdf')

for pno, page in enumerate(doc):
    print(f"\n================ PAGE {pno+1} RAW EMBEDDED IMAGES ================")
    image_list = page.get_images(full=True)
    for idx, img_info in enumerate(image_list):
        xref = img_info[0]
        base_img = doc.extract_image(xref)
        w, h = base_img['width'], base_img['height']
        ext = base_img['ext']
        
        # Skip full page background images (like page 1 marble background 1080x690)
        fname = f"img/productos/raw_p{pno+1}_img{idx+1}_{xref}.{ext}"
        with open(fname, 'wb') as f:
            f.write(base_img['image'])
        print(f"Index {idx+1} (xref {xref}): {fname} | Dimensions: {w}x{h} | Format: {ext}")
