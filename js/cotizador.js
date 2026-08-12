// Motor de Cotizaciones y Cálculo Dinámico para América Pulido SPA
// Soporta escala de descuentos por tramos, cálculo de IVA (19%), WhatsApp prefill y generación de PDF.

const PRODUCTOS_CATALOGO = [
  {
    id: "dpd4",
    nombre: "Disco Pulir Diamantado 4\"",
    categoria: "Discos de Diamante",
    precioLista: 4990,
    costoBodega: 2225,
    unidad: "unidad",
    img: "img/disco de resina premium.jpeg"
  },
  {
    id: "dpd115sc",
    nombre: "Disco Pulir Resina Seco 4.5\"",
    categoria: "Resinas de Pulido",
    precioLista: 6490,
    costoBodega: 3998,
    unidad: "unidad",
    img: "disco de resina seco.jpeg"
  },
  {
    id: "drh115",
    nombre: "Disco Pulir Resina Húmedo 4.5\"",
    categoria: "Resinas de Pulido",
    precioLista: 4990,
    costoBodega: 2225,
    unidad: "unidad",
    img: "disco de resina humedo.jpeg"
  },
  {
    id: "pcm14236",
    nombre: "Piedra Cónica Carburo Silicio M14 #36",
    categoria: "Piedras y Abrasivos",
    precioLista: 13990,
    costoBodega: 5938,
    unidad: "unidad",
    img: "disco de resina seco.jpeg"
  },
  {
    id: "trompo104295",
    nombre: "Trompo de Resina Diamantado (Kamasa Gris)",
    categoria: "Resinas de Pulido",
    precioLista: 15990,
    costoBodega: 10924,
    unidad: "unidad",
    img: "disco de resina seco.jpeg"
  },
  {
    id: "scdm35",
    nombre: "Sierra Copa Diamantada 35mm (M14)",
    categoria: "Brocas y Copas",
    precioLista: 16990,
    costoBodega: 9223,
    unidad: "unidad",
    img: "sacabocado de 35 mm.jpeg"
  },
  {
    id: "ds4",
    nombre: "Base Soporte Velcrada 4\" (M14)",
    categoria: "Accesorios y Bases",
    precioLista: 9990,
    costoBodega: 5831,
    unidad: "unidad",
    img: "disco de resina premium.jpeg"
  },
  {
    id: "dr11410",
    nombre: "Disco Ranurador Diamantado 114mm x 10mm",
    categoria: "Corte y Ranurado",
    precioLista: 54990,
    costoBodega: 38080,
    unidad: "unidad",
    img: "disco ranurador diamantado.jpeg"
  },
  {
    id: "dtg115",
    nombre: "Disco Traslapado 4.5\" Mármol/Piedra",
    categoria: "Discos Traslapados",
    precioLista: 2490,
    costoBodega: 893,
    unidad: "unidad",
    img: "rodillo diamantado.jpeg"
  }
];

// Regla de Descuentos Optimizada (Escala Protegida de 5 Tramos)
const TRAMOS_DESCUENTO = [
  { minQty: 100, dto: 0.25, label: "25% DTO Mayorista" },
  { minQty: 50,  dto: 0.20, label: "20% DTO Pro" },
  { minQty: 25,  dto: 0.15, label: "15% DTO Volumen" },
  { minQty: 10,  dto: 0.08, label: "8% DTO Inicial" },
  { minQty: 0,   dto: 0.00, label: "Precio Lista Web" }
];

// Estado global de la cotización
let carritoCotizacion = {};

// Obtener porcentaje de descuento aplicable según cantidad total de ítems
function obtenerTramoDescuento(totalUnidades) {
  for (let tramo of TRAMOS_DESCUENTO) {
    if (totalUnidades >= tramo.minQty) {
      return tramo;
    }
  }
  return TRAMOS_DESCUENTO[TRAMOS_DESCUENTO.length - 1];
}

// Obtener siguiente tramo para la barra de incentivo
function obtenerSiguienteTramo(totalUnidades) {
  for (let i = TRAMOS_DESCUENTO.length - 1; i >= 0; i--) {
    if (totalUnidades < TRAMOS_DESCUENTO[i].minQty) {
      return TRAMOS_DESCUENTO[i];
    }
  }
  return null;
}

// Formatear números a CLP ($ X.XXX)
function formatCLP(monto) {
  return new Intl.NumberFormat('es-CL', {
    style: 'currency',
    currency: 'CLP',
    maximumFractionDigits: 0
  }).format(Math.round(monto));
}

// Inicialización de la interfaz
document.addEventListener("DOMContentLoaded", () => {
  renderizarCatalogo();
  actualizarCalculos();
});

function renderizarCatalogo() {
  const container = document.getElementById("grid-productos");
  if (!container) return;

  container.innerHTML = PRODUCTOS_CATALOGO.map(prod => `
    <div class="card-producto" id="card-${prod.id}">
      <div class="img-wrapper">
        <img src="${prod.img}" alt="${prod.nombre}" onerror="this.src='img/logo_spiral_transparent.png'">
        <span class="badge-cat">${prod.categoria}</span>
      </div>
      <div class="info-prod">
        <h3>${prod.nombre}</h3>
        <div class="precios-row">
          <span class="precio-base">${formatCLP(prod.precioLista)} c/u</span>
        </div>
        <div class="cant-controls">
          <button type="button" class="btn-qty" onclick="modificarCantidad('${prod.id}', -1)">-</button>
          <input type="number" id="qty-${prod.id}" value="${carritoCotizacion[prod.id] || 0}" min="0" onchange="setCantidad('${prod.id}', this.value)">
          <button type="button" class="btn-qty" onclick="modificarCantidad('${prod.id}', 1)">+</button>
        </div>
      </div>
    </div>
  `).join("");
}

function modificarCantidad(id, delta) {
  const actual = carritoCotizacion[id] || 0;
  const nueva = Math.max(0, actual + delta);
  setCantidad(id, nueva);
}

function setCantidad(id, valor) {
  const num = Math.max(0, parseInt(valor) || 0);
  if (num > 0) {
    carritoCotizacion[id] = num;
  } else {
    delete carritoCotizacion[id];
  }
  const inputEl = document.getElementById(`qty-${id}`);
  if (inputEl) inputEl.value = num;
  
  actualizarCalculos();
}

function actualizarCalculos() {
  let totalUnidades = 0;
  let subtotalLista = 0;

  Object.keys(carritoCotizacion).forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    if (prod && qty > 0) {
      totalUnidades += qty;
      subtotalLista += (prod.precioLista * qty);
    }
  });

  const tramoActual = obtenerTramoDescuento(totalUnidades);
  const porcentajeDto = tramoActual.dto;
  const montoDescuento = subtotalLista * porcentajeDto;
  const subtotalConDto = subtotalLista - montoDescuento;
  const iva = subtotalConDto * 0.19; // IVA 19% Chile
  const totalFinal = subtotalConDto + iva;

  // Actualizar resumen en pantalla
  const elTotalUnid = document.getElementById("resumen-unidades");
  const elSubtotal = document.getElementById("resumen-subtotal");
  const elDtoPct = document.getElementById("resumen-dto-pct");
  const elDtoMonto = document.getElementById("resumen-dto-monto");
  const elIva = document.getElementById("resumen-iva");
  const elTotal = document.getElementById("resumen-total");

  if (elTotalUnid) elTotalUnid.textContent = totalUnidades;
  if (elSubtotal) elSubtotal.textContent = formatCLP(subtotalLista);
  if (elDtoPct) elDtoPct.textContent = `${Math.round(porcentajeDto * 100)}%`;
  if (elDtoMonto) elDtoMonto.textContent = `-${formatCLP(montoDescuento)}`;
  if (elIva) elIva.textContent = formatCLP(iva);
  if (elTotal) elTotal.textContent = formatCLP(totalFinal);

  // Barra de Enganche
  const elProgress = document.getElementById("progress-bar-fill");
  const elHookMsg = document.getElementById("hook-message");
  const siguienteTramo = obtenerSiguienteTramo(totalUnidades);

  if (elHookMsg && elProgress) {
    if (siguienteTramo) {
      const faltantes = siguienteTramo.minQty - totalUnidades;
      const pctProgreso = Math.min(100, Math.round((totalUnidades / siguienteTramo.minQty) * 100));
      elProgress.style.width = `${pctProgreso}%`;
      elHookMsg.innerHTML = `🔥 <strong>¡Estás a solo ${faltantes} unidades</strong> de desbloquear un <strong>${Math.round(siguienteTramo.dto * 100)}% de descuento total!</strong>`;
    } else {
      elProgress.style.width = `100%`;
      elHookMsg.innerHTML = `🏆 <strong>¡Felicidades!</strong> Has alcanzado el máximo nivel de <strong>25% de Descuento Mayorista</strong>.`;
    }
  }

  // Envío gratis
  const elEnvio = document.getElementById("badge-envio");
  if (elEnvio) {
    if (totalFinal >= 100000) {
      elEnvio.className = "badge-envio envio-gratis";
      elEnvio.innerHTML = "🚚 <strong>ENVÍO GRATIS A TODO SANTIAGO RM</strong>";
    } else {
      const leFalta = 100000 - totalFinal;
      elEnvio.className = "badge-envio envio-normal";
      elEnvio.innerHTML = `🚚 Agrega ${formatCLP(leFalta)} más para <strong>ENVÍO GRATIS</strong>`;
    }
  }

  renderizarTablaResumen();
}

function renderizarTablaResumen() {
  const container = document.getElementById("items-cotizados-list");
  if (!container) return;

  const itemsKeys = Object.keys(carritoCotizacion);
  if (itemsKeys.length === 0) {
    container.innerHTML = `<p class="empty-msg">No has seleccionado ningún producto aún. Elige del catálogo arriba para comenzar.</p>`;
    return;
  }

  let totalUnidades = 0;
  itemsKeys.forEach(id => totalUnidades += carritoCotizacion[id]);
  const tramo = obtenerTramoDescuento(totalUnidades);

  container.innerHTML = `
    <table class="tabla-resumen-cotizacion">
      <thead>
        <tr>
          <th>Producto</th>
          <th>Cant.</th>
          <th>Precio Unit.</th>
          <th>Desc. (${Math.round(tramo.dto * 100)}%)</th>
          <th>Total Neto</th>
        </tr>
      </thead>
      <tbody>
        ${itemsKeys.map(id => {
          const qty = carritoCotizacion[id];
          const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
          const precioUnitConDto = prod.precioLista * (1 - tramo.dto);
          const totalNeto = precioUnitConDto * qty;
          return `
            <tr>
              <td><strong>${prod.nombre}</strong></td>
              <td class="text-center">${qty}</td>
              <td class="text-right">${formatCLP(prod.precioLista)}</td>
              <td class="text-right text-gold">-${formatCLP(prod.precioLista * tramo.dto)}</td>
              <td class="text-right bold">${formatCLP(totalNeto)}</td>
            </tr>
          `;
        }).join("")}
      </tbody>
    </table>
  `;
}

// Enviar Cotización por WhatsApp prefillado
function enviarWhatsApp() {
  const itemsKeys = Object.keys(carritoCotizacion);
  if (itemsKeys.length === 0) {
    alert("Por favor selecciona al menos un producto antes de enviar a WhatsApp.");
    return;
  }

  let totalUnidades = 0;
  let subtotalLista = 0;

  itemsKeys.forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    totalUnidades += qty;
    subtotalLista += (prod.precioLista * qty);
  });

  const tramo = obtenerTramoDescuento(totalUnidades);
  const montoDto = subtotalLista * tramo.dto;
  const subtotalNeto = subtotalLista - montoDto;
  const iva = subtotalNeto * 0.19;
  const totalBruto = subtotalNeto + iva;

  let msg = `*COTIZACIÓN OFICIAL — AMÉRICA PULIDO SPA*\n\n`;
  msg += `Hola! Quisiera solicitar la siguiente cotización realizada desde la web:\n\n`;

  itemsKeys.forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    const precioUnitDto = prod.precioLista * (1 - tramo.dto);
    msg += `• *${prod.nombre}* x ${qty} unid. (${formatCLP(precioUnitDto)} c/u)\n`;
  });

  msg += `\n-------------------------------\n`;
  msg += `📦 *Total Unidades:* ${totalUnidades}\n`;
  msg += `🏷️ *Descuento Aplicado:* ${Math.round(tramo.dto * 100)}% (-${formatCLP(montoDto)})\n`;
  msg += `💰 *Subtotal Neto:* ${formatCLP(subtotalNeto)}\n`;
  msg += `📄 *IVA 19%:* ${formatCLP(iva)}\n`;
  msg += `✅ *TOTAL BRUTO FINAL:* ${formatCLP(totalBruto)}\n`;
  if (totalBruto >= 100000) {
    msg += `🚚 *Beneficio:* ¡Aplica a ENVÍO GRATIS Santiago RM!\n`;
  }
  msg += `\nQuedo atento a la confirmación de stock y emisión de factura/boleta. ¡Muchas gracias!`;

  const phone = "56978685664";
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
}

// Generación e Impresión / Descarga de PDF Formal
function descargarPDFCotizacion() {
  const itemsKeys = Object.keys(carritoCotizacion);
  if (itemsKeys.length === 0) {
    alert("Por favor selecciona productos para generar el documento PDF.");
    return;
  }

  let totalUnidades = 0;
  let subtotalLista = 0;
  itemsKeys.forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    totalUnidades += qty;
    subtotalLista += (prod.precioLista * qty);
  });

  const tramo = obtenerTramoDescuento(totalUnidades);
  const montoDto = subtotalLista * tramo.dto;
  const subtotalNeto = subtotalLista - montoDto;
  const iva = subtotalNeto * 0.19;
  const totalBruto = subtotalNeto + iva;

  const fechaHoy = new Date().toLocaleDateString('es-CL');
  const numCotizacion = "COT-" + Math.floor(100000 + Math.random() * 900000);

  const printWindow = window.open('', '_blank');
  printWindow.document.write(`
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>Cotización ${numCotizacion} - América Pulido SPA</title>
      <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; color: #1a202c; padding: 40px; margin: 0; background: #fff; }
        .header-pdf { display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #D4A843; padding-bottom: 20px; }
        .logo-box img { height: 75px; }
        .company-details { text-align: right; font-size: 13px; color: #4a5568; line-height: 1.4; }
        .company-name { font-size: 20px; font-weight: bold; color: #0A192F; }
        .title-doc { text-align: center; margin: 30px 0 20px 0; font-size: 22px; color: #0A192F; letter-spacing: 1px; }
        .meta-grid { display: flex; justify-content: space-between; background: #F8F9FA; padding: 15px 20px; border-radius: 8px; margin-bottom: 25px; font-size: 14px; }
        .tabla-pdf { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
        .tabla-pdf th { background: #0A192F; color: #ffffff; padding: 10px 14px; font-size: 13px; text-align: left; }
        .tabla-pdf td { padding: 10px 14px; border-bottom: 1px solid #e2e8f0; font-size: 13px; }
        .tabla-pdf tr:nth-child(even) { background: #f8fafc; }
        .totales-box { width: 320px; margin-left: auto; background: #F8F9FA; border: 1px solid #e2e8f0; padding: 18px; border-radius: 8px; }
        .row-total { display: flex; justify-content: space-between; padding: 6px 0; font-size: 14px; }
        .row-total.final { font-size: 18px; font-weight: bold; color: #0A192F; border-top: 2px solid #D4A843; margin-top: 8px; padding-top: 10px; }
        .footer-pdf { margin-top: 50px; text-align: center; font-size: 12px; color: #718096; border-top: 1px solid #e2e8f0; padding-top: 20px; }
        .gold-highlight { color: #D4A843; font-weight: bold; }
        @media print {
          body { padding: 0; }
          .no-print { display: none; }
        }
      </style>
    </head>
    <body>
      <div class="no-print" style="margin-bottom: 20px; text-align: right;">
        <button onclick="window.print()" style="background:#D4A843; color:#fff; border:none; padding:12px 24px; font-size:15px; font-weight:bold; border-radius:6px; cursor:pointer;">🖨️ Imprimir / Guardar en PDF</button>
      </div>
      <div class="header-pdf">
        <div class="logo-box">
          <img src="img/logo_spiral_transparent.png" alt="América Pulido SPA">
        </div>
        <div class="company-details">
          <div class="company-name">AMÉRICA PULIDO SPA</div>
          <div>Especialistas en Pulido de Pisos e Insumos Diamantados</div>
          <div>Santiago Oriente, Región Metropolitana</div>
          <div>Contacto: +56 9 7868 5664</div>
          <div>www.americapulido.cl</div>
        </div>
      </div>

      <div class="title-doc">COTIZACIÓN DE PRODUCTOS & INSUMOS</div>

      <div class="meta-grid">
        <div>
          <strong>N° Cotización:</strong> ${numCotizacion}<br>
          <strong>Fecha de Emisión:</strong> ${fechaHoy}
        </div>
        <div style="text-align: right;">
          <strong>Validez de Oferta:</strong> 15 Días corridos<br>
          <strong>Descuento Aplicado:</strong> <span class="gold-highlight">${Math.round(tramo.dto * 100)}% por Volumen</span>
        </div>
      </div>

      <table class="tabla-pdf">
        <thead>
          <tr>
            <th>Descripción de Producto</th>
            <th style="text-align: center;">Cantidad</th>
            <th style="text-align: right;">Precio Lista</th>
            <th style="text-align: right;">Precio DTO</th>
            <th style="text-align: right;">Total Neto</th>
          </tr>
        </thead>
        <tbody>
          ${itemsKeys.map(id => {
            const qty = carritoCotizacion[id];
            const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
            const precioUnitDto = prod.precioLista * (1 - tramo.dto);
            const totalNeto = precioUnitDto * qty;
            return `
              <tr>
                <td><strong>${prod.nombre}</strong> (${prod.categoria})</td>
                <td style="text-align: center;">${qty}</td>
                <td style="text-align: right;">${formatCLP(prod.precioLista)}</td>
                <td style="text-align: right; color:#D4A843; font-weight:bold;">${formatCLP(precioUnitDto)}</td>
                <td style="text-align: right; font-weight:bold;">${formatCLP(totalNeto)}</td>
              </tr>
            `;
          }).join("")}
        </tbody>
      </table>

      <div class="totales-box">
        <div class="row-total">
          <span>Subtotal Lista:</span>
          <span>${formatCLP(subtotalLista)}</span>
        </div>
        <div class="row-total" style="color: #D4A843;">
          <span>Descuento Volumen (${Math.round(tramo.dto * 100)}%):</span>
          <span>-${formatCLP(montoDto)}</span>
        </div>
        <div class="row-total">
          <span>Subtotal Neto:</span>
          <span>${formatCLP(subtotalNeto)}</span>
        </div>
        <div class="row-total">
          <span>IVA 19%:</span>
          <span>${formatCLP(iva)}</span>
        </div>
        <div class="row-total final">
          <span>TOTAL FINAL:</span>
          <span>${formatCLP(totalBruto)}</span>
        </div>
      </div>

      <div class="footer-pdf">
        <p>Gracias por preferir a <strong>América Pulido SPA</strong>. Esta cotización es válida por 15 días desde su emisión.</p>
        <p>Para coordinar pago y despacho rápido, contáctenos directamente al WhatsApp +56 9 7868 5664.</p>
      </div>
    </body>
    </html>
  `);
  printWindow.document.close();
}
