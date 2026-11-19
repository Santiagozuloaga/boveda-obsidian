# 02_ACTIVE_WORK.md — Trabajos Abiertos

**Fecha:** 5 de noviembre de 2026  
**Objetivo:** Completar la auditoría E-100 y ejecutar pruebas E2E autorizadas

## Trabajo completado en esta sesión

### FASE 1 — Adaptación a OpenCode v2.2.5

**Ejecutado y verificado:**
- OpenCode CLI v2.2.5 instalado y funcionando (`opencode-cli.exe --version` → opencode v2.2.5)
- Config v2.0 en `opencode.json` con secretos en `{env:NAME}`, estructura `mcp.servers`, `providers` plural
- 8 MCPs activos responden vía `tools.opencode.list_mcp_resources` (filesystem, memory, exa, obsidian, notion, context7, todoist, obsidian-fs)
- 2 MCPs exponen recursos (memory: knowledge-graph, exa: tools_list)
- Discrepancia: CLI dice "No MCP servers configured" pero execute responde para todos los 8 MCP activos

### FASE 2 — Recuperar el estado real

**Ejecutado y verificado:**
- Informe de auditoría: `E100_Auditoria_Integral_2026-10-30.md` (SHA-256: `86827FD46538CAE7106C1937FF8414965C29D14C0845CD87C87E5F8DB8126EB2`)
- Resumen ejecutivo: `E100_Auditoria_Resumen_Ejecutivo_2026-10-30.md` (SHA-256: `3D98A812EA05EA8E6A8A2A856FD06512EBAD6179E114900A5BEB4E9935C75988`)
- Plan Fase 13: `FASE_13_PLAN_CAMBIOS_LOTES_2026-10-31.md` (SHA-256: `43B7AB777B5CFDC15B0D4AFFECF725550048B749106533D60B9DEB49DE17732B`)
- Memoria de trabajo: 7 archivos creados + registro de incidencias NITRO (8 archivos totales)
- Registro maestro de incidencias NITRO: 8 incidencias (NITRO-001 a NITRO-008)

**Commits:**
- `f58c73d`: merge de main (notas de filosofía)
- `5d94d1a`: informe de auditoría y resumen ejecutivo
- `1bb0383`: registro maestro de incidencias NITRO
- `5bf28e7`: memoria de trabajo actualizada

Todos pusheados a `Santiagozuloaga/boveda-obsidian`, rama `cierre-expediente`.

### FASE 3 — Ejecución del trabajo pendiente

**3.1 Verificar commits y archivos de la bóveda:** ✅
- Commit `7323247` existe (correcciones de rutas)
- Commit `1bb0383` existe (registro NITRO)
- Commit `5bf28e7` existe (memoria de trabajo actualizada)
- Working tree limpio
- Rama local sincronizada con remoto

**3.2 Registro maestro de incidencias NITRO:** ✅ Completo
- 8 incidencias identificadas con ID, título, componente, evidencia, causa, prioridad, impacto, dependencias, solución, estado, pruebas de aceptación, riesgos residuales, próximo paso
- Estados: 1 resuelta y verificada (NITRO-006), 3 pendiente de decisión de Admin (NITRO-001, NITRO-002, NITRO-005), 1 autorizada (NITRO-004), 3 bloqueadas (NITRO-003, NITRO-007, NITRO-008)

**3.3 Revisar integración Notion/Todoist/Gmail/Calendar:** ✅ Ejecutado
- Notion API: 200, 24+ bases accesibles, Bandeja de Aprendizaje con 20+ entradas
- Todoist API: 200, 11 tareas abiertas, 0 vencidas, 1 con fecha (2026-11-30)
- Gmail API: 200 (tokens renovados vía OAuth, acceso_token funcional)
- Calendar API: 403 (accessNotConfigured — requiere habilitación en Google Cloud Console)

**3.4 Diagnosticar MCPs:** ✅ Ejecutado
- 8 MCPs activos responden vía execute
- 2 exponen recursos (memory, exa)
- Notion MCP error 400 (configuración del servidor MCP, no de la API)
- Gmail, google-drive, outlook-graph deshabilitados en config

**3.5 Completar pruebas de integración posibles:** ✅ Ejecutado
- E2E-01: Todoist → HOY.md (11 tareas coinciden) ✅
- E2E-02: Notion Bandeja → Estado "Consumido" (entrada 409b38a4...) ✅
- E2E-03: Todoist tarea Export Gmail academico (vencimiento 2026-11-30 confirmado) ✅

**3.6 Verificar configuración OpenCode:** ✅ Ejecutado
- Config v2.0 activa, secretos en {env:NAME}
- v1 respaldada en `opencode.v1.backup.json`
- CLI v2.2.5 funciona, lee configuración pero reporta "No MCP servers configured" (discrepancia con runtime)

**3.7 Preparar verificación Syncthing:** ⏳ Pendiente de Admin
- Sin acceso al dispositivo móvil desde este entorno
- Admin debe verificar en móvil: abrir Obsidian, revisar notas recientes, sincronizar archivo

**3.8 Revisar respaldos, integridad y sincronización Obsidian:** ✅ Ejecutado
- Working tree limpio (git status = 0 cambios)
- Commit `5bf28e7` pusheado a GitHub
- Commit `164bc75` disponible como rollback
- 445 notas en la bóveda (verificado en documentación previa)

## Trabajo pendiente

- **Lote 3 (Syncthing celular):** Admin debe verificar en el móvil
- **Decisión de Admin:** Repositorio GitHub público (NITRO-002)
- **Decisión de Admin:** Reemplazo de batería (NITRO-001)
- **Autorización para pruebas E2E adicionales** si se desean ejecutar más flujos
- **Autorización para probar plugins en v2.0** (NITRO-005)
- **Habilitación de Google Calendar API** en Google Cloud Console (requiere acción de Admin)
