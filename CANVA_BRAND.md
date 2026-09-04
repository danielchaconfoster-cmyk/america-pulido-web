# Canva Brand Guide — America Pulido SPA
> Referencia universal para cualquier asistente de IA (Antigravity, Gemini, Claude, Cursor) al crear proyectos o gestionar diseños en Canva vía MCP.

## Configuración de Canva MCP (mcp-remote)

Cualquier cliente o IDE con soporte MCP puede conectar a Canva usando esta configuración guardada en [mcp.json](file:///c:/Users/usuario/Desktop/america-pulido-web/mcp.json):

```json
{
  "mcpServers": {
    "Canva": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@latest",
        "https://mcp.canva.com/mcp"
      ]
    }
  }
}
```

- **Comando de ejecución:** `npx -y mcp-remote@latest https://mcp.canva.com/mcp`
- **¿Qué es?**: Conector puente (stdio bridge) que enlaza cualquier interfaz de IA con la API oficial y remota de Canva (`https://mcp.canva.com/mcp`).

| Elemento | Valor |
|----------|-------|
| **Nombre** | America Pulido SPA |
| **Tagline** | Pulido Profesional de Pisos |
| **Tono** | Profesional, confiable, premium pero accesible |
| **Estilo** | Oscuro, elegante, gold como acento de lujo |

## Paleta de Colores

| Nombre | HEX | Uso |
|--------|-----|-----|
| Gold principal | `#D4A843` | Titulos secundarios, CTAs, acentos |
| Gold claro | `#E8C875` | Hover, degradados |
| Gold oscuro | `#B8912E` | Sombras, degradados |
| Fondo negro | `#0A0A0A` | Background principal |
| Fondo oscuro | `#111111` | Secciones alternativas |
| Charcoal industrial | `#1A1A1A` | Fondo anuncios industriales |
| Blanco texto | `#FFFFFF` | Titulos principales |
| Gris texto | `#CCCCCC` | Texto secundario |

## Tipografía (disponible en Canva Free)

| Uso | Fuente | Peso | Notas |
|-----|--------|------|-------|
| Títulos grandes | **Montserrat** | Black / ExtraBold | Máximo impacto |
| Subtítulos | **Montserrat** | Bold | |
| Cuerpo | **Inter** o **Open Sans** | Regular | Legible en cualquier tamaño |
| Acento | **Playfair Display** | Bold | Solo para toques elegantes |

> ⚠️ EVITAR: Fuentes serif delgadas (tipo Cormorant, Garamond) — no funcionan para ads de servicios.
> ⚠️ Con Canva Free las fuentes premium (Bebas Neue, etc.) NO están disponibles.
> ✅ Con Canva Premium se desbloquean todas las fuentes y el Brand Kit.

## Formatos de Anuncios Meta Ads

| Formato | Dimensión | Uso |
|---------|-----------|-----|
| Feed Instagram/Facebook | 1080x1080 | Post estático principal |
| Story / Reel vertical | 1080x1920 | Stories e interstitials |
| Carrusel | 1080x1080 (c/slide) | Secuencia de 3-5 slides |
| Facebook Feed horizontal | 1200x628 | Feed Facebook desktop |

## Estructura de Layouts que Funcionan

### Layout Tipo A — Foto Abajo, Texto Arriba
```
[FONDO NEGRO]
[Texto grande bold blanco — headline]
[Texto gold — subheadline]
[Separador fino gold]
[FOTO real del trabajo — 50% inferior]
```

### Layout Tipo B — Foto Full con Overlay
```
[FOTO a full bleed]
[Overlay degradado oscuro 60%]
[Texto centrado encima — blanco y gold]
[CTA button gold inferior]
```

### Layout Tipo C — Split (Antes/Después)
```
[Mitad izquierda: foto ANTES]  |  [Mitad derecha: foto DESPUÉS]
[ANTES] label gold izq         |  [DESPUÉS] label gold der
[Texto central encima de la división]
```

## Copys Aprobados

### CTA Principal
- "ESCRÍBENOS POR WHATSAPP →"
- "COTIZA SIN COSTO →"
- "VISITA TÉCNICA GRATIS"

### Headlines Residencial
- "TUS PISOS COMO NUEVOS"
- "¿Tus pisos perdieron el brillo?"
- "Los restauramos sin reemplazarlos"

### Headlines Industrial
- "HORMIGÓN PULIDO PROFESIONAL"
- "Superficies industriales que duran"
- "Galpones · Bodegas · Locales Comerciales"

### Beneficios
- ✅ 10+ años de experiencia
- ✅ Trabajo limpio — sin polvo
- ✅ Sellante permanente
- ✅ Visita técnica gratuita
- ✅ Cotización sin compromiso

## Contacto (siempre incluir en última slide)
- **WhatsApp:** +56 9 6822 1431
- **Instagram:** @americapulidospa
- **Zona:** Santiago Oriente — cobertura RM completa

## Assets en Canva (IDs)

| Asset / Fotografía | ID Canva | Descripción |
|---------------------|----------|-------------|
| **Folder Proyecto América Pulido** | `FAHQoFboXK8` | Carpetas y proyecto principal en Canva |
| **Logo Oficial América Pulido** | `MAHQoN3XQ_o` | Logo vector/PNG transparente subido vía Canva MCP |
| **Local Comercial Pulido** | `MAHQoWZCDCc` | Foto real piso comercial con alto brillo |
| **Antes y Después Baldosa 1** | `MAHQoZ1iW5U` | Comparativa real restauración baldosa |
| **Antes y Después Baldosa 2** | `MAHQoRqH2Lc` | Comparativa real brillo y pulido baldosa |
| **Hormigón Industrial** | `MAHQoWcs6CM` | Pulido industrial helicóptero para galpones |
| **Hormigón Galpón** | `MAHQoelh9-I` | Galpón comercial con acabado espejo |
| **Piso Parquet Madera** | `MAHQoXNxioU` | Parquet restaurado residencial |
| **Madera Alto Brillo** | `MAHQodSwpSA` | Piso de madera vitrificado/brillante |
| **Calidad Brillo Espejo** | `MAHQoYEAMrA` | Reflejo espejo en superficie pulida |
| **Hero Servicios Pulido** | `MAHQoV9mhng` | Foto principal de servicios de pulido |

## Diseños Creados (IDs)

| Diseño | ID | Link edición |
|--------|----|--------------|
| **Tarjeta Institucional Servicios (Piso Espejo)** | `DAHUQ6a3K5A` | https://www.canva.com/d/TeEUu6oyo8zb2-Z |
| **Tarjeta Institucional Productos (Mármol Calacatta)** | `DAHURZEwBBI` | https://www.canva.com/d/sfBDg6_rT7R9OSI |
| **Tarjeta Presentación Servicios (Borrador)** | `DAHUQm4g6iM` | https://www.canva.com/d/BTmRvEU0Yk8b0Vg |
| **Tarjeta Presentación Productos (Borrador)** | `DAHUQkffymk` | https://www.canva.com/d/FZca3hPhmqXgxhJ |
| **Post Instagram 1 (General)** | `DAHQoJWA3h0` | https://www.canva.com/d/gO1vU9QAFVo5UgK |
| **Post Instagram 2 (Parquet Residencial)** | `DAHQoSYbYeI` | https://www.canva.com/d/dZQy_eV-5YJxn58 |
| **Post Instagram 3 (Hormigón Industrial)** | `DAHQoe5ZV8I` | https://www.canva.com/d/V6Jj87lh_21NmSi |
| **Carrusel Residencial** | `DAHGD4pNGWY` | https://www.canva.com/d/L48gPZxz1gBEHaN |
| **Carrusel Industrial** | `DAHGDxTMIE8` | https://www.canva.com/d/vAyMcUOjy5mJwTq |
| **Anuncio Saca Bocado 35mm Real** | `DAHQyU55YBI` | https://www.canva.com/d/UuLkB38Hhu6sD6S |
| **Industrial (borrador)** | `DAHGAcgoJog` | https://www.canva.com/d/g1LLGafUR40KBrg |

## Limitaciones Actuales (Canva Free)

1. **Sin Brand Kit** — colores y fuentes se deben especificar manualmente en cada diseño
2. **Sin fuentes premium** — limita a fuentes del catálogo free
3. **Sin redimensionado automático** — hay que recrear para cada formato
4. **Elementos de template bloqueados** — algunos elementos de templates generados no son editables via API

## Con Canva Premium se desbloquea

- Brand Kit → Claude puede aplicar automáticamente colores, fuentes y logo
- Fuentes premium → Bebas Neue, fuentes bold industriales
- Magic Resize → un diseño → todos los formatos automáticamente
- Background Remover → limpiar fotos con logos/fondo

## Instrucciones para Claude al Generar Diseños

1. **Siempre especificar** "ALL TEXT IN SPANISH" en el prompt
2. **Especificar fuente** "BOLD, HEAVY, MODERN SANS-SERIF, NO thin serif fonts"
3. **Dar texto exacto** en el prompt — no dejar que el AI invente copy
4. **Verificar** que la foto usada no tenga texto/flyer encima antes de usar
5. **Editar después** de generar: siempre revisar y corregir textos con perform-editing-operations
6. **Usar asset IDs** de la tabla de arriba en vez de re-subir fotos
