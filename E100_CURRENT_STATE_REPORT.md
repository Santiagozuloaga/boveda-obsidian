# E-100 CURRENT STATE REPORT — 06 Oct 2026 (auditoria forense, Admin)

## Estado ejecutivo
- Obsidian local: boveda accesible, sin corrupcion evidente, 522 archivos totales, 362 .md, 98 directorios.
- NOT verificado 613/522/362 como cifras maestras: conteo real al 06/10/2026 = 522 archivos / 362 md / 98 dirs (diff: 613 vs 522 = -91 entradas).
- 18 archivos 0 bytes: 15 cifrados intencionales en 03_Cifrado_Shard + 2 en .trash + .obsidian/graph.json (ANOMALIA: grafo vacio).
- community-plugins.json lista 22 activos; en disco hay 26 carpetas de plugin (incluye obsidian-importer y sheet-plus no listados). ESTADO_FINAL (6 plugins) esta desactualizado.
- generate_grafo.py ROTO: SALIDA_DEF apunta a C:\Temp\STAGING_20261004\CERTIFICACION\ (borrado) → FileNotFoundError (l.18, l.279).
- Notion API OK (bot 'opencode'). Duplicacion masiva de BDs: universo paralelo 3d2b38a4-* (CENTRAL, PIPELINE, C1, FINANCIERA, INTEGRIDAD, EVIDENCIAS, HARDWARE, CALENDARIO x2, EVOLUCION).
- Filas Notion (originales): PIPELINE 1, CENTRAL 5, C1 9, RADAR 2, FINANCIERA 1, INTEGRIDAD 1, EVIDENCIAS 0, HARDWARE 0, ARSENAL 6, ORDEN 4, INTERFERENCIA 0, EVOLUCION 1.
- Todoist API OK. 5 proyectos (Inbox, Universidad, Aleman, Estudio, Habitos). 11 tareas, TODAS en Universidad; 10 sin fecha; 0 vencidas; 1 con fecha 2026-11-30. Inbox/Aleman/Estudio/Habitos sin tareas.
- MCPs notion/todoist/obsidian/obsidian-fs: enabled:false (Pinterest OFF). Solo filesystem, memory, exa, context7 ON.
- Historial: e-100-obsidian-plugins-y-omniroute.json, 4182 mensajes, SHA256 3D83A261..., 145 MB, 1 sola sesion (C-30), .87, ~117M input tokens.
- C:\Temp\STAGING_20261004 BORRADO: el ledger forense C-1..C-46 y el CERTIFICACION previo no son verificables desde disco (solo sobrevive resumen en ESTADO_FINAL.md).
- Seguridad: token Notion (ntn_...) y API key Todoist funcionales en opencode.json; local-rest-api con apiKey + puerto 27124/insecure 27123; .gitignore cubre *token*.json pero NO opencode.json (no tracked en git, mitigado).
- No existe .git en la boveda Obsidian (riesgo de commit accidental de .obsidian: ninguno hoy).
- Pendiente historico sin verificar: RNG state RCS, cadenas 0/24, demo RCS, Syncthing solapamiento, umbral 65 vs 75 (C-43).

## Obsidian — inventario
- Base PARA + MOC: 00 ENTRADA, 00_INBOX_TEMPORAL, 01_DIARIO_DE_GUERRA, 02_ALEMANIA_ZETTELKASTEN, 03_PROGRAMACION_Y_LOGICA, 04_LITERATURA_Y_FUENTES, 05_PROTOCOLOS_Y_SISTEMAS, 06_FE_Y_FILOSOFIA, 07_TABLERO, 10 PROYECTOS, 20 AREAS (x2: '20  AREAS' con doble espacio + '20 AREAS'), 30 RECURSOS, 40 ARCHIVOS X, 90 SISTEMA, 10.02 MONOGRAFIA.
- 15 cifrados 0 bytes en 01_DIARIO_DE_GUERRA\03_Cifrado_Shard (intencional, confirmado combinacion: Bill chiper, E-100 HEAVY KING, E-101/102/105 BETA, E-123 OMEGA, Eggman, FREEZER, John 117, Metal sonic, ORBOT Y CUBOT, Shard, Silver, Tails, Ultron).
- .obsidian: 16 plugins dirs listados + dataview instalado; 26 paquetes en plugins/.
- HOME.md presente. graph.json 0 bytes → Graph View SIN persistencia (coincide con ESTADO_FINAL: grafo pobre, requiere apertura manual).
- generar_grafo.py existe pero falla (ver Seguridad/Pruebas).

## Notion — inventario
- THE EGG-NETWORK (2eeb38a4): 42 hijos — 3 child_database (ARCHIVO EVOLUCION, RADAR TEMPORAL, Active Recall), 5 child_page, 4 callout, 2 column_list, 2 toggle, 6 paragraph, 3 numbered_list_item, headings, 2 link_to_page.
- Bases hijas directas: ARCHIVO DE EVOLUCION (9dfb38a4, dup 2f5b38a4), RADAR TEMPORAL (2f0b38a4), Active Recall Zettel Cards.
- BD prioritarias (original vs duplicado 3d2b): CENTRAL ACADmICA 95eb38a4 (5 filas) / 3d2b38a4 (5 filas); PIPELINE 033b38a4 (1) / 3d2b38a4 (dupes); C1 19ab38a4 (9) / 3d2b38a4; LOGISTICA FINANCIERA 3e5b38a4 (1) / 3d2b38a4; MONITOR INTEGRIDAD cd1b38a4 (1) / 3d2b38a4; BDVEDA EVIDENCIAS 530b38a4 (0) / 3d2b38a4; HARDWARE 2e4b38a4 (0) / 3d2b38a4; ARSENAL 2f0b38a4 (6); ORDEN BATALLA 5dbcdb21 (4); INTERFERENCIA 0ec536d9 (0); RADAR 2f0b38a4 (2).
- BDs VACIAS: EVIDENCIAS, HARDWARE, INTERFERENCIA. RADAR: 2. FINANCIERA: 1. C1: 9.
- Nombres de BD con mojibake/emojis degradados (ej. 'RADAR TEMPORAL DE LA FLOTA' con char roto, 'LOGISTICA' con acento).
- Existencia de universe paralelo: misma BDs duplicadas bajo 3d2b38a4 → requiere decision (consolidar o archivar).

## Todoist — inventario
- Proyectos: Inbox (inbox_project:true), Universidad, Aleman, Estudio, Habitos — todos vistos como list/creator, sin compartir.
- Tareas: 11 total. Universidad=11, Inbox=0, Aleman=0, Estudio=0, Habitos=0.
- Sin fecha: 10. Con fecha: 1 (Export Gmail academico, 2026-11-30, p1). Vencidas hoy: 0.
- Ejemplos: 'Revisar plan de estudios', 'Export Gmail academico', 'Lenguaje: Friso en grupos', 'Religion: Trabajo Puente Creativo'.
- Etiquetas/filtros: NO inspeccionados (endpoint /labels y /filters no consultado). NO VERIFICADO.

## Integraciones
- MCP activos: filesystem, memory, exa, context7 (Pinterest ON, 4).
- MCP OFF: notion, todoist, obsidian, obsidian-fs, google-drive, gmail, outlook, supabase, postgres, sqlite, docker, github, puppeteer, etc. (25 OFF).
- APIs directas verificadas hoy: Notion 200 OK (bot opencode), Todoist 200 OK (results+next_cursor).
- Syncthing: carpeta .stfolder presente en boveda → probable solapamiento padre/vault SIN resolver (ESTADO_FINAL).

## Seguridad
- opencode.json: env con OPENAPI_MCP_HEADERS (Notion Bearer ntn_…), todoist API_KEY (hex 40), youtube API_KEY, elevenlabs sk_, 21st_sk_ — existencia y estado funcional; NO se imprimen valores.
- obsidian-local-rest-api/data.json: apiKey presente (tipo string), port 27124, insecurePort 27123, enableInsecureServer (revisar valor), enableSignedUrls, crypto.
- .gitignore: cubre *token*.json, *token*.txt, .opencode/auth.json. NO cubre opencode.json explicitamente (mitigado: no esta dentro del repo).
- .obsidian NO en .gitignore (boveda sin .git → sin riesgo actual de indexar workspace.json con tokens? Ninguno en workspace.json).
- 15 archivos cifrados 0 bytes: intencionales (cifrado MELD/Sham? NO VERIFICADO plugin que los genera).

## Plugins (decisiones)
- ESTADO_FINAL dice 6 instalados; realidad: 26 directorios. Reactivar decision: ¿mantener 22 activos o podar?
- obsidian-kanban y periodic-notes PRESENTES y activos (ESTADO_FINAL insinua retirados): NO se verifico desinstalacion.
- obsidian-git instalado pero boveda sin .git.
- quickadd, smart-connections, notebook-navigator, local-rest-api, homepage presentes.

## Cumplimiento historico (ledger)
- NO VERIFICABLE desde disco: C:\Temp\STAGING_20261004 (CERTIFICACION + hashes) BORRADO (ESTADO_FINAL §4: staging limpiado).
- Fuente unica localizable: C:\Users\Admin\Downloads\e-100-obsidian-plugins-y-omniroute.json (4182 msgs, una sola sesion, agent plan, modelo opencode muse-spark-1.3, .87, ~117M in / 1.09M out tokens).
- read_idx.py: NO localizado (C:\Temp\STAGING_20261004\hashes borrado).
- C-30 (session_id no segmenta): confirmado por info.id unico.
- C-40 (Todoist enabled:false): CONFIRMADO hoy (sigue false).
- C-43 (umbral 75 vs 65): decision documentada en ESTADO_FINAL (75 valido), no re-verificada.
- C-44/C-45 (.ino carro Bluetooth nunca en disco): NO VERIFICADO esta sesion.
- Cadenas 0/24 pobladas, Passwords sin hash, Demo RCS: NO VERIFICADO (dependen de staging borrado).

## Pendientes reales
- C:\Temp\STAGING_20261004 borrado → sin ledger, sin CERTIFICACION, generar_grafo.py roto.
- graph.json vacio → Graph View no persiste.
- Duplicacion de BDs Notion (universo 3d2b38a4).
- BDs vacias: EVIDENCIAS, HARDWARE, INTERFERENCIA.
- Todoist: 10/11 tareas sin fecha; proyectos vacios.
- Syncthing solapamiento padre/vault.
- RCS: demo cronometrada, RNG state, cadenas 0/24, umbral (documentado pero no re-verificado).
- Epic Games MSI 1603 residual (de fuente ESTADO_FINAL).

## Decisiones humanas necesarias (max 10)
1. Recuperar/restaurar C:\Temp\STAGING_20261004 (CERTIFICACION + hashes) o aceptar perdida del ledger C-1..C-46.
2. Consolidar o archivar el universo duplicado de BDs Notion (3d2b38a4-*).
3. Poblar o desactivar BDs vacias (EVIDENCIAS, HARDWARE, INTERFERENCIA).
4. Corregir generar_grafo.py (path hardcoded a staging) y regenerar grafo/HTML.
5. Reactivar Graph View / fix graph.json vacio si se desea persistencia.
6. Anadir fechas a las 10 tareas Todoist sin fecha y distribuir en proyectos.
7. Rotar tokens (Notion ntn_..., Todoist hex40) al haber sido expuestos en MD y opencode.json.
8. Ampliar .gitignore para cubrir opencode.json y .obsidian/ (defensa).
9. Decidir sobre Syncthing (excluir vault o excluir padre).
10. Reabrair MCP Notion/Todoist/Obsidian en OpenCode o documentar como intencionalmente OFF.

## Siguiente fase priorizada
- Restaurar staging desde backup o export; reparar generar_grafo.py; luego consolidacion de BDs Notion duplicadas.
