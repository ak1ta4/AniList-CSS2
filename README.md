# AniList-CSS2

CSS personalizado para perfiles de [AniList](https://anilist.co): oscuro, redondeado, a pantalla completa y responsive.

## Qué incluye

- **Pantalla completa:** el perfil ocupa todo el ancho, con márgenes que se adaptan a la ventana.
- **Barra superior en forma de notch:** del mismo ancho que el banner y alineada con él.
- **Banner:** avatar y nombre centrados, con el hueco entre ambos en el centro exacto.
- **Pestañas:** un color por pestaña y animación al pasar el puntero. Reviews y Submissions están ocultas.
- **Estadísticas del resumen:** el número crece y toma el color de su etiqueta al pasar el puntero.
- **Favoritos:** 5 por fila a pantalla completa, 4 en media pantalla y sin barra de scroll visible.
- **Puntero propio:** flecha oscura con borde rojo, y mano sobre lo clicable.
- **Subpáginas:** Anime List, Manga List, Favorites, Stats y Social siguen el mismo estilo.

## Instalación

### Automail

1. Copia todo el contenido de [`anilist-automail.css`](anilist-automail.css).
2. Pégalo en el apartado de CSS personalizado de Automail, sustituyendo el anterior.
3. Guarda y recarga el perfil.

### Stylus

Instala [`anilist-fullscreen.user.css`](anilist-fullscreen.user.css) como estilo de usuario. Se aplica a todo `anilist.co`.

## Archivos

| Archivo | Función |
| --- | --- |
| `anilist-automail.css` | Fuente principal: es el único CSS que se edita. |
| `anilist-fullscreen.user.css` | Versión para Stylus, generada automáticamente. |
| `scripts/build_userstyle.py` | Valida el CSS y genera la versión para Stylus. |

## Cómo editarlo

Los cambios más habituales se hacen en las variables de la sección 1 de `anilist-automail.css`:

| Quiero cambiar | Variable |
| --- | --- |
| Colores | `--af-bg`, `--af-card`, `--af-black`, `--af-accent`, `--af-text` |
| Márgenes laterales | `--af-gutter` |
| Separación entre bloques | `--af-gap` |
| Redondeo | `--af-radius` |
| Alto del banner | `--af-banner-height` |
| Tamaño de las actividades | `--af-entry-height`, `--af-entry-min` |
| Favoritos por fila | `--af-fav-cols` (también cambia en la sección Responsive) |

Después de editar, valida y regenera la versión de Stylus (requiere Python 3):

```bash
python scripts/build_userstyle.py
```

Para comprobar sin modificar nada:

```bash
python scripts/build_userstyle.py --check
```

### Antes de tocar el código

- **El orden importa.** El bloque Responsive debe seguir siendo el último.
- **Colores:** las variables guardan canales sueltos (`255, 65, 80`), no `rgb(...)`.
- **Acento y puntero:** los SVG del puntero no pueden usar variables. Si cambias `--af-accent`, cambia también `%23ff4150` en la sección 3.
- **Favoritos:** Automail fija ahí 470 px de ancho y filas de 115 px, de ahí los selectores reforzados y `!important`.
- **Selector del resumen:** usa `.content > .overview`, porque la página Stats tiene otro `.overview` dentro.

## Limitaciones

- AniList carga un máximo de 25 favoritos por categoría en el resumen, y el CSS no puede cargar más.
- El CSS tampoco puede cargar más actividad: el botón Load More sigue siendo necesario.
- El estilo depende de las clases actuales de AniList y puede requerir ajustes si cambian.
