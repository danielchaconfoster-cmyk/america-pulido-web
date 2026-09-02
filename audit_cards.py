import re

with open('productos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all <div class="producto-card" ...> ... </div> blocks
cards = re.findall(r'<div class="producto-card".*?>(.*?)(?=<!-- \d+\.|\s*</div>\s*<!-- Wholesale|\s*</div>\s*</div>\s*</section>)', content, re.DOTALL)

print(f"Found {len(cards)} card blocks:\n")

for idx, card in enumerate(cards):
    title_match = re.search(r'<h3>(.*?)</h3>', card)
    price_match = re.search(r'<div class="producto-price">(.*?)</div>', card, re.DOTALL)
    img_match = re.search(r'<img [^>]*class="producto-img"[^>]*src="([^"]+)"', card)
    if not img_match:
        img_match = re.search(r'<img [^>]*src="([^"]+)"[^>]*class="producto-img"', card)
        
    title = title_match.group(1).strip() if title_match else "N/A"
    price = re.sub(r'\s+', ' ', price_match.group(1).strip()) if price_match else "N/A"
    img = img_match.group(1) if img_match else "N/A"
    
    print(f"{idx+1:2d}. {title:<35} | Price: {price:<25} | Img: {img}")
