---
tipo: informe
estado: cerrado
fecha: 2026-10-11
materia: auditoria
dominio: 90 SISTEMA
agente: Qoder (sesion 4f98c400)
dirigido_a: Admin
severidad_maxima: CRITICA
---

# REPORTE DE AUDITORÍA E-100 — 2026-10-11

Auditoría externa sobre la bóveda `Mente Maestra E-100`, encargada por Admin en una sesión de Qoder.
Cumple la regla 4 de `AGENTS.md`: toda afirmación va clasificada y con el comando que la produjo.
**Nada fue modificado, movido, renombrado ni borrado.** Este fichero es el único write de la auditoría, y queda sin versionar (ver F-9).

## F-1 · CRÍTICA · La apiKey del plugin Local REST API es pública en GitHub

Cadena de evidencia, en orden:

| # | Hecho | Cómo se verificó |
|---|---|---|
| 1 | La bóveda es un repo git con remoto | `git remote -v` → `origin https://github.com/Santiagozuloaga/boveda-obsidian.git` |
| 2 | El repo **es público** | HTTP sin credenciales sobre la URL; la página se sirve con el rótulo `Public` y el listado completo de 574 ficheros |
| 3 | Existe una norma anti-secretos y funciona a nivel de árbol | `.gitignore` → `# Secretos (API keys en configs de plugins)` / `.obsidian/plugins/obsidian-local-rest-api/data.json`. `git ls-tree -r origin/main` confirma que ese fichero **no** está versionado (solo `main.js` y `manifest.json`) |
| 4 | `Mente Maestra E-100.zip` (20 MB) **sí** está versionado y en el remoto | `git branch -r --contains 4a0add6` → `origin/main`; `git ls-tree -r --name-only origin/main \| grep .zip` → los dos zips |
| 5 | El zip contiene la ruta exacta que el `.gitignore` protege | `unzip -l` → `Mente Maestra E-100/.obsidian/plugins/obsidian-local-rest-api/data.json` (6822 B) |
| 6 | Ese fichero dentro del zip lleva credencial | `unzip -p … \| grep -cE` con patrones `AKIA…`, `sk-live/proj/ant…`, `ghp_…`, `-----BEGIN PRIVATE KEY`, `"apiKey"`, `Bearer …` → **3 coincidencias**, el mismo recuento que el fichero en disco. El valor nunca fue impreso ni extraído |
| 7 | El commit que lo subió afirma lo contrario | `git log` → `4a0add6 backup boveda E-100 (sin secretos, sin sync-trash)` |

**Por qué ocurre:** un `.gitignore` mira rutas del árbol de trabajo, no el interior de un archivo contenedor. Un zip de backup metido dentro de la propia bóveda versionada esquiva todas las normas de secretos del repo de una vez.

**Alcance real de la exposición (sin alarmismo):** la clave del Local REST API autoriza lectura y escritura de toda la bóveda a través del servidor HTTP del plugin. Su peligro depende de que ese puerto haya sido alcanzable desde fuera del PC (ADB reverse, red local, túnel). No verifiqué el estado de escucha del plugin — ver F-8, `NO-EJECUTADO`. También son públicos: `parte 2.zip` (PDFes de la monografía con nombre y apellidos) y las 8 notas de `01_DIARIO_DE_GUERRA/03_Cifrado_Shard/`.

**Contención, en este orden (ninguna ejecutada por el auditor):**

1. **Rotar la apiKey** en Obsidian → Ajustes → Local REST API. Es lo único que caduca el valor de la filtración, y va antes que cualquier borrado de historial.
2. **Poner el repo privado**: `gh repo edit Santiagozuloaga/boveda-obsidian --visibility private`. Reduce exposición futura; no borra el pasado para quien ya lo clonó.
3. **Expulsar los zips del historial**: `git filter-repo --invert-paths --path "Mente Maestra E-100.zip" --path "parte 2.zip"` + force-push. Reescribe historia compartida: requiere autorización explícita de Admin, y la caché por SHA de GitHub no se purga sola (solicitud a soporte).
4. **Regla de fondo**: prohibir `*.zip` dentro de la bóveda con un pre-commit. El `.git` ya pesa 50 MB en buena parte por esto.

## F-2 · ALTA · Hay 2 commits locales sin subir, y uno de ellos es justo la carpeta de agentes

`git status -sb` → `## main...origin/main [ahead 2]`; `git log --oneline origin/main..HEAD` → `b288274 freeze: blinda community-plugins.json…` y `380b39d v2.0: espacio agentes (8 fichas)…`.
Consecuencia: `08 AGENTES` **todavía no es pública**. No subir nada hasta cerrar el paso 1 de F-1.
Untracked: `E100_CURRENT_STATE_REPORT.md`.

## F-3 · MEDIA · 245 de 422 notas no tienen frontmatter, contra la norma declarada

`AGENTS.md` fija frontmatter mínimo `tipo, estado, fecha, materia`. Muestreo verificado: `00_INBOX_TEMPORAL/_MOC_INBOX.md` y `01_DIARIO_DE_GUERRA/03_Cifrado_Shard/*.md` empiezan en texto directo.
Los dailies **sí cumplen** (`2026-09-27.md` → `tipo: daily / fecha / estado`) → el schema se abandonó fuera del flujo diario, justo en MOCs e informes, que son los nodos más enlazados y los únicos que Dataview puede filtrar.
Nota de honestidad: el primer conteo dio 421 porque el script no manejaba CRLF; corregido, el número real es 245.

## F-4 · MEDIA · 61 wikilinks sin destino

Recuento original: 102. Corregido a 61 tras clasificar y excluir 27 placeholders de Templater (`<% tp.date.now(…) %>`) y 25 enlaces dentro de bloques de código.
Muestras confirmadas:
- `[[Derivadas]]`, `[[Álgebra Lineal]]`, `[[Teorema de L'Hôpital]]` desde `_MOC_CIENCIAS`: el fichero real se llama `Derivadas Fracciones Raices.md`.
- `[[04_LITERATURA_Y_FUENTES/_MOC_LITERATURA]]` citado desde 2 ficheros: **ese MOC no existe**.
- `_INDICE_SESIONES`: enlaces partidos por el propio redactado → `[[SES-i0BgS0Mj-A[REDACTED]]`.
- `05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/00_ARCHIVO_HISTORICO/_INICIO_antiguo.md` apunta a rutas del esquema viejo (`00 ENTRADA (Inbox)/_INICIO`, `20 AREAS/_AREAS`).
- Un PDF enlazado sin estar en el repo: `2007-8064-edsc-10-24-e2481347.pdf`.

`NO-EJECUTADO`: no evalué `aliases` del frontmatter, así que algunos de estos 61 sí resuelven en Obsidian. El número es techo, no suelo.

## F-5 · MEDIA · Dos carpetas de ÁREAS que solo se distinguen por un espacio

`20  AREAS` (doble espacio) contiene 34 notas y **no existe en `origin/main`**; `20 AREAS` tiene 1 nota (`_HISTORICO_V1.md`) y es la que sí está publicada. `E100_CURRENT_STATE_REPORT.md` referencia la variante con doble espacio.
Lectura: la divergencia es firma de **tres mecanismos escribiendo el mismo árbol** — `git`, Syncthing (hay `.stignore`, `.stfolder` ignorado) y la copia de OneDrive. Ver F-6.

## F-6 · MEDIA · La bóveda que Obsidian tiene abierta no es la que se respalda

`%APPDATA%\obsidian\obsidian.json`: dos vaults; el marcado `"open":true` es `C:\Users\Admin\Downloads\syn\Mente Maestra E-100`. La ruta de OneDrive (`OneDrive\Desktop\syn\Mente Maestra E-100`) contiene **un único fichero**, `Cursor (GPU FIX).lnk`.
Si la idea era tener respaldo en la nube, OneDrive no lo está dando: el árbol vivo está en `Downloads` y su respaldo real es el repo de GitHub (con lo que eso implica tras F-1).

## F-7 · BAJA · `AGENTS.md` ignora la carpeta que los agentes necesitan

El "Mapa mínimo" enumera `00,01,02,03,04,05,06,07,10.02,90`. Faltan `08 AGENTES`, `10 PROYECTOS`, `20 AREAS`, `30 RECURSOS`, `40 ARCHIVOS X`. Es el agujero más barato de cerrar y el que más afecta al propósito del fichero: el documento que manda leer primero no menciona el registro de quién puede hacer qué.
Además, las 8 fichas de `08 AGENTES` usan `tags` + `status:` (inglés) en vez del schema declarado (`estado:`), así que un filtro por `estado` no las ve.

## F-8 · Las ~300 skills que se inyectan en cada turno son de Qoder, no de Obsidian/OpenCode/Devin

Pregunta de Admin sobre el origen. Evidencia:

| Fuente | SKILL.md en disco | ¿Se inyecta en este chat? |
|---|---|---|
| `~/.qoder/plugins` | **1314** | **Sí** — `~/.qoder/settings.json` tiene 69 plugins en `ON`, 64 de ellos `@qoder-marketplace` |
| `~/.qoder/skills` (usuario) | 6 | Sí (las tuyas: 4 de esta sesión + 2 previas) |
| `~/.codex/skills` | 659 | No (es el árbol de Codex CLI) |
| `~/.config/opencode` | 238 | No (OpenCode) |
| `~/.gemini` | 80 | No |
| `~/.claude` | 31 | No |
| `~/.cursor` | 27 | No |

Consecuencia práctica: la lista de skills y agentes viaja en cada mensaje, así que el coste de un turno trivial no es trivial. En una cuenta `Free` con 0 créditos medidos en `Settings → Profile` (`Current plan: Free`, `Past-year Credits: 0`), esto es impuesto, no capacidad.
`SUPUESTO` (no verificado): que los 69 plugins se activaron de golpe desde el marketplace en una sola operación, en lugar de instalarse uno a uno por necesidad.
`NO-EJECUTADO`: no medí los tokens reales de la cabecera inyectada; la afirmación de coste es estructural (el listing está en el prompt), no medida.
Acción barata: desactivar en `Settings → Extensiones` lo que no se use. No hace falta borrar nada de disco.

## F-9 · Lo que NO hice

- No toqué el repo, el remoto, los zips, ni el historial. No ejecuté `git add`, `commit`, `push`, `filter-repo` ni cambio de visibilidad.
- No abrí ni copié el valor de ninguna credencial; solo conté coincidencias de patrón.
- No roté la clave (corresponde a Admin, en Obsidian).
- Este fichero queda **untracked a propósito**: si lo versionas y subas antes de cerrar F-1, estarás publicando el índice de lo que hay que buscar.

## Opinión del auditor

Lo estructural está bien: las cuatro fuentes canónicas declaradas en `AGENTS.md` existen (4/4 verificadas), el MOC de agentes impone "ningún agente se certifica a sí mismo", y las fichas declaran límites en vez de capacidades infladas — `AutoCLAW` admite "pendiente demostración continua", que es la señal de madurez más clara de todo el sistema.

El riesgo de esta bóveda no es el desorden de formato. Es que **destruyó su propia frontera de confianza**: la regla 4 dice que los archivos reales mandan sobre los informes, y a la vez el backup de esos archivos se metió dentro de un repo público. El `.gitignore` anti-secretos está bien escrito y no sirvió de nada, porque la superficie real no era el árbol, era un contenedor de 20 MB. Cualquier norma futura que se escriba sobre rutas volverá a fallar del mismo modo; la que funciona es la que bloquea el artefacto en el pre-commit.

Segundo punto: hay tres mecanismos de sincronía (git, Syncthing, OneDrive) y ninguno de los tres es consciente de los otros dos. Eso produce exactamente lo que se ve — dos carpetas `20 AREAS` distintas, un `20 AREAS` publicado y otro local, cinco backups de `workspace.json` con sufijos de herramienta distinta (`.bak-admin`, `.bak-admin2`, `.bak-opencode`, `.dbg`, `.presplitbackup`, `.testbackup`). No es falta de disciplina, es la ausencia de un dueño designado. Elegir uno y desactivar los otros dos vale más que cualquier limpieza de notas.

Y lo único urgente es F-1. Todo lo demás puede esperar al lunes.
