import os
import sys
import json
import argparse
import requests
from pathlib import Path

# Configurar encoding utf-8 para la consola de Windows
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


# Cargar variables de entorno desde .env
def load_env():
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ[k.strip()] = v.strip()

load_env()

FB_PAGE_ID = os.getenv("FB_PAGE_ID", "1001159099738099")
IG_USER_ID = os.getenv("IG_USER_ID")
META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
PUBLIC_IMAGE_BASE_URL = os.getenv("PUBLIC_IMAGE_BASE_URL", "https://www.americapulidospa.cl")

# Parrilla integrada de 18 posts con imágenes y copies
PARRILLA_POSTS = {
    1: {
        "title": "Saca Bocado Diamantado 35mm",
        "image": "img/productos/prod_sacabocado_35mm.jpg",
        "caption": """🔥 ¡Perforaciones perfectas en porcelanato y mármol sin romper nada! 💎

¿Cansado de despostillar palmetas costosas al instalar grifería o cañerías? Con nuestro Saca Bocado Diamantado de 35mm logras cortes limpios, rápidos y precisos en segundos.

✨ Ideal para: Porcelanato, mármol, granito y baldosas.
📏 Medida estándar de 35mm (la medida justa para griferías).
🔄 Uso en seco o húmedo.

💰 PRECIO: $17.000 CLP c/u

🚚 PAGO CONTRA ENTREGA EN SANTIAGO (RM): Recibes en tu taller u obra y pagas al instante.
📦 ENVÍOS A TODO CHILE: Despachamos a regiones previa transferencia.

📲 ¡Pide el tuyo ahora mismo por WhatsApp al +56 9 7868 5664! 🔗

#AmericaPulido #SacaBocado35mm #HerramientasDePulido #MarmoleriaChile #PorcelanatoSantiago #ConstruccionChile #PagoContraEntrega"""
    },
    2: {
        "title": "Discos de Resina Premium",
        "image": "img/productos/prod_resina_premium.jpg",
        "caption": """✨ Brillo espejo profesional en mármol, hormigón y terrazo 🏢💎

Eleva la calidad de tus trabajos con nuestros Discos de Resina Premium. Diseñados con máxima densidad diamantada para un refinado ultrarrápido y un acabado brillante duradero.

🔹 Granos disponibles: 50, 100, 200, 400, 800, 1500, 3000.
🔹 Rendimiento superior por disco.
🔹 Apto uso en seco y húmedo.

💰 PRECIO: $11.990 CLP c/u

🚚 PAGO CONTRA ENTREGA EXCLUSIVO EN SANTIAGO: Pagas al recibir en tu domicilio/obra.
📦 ENVÍOS A REGIONES: Cobertura a todo Chile vía Starken / Chilexpress.

📩 Escríbenos al WhatsApp +56 9 7868 5664 y cotiza tu juego de resinas hoy.

#PulidoDePisos #DiscosDeResina #MarmolChile #HormigonPulido #InsumosDePulido #AmericaPulido"""
    },
    3: {
        "title": "Disco de Resina en Seco",
        "image": "img/productos/prod_resina_seco.jpg",
        "caption": """🚫💧 ¡Trabaja en seco sin quemar la piedra ni dejar marcas! 

Nuestros Discos de Resina en Seco están formulados para resistir alta fricción sin desprender polvo nocivo ni dañar el material base.

✅ Ideal para terminaciones rápidas y repasos en seco.
✅ Disponible en todos los granos refinadores.

💰 PRECIO: $5.800 CLP c/u

🚚 Santiago: ¡PAGO CONTRA ENTREGA! Paga cuando el pedido llegue a tus manos.
📦 Regiones: Envíos diarios a todo Chile.

📲 Haz tu pedido rápido por WhatsApp al +56 9 7868 5664. ¡Respondemos al instante!

#InsumosMarmoleria #PulidoEnSeco #HerramientasChile #SantiagoChile #ConstruccionRM"""
    },
    4: {
        "title": "Disco Ranurador Diamantado 114mm x 10mm",
        "image": "img/productos/prod_ranurador_114mm.jpg",
        "caption": """💪 Ranurado pesado de 10mm de espesor para mármol y granito 🪨⚡

Si realizas ranuras de drenaje en cubiertas, escurridores o canterías técnicas, necesitas el Disco Ranurador Diamantado 114mm x 10mm de América Pulido.

⚙️ Espesor exacto de 10mm.
⚙️ Rendimiento extremo en cortes profundos y repetitivos.

💰 PRECIO: $49.000 CLP c/u

🚚 SANTIAGO: Entrega con Pago Contra Entrega (efectivo o transferencia al recibir).
📦 RESTO DE CHILE: Envío seguro a regiones previo pago.

📲 Cotiza directo en WhatsApp: +56 9 7868 5664.

#MarmolerosChile #GranitoSantiago #RanuradorDiamantado #AmericaPulidoSPA #HerramientasProfesionales"""
    },
    5: {
        "title": "Masilla Mágica Dermax",
        "image": "img/productos/prod_masilla_dermax.jpg",
        "caption": """🧪 Rellena, pega y restaura mármol con acabado invisible ✨

La Masilla Mágica de Poliéster Dermax es la aliada número 1 para reparar grietas, saltaduras o unir piezas de piedra natural y baldosas.

⚪ Disponible en color Blanco y Negro.
🧪 Incluye su catalizador de secado rápido.
🎨 Apta para pigmentar y pulir al ras.

💰 PRECIO: $21.990 CLP c/u (Tarro + Catalizador)

🚚 PAGO CONTRA ENTREGA EN SANTIAGO (RM).
📦 ENVÍOS A REGIONES en 24-48 horas.

📲 Pídela hoy al WhatsApp +56 9 7868 5664!

#MasillaDermax #RestauracionDeMarmol #PegadoDePiedra #MarmoleriaSantiago #AmericaPulido"""
    },
    6: {
        "title": "Piedra Cónica de Desbaste",
        "image": "img/productos/prod_piedra_conica.jpg",
        "caption": """📐 Llega a donde la pulidora plana no puede llegar 📐

La Piedra Cónica de Carburo de Silicio (M14) es imprescindible para desbastar bordes, zócalos, escalones y esquinas difíciles.

🔹 Granos disponibles: 36 (Desbaste agresivo), 60 y 80.
🔹 Conexión M14 estándar para esmeril/galleteadora.

💰 PRECIO: $12.990 CLP c/u

🚚 Santiago: PAGO CONTRA ENTREGA directito a tu taller u obra.
📦 Regiones: Despachos a todo Chile.

📲 ¿Necesitas asesoría o comprar? Escríbenos al WhatsApp +56 9 7868 5664.

#PiedraConica #EsquinasYTerminaciones #PulidoDeZocalos #InsumosSantiago #AmericaPulido"""
    },
    7: {
        "title": "Rodillo Diamantado M14",
        "image": "img/productos/prod_rodillo_diamantado.jpg",
        "caption": """🌀 Biselado y perfilado perfecto en cantos curvos 🪨

El Rodillo Diamantado M14 te permite moldear y dar acabado a bordes redondeados, curvas de encimeras y perfilados cóncavos con total suavidad.

▫️ Rosca directa M14.
▫️ Diámetros: 30mm, 40mm y 50mm.

💰 PRECIO: $59.990 CLP c/u

🚚 SANTIAGO: PAGO CONTRA ENTREGA en toda la Región Metropolitana.
📦 REGIONES: Envíos por pagar a través de Starken/Chilexpress.

📲 WhatsApp directo: +56 9 7868 5664.

#RodilloDiamantado #EncimerasDeMarmol #GranitoChile #AmericaPulido #HerramientasDeMarmoleria"""
    },
    8: {
        "title": "Bases para Pulir M14",
        "image": "img/productos/prod_base_pulir_reforzada.jpg",
        "caption": """🧩 ¿Base Flexible o Base Reforzada de Bronce? Tenemos las dos 👇

Para que tus discos rindan al 100%, necesitas el soporte adecuado:

1️⃣ Base Flexible ($3.000 CLP): Se adapta a desniveles suaves y relieves sin marcar la superficie.
2️⃣ Base Reforzada con Inserto de Bronce M14 ($9.990 CLP): Ultra resistente para trabajos pesados.

💰 PRECIOS: Desde $3.000 CLP

🚚 PAGO CONTRA ENTREGA EN SANTIAGO (RM).
📦 ENVÍOS A REGIONES previo pago.

📲 Escríbenos al WhatsApp +56 9 7868 5664!

#BasesParaPulir #SoporteVelcro #HerramientasSantiago #PisosPulidos #AmericaPulido"""
    },
    9: {
        "title": "Discos Diamantados de Corte",
        "image": "img/productos/prod_corte_segmentado.jpg",
        "caption": """✂️ Corte fino y rápido en concreto, porcelanato y azulejos 🧱✨

Línea de Discos Diamantados de Corte América Pulido:
🔸 Continuous Rim (Continuo): Para cortes extra limpios sin astillar azulejos o porcelanatos.
🔸 Segmented Rim (Segmentado): Para velocidad e impacto en concreto, ladrillo y piedra.

📏 Medidas: 4 1/2" y 7"

💰 PRECIOS: 4 1/2": $5.990 CLP | 7": $13.990 CLP

🚚 PAGO CONTRA ENTREGA EN SANTIAGO.
📦 ENVÍOS A TODO CHILE.

📲 Paga al recibir en Santiago escribiendo al WhatsApp +56 9 7868 5664.

#DiscosDeCorte #PorcelanatoChile #ConstruccionSantiago #AmericaPulido"""
    },
    10: {
        "title": "Pañete Industrial de Lustrado Final",
        "image": "img/productos/prod_panete.jpg",
        "caption": """🪞 El secreto del verdadero Brillo Espejo 🪞

Logra el sello final profesional en mármol y superficies pulidas con nuestro Pañete Textil Industrial de Lustrado.

✨ Elimina micro-rayas.
✨ Realza el tono natural de la piedra con cera o cristalizador.

💰 PRECIO: $19.990 CLP

🚚 PAGO CONTRA ENTREGA EN SANTIAGO (RM).
📦 ENVÍOS A REGIONES a diario.

📲 ¡Haz tu pedido ahora al WhatsApp +56 9 7868 5664!

#LustradoEspejo #RestauracionDePisos #MarmolSantiago #AmericaPulido"""
    },
    11: {
        "title": "Pulido y Restauración de Parquet",
        "image": "img/madera-brillo.jpg",
        "caption": """🪵 ¿Tu piso de parquet perdió la vida y el color? ¡No lo reemplaces, restáuralo! 🪵

En América Pulido devolvemos el esplendor original a tu piso de madera o parquet con nuestro proceso de pulido profesional.

✅ 100% Trabajo Limpio: Tecnología de aspirado de polvo para no ensuciar tu hogar.
✅ Sellado Protector: Capa vitrificada o plastificada resistente a rayas y humedad.
✅ Visita Técnica GRATIS en Santiago.

💰 Cotización transparente por m² según el estado de tu piso.

📍 Cobertura completa en Región Metropolitana.

📲 Escríbenos hoy al WhatsApp +56 9 7868 5664!

#PulidoDeParquet #PisosDeMadera #RestauracionDeParquet #Vitrificado #SantiagoOriente #AmericaPulido"""
    },
    12: {
        "title": "Pulido y Vitrificado de Mármol y Granito",
        "image": "img/calidad-brillo.jpg",
        "caption": """🏛️ Recupera la elegancia y el brillo espejo de tus pisos de Mármol ✨

El mármol opaco o manchado le quita valor a tu propiedad. Con nuestro servicio especializado de desbaste, diamantado y vitrificado, tu mármol lucirá impecable por años.

💎 Eliminación de manchas, porosidad y desnivelaciones.
💎 Sellado cristalizador de alta resistencia.
💎 Experiencia comprobada en residencias y halls comerciales.

📍 Atendemos en toda la Región Metropolitana.

📲 Agenda una Visita Técnica GRATIS en Santiago llamando o escribiendo al WhatsApp +56 9 7868 5664!

#PulidoDeMarmol #MarmolSantiago #PisosDeLujo #InteriorismoChile #AmericaPulidoSPA"""
    },
    13: {
        "title": "Pulido de Hormigón Industrial",
        "image": "img/hormigon-industrial.jpg",
        "caption": """🏭 Piso industrial resistente, reflectante y libre de polvo para tu empresa 🚚

Mejora la seguridad y durabilidad de tus bodegas o locales comerciales con nuestro servicio de Pulido y Tratamiento de Hormigón / Concreto.

⚡ Superficie endurecida y antideslizante.
⚡ Resiste alto tráfico de grúas horquilla y carga pesada.
⚡ Reduce el desgaste de maquinarias y elimina el polvo en suspensión.

📍 Servicio en toda la Región Metropolitana.

📲 Cotiza rápido para tu empresa llamando o escribiendo al WhatsApp +56 9 7868 5664.

#HormigonPulido #PisosIndustriales #GalponesChile #BodegasSantiago #LogisticaChile #AmericaPulido"""
    },
    14: {
        "title": "Restauración de Baldosas Graníticas",
        "image": "img/baldosa-comercial.jpg",
        "caption": """🧱 ¿Baldosas antiguas o manchadas? ¡Les devolvemos su color vibrante! 🎨

Las baldosas y baldosines graníticos son materiales nobles que duran toda la vida si reciben el tratamiento adecuado.

🔹 Desbaste profundo para eliminar ceras viejas y mugre incrustada.
🔹 Pulido progresivo con diamantes.
🔹 Sellante protector repelente al agua y manchas.

📍 Visita de evaluación GRATIS en todo Santiago.

📲 Escríbenos al WhatsApp +56 9 7868 5664!

#BaldosasGraniticas #RestauracionDePisos #PisosAntiguos #AmericaPulido #SantiagoRM"""
    },
    15: {
        "title": "4 Garantías América Pulido",
        "image": "img/hero-servicios.jpg",
        "caption": """🔒 Por qué cientos de clientes confían en América Pulido SPA 🇨🇱

Cuando contratas un servicio para tu hogar o empresa, la tranquilidad lo es todo. Por eso te ofrecemos nuestras 4 Garantías Únicas:

1️⃣ Trabajo 100% Limpio: Sistema con aspirado continuo para no llenar tu casa de polvo.
2️⃣ Puntualidad y Rapidez: Cumplimos los plazos acordados sin demoras innecesarias.
3️⃣ Brillo Duradero: Usamos los mejores insumos diamantados y sellantes del mercado.
4️⃣ Transparencia Total: Precio cerrado desde la visita técnica, sin sorpresas ni cobros ocultos.

📲 Solicita tu evaluación gratuita en Santiago al WhatsApp +56 9 7868 5664.

#Garantia #PisosLimpios #ServicioProfesional #PulidoDePisos #AmericaPulido"""
    },
    16: {
        "title": "Caso Real Antes y Después",
        "image": "img/antes-despues.jpg",
        "caption": """👀 Desliza para ver la transformación completa ➡️✨

De un piso rayado, opaco y desgastado a una superficie que parece un espejo recién instalado. 

No gastes millones en cambiar tus pisos. La restauración con pulido diamantado cuesta una fracción y dura muchísimos años.

📍 Servicio disponible en toda la Región Metropolitana.
🆓 Visita técnica de evaluación 100% GRATUITA.

📲 Escríbenos un mensaje al WhatsApp +56 9 7868 5664 con las fotos de tu piso y te orientamos al instante.

#AntesYDespues #Transformacion #RemodelacionCasa #PisosBrillantes #AmericaPulido"""
    },
    17: {
        "title": "Servicio para Comunidades y Edificios",
        "image": "img/foto-real-comercial.jpg",
        "caption": """🏢 Mantén las áreas comunes de tu edificio impecables y revaloriza la comunidad 👥

Un hall de entrada o escaleras con mármol y granito brillante cambian completamente la percepción de un edificio o condominio.

Ofrecemos:
🏢 Pulido y vitrificado de recepción, pasillos y ascensores.
🏢 Trabajos programados para no interrumpir el tránsito de residentes.
🏢 Emitimos factura y entregamos garantía por escrito.

📲 Administradores y miembros de comité: Contáctennos al WhatsApp +56 9 7868 5664 para una cotización formal.

#EdificiosSantiago #AdministracionDeEdificios #ComunidadesChile #PulidoMarmol #AmericaPulido"""
    },
    18: {
        "title": "Visita Técnica Gratuita + Cotización Inmediata",
        "image": "img/logo-showcase.jpg",
        "caption": """⚡ ¿Pensando en renovar los pisos de tu casa u oficina antes que termine el mes? 🏡

¡No lo pienses más! En América Pulido SPA te lo ponemos fácil:

🎁 VISITA TÉCNICA 100% GRATUITA EN SANTIAGO
Evaluamos el estado de tu piso en persona, medimos los m² y te entregamos un presupuesto exacto en menos de 24 hrs. Sin compromisos.

Atendemos pisos de:
Madera / Parquet | Mármol / Granito | Hormigón Industrial | Baldosa

📲 Agenda tu hora hoy mismo escribiendo al WhatsApp +56 9 7868 5664!

#RemodelacionSantiago #VisitaTecnicaGratis #AmericaPulido #PisosNuevos #CotizaGratis"""
    }
}

def publish_to_facebook_page(image_url, caption):
    """
    Publica una foto con texto en la Página de Facebook de América Pulido vía Graph API.
    """
    if not FB_PAGE_ID or not META_ACCESS_TOKEN:
        print("[ERROR] Falta FB_PAGE_ID o META_ACCESS_TOKEN en el archivo .env")
        return False

    url = f"https://graph.facebook.com/v21.0/{FB_PAGE_ID}/photos"
    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": META_ACCESS_TOKEN
    }
    res = requests.post(url, data=payload)
    data = res.json()
    if "id" in data:
        print(f"✅ Post publicado exitosamente en la Página de Facebook 'America Pulido' (ID del Post: {data['id']})")
        return True
    else:
        print(f"❌ Error al publicar en Facebook: {json.dumps(data, indent=2)}")
        return False

def publish_to_instagram(image_url, caption):
    """
    Publica en Instagram Business vía Instagram Content Publishing API.
    """
    if not IG_USER_ID or not META_ACCESS_TOKEN:
        print("⚠️ [NOTA] IG_USER_ID no configurado aún o requiere permisos de Instagram Business en el Token.")
        return False

    # Paso 1: Crear Contenedor
    container_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
    container_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": META_ACCESS_TOKEN
    }
    c_res = requests.post(container_url, data=container_payload)
    c_data = c_res.json()

    if "id" not in c_data:
        print(f"❌ Error al crear contenedor de Instagram: {json.dumps(c_data, indent=2)}")
        return False

    creation_id = c_data["id"]
    print(f"🔄 Contenedor de Instagram creado ({creation_id}). Publicando...")

    # Paso 2: Publicar
    publish_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        "creation_id": creation_id,
        "access_token": META_ACCESS_TOKEN
    }
    p_res = requests.post(publish_url, data=publish_payload)
    p_data = p_res.json()

    if "id" in p_data:
        print(f"✅ Post publicado exitosamente en Instagram (ID del Post: {p_data['id']})")
        return True
    else:
        print(f"❌ Error al finalizar publicación en Instagram: {json.dumps(p_data, indent=2)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Publicador Automático de América Pulido SPA")
    parser.add_argument("--post", type=int, help="Número del post a publicar (1 al 18)")
    parser.add_argument("--image_url", type=str, help="URL pública de la imagen")
    parser.add_argument("--caption", type=str, help="Texto del post")
    parser.add_argument("--target", choices=["all", "fb", "ig"], default="fb", help="Destino (fb, ig, all)")

    args = parser.parse_args()

    image_url = args.image_url
    caption = args.caption

    if args.post:
        if args.post in PARRILLA_POSTS:
            post_info = PARRILLA_POSTS[args.post]
            print(f"📌 Seleccionado Post N° {args.post}: {post_info['title']}")
            # Convertir imagen local a URL accesible públicamente o usar URL configurada
            rel_img = post_info["image"]
            image_url = f"{PUBLIC_IMAGE_BASE_URL}/{rel_img}"
            caption = post_info["caption"]
        else:
            print(f"❌ El post N° {args.post} no existe en la parrilla (disponibles 1 a 18).")
            sys.exit(1)

    if not image_url or not caption:
        print("❌ Error: Debes especificar --post N o entregar --image_url y --caption.")
        sys.exit(1)

    print(f"🚀 Iniciando publicación en Facebook/Instagram para América Pulido...")
    print(f"📸 Imagen: {image_url}")

    if args.target in ["all", "fb"]:
        publish_to_facebook_page(image_url, caption)
    if args.target in ["all", "ig"]:
        publish_to_instagram(image_url, caption)

if __name__ == "__main__":
    main()
