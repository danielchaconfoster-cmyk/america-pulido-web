import fitz, os
from PIL import Image

doc = fitz.open('America.pdf')
out_dir = 'img/productos'
os.makedirs(out_dir, exist_ok=True)

# Render pages at 300 DPI (scale 4.166666 = 300/72)
scale = 300.0 / 72.0
mat = fitz.Matrix(scale, scale)

pages_img = []
for pno, page in enumerate(doc):
    pix = page.get_pixmap(matrix=mat)
    img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
    pages_img.append(img)
    print(f"Rendered Page {pno+1}: {img.size}")

# Let's define the EXACT bounding box (in PDF points, 72 dpi) for each product image on each page:
# Page 1 (W=810.5, H=1440 roughly or 810x1440):
# 1. Disco de resina en seco:
#    Image box: [75.8, 493.1, 405.8, 823.1]
# 2. Disco de Resina Premium:
#    Image box: [99.6, 892.7, 230.8, 1024.0] -> Wait, on Page 1:
#    Let's check [120, 615, 275, 770] or similar. Let's inspect the page image directly.

