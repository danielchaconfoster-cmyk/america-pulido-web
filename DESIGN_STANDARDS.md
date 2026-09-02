# 🏛️ ESTÁNDAR MAESTRO DE DISEÑO WEB LIMPIO, MINIMALISMO Y ANTI-IA
# Aplicable a todos los proyectos web del sistema (América Pulido, Danyes, Paraíso, etc.)

## 1. PROHIBICIÓN ESTRICTA DE ELEMENTOS ARTIFICIALES / CLICHÉS DE IA
- **Cero Membretes con Emojis**: NUNCA usar píldoras redondeadas con emojis (e.g. `⚡ Cotizador Inteligente`, `🔥 Oferta`, `⭐ Producto Estrella`, `🏆 Nivel Máximo`).
- **Cero Datos Falsos**: NUNCA inventar estadísticas ("99.9% satisfacción", "5000 clientes", RUTs inventados, testimonios ficticios). Usar únicamente datos reales o especificaciones técnicas comprobables.
- **Cero Estilo Juguete / Neon Exagerado**: Prohibido el uso de resplandores de neón intensos o degradados sobrecargados. El estilo debe ser sobrio, mate, minimalista y de alto valor corporativo.

## 2. TIPOGRAFÍA Y COMPOSICIÓN MINIMALISTA
- **Títulos Moderados y Elegantes**: Evitar textos gigantescos centrados que gritan. Usar tamaños controlados (`clamp(1.4rem, 2.5vw, 2.0rem)`), alineación ordenada (a la izquierda o estructurada) y espaciados generosos.
- **Bordes Finos y Materiales Refinados**: Bordes de 1px con opacidad sutil (`rgba(255,255,255,0.08)` o tonos neutros), micro-interacciones suaves y fondos de vidrio oscuro/mate.

## 3. UNIFICACIÓN DE COMPONENTES GLOBALES
- **Navbar y Footer Idénticos**: En cualquier sitio web, el `<nav>` y el `<footer>` deben tener exactamente la misma estructura HTML, mismas clases CSS, mismos enlaces y mismos estilos en todas las páginas (`index.html`, `productos.html`, `cotizador.html`, etc.).
- **Fotografía Real**: Privilegiar siempre sliders / carruseles de fotos reales de trabajos ejecutados por el cliente antes que recursos generados por IA o ilustraciones genéricas.

## 4. RESPONSIVIDAD 100% GARANTIZADA
- Diseñar mobile-first o con adaptabilidad fluida garantizada en 320px, 375px, 390px, 768px, 1024px, 1440px y 1920px.
- Cero desbordamientos horizontales (`overflow-x: hidden`), áreas táctiles de al menos 44x44px en controles móviles y drawers móviles sólidos y opacos.
