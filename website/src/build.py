# -*- coding: utf-8 -*-
"""Generador estático del sitio AutoconsumoPro.

Uso:
    python3 build.py

Lee el contenido de content.py, lo combina con las plantillas HTML
definidas en este mismo archivo y escribe el sitio completo (listo para
subir a cualquier hosting estático) en ../public/.

No tiene dependencias externas: solo la librería estándar de Python 3.
"""
import json
import os
import shutil
import unicodedata
from datetime import date

from content import SITE, CATEGORIES, ARTICLES, LEGAL_PAGES

ROOT = os.path.dirname(os.path.abspath(__file__))
WEBSITE_DIR = os.path.dirname(ROOT)
OUT_DIR = os.path.join(WEBSITE_DIR, "public")
STATIC_SRC = os.path.join(WEBSITE_DIR, "static")

CATS_BY_SLUG = {c["slug"]: c for c in CATEGORIES}


# --------------------------------------------------------------------------- helpers

def cat_of(article):
    return CATS_BY_SLUG[article["category"]]


def articles_of(cat_slug):
    return [a for a in ARTICLES if a["category"] == cat_slug]


def url_for(path):
    """Absolute canonical URL for a site-relative path like '/aerotermia/'."""
    return SITE["base_url"].rstrip("/") + path


NAV_LABELS = {
    "placas-solares": "Placas solares",
    "baterias-solares": "Baterías",
    "aerotermia": "Aerotermia",
    "subvenciones-tarifas": "Ayudas y tarifas",
}


def nav_html(active_slug=None):
    items = []
    for c in CATEGORIES:
        active = " active" if c["slug"] == active_slug else ""
        items.append(
            f'<li><a class="nav-link{active}" href="/{c["slug"]}/">{NAV_LABELS[c["slug"]]}</a></li>'
        )
    return "\n".join(items)


def header_html(active_slug=None):
    return f"""
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="{SITE['name']} — inicio">
      <span class="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="28" height="28" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M16 3 L16 8 M16 24 L16 29 M3 16 L8 16 M24 16 L29 16 M7 7 L10.5 10.5 M21.5 21.5 L25 25 M25 7 L21.5 10.5 M10.5 21.5 L7 25" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          <circle cx="16" cy="16" r="5.5" stroke="currentColor" stroke-width="2"/>
        </svg>
      </span>
      <span class="brand-word">Autoconsumo<span class="brand-word-accent">Pro</span></span>
    </a>
    <nav class="site-nav" aria-label="Categorías principales">
      <ul>
        {nav_html(active_slug)}
      </ul>
    </nav>
    <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Abrir menú">
      <span></span><span></span><span></span>
    </button>
  </div>
  <nav id="mobile-nav" class="mobile-nav" aria-label="Categorías principales (móvil)">
    <ul>
      {nav_html(active_slug)}
    </ul>
  </nav>
</header>
""".strip()


def footer_html():
    cat_links = "\n".join(
        f'<li><a href="/{c["slug"]}/">{c["name"]}</a></li>' for c in CATEGORIES
    )
    # El rótulo sale del título real de la página, no del slug: derivarlo del
    # slug perdía las tildes ("Politica de privacidad").
    legal_links = "\n".join(
        f'<li><a href="/{slug}/">{LEGAL_CONTENT[slug]["title"]}</a></li>'
        for slug in LEGAL_PAGES
    )
    year = date.today().year
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <span class="brand-word">Autoconsumo<span class="brand-word-accent">Pro</span></span>
      <p>{SITE['description']}</p>
      <p class="footer-disclosure">Contenido editorial independiente. Este sitio puede mostrar publicidad
      contextual (Google AdSense) y enlaces con fines de generación de presupuestos, señalizados como tal.</p>
    </div>
    <div class="footer-col">
      <h3 class="eyebrow">Secciones</h3>
      <ul>{cat_links}</ul>
    </div>
    <div class="footer-col">
      <h3 class="eyebrow">Legal</h3>
      <ul>{legal_links}</ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>&copy; {year} {SITE['name']}. Todos los derechos reservados.</p>
  </div>
</footer>
""".strip()


def ad_slot(position_id, label="Espacio publicitario", modifier=""):
    classes = "ad-slot" + (f" {modifier}" if modifier else "")
    return f"""<div class="{classes}" data-ad-position="{position_id}" aria-hidden="true">
  <span class="ad-slot-label">{label}</span>
  <!-- Bloque AdSense: sustituir por <ins class="adsbygoogle"> con el ad-slot real antes de publicar -->
</div>"""


def breadcrumb_html(crumbs):
    """crumbs: list of (label, path or None for current page)."""
    items = []
    for label, path in crumbs:
        if path:
            items.append(f'<li><a href="{path}">{label}</a></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
    return f'<nav class="breadcrumbs" aria-label="Miga de pan"><ol>{"".join(items)}</ol></nav>'


def breadcrumb_schema(crumbs):
    elements = []
    for i, (label, path) in enumerate(crumbs, start=1):
        item = {"@type": "ListItem", "position": i, "name": label}
        if path:
            item["item"] = url_for(path)
        elements.append(item)
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site_name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Saltar al contenido</a>
{header}
<main id="main">
{body}
</main>
{footer}
<div id="cookie-banner" class="cookie-banner" hidden>
  <div class="wrap cookie-inner">
    <p>Usamos cookies propias y de terceros (incluida publicidad) para analizar el tráfico y mostrar
    contenido relevante. Puedes aceptarlas, rechazarlas o configurarlas en cualquier momento desde
    <a href="/cookies/">nuestra política de cookies</a>.</p>
    <div class="cookie-actions">
      <button id="cookie-reject" class="btn btn-ghost">Rechazar</button>
      <button id="cookie-accept" class="btn btn-primary">Aceptar</button>
    </div>
  </div>
</div>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def render_page(title, description, canonical_path, body, header=None, extra_head="", active_slug=None):
    return BASE_TEMPLATE.format(
        title=title,
        description=description,
        canonical=url_for(canonical_path),
        site_name=SITE["name"],
        extra_head=extra_head,
        header=header if header is not None else header_html(active_slug),
        body=body,
        footer=footer_html(),
    )


# --------------------------------------------------------------------------- home

def render_home():
    hero = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Guías independientes · España · {date.today().year}</p>
      <h1>{SITE['tagline']}</h1>
      <p class="hero-lede">Analizamos placas solares, baterías físicas y virtuales, aerotermia
      y las ayudas públicas vigentes con la misma vara de medir: números reales, fuentes
      contrastables y sin venderte nada por el camino.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/placas-solares/">Empezar por autoconsumo solar</a>
        <a class="btn btn-ghost" href="/aerotermia/">Ver guías de aerotermia</a>
      </div>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <svg viewBox="0 0 480 300" class="arc-svg" xmlns="http://www.w3.org/2000/svg">
        <line x1="0" y1="230" x2="480" y2="230" stroke="var(--line)" stroke-width="1"/>
        <path d="M0 230 C 90 230, 110 40, 240 40 C 370 40, 390 230, 480 230" fill="none" stroke="var(--amber)" stroke-width="2.5"/>
        <path d="M0 230 C 90 230, 130 190, 240 190 C 350 190, 390 230, 480 230" fill="none" stroke="var(--teal)" stroke-width="2.5" stroke-dasharray="1 7" stroke-linecap="round"/>
        <circle cx="240" cy="40" r="5" fill="var(--amber)"/>
        <circle cx="240" cy="190" r="5" fill="var(--teal)"/>
        <text x="248" y="35" class="arc-label">producción solar</text>
        <text x="248" y="205" class="arc-label">demanda de calor</text>
      </svg>
    </div>
  </div>
</section>
""".strip()

    planned_total = sum(c["planned"] for c in CATEGORIES)
    trust = f"""
<section class="trust-strip">
  <div class="wrap trust-grid">
    <div><span class="trust-num">{len(ARTICLES)}</span><span class="trust-label">guías publicadas y revisadas</span></div>
    <div><span class="trust-num">{planned_total}</span><span class="trust-label">artículos en el mapa de contenidos</span></div>
    <div><span class="trust-num">0</span><span class="trust-label">marcas patrocinadoras de nuestras comparativas</span></div>
  </div>
</section>
""".strip()

    cat_cards = []
    for c in CATEGORIES:
        n = len(articles_of(c["slug"]))
        cat_cards.append(f"""
<a class="cat-card cat-card--{c['accent']}" href="/{c['slug']}/">
  <span class="eyebrow">{c['eyebrow']}</span>
  <h3>{c['name']}</h3>
  <p>{c['short']}</p>
  <span class="cat-card-meta">{n} guías publicadas &rarr;</span>
</a>""")
    categories_section = f"""
<section class="section">
  <div class="wrap">
    <h2 class="section-title">Explora por silo temático</h2>
    <div class="cat-grid">
      {''.join(cat_cards)}
    </div>
  </div>
</section>
""".strip()

    ad_block = f"""
<section class="section section-ad">
  <div class="wrap">{ad_slot('home-in-content', 'Espacio publicitario (in-content)')}</div>
</section>
""".strip()

    latest = sorted(ARTICLES, key=lambda a: a["updated"], reverse=True)[:6]
    latest_cards = []
    for a in latest:
        c = cat_of(a)
        latest_cards.append(f"""
<a class="article-card" href="/{c['slug']}/{a['slug']}/">
  <span class="eyebrow">{NAV_LABELS[c['slug']]}</span>
  <h3>{a['title']}</h3>
  <p>{a['meta_description']}</p>
  <span class="article-card-meta">{a['reading_minutes']} min de lectura · Actualizado {a['updated']}</span>
</a>""")
    latest_section = f"""
<section class="section">
  <div class="wrap">
    <h2 class="section-title">Últimas guías actualizadas</h2>
    <div class="article-grid">
      {''.join(latest_cards)}
    </div>
  </div>
</section>
""".strip()

    methodology = """
<section class="section section-alt">
  <div class="wrap method-grid">
    <div>
      <h2 class="section-title">Cómo trabajamos</h2>
      <p>Cada guía se documenta con normativa oficial, fichas técnicas de fabricantes y
      condiciones contractuales reales de comercializadoras, y se revisa periódicamente
      cuando cambian precios, ayudas o normativa. Marcamos siempre la fecha de la última
      actualización al final de cada artículo.</p>
      <a class="text-link" href="/sobre-nosotros/">Más sobre nuestra metodología &rarr;</a>
    </div>
    <div>
      <h2 class="section-title">Independencia editorial</h2>
      <p>No recibimos pago de fabricantes ni comercializadoras por posicionar sus productos
      en las comparativas. El sitio se financia con publicidad contextual y con la
      derivación, señalizada, de solicitudes de presupuesto a instaladores.</p>
      <a class="text-link" href="/politica-de-privacidad/">Política de privacidad &rarr;</a>
    </div>
  </div>
</section>
""".strip()

    body = hero + trust + categories_section + ad_block + latest_section + methodology
    return render_page(
        title=f"{SITE['name']} — {SITE['tagline']}",
        description=SITE["description"],
        canonical_path="/",
        body=body,
    )


# --------------------------------------------------------------------------- category

def render_category(cat):
    arts = articles_of(cat["slug"])
    crumbs = [("Inicio", "/"), (cat["name"], None)]
    cards = []
    for a in arts:
        cards.append(f"""
<a class="article-card" href="/{cat['slug']}/{a['slug']}/">
  <span class="eyebrow">{a['intent']}</span>
  <h3>{a['title']}</h3>
  <p>{a['meta_description']}</p>
  <span class="article-card-meta">{a['reading_minutes']} min de lectura · Actualizado {a['updated']}</span>
</a>""")

    roadmap_note = f"""
<div class="roadmap-note">
  <p>Publicadas {len(arts)} de las {cat['planned']} guías previstas para este silo. Ampliamos la
  categoría cada semana siguiendo nuestro <a href="/sobre-nosotros/">plan de contenidos</a>.
  Si buscas un tema que todavía no está publicado,
  <a href="/contacto/">escríbenos</a> y lo priorizamos.</p>
</div>
""".strip()

    body = f"""
<section class="page-header">
  <div class="wrap">
    {breadcrumb_html(crumbs)}
    <p class="eyebrow">{cat['eyebrow']}</p>
    <h1>{cat['name']}</h1>
    <p class="page-lede">{cat['description']}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="article-grid">
      {''.join(cards)}
    </div>
    {roadmap_note}
  </div>
</section>
<section class="section section-ad">
  <div class="wrap">{ad_slot(f"category-{cat['slug']}-footer", 'Espacio publicitario')}</div>
</section>
""".strip()

    extra_head = breadcrumb_schema(crumbs)
    return render_page(
        title=f"{cat['name']} | {SITE['name']}",
        description=cat["short"],
        canonical_path=f"/{cat['slug']}/",
        body=body,
        extra_head=extra_head,
        active_slug=cat["slug"],
    )


# --------------------------------------------------------------------------- article

def slugify(text):
    """Slug ASCII a partir de un titular en castellano (para anclas #id)."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    out = []
    for ch in ascii_text.lower():
        if ch.isalnum():
            out.append(ch)
        elif out and out[-1] != "-":
            out.append("-")
    return "".join(out).strip("-")


def render_article_section(sec):
    html = [f'<h2 id="{slugify(sec["h2"])}">{sec["h2"]}</h2>']
    for p in sec.get("paragraphs", []):
        html.append(f"<p>{p}</p>")
    if "table" in sec:
        t = sec["table"]
        thead = "".join(f"<th>{h}</th>" for h in t["headers"])
        rows = "".join(
            "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in t["rows"]
        )
        html.append(
            f'<div class="table-wrap"><table><thead><tr>{thead}</tr></thead><tbody>{rows}</tbody></table></div>'
        )
    if "note" in sec:
        html.append(f'<p class="note">{sec["note"]}</p>')
    return "\n".join(html)


def render_article(article):
    cat = cat_of(article)
    crumbs = [("Inicio", "/"), (cat["name"], f"/{cat['slug']}/"), (article["title"], None)]

    intro_html = "\n".join(f"<p>{p}</p>" for p in article["intro"])

    # Los huecos in-content se reparten por volumen de contenido, no por índice:
    # dos anuncios seguidos en secciones cortas empeoran la lectura y la densidad
    # publicitaria que exigen las políticas de AdSense.
    total_sections = len(article["sections"])
    ad_after = {0}
    if total_sections >= 4:
        ad_after.add(total_sections // 2 + total_sections % 2)

    sections_html = []
    ad_n = 0
    for i, sec in enumerate(article["sections"]):
        sections_html.append(render_article_section(sec))
        if i in ad_after and i < total_sections - 1:
            ad_n += 1
            label = "Espacio publicitario (tras el primer bloque)" if ad_n == 1 else "Espacio publicitario (in-content)"
            sections_html.append(ad_slot(f"article-{article['slug']}-{ad_n}", label))

    faq_html = ""
    if article.get("faq"):
        items = "".join(
            f'<div class="faq-item"><h3>{f["q"]}</h3><p>{f["a"]}</p></div>' for f in article["faq"]
        )
        faq_html = f'<section class="faq"><h2>Preguntas frecuentes</h2>{items}</section>'

    related = [a for a in articles_of(cat["slug"]) if a["slug"] != article["slug"]][:3]
    related_html = ""
    if related:
        cards = "".join(
            f'<a class="article-card article-card--compact" href="/{cat["slug"]}/{r["slug"]}/">'
            f'<h3>{r["title"]}</h3><span class="article-card-meta">{r["reading_minutes"]} min de lectura</span></a>'
            for r in related
        )
        related_html = f"""
<section class="section section-alt">
  <div class="wrap">
    <h2 class="section-title">Sigue leyendo sobre {cat['name'].lower()}</h2>
    <div class="article-grid">{cards}</div>
    <a class="text-link" href="/{cat['slug']}/">Ver todas las guías de este silo &rarr;</a>
  </div>
</section>
""".strip()

    # El índice solo aporta navegación si el artículo tiene suficientes secciones.
    toc_html = ""
    if len(article["sections"]) >= 3:
        toc_items = "".join(
            f'<li><a href="#{slugify(s["h2"])}">{s["h2"]}</a></li>' for s in article["sections"]
        )
        toc_html = f"""
    <nav class="toc" aria-label="Contenido de esta guía">
      <h2 class="eyebrow">En esta guía</h2>
      <ol>{toc_items}</ol>
    </nav>"""

    aside_html = f"""
<aside class="article-aside">
  <div class="aside-sticky">{toc_html}
    {ad_slot(f"article-{article['slug']}-sidebar", 'Espacio publicitario (300x600)', modifier='ad-slot--tower')}
  </div>
</aside>
""".strip()

    body = f"""
<article class="article">
  <header class="page-header">
    <div class="wrap">
      <div class="article-head">
        {breadcrumb_html(crumbs)}
        <p class="eyebrow">{cat['name']} · {article['intent']}</p>
        <h1>{article['title']}</h1>
        <p class="article-meta">{article['reading_minutes']} min de lectura · Actualizado el {article['updated']} · Equipo editorial de {SITE['name']}</p>
      </div>
    </div>
  </header>
  <div class="wrap article-layout">
    <div class="article-body">
      {intro_html}
      {''.join(sections_html)}
      {faq_html}
      <p class="article-disclosure">Las cifras de este artículo son orientativas y pueden variar según
      proveedor, comunidad autónoma y fecha de consulta. Contrasta siempre con al menos dos
      presupuestos o fuentes oficiales antes de tomar una decisión de inversión.</p>
    </div>
    {aside_html}
  </div>
</article>
{related_html}
""".strip()

    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "description": article["meta_description"],
        "dateModified": article["updated"],
        "author": {"@type": "Organization", "name": f"Equipo editorial de {SITE['name']}"},
        "publisher": {"@type": "Organization", "name": SITE["name"]},
        "mainEntityOfPage": url_for(f"/{cat['slug']}/{article['slug']}/"),
    }
    extra_head = breadcrumb_schema(crumbs) + f'\n<script type="application/ld+json">{json.dumps(article_schema, ensure_ascii=False)}</script>'

    return render_page(
        title=f"{article['title']} | {SITE['name']}",
        description=article["meta_description"],
        canonical_path=f"/{cat['slug']}/{article['slug']}/",
        body=body,
        extra_head=extra_head,
        active_slug=cat["slug"],
    )


# --------------------------------------------------------------------------- legal pages

LEGAL_CONTENT = {
    "sobre-nosotros": {
        "title": "Sobre nosotros",
        "description": "Quiénes somos, cómo documentamos cada guía y cuál es nuestro modelo editorial en AutoconsumoPro.",
        "body": """
<p><strong>AutoconsumoPro</strong> es un proyecto editorial independiente centrado en el
autoconsumo fotovoltaico y la climatización renovable en España. Nuestro objetivo es dar
respuesta a la pregunta que casi ningún comercial contesta con precisión: <em>cuánto vas a
pagar y cuánto vas a ahorrar realmente</em>, con números desglosados en lugar de promesas
genéricas de ahorro.</p>
<h2>Nuestra metodología</h2>
<p>Cada guía se elabora contrastando normativa oficial (BOE, reglamentos técnicos como el
REBT y el RITE, convocatorias de ayudas autonómicas), fichas técnicas de fabricantes y
condiciones contractuales reales de comercializadoras eléctricas. Cuando una cifra es una
estimación y no un dato certificado, lo indicamos explícitamente en el propio texto.</p>
<h2>Actualización de contenidos</h2>
<p>El sector cambia con frecuencia: precios de equipos, convocatorias de ayudas y normativa
se revisan y actualizan. Cada artículo muestra la fecha de su última revisión. Si detectas
un dato desactualizado, puedes avisarnos desde la página de <a href="/contacto/">contacto</a>.</p>
<h2>Plan de contenidos</h2>
<p>Trabajamos con un mapa de contenidos de 60 artículos organizados en cuatro silos:
<a href="/placas-solares/">placas solares y autoconsumo fotovoltaico</a>,
<a href="/baterias-solares/">baterías físicas y virtuales</a>,
<a href="/aerotermia/">aerotermia y climatización eficiente</a>, y
<a href="/subvenciones-tarifas/">subvenciones, tarifas y mantenimiento</a>.
Publicamos de forma progresiva siguiendo ese mapa, priorizando en cada silo las
preguntas que hoy se resuelven peor en internet.</p>
""",
    },
    "contacto": {
        "title": "Contacto",
        "description": "Cómo ponerte en contacto con el equipo editorial de AutoconsumoPro.",
        "body": """
<p>¿Has detectado un dato desactualizado, quieres proponer un tema o eres instalador y te
interesa nuestra red de generación de presupuestos? Escríbenos indicando el motivo de tu
consulta.</p>
<form class="contact-form" onsubmit="return false;">
  <label for="name">Nombre</label>
  <input id="name" name="name" type="text" autocomplete="name" required>
  <label for="email">Correo electrónico</label>
  <input id="email" name="email" type="email" autocomplete="email" required>
  <label for="message">Mensaje</label>
  <textarea id="message" name="message" rows="5" required></textarea>
  <button class="btn btn-primary" type="submit">Enviar mensaje</button>
  <p class="note">Formulario de ejemplo: conecta este formulario a tu proveedor de envío
  de correo (Formspree, backend propio, etc.) antes de publicar el sitio en producción.</p>
</form>
""",
    },
    "politica-de-privacidad": {
        "title": "Política de privacidad",
        "description": "Cómo se tratan los datos personales de las personas usuarias de AutoconsumoPro.",
        "body": """
<p><em>Plantilla orientativa — sustituir por el texto legal definitivo, revisado por un
profesional del derecho, antes de publicar el sitio en producción e indicar el
responsable real del tratamiento.</em></p>
<h2>Responsable del tratamiento</h2>
<p>[Razón social / titular del sitio], con domicilio en [dirección], es responsable del
tratamiento de los datos personales facilitados a través de este sitio web.</p>
<h2>Finalidad del tratamiento</h2>
<p>Los datos facilitados mediante el formulario de contacto o los formularios de solicitud
de presupuesto se utilizan para responder a la consulta o, en su caso, ponerte en contacto
con instaladores colaboradores, siempre con tu consentimiento explícito en el momento del
envío.</p>
<h2>Publicidad</h2>
<p>Este sitio muestra anuncios servidos por Google AdSense y, potencialmente, otras redes
publicitarias, que pueden utilizar cookies para mostrar anuncios basados en visitas
anteriores. Puedes gestionar tus preferencias de cookies desde nuestra
<a href="/cookies/">política de cookies</a> y desde la configuración de anuncios de Google.</p>
<h2>Derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación
y portabilidad escribiendo a [email de contacto].</p>
""",
    },
    "aviso-legal": {
        "title": "Aviso legal",
        "description": "Condiciones legales de uso del sitio web AutoconsumoPro.",
        "body": """
<p><em>Plantilla orientativa — sustituir por el texto legal definitivo antes de publicar
el sitio en producción, incluyendo los datos identificativos reales del titular exigidos
por la Ley de Servicios de la Sociedad de la Información (LSSI).</em></p>
<h2>Titularidad del sitio</h2>
<p>[Nombre/razón social], [NIF/CIF], con domicilio en [dirección], correo de contacto
[email].</p>
<h2>Objeto</h2>
<p>Este sitio ofrece contenido informativo y editorial sobre autoconsumo fotovoltaico y
climatización renovable. La información publicada tiene carácter orientativo y no
sustituye el asesoramiento de un profesional certificado para tu caso concreto.</p>
<h2>Propiedad intelectual</h2>
<p>Los contenidos, textos, gráficos e imágenes de este sitio son propiedad de
{site_name} o de sus licenciantes, salvo indicación expresa en contrario.</p>
<h2>Enlaces a terceros y publicidad</h2>
<p>Este sitio puede incluir enlaces a sitios de terceros (fabricantes, comercializadoras,
instaladores) y publicidad contextual. {site_name} no se hace responsable del contenido
ni de las políticas de privacidad de dichos sitios de terceros.</p>
""".format(site_name=SITE["name"]),
    },
    "cookies": {
        "title": "Política de cookies",
        "description": "Qué cookies utiliza AutoconsumoPro y cómo puedes gestionarlas.",
        "body": """
<p><em>Plantilla orientativa. Antes de publicar en producción, sustituye este texto por el
generado por una plataforma de gestión del consentimiento (CMP) certificada por Google,
obligatoria para servir anuncios de AdSense a usuarios en el Espacio Económico Europeo.</em></p>
<h2>Qué son las cookies</h2>
<p>Pequeños archivos que se almacenan en tu navegador al visitar un sitio web y que
permiten, entre otras cosas, recordar tus preferencias o analizar el uso del sitio.</p>
<h2>Cookies que utilizamos</h2>
<table>
  <thead><tr><th>Tipo</th><th>Finalidad</th><th>¿Requiere consentimiento?</th></tr></thead>
  <tbody>
    <tr><td>Técnicas</td><td>Funcionamiento básico del sitio (por ejemplo, recordar que has cerrado el aviso de cookies)</td><td>No</td></tr>
    <tr><td>Analíticas</td><td>Medir visitas y comportamiento agregado de navegación</td><td>Sí</td></tr>
    <tr><td>Publicitarias (Google AdSense y similares)</td><td>Mostrar anuncios, potencialmente personalizados según tu navegación</td><td>Sí</td></tr>
  </tbody>
</table>
<h2>Cómo gestionar tus preferencias</h2>
<p>Puedes aceptar o rechazar las cookies no esenciales desde el aviso que se muestra en tu
primera visita, o modificar tu elección en cualquier momento desde la configuración de tu
navegador o desde la configuración de anuncios de Google en
<a href="https://myadcenter.google.com/" rel="noopener noreferrer" target="_blank">myadcenter.google.com</a>.</p>
""",
    },
}


def render_legal(slug):
    data = LEGAL_CONTENT[slug]
    crumbs = [("Inicio", "/"), (data["title"], None)]
    body = f"""
<section class="page-header">
  <div class="wrap">
    {breadcrumb_html(crumbs)}
    <h1>{data['title']}</h1>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    {data['body']}
  </div>
</section>
""".strip()
    return render_page(
        title=f"{data['title']} | {SITE['name']}",
        description=data["description"],
        canonical_path=f"/{slug}/",
        body=body,
    )


# --------------------------------------------------------------------------- 404

def render_404():
    body = """
<section class="page-header">
  <div class="wrap">
    <h1>Página no encontrada</h1>
    <p class="page-lede">El contenido que buscas no existe o se ha movido de dirección.</p>
    <a class="btn btn-primary" href="/">Volver al inicio</a>
  </div>
</section>
""".strip()
    return render_page(
        title=f"Página no encontrada | {SITE['name']}",
        description="La página solicitada no existe.",
        canonical_path="/404.html",
        body=body,
        extra_head='<meta name="robots" content="noindex, follow">',
    )


# --------------------------------------------------------------------------- sitemap / robots

def write_sitemap():
    # (ruta, lastmod). La home y las categorías heredan la fecha del artículo
    # más reciente que enlazan; las páginas legales no declaran lastmod.
    newest_overall = max(a["updated"] for a in ARTICLES)
    urls = [("/", newest_overall)]
    for c in CATEGORIES:
        arts = articles_of(c["slug"])
        newest = max((a["updated"] for a in arts), default=None)
        urls.append((f"/{c['slug']}/", newest))
    urls += [(f"/{cat_of(a)['slug']}/{a['slug']}/", a["updated"]) for a in ARTICLES]
    urls += [(f"/{slug}/", None) for slug in LEGAL_PAGES]

    entries = "\n".join(
        f"  <url><loc>{url_for(u)}</loc>"
        + (f"<lastmod>{lastmod}</lastmod>" if lastmod else "")
        + "</url>"
        for u, lastmod in urls
    )
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'
    with open(os.path.join(OUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def write_robots():
    txt = f"User-agent: *\nAllow: /\n\nSitemap: {url_for('/sitemap.xml')}\n"
    with open(os.path.join(OUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)


# --------------------------------------------------------------------------- main

def write(path, html):
    full_dir = os.path.join(OUT_DIR, path.strip("/"))
    os.makedirs(full_dir, exist_ok=True)
    with open(os.path.join(full_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR)

    # static assets
    shutil.copytree(STATIC_SRC, os.path.join(OUT_DIR, "assets"))

    write("/", render_home())

    for c in CATEGORIES:
        write(f"/{c['slug']}/", render_category(c))

    for a in ARTICLES:
        c = cat_of(a)
        write(f"/{c['slug']}/{a['slug']}/", render_article(a))

    for slug in LEGAL_PAGES:
        write(f"/{slug}/", render_legal(slug))

    with open(os.path.join(OUT_DIR, "404.html"), "w", encoding="utf-8") as f:
        f.write(render_404())

    write_sitemap()
    write_robots()

    n_pages = 1 + len(CATEGORIES) + len(ARTICLES) + len(LEGAL_PAGES) + 1
    print(f"Sitio generado en {OUT_DIR} ({n_pages} páginas, {len(ARTICLES)} artículos).")


if __name__ == "__main__":
    main()
