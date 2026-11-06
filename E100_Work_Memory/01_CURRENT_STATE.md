# 01_CURRENT_STATE.md — Estado Actual E-100

**Fecha de verificación:** 5 de noviembre de 2026  
**Última sesión:** Reanudación y ejecución real — Fases 1, 2, 3, 4, 5 del protocolo E-100

## Estado general

El ecosistema E-100 está operativo como línea base de auditoría. OpenCode v2.2.5 activo, bóveda commitada y pusheada (commit `5bf28e7`), Notion y Todoist APIs verificadas vía HTTP directa, informes de auditoría creados, memoria de trabajo creada, registro maestro de incidencias NITRO creado, 3 pruebas E2E pasadas.

## MCPs de OpenCode v2.2.5 (estado actual)

| MCP | Estado | Recursos | Templates | Notas |
|-----|--------|----------|-----------|-------|
| context7 | Conectado | 0 | 0 | Responde vía execute |
| exa | Conectado | 1 | 0 | tools_list disponible |
| filesystem | Conectado | 0 | 0 | Responde vía execute |
| memory | Conectado | 1 | 0 | knowledge-graph disponible |
| obsidian | Conectado | 0 | 0 | Responde vía execute |
| obsidian-fs | Conectado | 0 | 0 | Responde vía execute |
| notion | Conectado | 0 | 0 | MCP error HTTP 400 (invalid_request_url), pero API HTTP directa funciona (200) |
| todoist | Conectado | 0 | 0 | Responde vía execute |
| gmail | Deshabilitado | — | — | Token OAuth renovado, API funciona vía HTTP directa (200) |
| google-drive | Deshabilitado | — | — | Token presente, no probado |
| outlook-graph | Deshabilitado | — | — | Token presente, no probado |
| Otros 15 | Deshabilitados | — | — | No probados |

**Nota:** El CLI v2.2.5 reporta "No MCP servers configured" al leer opencode.json, pero los MCP responden vía `tools.opencode.list_mcp_resources`. Hay una discrepancia entre la CLI y el runtime.

## Riesgos actuales (NITRO)

| ID | Riesgo | Prioridad | Estado | Bloqueo |
|----|--------|-----------|--------|---------|
| NITRO-001 | Batería 43% de salud, sensor defectuoso | P0 | Sin cambios (queda como está por decisión de Admin) | No |
| NITRO-002 | Repositorio GitHub público con material sensible | P0 | Sin cambios (queda como está por decisión de Admin) | No |
| NITRO-003 | Syncthing con celular no verificable | P1 | Pendiente de verificación manual de Admin | Sí — sin acceso al celular |
| NITRO-004 | Tokens Gmail/Calendar expiran en 7 días | P1 | Tokens renovados (31-oct-2026) | No |
| NITRO-005 | Plugins de OpenCode v1 incompatibles con v2 | P2 | Verificados parcialmente (5/8 MCPs conectan en v2.0) | No |
| NITRO-006 | Rutas obsoletas en Obsidian | P2 | **RESUELTA Y VERIFICADA** (4 archivos, commit `7323247`) | No |
| NITRO-007 | Automatizaciones Grok/Vibe no verificables | P2 | Bloqueada (sin acceso a paneles) | Sí — sin acceso a paneles |
| NITRO-008 | Notion papelera no accesible por API | P2 | Bloqueada (limitación de API) | Sí — limitación de Notion API |
| NITRO-009 | Google Calendar API deshabilitada en proyecto | P2 | Detectada (403 accessNotConfigured) | Sí — requiere habilitación en Google Cloud Console |
| NITRO-010 | OpenCode CLI v2.2.5 no lee MCPs de opencode.json | P2 | Detectado (CLI dice "No MCP servers configured", pero execute responde) | Sí — discrepancia CLI vs runtime |

## Bloqueos

- Syncthing celular: no accesible desde este entorno, requiere verificación manual de Admin
- Notion papelera: no accesible por API (limitación de Notion)
- Automatizaciones Grok/Vibe: 0 de 9 verificables (sin acceso a paneles)
- Notion MCP: error HTTP 400 invalid_request_url (configuración del servidor MCP)
- Google Calendar API: deshabilitada en proyecto de Google Cloud (requiere habilitación en Console)
- OpenCode CLI v2.2.5: no lee MCPs de opencode.json (discrepancia con runtime)

## Próximo paso

Verificar Syncthing en celular (pendiente de Admin) o ejecutar pruebas E2E adicionales autorizadas.
