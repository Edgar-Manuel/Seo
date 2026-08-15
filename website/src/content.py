# -*- coding: utf-8 -*-
"""Datos de contenido del sitio AutoconsumoPro.

Este módulo separa el CONTENIDO (textos, artículos, categorías) del
maquetado (build.py). Para añadir uno de los ~48 artículos restantes
del plan de contenidos (docs/plan-nicho-autoconsumo-solar.md), basta con
añadir una nueva entrada al final de ARTICLES siguiendo el mismo formato
y volver a ejecutar `python3 build.py`.
"""

SITE = {
    "name": "AutoconsumoPro",
    "domain": "autoconsumopro.es",
    "base_url": "https://www.autoconsumopro.es",
    "tagline": "Autoconsumo solar y climatización renovable, explicados con números reales",
    "description": (
        "Guías técnicas independientes sobre placas solares, baterías físicas y "
        "virtuales, aerotermia y ayudas públicas en España. Sin humo, con datos."
    ),
}

CATEGORIES = [
    {
        "slug": "placas-solares",
        "eyebrow": "Silo 01",
        "planned": 15,
        "name": "Placas Solares y Autoconsumo Fotovoltaico",
        "short": "Dimensionado, inversores, orientación y legalización de una instalación fotovoltaica.",
        "description": (
            "La puerta de entrada al autoconsumo: cuántos paneles necesitas, qué inversor "
            "elegir, cómo orientar el tejado y qué trámites exige la ley para legalizar la "
            "instalación sin sorpresas."
        ),
        "accent": "amber",
    },
    {
        "slug": "baterias-solares",
        "eyebrow": "Silo 02",
        "planned": 15,
        "name": "Baterías Físicas y Virtuales",
        "short": "Litio, baterías virtuales de las comercializadoras y cuándo compensa cada opción.",
        "description": (
            "El excedente solar tiene varios destinos posibles. Comparamos el almacenamiento "
            "físico en baterías de litio con las baterías virtuales que ofrecen las eléctricas, "
            "con números de amortización reales."
        ),
        "accent": "teal",
    },
    {
        "slug": "aerotermia",
        "eyebrow": "Silo 03",
        "planned": 15,
        "name": "Aerotermia y Climatización Eficiente",
        "short": "Bombas de calor aire-agua: consumo real, rendimiento COP/SCOP y combinación con solar.",
        "description": (
            "Cómo funciona una bomba de calor de aerotermia, qué consume de verdad en invierno "
            "y cómo programarla para aprovechar cada kWh que producen tus placas solares."
        ),
        "accent": "teal",
    },
    {
        "slug": "subvenciones-tarifas",
        "eyebrow": "Silo 04",
        "planned": 15,
        "name": "Subvenciones, Tarifas y Mantenimiento",
        "short": "Deducciones fiscales, ayudas Next Generation, normativa y mantenimiento preventivo.",
        "description": (
            "La letra pequeña que decide si una instalación sale rentable: deducciones en el "
            "IRPF, bonificaciones del IBI, obligaciones de mantenimiento y el marco legal del "
            "autoconsumo en España."
        ),
        "accent": "amber",
    },
]

# Cada artículo referencia un `category` por slug y debe existir en CATEGORIES.
ARTICLES = [
    # ---------------------------------------------------------------- Placas solares
    {
        "slug": "cuantas-placas-solares-necesito-casa-100m2",
        "category": "placas-solares",
        "title": "Cuántas placas solares necesito para una casa de 100 m²: cálculo real",
        "meta_description": (
            "Cálculo paso a paso de cuántos paneles solares necesita una vivienda de 100 m² "
            "según consumo real, no según metros cuadrados. Incluye tabla orientativa por perfil de consumo."
        ),
        "keyword": "cuantas placas solares necesito casa 100m2",
        "intent": "Informativa",
        "reading_minutes": 7,
        "updated": "2026-08-01",
        "intro": [
            "La pregunta \"¿cuántas placas necesito para 100 m²\" parte de un supuesto erróneo: "
            "el tamaño de la vivienda no determina el número de paneles solares, lo hace el "
            "consumo eléctrico anual de quienes viven en ella. Una casa de 100 m² habitada por "
            "una persona teletrabajando consume de forma muy distinta a la misma casa con una "
            "familia de cuatro miembros y un coche eléctrico.",
            "Aun así, es posible dar una horquilla orientativa útil para hacer una primera "
            "criba antes de pedir presupuesto, y es exactamente lo que vamos a calcular aquí, "
            "explicando también por qué la cifra final puede variar en ±30% según tu perfil de consumo.",
        ],
        "sections": [
            {
                "h2": "El dato que de verdad importa: tu consumo anual en kWh",
                "paragraphs": [
                    "Busca en tu última factura eléctrica el consumo de los últimos 12 meses, o "
                    "consulta el histórico completo en la web de tu distribuidora (e-distribución, "
                    "i-DE, e-Redes, etc.). Un hogar medio español de 2-3 personas en una vivienda "
                    "de 100 m² sin calefacción ni ACS eléctricas consume entre 2.500 y 3.500 kWh al año. "
                    "Si tienes aerotermia, inducción y coche eléctrico, esa cifra puede subir a 6.000-9.000 kWh.",
                ],
            },
            {
                "h2": "De consumo anual a número de paneles",
                "paragraphs": [
                    "En España, un panel solar estándar de 450-500 Wp bien orientado produce entre "
                    "550 y 750 kWh al año, dependiendo de la irradiancia de tu provincia, la orientación "
                    "y las sombras. La fórmula simplificada es:",
                ],
                "table": {
                    "headers": ["Perfil de vivienda", "Consumo anual aprox.", "Paneles orientativos (450 Wp)", "Potencia instalada"],
                    "rows": [
                        ["Piso/casa pequeña, 1-2 personas", "1.800 - 2.500 kWh", "4 - 6 paneles", "1,8 - 2,7 kWp"],
                        ["Vivienda 100 m², 2-3 personas, sin electrificar", "2.500 - 3.500 kWh", "6 - 8 paneles", "2,7 - 3,6 kWp"],
                        ["Vivienda 100 m² con aerotermia", "4.500 - 6.000 kWh", "10 - 13 paneles", "4,5 - 5,9 kWp"],
                        ["Vivienda 100 m² con aerotermia + coche eléctrico", "6.500 - 9.000 kWh", "14 - 19 paneles", "6,3 - 8,6 kWp"],
                    ],
                },
                "note": "Cifras orientativas para irradiación media peninsular. En Andalucía o Canarias, el mismo consumo puede cubrirse con un 10-15% menos de paneles; en Cantabria o Asturias, puede requerir un 10-15% más.",
            },
            {
                "h2": "Por qué no conviene sobredimensionar la instalación",
                "paragraphs": [
                    "Instalar más paneles de los que tu consumo justifica no es gratis: cada panel "
                    "adicional cuesta dinero y, sin batería, el excedente que no consumes en el momento "
                    "se vierte a la red a un precio de compensación muy inferior al que pagas por comprar "
                    "electricidad. Dimensionar la instalación al 80-100% de tu consumo diurno suele dar "
                    "mejor retorno que apuntar al 100% del consumo total del año.",
                    "Si tu objetivo es maximizar el autoconsumo (por ejemplo, porque planeas incorporar "
                    "aerotermia o un coche eléctrico en los próximos 2-3 años), es razonable sobredimensionar "
                    "moderadamente pensando en esa demanda futura, ya que ampliar una instalación ya "
                    "hecha suele ser más caro que instalar unos paneles de más desde el principio. Si ese "
                    "es tu caso, conviene leer antes cómo "
                    "<a href=\"/aerotermia/aerotermia-con-placas-solares-fotovoltaicas/\">combinar aerotermia "
                    "con placas solares</a>, porque cambia bastante el dimensionado recomendado.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Puedo calcularlo solo con los m² de la vivienda?",
                "a": "No de forma fiable. Los metros cuadrados influyen indirectamente (viviendas más grandes suelen tener más ocupantes y más electrodomésticos), pero el dato que determina el número de paneles es el consumo eléctrico real en kWh/año.",
            },
            {
                "q": "¿Qué pasa si mi tejado no tiene espacio para todos los paneles que necesito?",
                "a": "Puedes priorizar paneles de mayor potencia (500-600 Wp) para aprovechar mejor la superficie disponible, o aceptar una cobertura parcial del consumo, que sigue generando ahorro proporcional.",
            },
            {
                "q": "¿Cuánto ocupa cada panel solar?",
                "a": "Un panel residencial estándar mide aproximadamente 1,9 x 1,1 m (unos 2,1 m²), aunque varía ligeramente según fabricante y potencia.",
            },
        ],
    },
    {
        "slug": "inversor-central-vs-microinversores",
        "category": "placas-solares",
        "title": "Inversor central vs microinversores: cuál elegir según tu tejado",
        "meta_description": (
            "Diferencias reales entre inversor central (string) y microinversores en una instalación "
            "solar residencial: rendimiento con sombras, coste, mantenimiento y monitorización."
        ),
        "keyword": "inversor central vs microinversores",
        "intent": "Comparativa",
        "reading_minutes": 6,
        "updated": "2026-07-18",
        "intro": [
            "La elección del inversor determina cómo se comporta tu instalación ante sombras "
            "parciales, cuánto pagarás por mantenimiento a largo plazo y qué nivel de detalle "
            "tendrás sobre la producción de cada panel. No es una decisión menor: dos tejados "
            "aparentemente similares pueden requerir soluciones distintas.",
        ],
        "sections": [
            {
                "h2": "Cómo funciona cada arquitectura",
                "paragraphs": [
                    "Un inversor central (o de tipo string) convierte la corriente continua de "
                    "toda una cadena de paneles a corriente alterna en un único punto. Todos los "
                    "paneles de esa cadena funcionan como un conjunto: si uno se sombrea, penaliza "
                    "el rendimiento de toda la cadena a la que pertenece.",
                    "Un microinversor, en cambio, se instala panel a panel: cada uno convierte su "
                    "propia energía de forma independiente. La sombra sobre un panel afecta solo a "
                    "ese panel, sin arrastrar al resto.",
                ],
            },
            {
                "h2": "Comparativa directa",
                "table": {
                    "headers": ["Criterio", "Inversor central (string)", "Microinversores"],
                    "rows": [
                        ["Coste inicial", "Más económico", "10-20% más caro por Wp instalado"],
                        ["Rendimiento con sombras parciales", "Penaliza toda la cadena", "Aísla el panel afectado"],
                        ["Monitorización", "A nivel de instalación (o de cadena con optimizadores)", "Panel a panel, muy detallada"],
                        ["Mantenimiento", "Un único punto de fallo, fácil acceso", "Cada microinversor va en el tejado, sustitución más laboriosa"],
                        ["Vida útil típica", "10-15 años (sustitución a mitad de vida de los paneles)", "20-25 años, similar a los paneles"],
                        ["Escalabilidad", "Ampliar exige revisar dimensionado del inversor", "Se añade panel + microinversor sin rediseñar el conjunto"],
                    ],
                },
            },
            {
                "h2": "Entonces, ¿cuál elegir?",
                "paragraphs": [
                    "Si tu tejado está libre de sombras (chimeneas, antenas, árboles, edificios "
                    "colindantes, otras aguas del propio tejado) a lo largo del día, un inversor "
                    "central con optimizadores de potencia en los paneles más problemáticos suele "
                    "ser la opción más económica sin sacrificar apenas rendimiento. Antes de decidir, "
                    "calcula "
                    "<a href=\"/placas-solares/cuantas-placas-solares-necesito-casa-100m2/\">cuántos "
                    "paneles necesitas realmente</a>: el número de cadenas condiciona el inversor.",
                    "Si tienes sombras parciales recurrentes, varias orientaciones de tejado en la "
                    "misma instalación, o quieres poder ampliar la instalación por fases sin "
                    "rediseñarla, los microinversores suelen compensar su sobrecoste inicial con "
                    "una producción más estable y una gestión más flexible.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Qué son los optimizadores de potencia y sustituyen a los microinversores?",
                "a": "Los optimizadores (como los de Tigo o SolarEdge) se instalan panel a panel igual que los microinversores, pero solo acondicionan la corriente continua; la conversión a corriente alterna sigue haciéndose en un inversor central. Son un punto intermedio: mitigan el problema de sombras a menor coste que los microinversores completos.",
            },
            {
                "q": "¿Puedo mezclar orientaciones (por ejemplo, este y oeste) con un inversor central?",
                "a": "Sí, siempre que el inversor tenga varios trackers MPPT independientes (normalmente 2), uno por cada orientación. Si solo tiene un tracker, necesitarás optimizadores o microinversores para no penalizar el conjunto.",
            },
        ],
    },
    {
        "slug": "legalizacion-instalacion-solar-pasos",
        "category": "placas-solares",
        "title": "Legalización de autoconsumo fotovoltaico en España: paso a paso en 2026",
        "meta_description": (
            "Guía completa de los trámites para legalizar una instalación de autoconsumo "
            "fotovoltaico en España: memoria técnica, boletín eléctrico, CAU y alta con la distribuidora."
        ),
        "keyword": "legalizacion instalacion solar pasos",
        "intent": "Guía / Informativa",
        "reading_minutes": 8,
        "updated": "2026-06-30",
        "intro": [
            "Una instalación fotovoltaica no está terminada cuando se atornilla el último panel: "
            "para poder verter excedentes a la red, acogerte a la compensación de excedentes y "
            "evitar sanciones, la instalación debe legalizarse ante la administración y la "
            "distribuidora eléctrica. El proceso varía ligeramente por comunidad autónoma, pero "
            "el esqueleto es el mismo en toda España.",
        ],
        "sections": [
            {
                "h2": "Paso 1: Proyecto o memoria técnica de diseño",
                "paragraphs": [
                    "Para instalaciones residenciales de baja potencia (la inmensa mayoría de "
                    "viviendas unifamiliares, normalmente por debajo de 15-25 kW según comunidad), "
                    "basta con una memoria técnica de diseño (MTD) firmada por un instalador "
                    "autorizado. Instalaciones de mayor potencia requieren proyecto firmado por "
                    "un técnico competente (ingeniero).",
                ],
            },
            {
                "h2": "Paso 2: Boletín eléctrico (certificado de instalación)",
                "paragraphs": [
                    "El instalador emite el Certificado de Instalación Eléctrica (CIE), conocido "
                    "coloquialmente como boletín. Este documento certifica que la instalación "
                    "cumple el Reglamento Electrotécnico de Baja Tensión (REBT) y es imprescindible "
                    "para el resto de trámites.",
                ],
            },
            {
                "h2": "Paso 3: Registro en la comunidad autónoma",
                "paragraphs": [
                    "La instalación debe inscribirse en el registro de autoconsumo de la comunidad "
                    "autónoma correspondiente. En instalaciones sin excedentes o con excedentes "
                    "acogidas a compensación, el trámite suele ser una simple declaración "
                    "responsable; con excedentes sin compensación puede requerir autorización previa.",
                ],
            },
            {
                "h2": "Paso 4: Alta del CAU con la distribuidora",
                "paragraphs": [
                    "La distribuidora (no la comercializadora que te factura la luz) asigna el "
                    "Código de Autoconsumo (CAU), necesario para que el contador registre "
                    "correctamente la energía exportada e importada. Sin CAU, no puedes "
                    "acogerte a la compensación de excedentes aunque tu instalación esté "
                    "físicamente terminada, ni contratar una "
                    "<a href=\"/baterias-solares/mejor-bateria-virtual-sin-cuotas/\">batería "
                    "virtual</a> con tu comercializadora.",
                ],
            },
            {
                "h2": "Paso 5: Contrato de autoconsumo con tu comercializadora",
                "paragraphs": [
                    "Con el CAU asignado, tu comercializadora actualiza el contrato de suministro "
                    "para reflejar la modalidad de autoconsumo elegida (con o sin excedentes, "
                    "individual o colectivo) y activar la compensación de excedentes si corresponde.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Cuánto tarda todo el proceso de legalización?",
                "a": "Entre 1 y 3 meses de media desde que finaliza la instalación física, dependiendo de la comunidad autónoma y de la carga de trabajo de la distribuidora. Algunos territorios lo resuelven en semanas; otros pueden superar los 3 meses en épocas de alta demanda.",
            },
            {
                "q": "¿Puedo empezar a autoconsumir antes de tener el CAU?",
                "a": "Puedes consumir la energía que generas en el momento (autoconsumo instantáneo) desde que la instalación está operativa, pero no podrás compensar los excedentes vertidos a la red hasta tener el CAU activo, por lo que esos excedentes se pierden sin compensación durante ese periodo.",
            },
        ],
    },
    # ---------------------------------------------------------------- Baterías
    {
        "slug": "bateria-fisica-vs-bateria-virtual",
        "category": "baterias-solares",
        "title": "Batería física vs batería virtual: comparativa económica y amortización",
        "meta_description": (
            "Comparativa económica entre instalar una batería física de litio y contratar una "
            "batería virtual con tu comercializadora: coste, comisiones y años de amortización."
        ),
        "keyword": "bateria fisica vs bateria virtual",
        "intent": "Comparativa",
        "reading_minutes": 8,
        "updated": "2026-07-05",
        "intro": [
            "Ambas soluciones persiguen el mismo objetivo, aprovechar el excedente solar que no "
            "consumes en el momento, pero funcionan de forma radicalmente distinta y el reparto "
            "de riesgos y costes entre ambas es muy diferente. Antes de decidir, conviene entender "
            "qué compras exactamente en cada caso.",
        ],
        "sections": [
            {
                "h2": "Qué es cada cosa",
                "paragraphs": [
                    "Una batería física almacena electricidad real en celdas de litio instaladas en "
                    "tu vivienda. Es tuya, no depende de ningún contrato con una comercializadora y "
                    "funciona incluso sin conexión a la red (con la función backup adecuada).",
                    "Una batería virtual es un servicio contable: la comercializadora convierte tus "
                    "excedentes vertidos a la red en un 'saldo' expresado en euros o kWh, que puedes "
                    "descontar de facturas futuras. No hay ningún equipo físico adicional en tu casa; "
                    "es, en esencia, un monedero energético gestionado por un tercero.",
                ],
            },
            {
                "h2": "Comparativa de coste y compromiso",
                "table": {
                    "headers": ["Criterio", "Batería física (litio)", "Batería virtual"],
                    "rows": [
                        ["Inversión inicial", "3.000 € - 7.000 € (según capacidad)", "0 € (algunas exigen cuota mensual)"],
                        ["Propiedad del activo", "Tuya, revaloriza la vivienda", "Ninguna, es un servicio contratado"],
                        ["Pérdidas por conversión/comisión", "5-10% (eficiencia de carga/descarga)", "Peajes y comisiones variables, suelen rondar el 10-30% del valor del kWh"],
                        ["Funciona sin red eléctrica (apagones)", "Sí, con función backup", "No, depende de la red"],
                        ["Caducidad del saldo acumulado", "No aplica", "Frecuente: muchas ofertas caducan el saldo no consumido a los 12 meses"],
                        ["Portabilidad si cambias de comercializadora", "Total, es tu equipo", "El saldo suele perderse o no ser transferible"],
                    ],
                },
            },
            {
                "h2": "Cuándo compensa cada una",
                "paragraphs": [
                    "La batería virtual tiene sentido como solución de entrada: sin inversión inicial, "
                    "reduce factura desde el primer mes y es reversible si cambias de opinión. Es "
                    "razonable para quien no tiene claro si va a quedarse mucho tiempo en la vivienda "
                    "o prefiere no inmovilizar capital.",
                    "La batería física compensa cuando ya tienes cubierta la inversión en paneles, "
                    "valoras la independencia energética ante cortes de suministro, y tu patrón de "
                    "consumo nocturno es alto (por ejemplo, con coche eléctrico que cargas de noche, "
                    "o con una <a href=\"/aerotermia/consumo-aerotermia-mensual-invierno/\">bomba de "
                    "calor de aerotermia funcionando en invierno</a>). "
                    "El plazo de amortización habitual, sin ayudas, se sitúa entre 8 y 14 años; con "
                    "subvención, puede bajar a 5-8 años.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Puedo tener batería física y virtual a la vez?",
                "a": "No de forma simultánea sobre el mismo excedente: una vez que tu excedente carga la batería física, ya no llega a la red para generar saldo virtual. Sí es posible cambiar de una a otra con el tiempo.",
            },
            {
                "q": "¿La batería virtual me protege de un apagón?",
                "a": "No. Al ser un servicio contable sin equipo físico en tu vivienda, si se corta el suministro eléctrico, te quedas sin luz igual que sin autoconsumo, independientemente del saldo virtual acumulado.",
            },
        ],
    },
    {
        "slug": "huawei-luna2000-precio-instalacion",
        "category": "baterias-solares",
        "title": "Huawei Luna2000 precio e instalación: ¿cuántos kWh necesita tu hogar?",
        "meta_description": (
            "Precio orientativo de la batería Huawei Luna2000, módulos disponibles, compatibilidad "
            "con inversores y cómo dimensionar la capacidad según tu consumo nocturno."
        ),
        "keyword": "huawei luna2000 precio instalacion",
        "intent": "Transaccional",
        "reading_minutes": 6,
        "updated": "2026-07-22",
        "intro": [
            "La Luna2000 es una de las baterías domésticas más instaladas en España, principalmente "
            "por su integración directa con los inversores híbridos de la propia Huawei (series SUN2000). "
            "Antes de pedir presupuesto, conviene entender cómo se dimensiona y qué determina su precio final.",
        ],
        "sections": [
            {
                "h2": "Cómo se compone la capacidad de la Luna2000",
                "paragraphs": [
                    "La Luna2000 funciona con módulos de batería apilables de 5 kWh cada uno, más una "
                    "unidad de control (Smart String ESS o BCU según la generación). Esto permite "
                    "ajustar la capacidad total a la medida del hogar, en múltiplos de 5 kWh, en "
                    "lugar de tener que elegir entre unos pocos tamaños fijos.",
                ],
            },
            {
                "h2": "Precio orientativo por capacidad",
                "table": {
                    "headers": ["Capacidad", "Módulos", "Precio orientativo instalado*"],
                    "rows": [
                        ["5 kWh", "1 módulo", "3.200 € - 4.200 €"],
                        ["10 kWh", "2 módulos", "5.500 € - 7.000 €"],
                        ["15 kWh", "3 módulos", "7.800 € - 9.800 €"],
                    ],
                },
                "note": "*Precio orientativo de mercado en España incluyendo instalación, sin contar el inversor híbrido (necesario para la compatibilidad) ni posibles ayudas o subvenciones aplicables. Pide siempre 2-3 presupuestos: el rango real varía según instalador, provincia y complejidad de la instalación eléctrica existente.",
            },
            {
                "h2": "Cómo saber cuántos kWh necesitas",
                "paragraphs": [
                    "El criterio más práctico es calcular tu consumo entre el atardecer y el amanecer, "
                    "cuando los paneles no producen. Si tu factura muestra un consumo nocturno medio "
                    "de 4-6 kWh, una batería de 5 kWh puede cubrir la mayoría de noches; con consumo "
                    "nocturno más alto (aerotermia funcionando de noche, carga de coche eléctrico), "
                    "10-15 kWh es un rango más realista.",
                    "Sobredimensionar la batería respecto a tu excedente solar diario disponible no "
                    "aporta ahorro adicional: si tus paneles no generan suficiente excedente para "
                    "llenarla, la capacidad extra queda infrautilizada gran parte del año.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿La Luna2000 funciona con inversores de otras marcas?",
                "a": "No de forma nativa: está diseñada para integrarse con los inversores híbridos Huawei SUN2000. Si ya tienes un inversor de otra marca, normalmente necesitarás sustituirlo o buscar una batería compatible con tu equipo actual.",
            },
            {
                "q": "¿Incluye función de respaldo ante apagones (backup)?",
                "a": "Sí, siempre que la instalación incorpore el módulo de conmutación de emergencia (Backup Box) correspondiente, que suele contratarse como elemento adicional al pack estándar.",
            },
        ],
    },
    {
        "slug": "mejor-bateria-virtual-sin-cuotas",
        "category": "baterias-solares",
        "title": "Comparativa de las 5 mejores baterías virtuales sin cuota mensual en España",
        "meta_description": (
            "Comparamos las principales baterías virtuales sin cuota fija en España: caducidad del "
            "saldo, comisiones aplicadas y portabilidad al cambiar de comercializadora."
        ),
        "keyword": "mejor bateria virtual sin cuotas",
        "intent": "Comparativa",
        "reading_minutes": 7,
        "updated": "2026-08-05",
        "intro": [
            "No todas las baterías virtuales del mercado cobran una cuota fija mensual: varias "
            "comercializadoras han lanzado versiones \"sin permanencia y sin cuota\" para captar "
            "clientes de autoconsumo. La letra pequeña, sin embargo, varía mucho de una oferta a "
            "otra en aspectos que sí importan al bolsillo: comisión aplicada al convertir el "
            "excedente en saldo, y plazo de caducidad de ese saldo.",
        ],
        "sections": [
            {
                "h2": "Qué mirar más allá del \"sin cuota\"",
                "paragraphs": [
                    "El reclamo comercial de \"sin cuota mensual\" no dice nada sobre dos variables "
                    "que determinan el ahorro real: qué comisión o peaje se aplica al convertir cada "
                    "kWh de excedente en saldo (habitualmente entre el 10% y el 30% de su valor), y "
                    "si el saldo acumulado caduca a los 12 meses, no caduca, o se limita a un tope máximo.",
                ],
            },
            {
                "h2": "Criterios de comparación",
                "table": {
                    "headers": ["Aspecto a revisar", "Por qué importa"],
                    "rows": [
                        ["Comisión sobre el excedente convertido", "Determina cuánto vale realmente cada kWh que viertes a la red"],
                        ["Caducidad del saldo", "Un saldo que caduca en 12 meses penaliza a quien produce mucho en verano y consume ese ahorro en invierno"],
                        ["Tope máximo de saldo acumulable", "Algunas ofertas limitan cuánto puedes acumular, perdiendo el resto"],
                        ["Portabilidad al cambiar de compañía", "La inmensa mayoría de saldos no son transferibles a otra comercializadora"],
                        ["Requisito de coeficiente de reparto o instalación mínima", "Algunas exigen una potencia instalada mínima para poder contratarlo"],
                    ],
                },
            },
            {
                "h2": "Cómo comparar ofertas reales antes de firmar",
                "paragraphs": [
                    "Pide siempre por escrito (no solo en la web comercial) la comisión exacta "
                    "aplicada y la política de caducidad del saldo, ya que ambas condiciones cambian "
                    "con frecuencia y las campañas promocionales no siempre reflejan las condiciones "
                    "contractuales reales. Compara también contra la opción de no contratar batería "
                    "virtual y quedarte simplemente con la compensación de excedentes estándar del "
                    "mercado libre, que en muchos casos, para excedentes moderados, resulta más simple "
                    "y con menos condiciones ocultas. Y si te planteas dar el salto al almacenamiento "
                    "real, revisa antes la <a href=\"/baterias-solares/bateria-fisica-vs-bateria-virtual/\">"
                    "comparativa económica entre batería física y virtual</a>.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Es obligatorio tener batería física para contratar una batería virtual?",
                "a": "No, son alternativas independientes. La batería virtual solo requiere tener una instalación de autoconsumo con excedentes dados de alta con CAU.",
            },
            {
                "q": "¿Puedo cancelar una batería virtual en cualquier momento?",
                "a": "Depende de la oferta contratada. Las que se anuncian \"sin permanencia\" permiten la baja sin penalización, pero conviene confirmar qué ocurre con el saldo acumulado en el momento de la baja, ya que habitualmente se pierde.",
            },
        ],
    },
    # ---------------------------------------------------------------- Aerotermia
    {
        "slug": "consumo-aerotermia-mensual-invierno",
        "category": "aerotermia",
        "title": "Consumo real de la aerotermia al mes en invierno: euros y kWh desglosados",
        "meta_description": (
            "Cuánto consume realmente una bomba de calor de aerotermia en un mes de invierno: "
            "ejemplo desglosado en kWh y euros según superficie y aislamiento de la vivienda."
        ),
        "keyword": "consumo aerotermia mensual invierno",
        "intent": "Comercial / Informativa",
        "reading_minutes": 7,
        "updated": "2026-07-10",
        "intro": [
            "El consumo de una bomba de calor de aerotermia en invierno depende de tres variables "
            "que pesan mucho más que la marca del equipo: la superficie a climatizar, el nivel de "
            "aislamiento de la vivienda y la temperatura exterior media de la zona. Dos viviendas "
            "de 120 m² pueden tener consumos que difieren en más del doble solo por el aislamiento.",
        ],
        "sections": [
            {
                "h2": "Ejemplo desglosado para una vivienda de 120 m²",
                "table": {
                    "headers": ["Nivel de aislamiento", "Consumo mensual orientativo (enero)", "Coste orientativo (0,15 €/kWh)"],
                    "rows": [
                        ["Vivienda bien aislada (construcción reciente o rehabilitada)", "250 - 400 kWh", "38 € - 60 €"],
                        ["Aislamiento medio (construcción años 90-2000)", "400 - 650 kWh", "60 € - 98 €"],
                        ["Aislamiento deficiente (vivienda antigua sin reforma)", "650 - 1.000+ kWh", "98 € - 150 €+"],
                    ],
                },
                "note": "Estimaciones para climas peninsulares de invierno moderado-frío con un COP medio estacional de 3-4. En zonas muy frías (interior de Castilla, Pirineo) el consumo puede superar estos rangos; en climas suaves de costa mediterránea o sur peninsular, puede ser inferior.",
            },
            {
                "h2": "Por qué el precio del kWh contratado importa tanto como el consumo",
                "paragraphs": [
                    "Como la aerotermia funciona con electricidad, el coste final depende directamente "
                    "de tu tarifa. Con discriminación horaria y programación de la bomba de calor para "
                    "trabajar en horas valle (de madrugada), es posible reducir el coste mensual entre "
                    "un 15% y un 30% frente a un consumo sin optimizar el horario, sin cambiar el consumo en kWh.",
                    "Si además dispones de placas solares, cada kWh que la bomba de calor consume "
                    "durante las horas de sol tiene coste marginal cero (o casi), lo que cambia por "
                    "completo la ecuación económica frente a depender solo de la red. Explicamos cómo "
                    "conseguirlo en la guía de "
                    "<a href=\"/aerotermia/aerotermia-con-placas-solares-fotovoltaicas/\">programación "
                    "de los impulsos de calor con excedente solar</a>.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿La aerotermia consume más que una caldera de gas en invierno?",
                "a": "En kWh de energía final, la aerotermia consume bastante menos porque produce 3-4 kWh de calor por cada kWh eléctrico consumido (su COP), mientras que una caldera de gas produce como máximo 1 kWh de calor por kWh de gas. El coste final en euros depende del precio comparado de la luz y el gas en cada caso.",
            },
            {
                "q": "¿Se puede reducir el consumo sin pasar frío?",
                "a": "Sí: mantener una temperatura de impulsión adecuada (ni excesivamente alta), programar temperaturas de confort más bajas por la noche, y sellar bien puertas y ventanas tienen más impacto en el consumo que ajustar el termostato uno o dos grados.",
            },
        ],
    },
    {
        "slug": "rendimiento-cop-scop-aerotermia",
        "category": "aerotermia",
        "title": "Rendimiento COP y SCOP en aerotermia: qué significan estos números",
        "meta_description": (
            "Explicación clara de qué son el COP y el SCOP en una bomba de calor de aerotermia, "
            "por qué el SCOP es el dato relevante para comparar equipos y qué valores son buenos."
        ),
        "keyword": "rendimiento cop scop aerotermia",
        "intent": "Técnica",
        "reading_minutes": 6,
        "updated": "2026-06-15",
        "intro": [
            "Las fichas técnicas de las bombas de calor están llenas de siglas —COP, SCOP, EER, "
            "SEER— que los folletos comerciales rara vez explican con claridad. Entender la "
            "diferencia entre COP y SCOP es lo único que necesitas para comparar equipos de forma "
            "justa, en lugar de fijarte solo en la cifra más alta del catálogo.",
        ],
        "sections": [
            {
                "h2": "COP: el rendimiento en un instante concreto",
                "paragraphs": [
                    "El COP (Coefficient of Performance) mide cuántos kWh de calor entrega el equipo "
                    "por cada kWh eléctrico que consume, en unas condiciones de laboratorio fijas "
                    "(normalmente 7°C de temperatura exterior y 35°C de temperatura de impulsión). "
                    "Un COP de 4 significa que, en esas condiciones concretas, obtienes 4 kWh de calor "
                    "por cada kWh eléctrico consumido.",
                ],
            },
            {
                "h2": "SCOP: el rendimiento medio a lo largo de toda una temporada",
                "paragraphs": [
                    "El problema del COP es que solo describe un punto de funcionamiento, y el "
                    "rendimiento real de una bomba de calor varía mucho según la temperatura exterior: "
                    "rinde peor en un día de -2°C que en uno de 10°C. El SCOP (Seasonal COP) promedia "
                    "el rendimiento a lo largo de toda una temporada de calefacción para una zona "
                    "climática de referencia, y por eso es el dato que hay que comparar entre marcas, "
                    "no el COP puntual del folleto.",
                ],
            },
            {
                "h2": "Qué valores de SCOP son buenos en 2026",
                "table": {
                    "headers": ["SCOP", "Valoración"],
                    "rows": [
                        ["Por debajo de 3,0", "Rendimiento bajo para los estándares actuales"],
                        ["3,0 - 4,0", "Rango correcto, habitual en equipos de gama media"],
                        ["4,0 - 5,0", "Buen rendimiento, equipos de gama alta bien dimensionados"],
                        ["Superior a 5,0", "Excelente, típico de instalaciones con suelo radiante (temperaturas de impulsión bajas)"],
                    ],
                },
                "note": "El SCOP real también depende de la temperatura de impulsión de tu sistema de emisión: cuanto más baja (suelo radiante frente a radiadores de alta temperatura), mejor rendimiento estacional obtendrás con el mismo equipo. Ese rendimiento es el que determina, en última instancia, <a href=\"/aerotermia/consumo-aerotermia-mensual-invierno/\">cuánto pagarás cada mes en invierno</a>.",
            },
        ],
        "faq": [
            {
                "q": "¿El SCOP es el mismo en toda España?",
                "a": "No. El SCOP se certifica para zonas climáticas de referencia (fría, media, cálida). Un mismo equipo publicará SCOP distintos según la zona; compara siempre el dato correspondiente a tu zona climática, no el más favorable del catálogo.",
            },
            {
                "q": "¿Existe un equivalente al SCOP para el modo refrigeración?",
                "a": "Sí, se llama SEER (Seasonal Energy Efficiency Ratio) y funciona con la misma lógica que el SCOP, pero aplicado al rendimiento estacional en modo frío.",
            },
        ],
    },
    {
        "slug": "aerotermia-con-placas-solares-fotovoltaicas",
        "category": "aerotermia",
        "title": "Combinar aerotermia con placas solares: cómo programar los impulsos de calor",
        "meta_description": (
            "Cómo programar una bomba de calor de aerotermia para consumir el excedente solar "
            "del mediodía y maximizar el ahorro conjunto con una instalación fotovoltaica."
        ),
        "keyword": "aerotermia con placas solares fotovoltaicas",
        "intent": "Guía / Técnica",
        "reading_minutes": 7,
        "updated": "2026-08-10",
        "intro": [
            "La aerotermia es, con diferencia, el electrodoméstico que mejor combina con el "
            "autoconsumo fotovoltaico: es un consumo eléctrico grande, predecible y desplazable "
            "en el tiempo, exactamente el tipo de carga que conviene concentrar en las horas de "
            "sol para no depender de baterías caras.",
        ],
        "sections": [
            {
                "h2": "El desajuste natural entre producción solar y demanda de calor",
                "paragraphs": [
                    "Sin optimizar, hay un desajuste evidente: las placas producen al máximo entre "
                    "las 11h y las 16h, mientras que la mayor demanda de calefacción suele darse por "
                    "la mañana temprano y al anochecer, cuando ya no hay sol. La clave para "
                    "aprovechar el excedente solar en la bomba de calor no es cambiar cuándo la "
                    "necesitas, sino cambiar cuándo produce el calor que vas a consumir después.",
                ],
            },
            {
                "h2": "Estrategia: usar la inercia térmica como \"batería de calor\"",
                "paragraphs": [
                    "La mayoría de bombas de calor modernas permiten programar horarios de "
                    "funcionamiento (o se integran con gestores de energía / SmartGrid Ready). La "
                    "estrategia habitual consiste en subir ligeramente la temperatura de consigna "
                    "durante las horas centrales del día, cuando hay excedente solar, aprovechando "
                    "la inercia térmica de la vivienda (y del depósito de inercia o el suelo radiante, "
                    "si existen) para mantener el confort durante la tarde-noche sin que el "
                    "compresor tenga que trabajar tanto con electricidad de red.",
                    "Para el ACS (agua caliente sanitaria), la estrategia es más sencilla todavía: "
                    "programar el calentamiento del depósito de acumulación en las horas de mayor "
                    "producción solar, en lugar de dejarlo en modo automático sin restricciones "
                    "horarias.",
                ],
            },
            {
                "h2": "¿Merece la pena un gestor de excedentes dedicado?",
                "paragraphs": [
                    "Existen dispositivos y funciones de inversor (por ejemplo, salidas de relé "
                    "programables por excedente) que activan automáticamente cargas como la "
                    "aerotermia solo cuando hay excedente solar disponible, sin necesidad de "
                    "programar horarios fijos manualmente. Para instalaciones con un patrón de sol "
                    "muy variable (nubosidad frecuente), este tipo de gestión dinámica aprovecha "
                    "mejor el excedente real que una programación horaria fija.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Necesito batería física para aprovechar el excedente solar con la aerotermia?",
                "a": "No es imprescindible. Al desplazar el consumo de la bomba de calor a las horas de sol, usas la propia inercia térmica de la vivienda como forma de \"almacenar\" ese excedente en forma de calor, sin necesidad de una batería eléctrica.",
            },
            {
                "q": "¿Reduce esto la vida útil de la bomba de calor por encender y apagar más veces?",
                "a": "Si se programa correctamente (consignas de temperatura, no encendidos/apagados bruscos y frecuentes), el impacto es mínimo. La mayoría de equipos modulantes actuales están diseñados para adaptar su potencia de forma progresiva, no solo para encender y apagar.",
            },
        ],
    },
    # ---------------------------------------------------------------- Subvenciones y tarifas
    {
        "slug": "deduccion-irpf-placas-solares-aerotermia",
        "category": "subvenciones-tarifas",
        "title": "Deducción IRPF por placas solares y aerotermia: cómo aplicarla en la Renta",
        "meta_description": (
            "Cómo funciona la deducción del IRPF por obras de mejora de la eficiencia energética "
            "al instalar placas solares o aerotermia: requisitos, porcentajes y certificado necesario."
        ),
        "keyword": "deduccion irpf placas solares aerotermia",
        "intent": "Guía / Legal",
        "reading_minutes": 7,
        "updated": "2026-05-20",
        "intro": [
            "Además de las ayudas y subvenciones directas, España cuenta con deducciones fiscales "
            "en el IRPF para obras de mejora de la eficiencia energética de la vivienda habitual, "
            "aplicables durante varios ejercicios fiscales. Instalar placas solares o sustituir un "
            "sistema de calefacción por aerotermia puede acogerse a estas deducciones si se cumplen "
            "determinados requisitos de reducción del consumo o la demanda energética.",
        ],
        "sections": [
            {
                "h2": "Qué acredita el derecho a deducción",
                "paragraphs": [
                    "La deducción no se aplica automáticamente por instalar placas solares o "
                    "aerotermia: es necesario acreditar una mejora de la eficiencia energética "
                    "mediante el certificado de eficiencia energética de la vivienda, comparando "
                    "el indicador antes y después de la obra. El ahorro exigido varía según el "
                    "tramo de deducción al que se quiera acoger la actuación.",
                ],
            },
            {
                "h2": "Documentación imprescindible que hay que conservar",
                "paragraphs": [
                    "Guarda desde el primer momento: el certificado de eficiencia energética "
                    "anterior a la obra, el certificado posterior, las facturas de la instalación "
                    "con el desglose de materiales y mano de obra, y el justificante de pago por "
                    "medios que dejen constancia (transferencia, tarjeta), ya que el pago en "
                    "efectivo no suele admitirse para esta deducción.",
                ],
            },
            {
                "h2": "Compatibilidad con otras ayudas",
                "paragraphs": [
                    "La deducción del IRPF es, en general, compatible con las subvenciones "
                    "autonómicas o los fondos Next Generation (y se aplica tanto si la obra ha sido "
                    "una instalación fotovoltaica como la sustitución de una caldera por "
                    "<a href=\"/aerotermia/rendimiento-cop-scop-aerotermia/\">una bomba de calor de "
                    "aerotermia</a>), pero la base de la deducción se "
                    "calcula sobre el importe efectivamente pagado por el contribuyente, es decir, "
                    "descontando la parte ya cubierta por la subvención recibida. Conviene revisar "
                    "la normativa vigente en el ejercicio fiscal concreto, ya que los porcentajes y "
                    "plazos de esta deducción se han prorrogado y ajustado en distintos Presupuestos "
                    "Generales del Estado.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Se puede aplicar la deducción sobre una segunda residencia?",
                "a": "Depende del tramo de deducción: algunos tramos se limitan a la vivienda habitual, mientras que otros (orientados a reducción del consumo de energía primaria no renovable) admiten también viviendas arrendadas o en expectativa de alquiler. Revisa el detalle normativo vigente antes de presentar la declaración.",
            },
            {
                "q": "¿Es obligatorio contratar un técnico certificador independiente del instalador?",
                "a": "El certificado de eficiencia energética debe estar firmado por un técnico competente habilitado para ello; puede o no coincidir con la empresa instaladora, pero debe tratarse de un profesional con la habilitación específica para emitir certificados energéticos.",
            },
        ],
    },
    {
        "slug": "mantenimiento-aerotermia-precio-anual",
        "category": "subvenciones-tarifas",
        "title": "Mantenimiento de aerotermia: qué revisiones exige la ley y cuál es su coste",
        "meta_description": (
            "Qué mantenimiento es obligatorio por normativa en una bomba de calor de aerotermia, "
            "con qué periodicidad y cuánto cuesta un contrato de mantenimiento anual en España."
        ),
        "keyword": "mantenimiento aerotermia precio anual",
        "intent": "Legal / Comercial",
        "reading_minutes": 6,
        "updated": "2026-06-02",
        "intro": [
            "El Reglamento de Instalaciones Térmicas en los Edificios (RITE) establece obligaciones "
            "de mantenimiento para equipos de climatización según su potencia. Para la mayoría de "
            "bombas de calor residenciales, las exigencias legales estrictas son limitadas, pero "
            "eso no significa que puedas saltarte el mantenimiento sin consecuencias: afecta "
            "directamente a la eficiencia, la garantía del fabricante y la vida útil del equipo.",
        ],
        "sections": [
            {
                "h2": "Qué exige realmente la normativa",
                "paragraphs": [
                    "Para equipos residenciales de potencia térmica nominal reducida (el rango "
                    "habitual en vivienda unifamiliar), el RITE no exige un contrato de mantenimiento "
                    "periódico obligatorio con empresa habilitada, a diferencia de equipos de mayor "
                    "potencia en el sector terciario. Sí existen obligaciones específicas relacionadas "
                    "con el control de fugas de gases fluorados según la carga de refrigerante del "
                    "equipo, reguladas por normativa medioambiental independiente del RITE.",
                ],
            },
            {
                "h2": "Qué revisiones conviene hacer aunque no sean obligatorias",
                "table": {
                    "headers": ["Revisión", "Periodicidad recomendada"],
                    "rows": [
                        ["Limpieza de filtros de la unidad interior", "Cada 1-3 meses (uso propio)"],
                        ["Limpieza del intercambiador de la unidad exterior", "Anual"],
                        ["Comprobación de presión y estanqueidad del circuito de refrigerante", "Anual (técnico habilitado)"],
                        ["Revisión de conexiones eléctricas y consumo anómalo", "Anual"],
                        ["Purga del circuito hidráulico y comprobación de la presión del vaso de expansión", "Anual"],
                    ],
                },
            },
            {
                "h2": "Precio orientativo de un contrato de mantenimiento",
                "paragraphs": [
                    "Un contrato de mantenimiento anual con visita de técnico para una bomba de "
                    "calor residencial suele costar entre 90 € y 180 € al año (un coste que conviene "
                    "incluir al calcular <a href=\"/aerotermia/consumo-aerotermia-mensual-invierno/\">el "
                    "gasto real de la aerotermia</a>), según la complejidad "
                    "del sistema (con o sin ACS, con o sin suelo radiante) y la zona geográfica. "
                    "Mantener el equipo revisado no es solo una cuestión de garantía: un equipo con "
                    "el filtro sucio o la unidad exterior obstruida puede perder varios puntos de "
                    "rendimiento (SCOP efectivo) sin que sea evidente a simple vista.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Perder la garantía del fabricante si no contrato mantenimiento anual?",
                "a": "Depende del fabricante: algunas marcas condicionan la garantía ampliada (más allá de los 2-3 años legales) a la contratación de revisiones periódicas certificadas. Revisa las condiciones de garantía específicas de tu equipo antes de decidir prescindir del mantenimiento.",
            },
            {
                "q": "¿Puedo hacer yo mismo alguna de estas revisiones?",
                "a": "La limpieza de filtros de la unidad interior es una tarea de usuario habitual y sencilla. Las revisiones que implican manipular el circuito de refrigerante (gas fluorado) requieren obligatoriamente un técnico con la habilitación correspondiente, por normativa medioambiental.",
            },
        ],
    },
    {
        "slug": "regulacion-legal-autoconsumo-espana",
        "category": "subvenciones-tarifas",
        "title": "Peaje de respaldo e historia del impuesto al sol: situación jurídica actual",
        "meta_description": (
            "Qué fue el llamado impuesto al sol, por qué se eliminó, y qué cargos residuales "
            "(como el peaje de respaldo) pueden aplicarse todavía al autoconsumo en España."
        ),
        "keyword": "regulacion legal autoconsumo españa",
        "intent": "Legal",
        "reading_minutes": 6,
        "updated": "2026-05-05",
        "intro": [
            "Pocos términos generan tanta confusión en foros y redes como el \"impuesto al sol\". "
            "Es una etiqueta informal, no un tributo con ese nombre oficial, y entender su origen "
            "ayuda a valorar con perspectiva los cargos que sí pueden aplicarse hoy a determinadas "
            "instalaciones de autoconsumo.",
        ],
        "sections": [
            {
                "h2": "Qué fue realmente el \"impuesto al sol\"",
                "paragraphs": [
                    "El término popularizó el Real Decreto 900/2015, que introdujo un cargo por "
                    "autoconsumo (el llamado \"peaje de respaldo\") aplicable a determinadas "
                    "instalaciones conectadas a la red, especialmente las que superaban ciertos "
                    "umbrales de potencia. La medida generó una fuerte controversia social y "
                    "frenó de forma notable el desarrollo del autoconsumo residencial en España "
                    "durante varios años.",
                ],
            },
            {
                "h2": "La derogación con el Real Decreto-ley 15/2018",
                "paragraphs": [
                    "El marco cambió de forma sustancial con el Real Decreto-ley 15/2018 y, "
                    "posteriormente, el Real Decreto 244/2019, que eliminaron el cargo generalizado "
                    "al autoconsumo residencial y establecieron el marco actual: compensación de "
                    "excedentes simplificada, autoconsumo colectivo, y exención de cargos y peajes "
                    "para la energía autoconsumida instantáneamente en instalaciones de potencia "
                    "reducida (el caso habitual en vivienda unifamiliar).",
                ],
            },
            {
                "h2": "¿Sigue existiendo algún cargo residual hoy?",
                "paragraphs": [
                    "Para la inmensa mayoría de instalaciones residenciales de baja potencia, la "
                    "energía autoconsumida en el momento está exenta de cargos y peajes por el "
                    "término de energía. Los peajes de acceso a la red se siguen pagando por la "
                    "energía que efectivamente se importa de la red, como en cualquier suministro "
                    "eléctrico, y por la potencia contratada (término de potencia), pero no existe "
                    "hoy un cargo específico por autoconsumir tu propia energía solar en una "
                    "vivienda unifamiliar tipo.",
                    "Este es, precisamente, el marco que hace posible la "
                    "<a href=\"/baterias-solares/bateria-fisica-vs-bateria-virtual/\">compensación de "
                    "excedentes y las baterías virtuales</a> tal y como se comercializan hoy. "
                    "Es importante distinguir esta situación actual del debate periódico sobre "
                    "posibles nuevos cargos de \"respaldo\" al sistema eléctrico que en ocasiones "
                    "resurge en el debate regulatorio europeo; a la fecha de esta guía, no existe "
                    "en España un cargo equivalente al peaje de respaldo derogado en 2018 aplicable "
                    "al autoconsumo residencial estándar.",
                ],
            },
        ],
        "faq": [
            {
                "q": "¿Pago algo por verter excedentes a la red?",
                "a": "No, en la modalidad de compensación de excedentes no se paga ningún peaje o cargo por el excedente vertido; simplemente se compensa a un precio inferior al de compra, según lo pactado con tu comercializadora.",
            },
            {
                "q": "¿Esta normativa es igual en toda España?",
                "a": "El marco estatal (Real Decreto 244/2019 y normativa posterior) es de aplicación en todo el territorio, aunque cada comunidad autónoma puede regular aspectos procedimentales del registro y la tramitación administrativa de las instalaciones.",
            },
        ],
    },
]

# Páginas institucionales (obligatorias para la aprobación en Google AdSense)
LEGAL_PAGES = ["sobre-nosotros", "contacto", "politica-de-privacidad", "aviso-legal", "cookies"]
