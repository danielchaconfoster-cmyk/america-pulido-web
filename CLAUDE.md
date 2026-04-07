# America Pulido SPA — Landing Page & Campaña Meta Ads

> Landing page de cliente para servicio de pulido profesional de pisos en Santiago, Chile.
> Cliente de Agencia Digital DC Foster — Daniel Chacon Foster

## Proyecto

- **Tipo:** Landing page estática (HTML + CSS + JS puro, sin framework)
- **Repo GitHub:** `danielchaconfoster-cmyk/america-pulido-web`
- **Dev server:** `npx serve` en puerto 64100
- **Deploy:** Estático (GitHub / servidor simple)

## Cliente

- **Empresa:** America Pulido SPA
- **Servicio:** Pulido profesional de pisos (madera, mármol, hormigón, baldosa, industrial)
- **Zona:** Santiago Oriente — cobertura Región Metropolitana completa
- **WhatsApp:** +56 9 7868 5664
- **Instagram:** @americapulidospa
- **Colores:** Gold #D4A843, Dark #0A0A0A, Accent gradient #D4A843→#E8C875→#B8912E

## Estructura

```
index.html          # Landing completa (689 líneas — HTML + CSS + JS en un solo archivo)
img/                # 14 fotos JPG (logo, antes/después, servicios, materiales)
video/              # 4 videos MP4 (proceso de pulido)
public/images/      # Vacío (para uso futuro)
```

## Secciones de la landing
- Navbar fijo con menú móvil
- Hero con crossfade de imágenes (5s)
- Animación de partículas interactiva con logo
- Before/after slider drag
- Grid de servicios (residencial premium + hormigón industrial)
- 4 garantías (limpio, rápido, brillo permanente, transparencia)
- Testimonios
- CTAs a WhatsApp con mensajes prefillados
- Footer con datos de contacto

## Campaña Meta Ads (activa desde 06-04-2026)

Ver archivo: `CAMPANA_META_ADS.md` para toda la info operacional de la campaña.

## RESTRICCIÓN CRÍTICA
- NO instalar dependencias innecesarias — es HTML estático intencional
- NO agregar frameworks — el cliente no necesita complejidad
- Si se agrega Pixel de Meta, va en el `<head>` de index.html
- NO automatizar navegador en dominios Meta/Facebook/Instagram
