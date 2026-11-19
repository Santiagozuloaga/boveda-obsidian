# 🔌 Guía de plugins E-100 — uso diario y por qué cada uno

> Operador: Admin. 15 plugins (14 + Tasks 8.4.0) + `Dailies.base` (núcleo). Estado: 15/15 verificados el 2026-10-06. Detalle vivo en [[07_TABLERO/Pruebas Plugins]].
> Formato por plugin: **Uso** (qué haces tú cada día) · **Por qué** (qué se rompe si lo quitas).

## Memoria y repaso
- **Tracker** — **Uso:** cada noche copias tu energía (0.0–1.0) al frontmatter `energia:` de la daily; el gráfico sale solo en *ENERGÍA DEL MES*. **Por qué:** sin él no hay serie histórica de energía y la regla X pierde su tercer pilar. Se ve en: `01_DIARIO_DE_GUERRA/CALENDARIO_DE_VIDA` (vista lectura).
- **Spaced Repetition** — **Uso:** en bus/fila abres paleta (`Ctrl+P` → `spaced`) y repasas el mazo `#flashcards/Aleman`; tarjetas nuevas con `::`, `:::` reversible, `==x==` cloze. **Por qué:** es tu máquina de alemán C1; sin él el vocabulario se evapora. Mazos en `_MOC_ALEMAN`.

## Conocimiento
- **Dataview** — **Uso:** no lo tocas: alimenta solo el Rayos-X de `HOY`, las *Deudas* del semanal y el *Vocabulario vivo* del MOC alemán. Solo mantén el frontmatter (`energia:`, `tipo: vokabel`). **Por qué:** sin él esos tableros mueren y vuelves a contar a mano. Solo rinde en vista lectura.
- **Omnisearch** — **Uso:** `Ctrl+Shift+F` para todo (ej: `Klausur`, `Buenrostro`). **Por qué:** es tu memoria de recuperación; la búsqueda nativa no lee PDFs.
- **Text Extractor** — **Uso:** ninguno directo: trabaja por detrás para Omnisearch (PDF/Office). **Por qué:** sin él los papers son cajas negras.
- **Excel to Markdown** — **Uso:** cuando traigas planillas del colegio, pega la tabla 3x3 y listo. **Por qué:** evita reescribir datos; si en 3 meses no lo usas, es el primer candidato a salir.

## Organización
- **Tasks** (8.4.0) — **Uso:** `- [ ] tarea 📅 YYYY-MM-DD ⏫` en cualquier nota; `HOME` Bloque 1 + `Control Panel` las juntan (due today / week / overdue). **Por qué:** sin él no hay Tasks hoy y pierdes el motor GTD de vaultorial `gtd-task-vault`. Config: `useFilenameAsScheduledDate=false` (`data.json`).
- **Kanban** — RETIRADO 2026-09-23 (reemplazo: `Tubería Zettel.canvas` nativo). Sin uso diario.
- **Homepage** — **Uso:** abre `HOME.md` (dashboard) al arrancar (cambiado de grafo a HOME en 2026-09-19). **Por qué:** te recibe con 3 bloques vivos, no con nota vieja.
- **Periodic Notes** — **ACTIVO · INFRAESTRUCTURA CENTRAL** — Motor de plantillas Daily/Semanal/Mensual/Anual + score X ↔ `CALENDARIO_DE_VIDA`. Vía canónica: daily en `01_DIARIO_DE_GUERRA/01_Daily_Logs/YYYY-MM-DD`.
- **Templater** — **Uso:** `trigger_on_file_creation=true` + `auto_jump_to_cursor=true` — 6 folder_templates (dailies, libros, inbox, post-mortem, fuente, revisiones). **Por qué:** plantillas = formato consistente = Dataview funciona.
- **Dailies.base** (núcleo) — **Uso:** míralo en `HOME` y `Control Panel`, 3 vistas (Energía / X / Mes). **Por qué:** es tu tabla viva de dailies con energía y X.

## Escritura y estilo
- **LanguageTool** — **Uso:** escribe normal; revisa en español (`es-ES` fijado). **Por qué:** monografía y ensayos sin errores caros.
- **Style Settings** — **Uso:** ninguno hoy (vacío con EvilRed = normal). **Por qué:** solo servirá si algún día cambias de tema.
- **Meld Encrypt** — **Uso:** solo para `Keep Incidentes Feb-2026` (clave 123, sin recupero). **Por qué:** lo privado no va en texto plano ni en SyncTrayzor.

## Puentes externos
- **Zotero Integration** — **Uso:** con Zotero abierto, paleta (en inglés) *Import/Insert notes* para traer citas a tus fuentes. **Por qué:** sin puente, referencias a mano = errores APA.
- **YouTube Transcript Fetcher** — **Uso:** pega URL de video alemán → nota con transcripción (en español). **Por qué:** convierte tus 57 videos en apuntes buscables.
- **Custom Frames** — **ACTIVO · CON CONFIG** — Iframes de referencia: chat Z.ai (AutoCLAW), dashboard Notion EGG-NETWORK, monitor local (Grafana). **Por qué:** acceso rápido a IA/Notion/monitor sin cambiar ventana; revisión 30 días → si 0 uso → desinstalar.

## Tema
- **EvilRed** + `eggman-balance`: fondo `#0b0b11`, H1 oro `#f0b429`, Montserrat. No tocar.

---
## 📋 VEREDICTOS 2026-10-06 (auditoría + corrección docs)
| Plugin | Veredicto | Motivo |
|---|---|---|
| Tasks 8.4.0 | NÚCLEO | Muy activo; agenda unificada |
| Templater 2.25.1 | NÚCLEO | Activo; único mecanismo de plantillas |
| Dataview 0.5.68 | NÚCLEO (congelar) | Mantenimiento lento; migrar tablas simples a Bases core con el tiempo |
| Spaced Repetition | NÚCLEO | Activo; alemán C1 lo exige |
| Tracker | ÚTIL | Lento desarrollo; se queda por racha energía |
| Style Settings + snippets | ÚTIL | CSS sin JS |
| Zotero/LanguageTool/Custom Frames/Text Extractor/Excel/Meld/Omnisearch | ÚTIL | Uso real medido (tesis, Pomodoro, PDFs) |
| periodic-notes | **NÚCLEO · INFRAESTRUCTURA CENTRAL** | Motor Daily/Semanal/Mensual/Anual + score X ↔ `CALENDARIO_DE_VIDA` |
| obsidian-kanban | RETIRADO 2026-09-23 | Sin mantenedor; reemplazo: `Tubería Zettel.canvas` nativo |
| Homepage | CONSERVADO | Sin reemplazo nativo; riesgo bajo |
| obsidian-local-rest-api | NÚCLEO · INFRAESTRUCTURA AGENTES | API local autenticada para agentes (MCP) |
| obsidian-git | CONSERVADO | Backup/versionado bóveda (tras rotar secretos) |
| notebook-navigator | EVALUACIÓN | Navegación MOC/estructura; prueba 30 días |
| smart-connections | EVALUACIÓN | Búsqueda semántica; prueba 30 días |
| quickadd | EVALUACIÓN | Captura rápida; prueba 30 días |

---
*Actualizado 2026-10-06 tras auditoría completa: Periodic Notes = INFRAESTRUCTURA CENTRAL (no retirado). Kanban = RETIRADO. Custom Frames = ACTIVO CON CONFIG.*
