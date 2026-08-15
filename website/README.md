# AutoconsumoPro — sitio web

Implementación del plan de negocio descrito en
[`docs/plan-nicho-autoconsumo-solar.md`](../docs/plan-nicho-autoconsumo-solar.md):
un sitio estático (sin backend, sin dependencias) listo para desplegar en
cualquier hosting y para insertar Google AdSense cuando la cuenta esté aprobada.

## Estructura del proyecto

```
website/
├── src/
│   ├── content.py   # Todo el CONTENIDO: categorías y artículos (texto plano)
│   ├── build.py     # El generador: combina content.py con las plantillas HTML
│   └── check.py     # Validador: enlaces rotos, anclas, metadatos duplicados
├── static/
│   ├── css/style.css
│   ├── js/main.js   # Menú móvil + banner de cookies (placeholder)
│   └── img/favicon.svg
└── public/          # Salida generada — esto es lo que se despliega
```

`public/` se genera automáticamente y se sobrescribe por completo en cada
build. No lo edites a mano: edita `src/content.py` (textos) o `src/build.py`
(maquetado) y vuelve a generar.

## Cómo regenerar el sitio

Requiere solo Python 3 (sin dependencias externas):

```bash
cd website/src
python3 build.py
python3 check.py   # opcional pero recomendado antes de desplegar
```

Genera `website/public/` con 23 páginas: home, 4 páginas de categoría,
12 artículos completos, 5 páginas legales, `sitemap.xml` (con `lastmod` por
página), `robots.txt` y `404.html` (marcado `noindex`).

`check.py` recorre el HTML generado y falla (código de salida 1) si encuentra
enlaces internos rotos, anclas `#id` inexistentes, páginas sin `title`,
sin meta description o sin canonical, o títulos y descripciones duplicados
entre páginas — el tipo de error de canibalización que penaliza en SEO.

## Cómo previsualizarlo en local

```bash
cd website/public
python3 -m http.server 8000
# abrir http://localhost:8000/
```

## Ampliar el contenido (los ~48 artículos restantes del plan)

1. Añade una nueva entrada al final de la lista `ARTICLES` en `src/content.py`,
   siguiendo el mismo formato que los artículos existentes (título, meta
   descripción, keyword objetivo, intención, introducción, secciones con
   sus `h2`/párrafos/tablas opcionales, y FAQ).
2. Ejecuta `python3 build.py` de nuevo. La nueva página se crea sola, se
   añade al `sitemap.xml`, y aparece automáticamente en el listado de su
   categoría y en "últimas guías actualizadas" si corresponde.

No hace falta tocar `build.py` para añadir artículos: solo para cambiar el
maquetado o la estructura de las plantillas.

## Diseño

Dirección visual: panel técnico/instrumental (no el eco-blog cálido de
plantilla habitual del nicho) — fondo neutro frío, acento ámbar (solar) y
verde (aerotermia), tipografía grotesca (Archivo/IBM Plex Sans) combinada
con monoespaciada (IBM Plex Mono) para reforzar la lectura de datos y cifras.
El elemento distintivo es el gráfico de arco en el hero, que representa a la
vez la curva de producción solar y la curva de demanda de calefacción —
visualizando la complementariedad estacional entre los dos verticales del
sitio (ver sección 2 del plan de negocio).

Los artículos usan una maquetación de dos columnas en escritorio: la columna
de lectura (limitada a 72 caracteres de medida, alineada con el H1) y una
barra lateral fija con el índice de la guía y la torre publicitaria. Por
debajo de 1040 px la barra lateral desaparece y el texto pasa a una columna.

## Posiciones publicitarias ya preparadas (`.ad-slot`)

Siguiendo las posiciones recomendadas en la sección 6 del plan de negocio,
ya existen contenedores marcados (visualmente discretos, con borde discontinuo)
en:

- Home, tras la cuadrícula de categorías (`home-in-content`)
- Cada página de categoría, al final del listado (`category-<slug>-footer`)
- Cada artículo, in-content (`article-<slug>-1`, `article-<slug>-2`)
- Cada artículo, torre lateral 300x600 fija en escritorio
  (`article-<slug>-sidebar`), oculta por debajo de 1040 px

Los huecos in-content **no** se insertan en posiciones fijas: se reparten según
el número de secciones del artículo (uno tras la primera sección y, solo en
artículos de 4 o más secciones, otro hacia la mitad), y nunca justo antes del
cierre del artículo. Así se evita la densidad publicitaria excesiva que penalizan
las políticas de AdSense en artículos con secciones cortas.

Para activar AdSense, sustituye cada `<div class="ad-slot" ...>` en
`build.py` (función `ad_slot`) por el `<ins class="adsbygoogle">` real con
tu `data-ad-client` y `data-ad-slot`, y añade el script de carga de AdSense
en `BASE_TEMPLATE` (bloque `<head>`).

## Pendiente antes de publicar en producción

Este sitio es una base funcional y con contenido real, pero **antes de
lanzarlo con tráfico real y solicitar AdSense** hay que:

1. **Registrar un dominio real** (el plan sugiere `autoconsumopro.es`,
   `wattsvivienda.com` o `kilovatioverde.es`) y actualizar `SITE["base_url"]`
   y `SITE["domain"]` en `content.py`.
2. **Sustituir el texto legal de plantilla** en Aviso Legal, Política de
   Privacidad y Política de Cookies (`LEGAL_CONTENT` en `build.py`) por
   texto revisado por un profesional, con los datos reales del titular
   (NIF/CIF, domicilio, email) — obligatorio por la LSSI antes de publicar.
3. **Conectar una plataforma de gestión del consentimiento (CMP)**
   certificada por Google en lugar del banner de cookies de ejemplo en
   `main.js`, requisito para servir AdSense a usuarios del EEE.
4. **Conectar el formulario de contacto** (`/contacto/`) a un backend real
   (Formspree, función serverless, etc.); actualmente es solo maquetación.
5. **Completar el resto de los 103 artículos** del plan de contenidos según
   la cadencia de publicación de la sección 5, y solo entonces solicitar
   la revisión de Google AdSense (exige un volumen mínimo de contenido
   original y sustancial).
