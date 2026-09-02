import os
import sys
import json
import time
import requests
from pathlib import Path

# Configurar encoding utf-8 para Windows
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

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

META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID", "17841480439662331")
PUBLIC_IMAGE_BASE_URL = os.getenv("PUBLIC_IMAGE_BASE_URL", "https://www.americapulidospa.cl")

SERVICIOS_DIR = Path(__file__).parent / "img" / "servicios"

POSTS_SERVICIOS = {
    2: {
        "image": "2.png",
        "caption": """Pulido y Vitrificado Profesional de Pavimentos 🏛️✨

En América Pulido SPA ejecutamos tratamientos integrales de nivelado, pulido y vitrificado para la restauración de pisos desgastados por el uso continuo.

🔹 Metodología Limpia: Incorporamos unidades de aspirado industrial acoplado para minimizar la emisión de partículas durante la faena.

📲 Solicite su evaluación presencial en la Región Metropolitana al WhatsApp +56 9 7868 5664.

#PulidoDePisos #Vitrificado #Restauracion #PisosChile #AmericaPulido"""
    },
    3: {
        "image": "3.png",
        "caption": """Restauración y Vitrificado de Pisos de Madera de Alto Estándar 🪵✨

Devolvemos la nobleza y textura original a sus pavimentos de madera y parquet mediante procesos de desbaste diamantado y aplicación de sellantes de alta resistencia.

🔹 Preservación del Entorno: Metodología limpia que mitiga la emisión de partículas en suspensión y protege sus ambientes.

📲 Consultas y Cotizaciones: Escríbanos directamente al WhatsApp +56 9 7868 5664.

#ParquetChile #PisosDeMadera #VitrificadoProfesional #RemodelacionSantiago #LasCondes #AmericaPulido"""
    },
    4: {
        "image": "4.png",
        "caption": """Renovación de Parquet y Pisos Nobles 🪵🏠

El paso de los años opaca la madera original de su propiedad. Con nuestra tecnología de restauración diamantada y vitrificado, recuperamos su color y protección sin necesidad de reemplazo.

🔹 Proceso limpio y controlado con aspiración continua acoplada a la maquinaria.

📲 Agende su evaluación técnica gratuita al WhatsApp +56 9 7868 5664.

#RestauracionDePisos #ParquetSantiago #PisosDeMadera #Providencia #Vitacura #AmericaPulido"""
    },
    5: {
        "image": "5.png",
        "caption": """Protección y Sellado de Madera de Alta Resistencia 🪵🛡️

Aplicación de barnices vitrificantes de alto tráfico con acabados mate, satinado o brillante según la arquitectura de su inmueble.

🔹 Máxima durabilidad contra la humedad, rayones y desgaste diario.

📲 Cotice con nuestros especialistas al WhatsApp +56 9 7868 5664.

#VitrificadoChile #PisosResidenciales #RemodelacionCasa #SantiagoOriente #AmericaPulido"""
    },
    6: {
        "image": "6.png",
        "caption": """Tratamiento Especializado y Refinado Diamantado de Mármol 🏛️💎

El mármol requiere intervenciones técnicas orientadas a corregir la porosidad y recuperar su nivel de reflectividad natural.

🔹 Proceso en Húmedo: Refinado de superficie con supresión de polvo para garantizar acabados cristalinos y duraderos.

📲 Coordine su visita técnica sin costo en la Región Metropolitana al WhatsApp +56 9 7868 5664.

#MarmolChile #PulidoDeMarmol #PisosDeLujo #DiseñoDeInteriores #Vitacura #AmericaPulido"""
    },
    7: {
        "image": "7.png",
        "caption": """Hormigón Armado y Pavimentos de Alto Tráfico ⚙️🏭

Preparación y tratamiento de pisos de hormigón en instalaciones comerciales, oficinas y bodegas industriales.

🔹 Superficie Antipolvo: Densificado y sellado que incrementa la resistencia mecánica y facilita la mantenibilidad.

📲 Contacto corporativo directo al WhatsApp +56 9 7868 5664.

#HormigonPulido #PisosIndustriales #ConstruccionChile #BodegasSantiago #AmericaPulido"""
    },
    8: {
        "image": "8.png",
        "caption": """Restauración Técnica de Baldosas Graníticas y Terrazos 🏢✨

Recuperación del color original, brillo y protección de superficies desgastadas por el tránsito frecuente.

🔹 Proceso controlado sin generación de residuos molestos para sus espacios.

📲 Consulte por su superficie escribiendo al WhatsApp +56 9 7868 5664.

#BaldosasGraniticas #TerrazosChile #RestauracionPisos #SantiagoChile #AmericaPulido"""
    },
    9: {
        "image": "9.png",
        "caption": """Limpieza Profunda e Higienización de Alfombras 🧼🏠

Servicio complementario de sanitización y lavado profundo de alfombras para residencias, oficinas y espacios comerciales.

🔹 Eliminación de manchas y renovación de fibras para un ambiente fresco.

📲 Agende su servicio al WhatsApp +56 9 7868 5664.

#LavadoDeAlfombras #LimpiezaProfesional #OficinasSantiago #MantencionHogar #AmericaPulido"""
    },
    10: {
        "image": "10.png",
        "caption": """Sistemas Integrales: Pulido, Sellado y Vitrificado 🏛️🛡️

El tratamiento adecuado transforma la terminación estética y prolonga la vida útil de cualquier superficie.

🔹 Evaluación presencial sin costo para determinar el esquema diamantado correcto.

📲 Escríbanos al WhatsApp +56 9 7868 5664.

#PulidoDePisos #PisosBrillantes #SantiagoRM #Remodelacion #AmericaPulido"""
    },
    11: {
        "image": "11.png",
        "caption": """Terminaciones de Alto Brillo y Larga Durabilidad 💎✨

Nuestros procesos aseguran resistencia frente al tráfico continuo y fácil conservación diaria.

🔹 Trabajos limpios con contención de residuos en obra o vivienda.

📲 Cotización inmediata al WhatsApp +56 9 7868 5664.

#PisosDuraderos #PisosImpecables #VitrificadoProfesional #AmericaPulido"""
    },
    12: {
        "image": "12.png",
        "caption": """América Pulido SPA: Especialistas en Restauración de Pavimentos 🏆🏛️

Servicios de excelencia para clientes residenciales, comerciales e industriales en toda la Región Metropolitana.

🔹 Pulido diamantado, vitrificado, densificado y tratamiento de piedra natural.

📲 Solicite su visita técnica presencial sin costo al WhatsApp +56 9 7868 5664.

#AmericaPulido #ExpertosEnPisos #PulidoChile #RemodelacionRM #PisosDeLujo"""
    },
    13: {
        "image": "13.png",
        "caption": """Terminación Profesional para Espacios Comerciales e Institucionales 🏢✨

Soluciones eficientes para locales, recepciones y pasillos de alto flujo peatonal.

🔹 Protocolos de trabajo que garantizan limpieza y mínimo impacto operativo.

📲 Cotice con nuestro equipo al WhatsApp +56 9 7868 5664.

#LocalesComerciales #PisosComerciales #SantiagoCentro #LasCondes #AmericaPulido"""
    },
    14: {
        "image": "14.png",
        "caption": """Densificación y Pulido de Hormigón para Pavimentos Industriales 🏭⚡

Optimizamos las propiedades mecánicas de sus pavimentos de hormigón en bodegas, galpones y locales comerciales.

⚙️ Tratamiento Antipolvo: Neutralizamos el desprendimiento de partículas, facilitando la mantenibilidad y soportando alto tráfico operacional.
🏢 Emitimos factura y entregamos garantía técnica por escrito.

📲 Atención Corporativa: Contacto directo vía WhatsApp al +56 9 7868 5664.

#HormigonPulido #PisosIndustriales #BodegasChile #ConstruccionRM #GalponesSantiago #AmericaPulido"""
    },
    15: {
        "image": "15.png",
        "caption": """Restauración que Desplaza el Paso del Tiempo ➡️✨

Antes de contemplar la demolición o cambio de sus pavimentos, consulte por nuestra restauración diamantada.

🔹 Cuesta una fracción de un piso nuevo y conserva la piedra o madera original.
🎁 Visita técnica de evaluación 100% gratuita en Santiago.

📲 Envíenos fotos de su piso al WhatsApp +56 9 7868 5664.

#AntesYDespues #RestauracionPisos #RemodelacionCasa #SantiagoChile #AmericaPulido"""
    },
    16: {
        "image": "16.png",
        "caption": """Tratamiento Multisuperficie: Mármol, Hormigón y Piedra Natural 💎🏢

Soluciones a la medida según la densidad y estado de cada pavimento.

🔹 Mármol: Brillo espejo cristalino.
🔹 Hormigón: Máxima resistencia mecánica.
🔹 Piedra: Renovación profunda de la tonalidad natural.

📲 Agenda de servicio al WhatsApp +56 9 7868 5664.

#PiedraNatural #Marmol #Hormigon #PulidoProfesional #AmericaPulido"""
    },
    17: {
        "image": "17.png",
        "caption": """Refinado de Alta Reflectividad en Mármol y Terrazos 🏛️✨

Acabados cristalinos de alta gama para proyectos residenciales y corporativos.

🔹 Procesos diamantados en húmedo que garantizan ausencia de polvo en el ambiente.

📲 Presupuestos sin compromiso al WhatsApp +56 9 7868 5664.

#BrilloEspejo #MarmolDeLujo #Terrazos #SantiagoOriente #AmericaPulido"""
    },
    18: {
        "image": "18.png",
        "caption": """Acondicionamiento de Superficies para el Sector Hotelero y Comercial 🏨✨

Elevamos el estándar estético de sus recepciones, pasillos y áreas comunes con soluciones de vitrificado de alta durabilidad.

🌟 Planificación Flexible: Programación de trabajos adaptada a los flujos operativos de su establecimiento.

📲 Cotizaciones Corporativas: Solicite su presupuesto al WhatsApp +56 9 7868 5664.

#HotelesChile #HostalesSantiago #TurismoChile #AdministracionHotelera #AmericaPulido"""
    },
    19: {
        "image": "19.png",
        "caption": """Eliminación de Manchas, Opacidad y Sellado Protector 🛡️✨

Restaure la pulcritud de sus pisos afectados por agentes químicos o desgaste por uso.

🔹 Sellados de alta penetración que evitan absorción de líquidos.

📲 Consultas vía WhatsApp al +56 9 7868 5664.

#SelladoDePisos #ProteccionSuperficies #MantencionPisos #AmericaPulido"""
    },
    20: {
        "image": "20.png",
        "caption": """Recuperación de Opacidad y Brillo Perdido 🌟✨

Devolvemos la luminosidad a superficies desgastadas mediante refinado diamantado progresivo.

🔹 Proceso eficiente con contención de residuos.

📲 Visita técnica gratuita al WhatsApp +56 9 7868 5664.

#RecuperacionDePisos #PisosNuevos #SantiagoChile #AmericaPulido"""
    },
    21: {
        "image": "21.png",
        "caption": """Solución Inmediata para Pavimentos Dañados o Rayados 🛠️⚡

Intervención técnica rápida para reparar rayones profundos y pérdida de recubrimiento.

🔹 Resultados visibles en el menor tiempo posible.

📲 Contacto WhatsApp al +56 9 7868 5664.

#ReparacionPisos #PulidoUrgente #ServiciosSantiago #AmericaPulido"""
    },
    22: {
        "image": "22.png",
        "caption": """Soluciones de Pulido y Vitrificado para Departamentos 🏢✨

Maquinaria adaptada para intervenir áreas residenciales con un control riguroso de ruido y contención de residuos.

🔹 Cobertura en Las Condes, Providencia, Vitacura, Lo Barnechea, Ñuñoa y Santiago Centro.

📲 Agenda de Visita Técnica: WhatsApp directo +56 9 7868 5664.

#DepartamentosSantiago #RemodelacionDepto #PulidoPisos #Providencia #LasCondes #AmericaPulido"""
    }
}

def upload_image_to_catbox(file_path, filename):
    url = "https://catbox.moe/user/api.php"
    with open(file_path, "rb") as f:
        res = requests.post(url, data={"reqtype": "fileupload"}, files={"fileToUpload": (filename, f, "image/png")})
    if res.status_code == 200:
        return res.text.strip()
    return None

def publish_post_to_instagram(image_url, caption):
    # Step 1: Create Container
    c_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
    c_res = requests.post(c_url, data={
        "image_url": image_url,
        "caption": caption,
        "access_token": META_ACCESS_TOKEN
    })
    c_data = c_res.json()
    if "id" not in c_data:
        print(f"❌ Error en contenedor IG: {json.dumps(c_data, ensure_ascii=False)}")
        return False

    creation_id = c_data["id"]

    # Step 2: Publish Container
    p_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media_publish"
    p_res = requests.post(p_url, data={
        "creation_id": creation_id,
        "access_token": META_ACCESS_TOKEN
    })
    p_data = p_res.json()
    if "id" in p_data:
        print(f"✅ Publicado exitosamente en Instagram (Post ID: {p_data['id']})")
        return True
    else:
        print(f"❌ Error al publicar en Instagram: {json.dumps(p_data, ensure_ascii=False)}")
        return False

def main():
    print("🚀 Iniciando automatización masiva de Servicios para América Pulido SPA en Instagram...")
    print(f"📸 Total posts a procesar: {len(POSTS_SERVICIOS)}")
    
    success_count = 0
    for num in sorted(POSTS_SERVICIOS.keys()):
        info = POSTS_SERVICIOS[num]
        img_file = SERVICIOS_DIR / info["image"]
        caption = info["caption"]
        
        print(f"\n----------------------------------------")
        print(f"📌 Procesando Post N° {num}: {info['image']}")
        
        if not img_file.exists():
            print(f"⚠️ Imagen no encontrada: {img_file}")
            continue
            
        print(f"☁️ Subiendo imagen a servidor público CDN...")
        pub_url = upload_image_to_catbox(img_file, info["image"])
        if not pub_url:
            print(f"❌ Fallo al subir imagen {info['image']}")
            continue
            
        print(f"🔗 Imagen pública: {pub_url}")
        print(f"📲 Enviando a Instagram Graph API...")
        
        if publish_post_to_instagram(pub_url, caption):
            success_count += 1
            print(f"🎉 Post N° {num} completado.")
        else:
            print(f"⚠️ Fallo en Post N° {num}.")
            
        time.sleep(3)
        
    print(f"\n========================================")
    print(f"🏁 Automatización completada. {success_count}/{len(POSTS_SERVICIOS)} posts procesados exitosamente.")

if __name__ == "__main__":
    main()
