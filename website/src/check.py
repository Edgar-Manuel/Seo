# -*- coding: utf-8 -*-
"""Validador del sitio generado.

Uso (después de ejecutar build.py):
    python3 check.py

Comprueba sobre el HTML ya generado en ../public/:
  - que ningún enlace interno apunte a una página inexistente,
  - que ninguna ancla (#id) apunte a un id que no existe en esa página,
  - que toda página tenga title, meta description y canonical,
  - que no haya títulos ni descripciones duplicados entre páginas
    (canibalización SEO).

Devuelve código de salida 1 si encuentra algún problema, para poder
encadenarlo en un despliegue.
"""
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(os.path.dirname(ROOT), "public")


def load_pages():
    pages = {}
    for dirpath, _, files in os.walk(PUBLIC):
        for name in files:
            if name.endswith(".html"):
                path = os.path.join(dirpath, name)
                with open(path, encoding="utf-8") as fh:
                    pages[os.path.relpath(path, PUBLIC)] = fh.read()
    return pages


def target_exists(url_path):
    if url_path.startswith("/assets/"):
        return os.path.exists(os.path.join(PUBLIC, url_path.lstrip("/")))
    return os.path.exists(os.path.join(PUBLIC, url_path.strip("/"), "index.html"))


def main():
    if not os.path.isdir(PUBLIC):
        print("No existe ../public/. Ejecuta antes: python3 build.py")
        return 1

    pages = load_pages()
    problems = []
    titles = defaultdict(list)
    descriptions = defaultdict(list)

    for rel, html in sorted(pages.items()):
        ids = set(re.findall(r'id="([^"]+)"', html))

        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith("#"):
                if href[1:] not in ids:
                    problems.append(f"{rel}: ancla rota {href}")
            elif href.startswith("/") and not target_exists(href):
                problems.append(f"{rel}: enlace interno roto {href}")

        title = re.search(r"<title>(.*?)</title>", html, re.S)
        desc = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
        canonical = re.search(r'<link rel="canonical"', html)

        if not title:
            problems.append(f"{rel}: falta <title>")
        else:
            titles[title.group(1).strip()].append(rel)
        if not desc:
            problems.append(f"{rel}: falta meta description")
        else:
            descriptions[desc.group(1).strip()].append(rel)
        if not canonical:
            problems.append(f"{rel}: falta canonical")

    for value, where in titles.items():
        if len(where) > 1:
            problems.append(f"title duplicado en {', '.join(where)}: {value[:60]}…")
    for value, where in descriptions.items():
        if len(where) > 1:
            problems.append(f"meta description duplicada en {', '.join(where)}")

    print(f"Páginas analizadas: {len(pages)}")
    if problems:
        print(f"Problemas encontrados: {len(problems)}")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("Sin problemas: enlaces, anclas y metadatos correctos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
