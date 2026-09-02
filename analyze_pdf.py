import fitz, os

doc = fitz.open('America.pdf')

for pno, page in enumerate(doc):
    print(f"\n============================== PAGE {pno+1} ==============================")
    images = page.get_image_info(hashes=False)
    blocks = page.get_text('blocks')
    blocks.sort(key=lambda b: (b[1], b[0]))
    for b in blocks:
        txt = b[4].strip().replace('\n', ' ')
        if txt:
            print(f"Text [{b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}]: {txt}")
    
    print("--- Images ---")
    for idx, img in enumerate(images):
        bbox = img['bbox']
        w, h = img['width'], img['height']
        print(f"Img {idx+1} [bbox: {bbox[0]:.1f}, {bbox[1]:.1f}, {bbox[2]:.1f}, {bbox[3]:.1f}], dim: {w}x{h}")
