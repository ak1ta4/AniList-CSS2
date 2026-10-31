#!/usr/bin/env python3
"""Genera anilist-fullscreen.user.css (Stylus) a partir de anilist-automail.css.

La versión de Automail es la única fuente: edita solo ese archivo y ejecuta
este script. Antes de generar nada comprueba que comentarios, llaves y
paréntesis estén cerrados, los errores que dejan sin efecto el resto del CSS.

Uso:
    python scripts/build_userstyle.py          genera la versión de Stylus
    python scripts/build_userstyle.py --check  falla si el CSS está mal o la
                                               versión de Stylus no está al día
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "anilist-automail.css"
TARGET = ROOT / "anilist-fullscreen.user.css"
VERSION = "3.1.0"

HEADER = f"""/* ==UserStyle==
@name           AniList Fullscreen Dark
@namespace      anilist-fullscreen
@version        {VERSION}
@description    Perfil oscuro a pantalla completa y responsive para AniList
@license        MIT
@preprocessor   default
==/UserStyle== */

/* Archivo generado: edita anilist-automail.css y ejecuta scripts/build_userstyle.py */

@-moz-document domain("anilist.co") {{

"""


def strip_noise(css):
    """Quita comentarios y cadenas para contar solo la sintaxis real."""
    if css.count("/*") != css.count("*/"):
        raise ValueError("hay un comentario sin cerrar")
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return re.sub(r'"[^"\n]*"', '""', css)


def validate(css):
    """Devuelve la lista de errores de sintaxis encontrados."""
    try:
        code = strip_noise(css)
    except ValueError as error:
        return [str(error)]
    errors = []
    pairs = {"}": "{", ")": "("}
    stack = []
    for char in code:
        if char in "{(":
            stack.append(char)
        elif char in pairs and (not stack or stack.pop() != pairs[char]):
            errors.append(f"'{char}' no coincide con lo que tiene abierto")
    errors += [f"'{char}' sin cerrar" for char in stack]
    return errors


def main():
    css = SOURCE.read_text(encoding="utf-8")
    errors = validate(css)
    if errors:
        print("\n".join(f"Error: {error}" for error in errors))
        return 1

    output = f"{HEADER}{css.rstrip()}\n\n}}\n"
    if "--check" in sys.argv:
        current = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if current != output:
            print("Error: la versión de Stylus no está al día; ejecuta el script.")
            return 1
        print("Todo correcto.")
        return 0

    TARGET.write_text(output, encoding="utf-8", newline="\n")
    print(f"Generado {TARGET.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
