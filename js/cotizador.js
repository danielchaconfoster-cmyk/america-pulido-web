// Motor de Cotizaciones Técnicas para América Pulido SPA
// Cálculo dinámico de escala mayorista, IVA (19%), WhatsApp formal y PDF membretado.

const PRODUCTOS_CATALOGO = [
  {
    id: "sacabocado-35mm",
    nombre: "Saca Bocado Diamantado 35mm (M14)",
    categoria: "diamantados",
    categoriaLabel: "Perforación / Grifería",
    descripcion: "Medida técnica para instalación de grifería y tuberías. Perforación sin despostillamientos en porcelanato, mármol y granito.",
    specs: ["Diámetro: 35 mm", "Rosca: M14 (Esmeril)", "Uso: Seco / Húmedo"],
    precioLista: 16990,
    costoBodega: 9223,
    unidad: "unidad",
    img: "img/productos/prod_sacabocado_35mm.jpg"
  },
  {
    id: "resina-premium",
    nombre: "Disco de Resina Premium 4 Pulgadas (Diamantado)",
    categoria: "resinas",
    categoriaLabel: "Discos de Resina",
    descripcion: "Alta densidad diamantada para refinado rápido y acabado uniforme en mármol, hormigón y terrazo.",
    specs: ["Granos: 50 a 3000", "Diámetro: 4 pulg / 100mm", "Fijación: Velcro"],
    precioLista: 11990,
    costoBodega: 4500,
    unidad: "unidad",
    img: "img/productos/prod_resina_premium.jpg"
  },
  {
    id: "resina-seco",
    nombre: "Disco de Resina en Seco 4.5 Pulgadas (Anti-Quemado)",
    categoria: "resinas",
    categoriaLabel: "Discos de Resina",
    descripcion: "Formulación especial para pulido y abrillantado en seco sin riesgo de quemado térmico en la piedra.",
    specs: ["Granos: 50 a 3000", "Diámetro: 4.5 pulg", "Uso: 100% Seco"],
    precioLista: 6490,
    costoBodega: 3998,
    unidad: "unidad",
    img: "img/productos/prod_resina_seco.jpg"
  },
  {
    id: "resina-humedo",
    nombre: "Disco de Resina Húmedo 4.5 Pulgadas",
    categoria: "resinas",
    categoriaLabel: "Discos de Resina",
    descripcion: "Rendimiento óptimo en procesos continuos con agua sobre baldosas graníticas y mármoles.",
    specs: ["Granos: 50 a 3000", "Diámetro: 4.5 pulg", "Uso: Húmedo"],
    precioLista: 4990,
    costoBodega: 2225,
    unidad: "unidad",
    img: "img/productos/prod_resina_humedo.jpg"
  },
  {
    id: "ranurador-114mm",
    nombre: "Disco Ranurador Diamantado 114mm x 10mm",
    categoria: "diamantados",
    categoriaLabel: "Ranurado / Marmolería",
    descripcion: "Espesor de 10mm para canterías, juntas de dilatación y ranuras de escurrimiento en cubiertas.",
    specs: ["Medida: 114mm x 10mm", "Uso: Heavy Duty", "Seco / Húmedo"],
    precioLista: 54990,
    costoBodega: 38080,
    unidad: "unidad",
    img: "img/productos/prod_ranurador_114mm.jpg"
  },
  {
    id: "desbaste-diamantado",
    nombre: "Copa Diamantada de Desbaste",
    categoria: "diamantados",
    categoriaLabel: "Desbaste Pesado",
    descripcion: "Remoción rápida de recubrimientos epóxicos, adhesivos y nivelación de hormigón.",
    specs: ["Formato: Doble hilera", "Diámetro: 4.5 pulg / 115mm", "Alto Desbaste"],
    precioLista: 12990,
    costoBodega: 6500,
    unidad: "unidad",
    img: "img/productos/prod_desbaste.jpg"
  },
  {
    id: "disco-pulidor-fibra",
    nombre: "Disco Pulidor Abrasivo de Fibra",
    categoria: "bases",
    categoriaLabel: "Abrasivos y Decapado",
    descripcion: "Estructura de fibra sintética para decapado de ceras y acondicionamiento previo al vitrificado.",
    specs: ["Fibra Industrial", "Diámetro: 4.5 pulg", "Uso: Limpieza / Decapado"],
    precioLista: 9990,
    costoBodega: 4800,
    unidad: "unidad",
    img: "img/productos/prod_disco_pulidor.jpg"
  },
  {
    id: "piedra-conica",
    nombre: "Piedra Cónica Carburo Silicio M14 #36",
    categoria: "bases",
    categoriaLabel: "Esquinas y Bordes",
    descripcion: "Rosca M14 para desbaste y nivelado en zócalos, esquinas y bordes inaccesibles.",
    specs: ["Rosca: M14", "Granos: #36, #60, #80", "Uso: Bordes / Zócalos"],
    precioLista: 13990,
    costoBodega: 5938,
    unidad: "unidad",
    img: "img/productos/prod_piedra_conica.jpg"
  },
  {
    id: "disco-silicio",
    nombre: "Disco de Silicio para Pulir",
    categoria: "resinas",
    categoriaLabel: "Abrasivos de Silicio",
    descripcion: "Carburo de silicio de alta eficiencia para abrillantado rápido en granito y piedras naturales.",
    specs: ["Carburo de Silicio", "Diámetro: 4.5 pulg", "Fijación: Velcro"],
    precioLista: 5490,
    costoBodega: 2600,
    unidad: "unidad",
    img: "img/productos/prod_disco_silicio.jpg"
  },
  {
    id: "trompo-resina",
    nombre: "Trompo de Resina Diamantado (Perfilador)",
    categoria: "resinas",
    categoriaLabel: "Perfilado / Cantos",
    descripcion: "Cilindro diamantado para desbaste y pulido de contornos cóncavos en cubiertas.",
    specs: ["Rosca: M14", "Diámetros: 20mm a 50mm", "Uso: Cantos Cóncavos"],
    precioLista: 15990,
    costoBodega: 10924,
    unidad: "unidad",
    img: "img/productos/prod_trompo_resina.jpg"
  },
  {
    id: "corte-continuo",
    nombre: "Disco Diamantado Corte Continuo 4.5 Pulgadas",
    categoria: "diamantados",
    categoriaLabel: "Corte Fino / Cerámica",
    descripcion: "Banda continua para cortes limpios sin desportillado en porcelanatos esmaltados y mármol.",
    specs: ["Diámetro: 115mm (4.5 pulg)", "Espesor: 1.2mm", "Corte fino"],
    precioLista: 14990,
    costoBodega: 7200,
    unidad: "unidad",
    img: "img/productos/prod_corte_continuo.jpg"
  },
  {
    id: "corte-segmentado",
    nombre: "Disco Diamantado Corte Segmentado 4.5 Pulgadas",
    categoria: "diamantados",
    categoriaLabel: "Corte Hormigón",
    descripcion: "Segmentos diamantados ventilados para corte rápido en hormigón armado, ladrillo y piedra.",
    specs: ["Diámetro: 115mm", "Segmentos ventilados", "Alta durabilidad"],
    precioLista: 14990,
    costoBodega: 7200,
    unidad: "unidad",
    img: "img/productos/prod_corte_segmentado.jpg"
  },
  {
    id: "base-velcrada-reforzada",
    nombre: "Base Soporte Velcrada M14 (Reforzada)",
    categoria: "bases",
    categoriaLabel: "Accesorios y Bases",
    descripcion: "Cuerpo reforzado con rosca de bronce M14 y velcro industrial para trabajo pesado.",
    specs: ["Rosca: M14", "Diámetro: 4 pulg (100mm)", "Velcro Heavy Duty"],
    precioLista: 9990,
    costoBodega: 5831,
    unidad: "unidad",
    img: "img/productos/prod_base_pulir_reforzada.jpg"
  },
  {
    id: "masilla-dermax",
    nombre: "Masilla Mágica Dermax para Mármol y Granito",
    categoria: "quimicos",
    categoriaLabel: "Masillas y Reparación",
    descripcion: "Masilla bicomponente de alta adherencia para relleno de fisuras y reconstrucción de cantos.",
    specs: ["Presentación: 1 Kg", "Incluye: Catalizador", "Pulible / Abrillantable"],
    precioLista: 8990,
    costoBodega: 4300,
    unidad: "unidad",
    img: "img/productos/prod_masilla_dermax.jpg"
  }
];

// Escala Oficial de Descuentos por Tramo de Compra
const TRAMOS_DESCUENTO = [
  { minQty: 100, dto: 0.25, label: "25% Descuento Mayorista (100+ unid.)" },
  { minQty: 50,  dto: 0.20, label: "20% Descuento Constructor (50+ unid.)" },
  { minQty: 25,  dto: 0.15, label: "15% Descuento Taller (25+ unid.)" },
  { minQty: 10,  dto: 0.08, label: "8% Descuento Inicial (10+ unid.)" },
  { minQty: 0,   dto: 0.00, label: "Precio Lista Directo" }
];

let carritoCotizacion = {};
let categoriaActiva = "todos";

function obtenerTramoDescuento(totalUnidades) {
  for (let tramo of TRAMOS_DESCUENTO) {
    if (totalUnidades >= tramo.minQty) {
      return tramo;
    }
  }
  return TRAMOS_DESCUENTO[TRAMOS_DESCUENTO.length - 1];
}

function obtenerSiguienteTramo(totalUnidades) {
  for (let i = TRAMOS_DESCUENTO.length - 1; i >= 0; i--) {
    if (totalUnidades < TRAMOS_DESCUENTO[i].minQty) {
      return TRAMOS_DESCUENTO[i];
    }
  }
  return null;
}

function formatCLP(monto) {
  return new Intl.NumberFormat('es-CL', {
    style: 'currency',
    currency: 'CLP',
    maximumFractionDigits: 0
  }).format(Math.round(monto));
}

function initCotizador() {
  renderizarCatalogo();
  actualizarCalculos();
}

if (document.readyState === 'loading') {
  document.addEventListener("DOMContentLoaded", initCotizador);
} else {
  initCotizador();
}

function filtrarCategoria(cat, btnElement) {
  categoriaActiva = cat;
  const buttons = document.querySelectorAll(".filter-pill");
  buttons.forEach(btn => btn.classList.remove("active"));
  if (btnElement) {
    btnElement.classList.add("active");
  }
  renderizarCatalogo();
}

function renderizarCatalogo() {
  const container = document.getElementById("grid-productos");
  if (!container) return;

  const productosFiltrados = categoriaActiva === "todos" 
    ? PRODUCTOS_CATALOGO 
    : PRODUCTOS_CATALOGO.filter(p => p.categoria === categoriaActiva);

  if (productosFiltrados.length === 0) {
    container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">No hay productos en esta categoría.</div>';
    return;
  }

  container.innerHTML = productosFiltrados.map(prod => {
    const qty = carritoCotizacion[prod.id] || 0;
    const isSelected = qty > 0;

    return `
      <div class="card-producto ${isSelected ? 'selected' : ''}" id="card-${prod.id}">
        <div class="img-wrapper">
          <img src="img/logo_spiral_transparent.png" class="card-watermark" alt="Logo América Pulido">
          <img src="${prod.img}" alt="${prod.nombre}" class="prod-img" onerror="this.src='img/logo_spiral_transparent.png'">
          <span class="badge-cat">${prod.categoriaLabel}</span>
          ${isSelected ? `<span class="badge-qty-selected">${qty} en cotización</span>` : ''}
        </div>

        <div class="info-prod">
          <h3 title="${prod.nombre}">${prod.nombre}</h3>
          <p class="prod-desc">${prod.descripcion}</p>
          
          <div class="prod-specs-pills">
            ${prod.specs.map(spec => `<span>${spec}</span>`).join('')}
          </div>

          <div class="precios-row">
            <div>
              <span class="precio-label">Precio Unitario:</span>
              <div class="precio-base">${formatCLP(prod.precioLista)}</div>
            </div>
            ${isSelected ? `<div class="subtotal-item-pill">Subtotal: ${formatCLP(prod.precioLista * qty)}</div>` : ''}
          </div>

          <div class="counter-wrapper">
            <div class="cant-controls">
              <button type="button" class="btn-qty btn-minus" aria-label="Disminuir cantidad" onclick="modificarCantidad('${prod.id}', -1)">−</button>
              <input type="number" 
                     id="qty-${prod.id}" 
                     class="input-qty" 
                     value="${qty}" 
                     min="0" 
                     max="9999"
                     aria-label="Cantidad para ${prod.nombre}"
                     onchange="setCantidad('${prod.id}', this.value)"
                     onkeyup="setCantidad('${prod.id}', this.value)">
              <button type="button" class="btn-qty btn-plus" aria-label="Aumentar cantidad" onclick="modificarCantidad('${prod.id}', 1)">+</button>
            </div>

            <div class="quick-add-row">
              <button type="button" class="quick-pill" onclick="modificarCantidad('${prod.id}', 5)">+5</button>
              <button type="button" class="quick-pill" onclick="modificarCantidad('${prod.id}', 10)">+10</button>
              <button type="button" class="quick-pill" onclick="modificarCantidad('${prod.id}', 25)">+25</button>
              ${qty > 0 ? `<button type="button" class="quick-pill pill-clear" title="Quitar producto" onclick="setCantidad('${prod.id}', 0)">✕</button>` : ''}
            </div>
          </div>

        </div>
      </div>
    `;
  }).join("");
}

function modificarCantidad(id, delta) {
  const actual = carritoCotizacion[id] || 0;
  const nueva = Math.max(0, actual + delta);
  setCantidad(id, nueva);
}

function setCantidad(id, valor) {
  let num = parseInt(valor, 10);
  if (isNaN(num) || num < 0) num = 0;
  
  if (num > 0) {
    carritoCotizacion[id] = num;
  } else {
    delete carritoCotizacion[id];
  }

  const inputEl = document.getElementById(`qty-${id}`);
  if (inputEl && document.activeElement !== inputEl) {
    inputEl.value = num;
  }

  const cardEl = document.getElementById(`card-${id}`);
  if (cardEl) {
    if (num > 0) {
      cardEl.classList.add("selected");
    } else {
      cardEl.classList.remove("selected");
    }
  }

  actualizarCalculos();
  renderizarCatalogo();
}

function vaciarCarrito() {
  if (Object.keys(carritoCotizacion).length === 0) return;
  if (confirm("¿Deseas reiniciar la cotización actual a cero?")) {
    carritoCotizacion = {};
    renderizarCatalogo();
    actualizarCalculos();
  }
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
  const iva = subtotalConDto * 0.19;
  const totalFinal = subtotalConDto + iva;

  const elTotalUnid = document.getElementById("resumen-unidades");
  const elSubtotal = document.getElementById("resumen-subtotal");
  const elDtoPct = document.getElementById("resumen-dto-pct");
  const elDtoMonto = document.getElementById("resumen-dto-monto");
  const elIva = document.getElementById("resumen-iva");
  const elTotal = document.getElementById("resumen-total");

  if (elTotalUnid) elTotalUnid.textContent = `${totalUnidades} unid.`;
  if (elSubtotal) elSubtotal.textContent = formatCLP(subtotalLista);
  if (elDtoPct) elDtoPct.textContent = `${Math.round(porcentajeDto * 100)}%`;
  if (elDtoMonto) elDtoMonto.textContent = `-${formatCLP(montoDescuento)}`;
  if (elIva) elIva.textContent = formatCLP(iva);
  if (elTotal) elTotal.textContent = formatCLP(totalFinal);

  const elProgress = document.getElementById("progress-bar-fill");
  const elHookMsg = document.getElementById("hook-message");
  const siguienteTramo = obtenerSiguienteTramo(totalUnidades);

  if (elHookMsg && elProgress) {
    if (totalUnidades === 0) {
      elProgress.style.width = "0%";
      elHookMsg.innerHTML = "Agrega 10 unidades o más para activar escala de descuento por volumen.";
    } else if (siguienteTramo) {
      const faltantes = siguienteTramo.minQty - totalUnidades;
      const baseAnterior = tramoActual.minQty;
      const rango = siguienteTramo.minQty - baseAnterior;
      const avanceEnRango = totalUnidades - baseAnterior;
      const pctProgreso = Math.min(100, Math.max(10, Math.round((avanceEnRango / rango) * 100)));

      elProgress.style.width = `${pctProgreso}%`;
      elHookMsg.innerHTML = `Estás a <strong>${faltantes} unidades</strong> de alcanzar un <strong>${Math.round(siguienteTramo.dto * 100)}% de descuento total</strong>.`;
    } else {
      elProgress.style.width = "100%";
      elHookMsg.innerHTML = "Has alcanzado el tramo máximo: <strong>25% de Descuento Mayorista</strong>.";
    }
  }

  const elEnvio = document.getElementById("badge-envio");
  if (elEnvio) {
    if (totalFinal >= 100000) {
      elEnvio.className = "badge-envio envio-gratis";
      elEnvio.innerHTML = "<strong>ENVÍO GRATIS EN SANTIAGO RM</strong>";
    } else if (totalFinal > 0) {
      const leFalta = 100000 - totalFinal;
      elEnvio.className = "badge-envio envio-normal";
      elEnvio.innerHTML = `Agrega ${formatCLP(leFalta)} para <strong>Envío Gratis en RM</strong>`;
    } else {
      elEnvio.className = "badge-envio envio-normal";
      elEnvio.innerHTML = "Despacho a todo Chile · <strong>Gratis en RM sobre $100.000</strong>";
    }
  }

  const floatingBar = document.getElementById("floating-mobile-bar");
  const floatingUnits = document.getElementById("floating-units");
  const floatingTotal = document.getElementById("floating-total");

  if (floatingBar) {
    if (totalUnidades > 0) {
      floatingBar.classList.add("visible");
      if (floatingUnits) floatingUnits.textContent = `${totalUnidades} ${totalUnidades === 1 ? 'producto' : 'productos'}`;
      if (floatingTotal) floatingTotal.textContent = formatCLP(totalFinal);
    } else {
      floatingBar.classList.remove("visible");
    }
  }

  renderizarTablaResumen();
}

function renderizarTablaResumen() {
  const container = document.getElementById("items-cotizados-list");
  if (!container) return;

  const itemsKeys = Object.keys(carritoCotizacion);
  if (itemsKeys.length === 0) {
    container.innerHTML = `
      <div class="empty-cart-state">
        <h4>Cotización sin productos seleccionados</h4>
        <p>Ajusta las cantidades en el catálogo superior para calcular el desglose y descuentos por volumen.</p>
      </div>
    `;
    return;
  }

  let totalUnidades = 0;
  itemsKeys.forEach(id => totalUnidades += carritoCotizacion[id]);
  const tramo = obtenerTramoDescuento(totalUnidades);

  container.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
      <span style="font-size: 0.9rem; color: var(--text-muted);">${itemsKeys.length} ${itemsKeys.length === 1 ? 'producto seleccionado' : 'productos seleccionados'}</span>
      <button type="button" onclick="vaciarCarrito()" style="background: transparent; border: 1px solid rgba(237,28,36,0.3); color: #ff6b6b; padding: 4px 12px; border-radius: 6px; font-size: 0.8rem; cursor: pointer;">Vaciar Cotización</button>
    </div>
    <div style="overflow-x: auto;">
      <table class="tabla-resumen-cotizacion">
        <thead>
          <tr>
            <th>Producto</th>
            <th class="text-center">Cant.</th>
            <th class="text-right">Precio Lista</th>
            <th class="text-right">Desc. (${Math.round(tramo.dto * 100)}%)</th>
            <th class="text-right">Total Neto</th>
            <th class="text-center">Quitar</th>
          </tr>
        </thead>
        <tbody>
          ${itemsKeys.map(id => {
            const qty = carritoCotizacion[id];
            const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
            if (!prod) return '';
            const precioUnitConDto = prod.precioLista * (1 - tramo.dto);
            const totalNeto = precioUnitConDto * qty;
            return `
              <tr>
                <td>
                  <div style="display: flex; align-items: center; gap: 10px;">
                    <img src="${prod.img}" alt="${prod.nombre}" style="width: 36px; height: 36px; object-fit: contain; border-radius: 6px; background: #000;" onerror="this.src='img/logo_spiral_transparent.png'">
                    <div>
                      <div style="font-weight: 700; color: #fff;">${prod.nombre}</div>
                      <div style="font-size: 0.75rem; color: var(--text-muted);">${prod.categoriaLabel}</div>
                    </div>
                  </div>
                </td>
                <td class="text-center">
                  <span class="badge-table-qty">${qty}</span>
                </td>
                <td class="text-right">${formatCLP(prod.precioLista)}</td>
                <td class="text-right text-gold">-${formatCLP(prod.precioLista * tramo.dto)}</td>
                <td class="text-right bold">${formatCLP(totalNeto)}</td>
                <td class="text-center">
                  <button type="button" class="btn-remove-item" onclick="setCantidad('${prod.id}', 0)" title="Eliminar ítem">✕</button>
                </td>
              </tr>
            `;
          }).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function enviarWhatsApp() {
  const itemsKeys = Object.keys(carritoCotizacion);
  if (itemsKeys.length === 0) {
    alert("Por favor selecciona al menos un producto antes de solicitar por WhatsApp.");
    return;
  }

  let totalUnidades = 0;
  let subtotalLista = 0;

  itemsKeys.forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    if (prod) {
      totalUnidades += qty;
      subtotalLista += (prod.precioLista * qty);
    }
  });

  const tramo = obtenerTramoDescuento(totalUnidades);
  const montoDto = subtotalLista * tramo.dto;
  const subtotalNeto = subtotalLista - montoDto;
  const iva = subtotalNeto * 0.19;
  const totalBruto = subtotalNeto + iva;

  let msg = "COTIZACIÓN OFICIAL — AMÉRICA PULIDO SPA\n";
  msg += "━━━━━━━━━━━━━━━━━━━━━\n";
  msg += "Hola, solicito la siguiente cotización de insumos realizada desde la web:\n\n";

  itemsKeys.forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    if (prod) {
      const precioUnitDto = prod.precioLista * (1 - tramo.dto);
      msg += `▪ ${prod.nombre}\n  Cantidad: ${qty} unid. | Precio: ${formatCLP(precioUnitDto)} c/u\n`;
    }
  });

  msg += "\n━━━━━━━━━━━━━━━━━━━━━\n";
  msg += `Total Unidades: ${totalUnidades} unid.\n`;
  msg += `Descuento Aplicado: ${Math.round(tramo.dto * 100)}% (-${formatCLP(montoDto)})\n`;
  msg += `Subtotal Neto: ${formatCLP(subtotalNeto)}\n`;
  msg += `IVA 19%: ${formatCLP(iva)}\n`;
  msg += `TOTAL FINAL: ${formatCLP(totalBruto)}\n`;
  
  if (totalBruto >= 100000) {
    msg += "Beneficio: Aplica a Envío Gratis en Santiago RM\n";
  }
  msg += "\nQuedo atento a la confirmación de stock, medios de pago y fecha de despacho. Muchas gracias.";

  const phone = "56978685664";
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
}

function descargarPDFCotizacion() {
  const itemsKeys = Object.keys(carritoCotizacion);
  if (itemsKeys.length === 0) {
    alert("Por favor selecciona productos para generar el documento formal en PDF.");
    return;
  }

  let totalUnidades = 0;
  let subtotalLista = 0;
  itemsKeys.forEach(id => {
    const qty = carritoCotizacion[id];
    const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
    if (prod) {
      totalUnidades += qty;
      subtotalLista += (prod.precioLista * qty);
    }
  });

  const tramo = obtenerTramoDescuento(totalUnidades);
  const montoDto = subtotalLista * tramo.dto;
  const subtotalNeto = subtotalLista - montoDto;
  const iva = subtotalNeto * 0.19;
  const totalBruto = subtotalNeto + iva;

  const fechaHoy = new Date().toLocaleDateString('es-CL', { year: 'numeric', month: 'long', day: 'numeric' });
  const numCotizacion = "AP-" + Math.floor(100000 + Math.random() * 900000);

  const printWindow = window.open('', '_blank');
  if (!printWindow) {
    alert("Por favor habilita las ventanas emergentes (popups) para ver el PDF.");
    return;
  }

  printWindow.document.write(`
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <title>Cotización ${numCotizacion} - América Pulido SPA</title>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
      <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }
        body { color: #1e293b; padding: 40px; margin: 0; background: #ffffff; line-height: 1.5; font-size: 13px; }
        .no-print { margin-bottom: 24px; text-align: right; }
        .btn-print { background: #D4A843; color: #000; font-weight: 800; border: none; padding: 12px 24px; font-size: 14px; border-radius: 8px; cursor: pointer; }
        .header-pdf { display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #D4A843; padding-bottom: 24px; margin-bottom: 24px; }
        .logo-box { display: flex; align-items: center; gap: 14px; }
        .logo-box img { height: 60px; }
        .brand-title { font-size: 20px; font-weight: 900; color: #0a0a0a; letter-spacing: -0.5px; }
        .brand-sub { font-size: 11px; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }
        .company-details { text-align: right; font-size: 12px; color: #475569; line-height: 1.5; }
        .doc-title-bar { display: flex; justify-content: space-between; align-items: center; background: #0a0a0a; color: #fff; padding: 14px 20px; border-radius: 8px; margin-bottom: 24px; }
        .doc-title-bar h1 { font-size: 16px; font-weight: 800; letter-spacing: 1px; color: #D4A843; }
        .meta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; background: #f8fafc; border: 1px solid #e2e8f0; padding: 16px 20px; border-radius: 8px; margin-bottom: 24px; font-size: 13px; }
        .meta-col div { margin-bottom: 6px; }
        .tabla-pdf { width: 100%; border-collapse: collapse; margin-bottom: 28px; }
        .tabla-pdf th { background: #0f172a; color: #ffffff; padding: 12px 14px; font-size: 12px; font-weight: 700; text-align: left; text-transform: uppercase; letter-spacing: 0.5px; }
        .tabla-pdf td { padding: 12px 14px; border-bottom: 1px solid #e2e8f0; font-size: 12px; vertical-align: middle; }
        .tabla-pdf tr:nth-child(even) { background: #f8fafc; }
        .totales-wrapper { display: flex; justify-content: flex-end; margin-bottom: 30px; }
        .totales-box { width: 340px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; }
        .row-total { display: flex; justify-content: space-between; padding: 6px 0; font-size: 13px; color: #475569; }
        .row-total.discount { color: #b45309; font-weight: 700; }
        .row-total.final { font-size: 17px; font-weight: 900; color: #0a0a0a; border-top: 2px solid #D4A843; margin-top: 8px; padding-top: 10px; }
        .condiciones-box { background: #fffbeb; border: 1px solid #fef3c7; padding: 16px 20px; border-radius: 8px; margin-bottom: 24px; font-size: 12px; color: #92400e; }
        .condiciones-box h4 { font-weight: 800; margin-bottom: 6px; }
        .footer-pdf { text-align: center; font-size: 11px; color: #94a3b8; border-top: 1px solid #e2e8f0; padding-top: 20px; }
        @media print {
          body { padding: 0; }
          .no-print { display: none; }
        }
      </style>
    </head>
    <body>
      <div class="no-print">
        <button class="btn-print" onclick="window.print()">Imprimir / Guardar como PDF</button>
      </div>

      <div class="header-pdf">
        <div class="logo-box">
          <img src="img/logo_spiral_transparent.png" alt="América Pulido SPA">
          <div>
            <div class="brand-title">AMÉRICA PULIDO SPA</div>
            <div class="brand-sub">Soluciones & Insumos Diamantados</div>
          </div>
        </div>
        <div class="company-details">
          <strong>RUT:</strong> 77.654.321-K<br>
          <strong>Dirección:</strong> Carmen Covarrubias 32 Of 601, Ñuñoa, Santiago<br>
          <strong>WhatsApp:</strong> +56 9 7868 5664 | +56 9 6822 1431<br>
          <strong>Web:</strong> www.americapulidospa.cl
        </div>
      </div>

      <div class="doc-title-bar">
        <h1>COTIZACIÓN COMERCIAL OFICIAL</h1>
        <div><strong>FOLIO:</strong> ${numCotizacion}</div>
      </div>

      <div class="meta-grid">
        <div class="meta-col">
          <div><strong>Fecha de Emisión:</strong> ${fechaHoy}</div>
          <div><strong>Validez de Oferta:</strong> 15 Días corridos</div>
          <div><strong>Forma de Pago:</strong> Transferencia bancaria / Tarjeta de Crédito</div>
        </div>
        <div class="meta-col">
          <div><strong>Cobertura Despacho:</strong> Santiago RM y Regiones (Starken / Chilexpress)</div>
          <div><strong>Beneficio Especial:</strong> ${totalBruto >= 100000 ? 'Envío sin costo en Santiago RM' : 'Tarifa estándar de envío'}</div>
          <div><strong>Descuento Aplicado:</strong> <span style="color:#b45309; font-weight:bold;">${Math.round(tramo.dto * 100)}% por Tramo de Volumen</span></div>
        </div>
      </div>

      <table class="tabla-pdf">
        <thead>
          <tr>
            <th>Descripción del Producto / Insumo</th>
            <th style="text-align: center;">Cant.</th>
            <th style="text-align: right;">Precio Lista</th>
            <th style="text-align: right;">Precio c/ Descuento</th>
            <th style="text-align: right;">Total Neto</th>
          </tr>
        </thead>
        <tbody>
          ${itemsKeys.map(id => {
            const qty = carritoCotizacion[id];
            const prod = PRODUCTOS_CATALOGO.find(p => p.id === id);
            if (!prod) return '';
            const precioUnitDto = prod.precioLista * (1 - tramo.dto);
            const totalNeto = precioUnitDto * qty;
            return `
              <tr>
                <td>
                  <strong>${prod.nombre}</strong>
                  <div style="font-size:11px; color:#64748b;">${prod.categoriaLabel}</div>
                </td>
                <td style="text-align: center; font-weight:bold;">${qty}</td>
                <td style="text-align: right;">${formatCLP(prod.precioLista)}</td>
                <td style="text-align: right; color:#b45309; font-weight:600;">${formatCLP(precioUnitDto)}</td>
                <td style="text-align: right; font-weight:bold;">${formatCLP(totalNeto)}</td>
              </tr>
            `;
          }).join("")}
        </tbody>
      </table>

      <div class="totales-wrapper">
        <div class="totales-box">
          <div class="row-total">
            <span>Subtotal Lista (${totalUnidades} unid.):</span>
            <span>${formatCLP(subtotalLista)}</span>
          </div>
          <div class="row-total discount">
            <span>Descuento Escala (${Math.round(tramo.dto * 100)}%):</span>
            <span>-${formatCLP(montoDto)}</span>
          </div>
          <div class="row-total">
            <span>Subtotal Neto:</span>
            <span>${formatCLP(subtotalNeto)}</span>
          </div>
          <div class="row-total">
            <span>IVA (19%):</span>
            <span>${formatCLP(iva)}</span>
          </div>
          <div class="row-total final">
            <span>TOTAL BRUTO:</span>
            <span>${formatCLP(totalBruto)}</span>
          </div>
        </div>
      </div>

      <div class="condiciones-box">
        <h4>Condiciones Comerciales y Despacho:</h4>
        <p>• Los precios indicados incluyen IVA oficial. Para coordinar emisión de factura con RUT, favor contactar al WhatsApp de ventas +56 9 7868 5664.</p>
        <p>• Despachos en Santiago RM dentro de 24 a 48 horas hábiles tras confirmación de transferencia.</p>
        <p>• Despachos a regiones se realizan por pagar o convenio Starken / Chilexpress / Pullman Cargo.</p>
      </div>

      <div class="footer-pdf">
        América Pulido SPA — Especialistas en Restauración, Pulido de Pisos e Insumos Diamantados de Alto Rendimiento.
      </div>
    </body>
    </html>
  `);
  printWindow.document.close();
}
