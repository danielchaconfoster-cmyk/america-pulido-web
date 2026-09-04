---
name: canva-expert-mcp
description: Guía de nivel experto para dominar Canva vía MCP (Model Context Protocol). Incluye gestión de proyectos, Kit de Marca, edición mediante transacciones, cargas masivas de activos, importación desde HTML/URL y exportaciones profesionales.
---

# Canva Expert & MCP Master Skill — América Pulido SPA

Esta guía establece el estándar de oro para interactuar con **Canva** mediante **Canva MCP (`mcp-remote`)** y maximizar el rendimiento gráfico, de marca y publicitario para América Pulido SPA.

---

## 1. Conexión & Arquitectura MCP de Canva

- **Endpoint oficial:** `https://mcp.canva.com/mcp`
- **Bridge stdio:** `npx -y mcp-remote@latest https://mcp.canva.com/mcp`
- **Configuración local:** Guardada en [mcp.json](file:///c:/Users/usuario/Desktop/america-pulido-web/mcp.json).

```json
{
  "mcpServers": {
    "canva": {
      "command": "npx",
      "args": ["-y", "mcp-remote@latest", "https://mcp.canva.com/mcp"]
    }
  }
}
```

---

## 2. Kit de Marca Oficial (Brand Kit System)

En Canva Free o Pro, se deben garantizar estrictamente los siguientes valores en cada diseño:

### A. Paleta de Colores Primaria & Secundaria
- **Gold Principal:** `#D4A843` (Títulos secundarios, CTAs, líneas decorativas, bordes).
- **Gold Claro (Highlight):** `#E8C875` (Hover, degradados superiores, textos de acento).
- **Gold Oscuro (Shadow):** `#B8912E` (Sombras de texto, degradados inferiores, botones).
- **Fondo Oscuro Principal:** `#0A0A0A` (Dark Mode elegante de alto impacto).
- **Fondo Sección Alternativa:** `#111111` / `#1A1A1A` (Gris charcoal industrial).
- **Texto Principal:** `#FFFFFF` (Blanco impuro brillante).
- **Texto Secundario:** `#CCCCCC` (Gris neutro legible).

### B. Tipografía Oficial
- **Títulos / Headlines:** `Montserrat` (Black / ExtraBold / Heavy, 900 weight, Mayúsculas).
- **Cuerpo / Subtítulos:** `Inter` o `Open Sans` (Regular / Medium, 400-600 weight).
- **Regla:** ⚠️ Evitar fuentes serif delgadas para anuncios de servicios.

---

## 3. ID de Recursos & Proyectos en Canva

| Recurso | ID Canva | Descripción / URL |
|---------|----------|-------------------|
| **Carpeta Principal** | `FAHQoFboXK8` | [Ver Proyecto América Pulido SPA](https://www.canva.com/folder/FAHQoFboXK8) |
| **Logo Oficial (PNG)** | `MAHQoN3XQ_o` | Logo en alta resolución con transparencia |
| **Tarjeta Servicios** | `DAHUQm4g6iM` | [Editar Tarjeta Servicios](https://www.canva.com/d/BTmRvEU0Yk8b0Vg) |
| **Tarjeta Productos** | `DAHUQkffymk` | [Editar Tarjeta Productos](https://www.canva.com/d/FZca3hPhmqXgxhJ) |
| **Post Instagram 1** | `DAHQoJWA3h0` | [Editar Post en Canva](https://www.canva.com/d/gO1vU9QAFVo5UgK) |
| **Carrusel Residencial** | `DAHGD4pNGWY` | [Editar Carrusel en Canva](https://www.canva.com/d/L48gPZxz1gBEHaN) |
| **Carrusel Industrial** | `DAHGDxTMIE8` | [Editar Industrial en Canva](https://www.canva.com/d/vAyMcUOjy5mJwTq) |

---

## 4. Flujo de Trabajo Experto (MCP Workflows)

### Flujo A: Creación de Anuncios desde HTML (`import-design-from-url`)
1. Diseñar el post o story en HTML5 puro con CSS inline o embellecido en `public/`.
2. Incluir el atributo `data-document-role="page"` para especificar diapositivas/páginas.
3. Subir el archivo a GitHub Main.
4. Invocar `import-design-from-url` pasando el URL raw (`https://raw.githubusercontent.com/.../post.html`).
5. Invocar `move-item-to-folder` a la carpeta `FAHQoFboXK8`.

### Flujo B: Carga Masiva de Fotos & Logos (`upload-asset-from-url`)
1. Disponer de URLs HTTPS públicas (como GitHub raw).
2. Invocar `upload-asset-from-url` con `url` y `name`.
3. Inmediatamente mover el `asset_id` devuelto a la carpeta del proyecto `FAHQoFboXK8` con `move-item-to-folder`.

### Flujo C: Transacciones de Edición (`start-editing-transaction`)
1. Llamar a `start-editing-transaction` con el `design_id`.
2. Obtener el `transaction_id` y revisar `richtexts` y `fills`.
3. Ejecutar las modificaciones con `perform-editing-operations` (`replace_text`, `update_fill`, `update_title`, `find_and_replace_text`).
4. Confirmar los cambios de forma permanente con `commit-editing-transaction`.

### Flujo D: Exportación Profesional (`export-design`)
1. Consultar formatos soportados con `get-export-formats` pasándole el `design_id`.
2. Llamar a `export-design` con `format: { type: "png" | "jpg" | "pdf" | "mp4", export_quality: "pro" }`.
3. Entregar el URL de descarga directa de Canva al usuario.

---

## 5. Reglas de Copywriting Aprobadas para Meta Ads

- **CTAs:** `"ESCRÍBENOS POR WHATSAPP →"`, `"COTIZA SIN COSTO →"`, `"VISITA TÉCNICA GRATIS"`.
- **Headlines Residencial:** `"TUS PISOS COMO NUEVOS SIN REEMPLAZARLOS"`, `"¿TUS PISOS PERDIERON EL BRILLO?"`.
- **Headlines Industrial:** `"HORMIGÓN PULIDO PROFESIONAL"`, `"SUPERFICIES INDUSTRIALES DE ALTA RESISTENCIA"`.
- **Garantías Clave:** `✓ Sin Polvo`, `✓ 10+ Años Exp.`, `✓ Brillo Permanente`, `✓ Cotización Gratis`.
