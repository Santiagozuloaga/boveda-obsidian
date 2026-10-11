---
tipo: sesion-conversacion
fecha: 2026-08-30
proyecto: C:/Users/Admin/Downloads
sesion_id: ses_fac808044ffe8Pcvc9ok3Hzqo2
mensajes: 6
---

# Probar todos los MCPs de OpenCode (@general subagent)

**Fecha:** 2026-08-30 11:27 → 2026-08-30 11:38 | **Mensajes:** 1 usuario / 5 asistente | **Directorio:** `C:/Users/Admin/Downloads/01_Proyectos_Agentes`

## Objetivo inicial
> Sos un agente de prueba. Tu unica mision es **probar cada MCP de OpenCode** y reportar cual funciona y cual no.  ## Pasos exactos a ejecutar  1. **Lee la config actual** de los MCPs:    ```    Get-Content "C:\Users\Admin\.config\opencode\opencode.jsonc" -Raw | ConvertFrom-Json | Select-Object -ExpandProperty mcp    ```  2. **Lista los recursos MCP disponibles** usando la herramienta `list_mcp_resources` (si esta disponible en tu contexto). Si no esta, usa `bash` con este comando para ver que procesos MCP estan corriendo:    ```    Get-Process node -ErrorAction SilentlyContinue | Where-Object {

## Pendientes registrados (0)
- (ninguno)

---
*Importado de opencode.db (solo lectura). Extracto del primer mensaje + conteos; texto completo en historial de la app.*
