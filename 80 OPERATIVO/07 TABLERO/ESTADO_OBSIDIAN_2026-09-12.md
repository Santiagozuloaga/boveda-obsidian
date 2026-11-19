# 🧠 ESTADO OBSIDIAN — 2026-09-12 (Prioridad actual)

> Operador: Admin. Regla: pensar aquí, gestionar en Notion, ejecutar en Todoist.
> Verificado en disco hoy. Fuente: bóveda `Mente Maestra E-100`.

## 1. Estructura (S.O.P. V5.3 verificada)
- `00_INBOX_TEMPORAL/` + `_MOC_INBOX.md`
- `01_DIARIO_DE_GUERRA/` — `_MOC_DIARIO.md`, `CALENDARIO_DE_VIDA.md`, `01_Daily_Logs/` (3 archivos: `2026-09-11.md` + 2 `Sin título`), `02_Post_Mortem/`, `03_Cifrado_Shard/`, `04_Revisiones/`
- `02_ALEMANIA_ZETTELKASTEN/` — `_MOC_ALEMAN.md`
- `03_PROGRAMACION_Y_LOGICA/` — `_MOC_CODIGO.md`, `_MOC_CIENCIAS.md`
- `04_LITERATURA_Y_FUENTES/` — `_MOC_FUENTES.md`
- `05_PROTOCOLOS_Y_SISTEMAS/` — `_MOC_PROTOCOLOS.md` + `01_Constitucion_SOP/` (carpeta plantillas Templater)
- `06_FE_Y_FILOSOFIA/` — `_MOC_FE.md`
- `07_TABLERO/` — `HOY.md`, `TABLERO_SEMANAL.md`, `Tubería Zettel.md`, `Pruebas Plugins.md`, `CHECKLIST_PENDIENTES_Admin.md`, `Dailies.base`
- Total MOCs: 8. `HOME.md` raíz.

## 2. HOME — rediseño a conceptos ✅
`HOME.md` ya no muestra rutas técnicas:
- Navegación: Hoy / Semana / Tubería + Vida / Ritual
- MOCs: Alemán, Código, Diario (nombres, no `02_`, `03_`, `_MOC_`)
- Inbox: destilar 10 min/semana. Dailies vía `Dailies.base`.
- Pedido de Admin cumplido, sin borrar objetivos previos.

## 3. Tablero espejo (desactualizado)
- `HOY.md` y `TABLERO_SEMANAL.md` dicen `Sincronizado: 2026-09-06`.
- Muestran Todoist 2 abiertas (plan estudios U + export Gmail 30-nov) y Notion con fechas feb-2026 (Orden Batalla 4, Invasión 1, Pipeline 1).
- Rayos-X Dataview en HOY: `TABLE energia, x_ganada FROM 01_Daily_Logs LIMIT 14` — requiere frontmatter `energia:` en dailies.
- Deudas en Semanal: `TASK WHERE !completed LIMIT 30`.

## 4. Calendario de vida
- `CALENDARIO_DE_VIDA.md`: cuadrícula manual ENE-DIC. Solo X marcada: SEP-06 (`☒`).
- Ritual X (las 3): micro-auditoría + MCs liquidadas + energía ≥0.7. Marcar = borrar `☐` → escribir `☒`.
- Tracker automático debajo: `searchTarget: energia`, `folder: 01_Daily_Logs`, 2026-09-01 a 30, `yMin 0 yMax 1 showPoint true`. Ver en vista lectura.
- Día N y barra `████░░░░░░ 0%` pendientes de actualizar.

## 5. Tubería Zettel (Kanban)
- `Tubería Zettel.md` (`kanban-plugin: board`): Inbox vacío, MOC con 3 links, Evergreen vacío.
- Prueba 4: arrastrar Inbox→MOC y que persista tras reinicio.

## 6. Plugins — 16/16 en disco
Carpetas en `.obsidian/plugins`: tracker, spaced-repetition, templater, style-settings, dataview, kanban, meld-encrypt, homepage, periodic-notes, languagetool, omnisearch, zotero-connector, youtube-transcript, custom-frames, text-extractor, excel-to-markdown.
- `Pruebas Plugins.md`: 1/17 marcado (Tracker). Faltan 2-17, incluido Dataview (tabla Rayos-X con 2026-09-11), Kanban color, Templater (`Ctrl+P Insert template`, carpeta = `05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP`), Homepage (grafo al abrir), Periodic (`Open weekly note` en `04_Revisiones`), Omnisearch (`Klausur`), Meld, Zotero, YT, Custom Frames (leo.org), Text Extractor (PDF), Excel 3x3, Dailies.base.
- `app.json`: `updateInternalLinks true`, adjuntos a `00_INBOX_TEMPORAL/adjuntos`.

## 7. Tema
- `appearance.json`: `cssTheme: EvilRed`, `theme: obsidian`, `accent #0011ff`, `interfaceFont Montserrat`, snippet activo `eggman-balance`.
- `eggman-balance.css` v2: fondo `#0b0b11` negro cuervo, H1 oro `#f0b429`, H2 hueso `#ece7dd`, H3 platino, links rojo, código azul `#6cb2ff` sin fondo, callouts borde oro, tablas cabecera oro, Kanban tarjeta `#111118` borde `#8a5e1a`.
- Temas instalados: Blue Topaz, EvilRed, ITS, Prism, Things, Wasp. Icono app: República (decisión Admin).

## 8. Faltantes detectados hoy (Admin)
1. Plantillas vacías diaria/semanal/mensual/anual no encontradas — solo `PLANTILLA_Daily_Note` referenciada.
2. Dailies con basura: 2 `Sin título` en `01_Daily_Logs`.
3. HOY/SEMANAL con datos viejos (6 días). Re-sincronizar desde Todoist/Notion.
4. Pruebas 2-17 sin marcar. Hacer en orden con `Ctrl+P` + vista lectura.
5. `Dailies.base` y grafo Homepage por confirmar en app abierta.

## 9. Conexiones
- [[07_TABLERO/HOY]] · [[07_TABLERO/TABLERO_SEMANAL]] · [[07_TABLERO/Pruebas Plugins]] · [[07_TABLERO/CHECKLIST_PENDIENTES_Admin]]
- [[01_DIARIO_DE_GUERRA/CALENDARIO_DE_VIDA]] · [[01_DIARIO_DE_GUERRA/_MOC_DIARIO]]
