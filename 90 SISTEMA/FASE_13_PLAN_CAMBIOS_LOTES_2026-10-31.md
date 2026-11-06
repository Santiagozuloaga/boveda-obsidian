# FASE_13_PLAN_CAMBIOS_LOTES_2026-10-31.md

**Fecha:** 31 de octubre de 2026  
**Usuario:** Admin  
**Fase:** 13 — Preparación de cambios futuros (Paquete Maestro E-100)  
**Estado:** Plan documentado, cambios NO ejecutados (pendiente de autorización por lote)

---

## 1. Principio rector

> "Solo después de entregar el informe y recibir autorización explícita: planificar cambios en lotes pequeños; crear copias de seguridad verificables; probar primero en un área no crítica; comprobar integridad y sincronización; documentar resultados; detenerse si una prueba falla; no ejecutar un lote posterior hasta validar el anterior."

---

## 2. Estado actual de MCPs (verificado en opencode.json v1)

### MCPs HABILITADOS (8)

| MCP | Comando | Ruta/Target | Estado |
|-----|---------|-------------|--------|
| filesystem | node @modelcontextprotocol/server-filesystem | C:\Users\Admin\Downloads | ✅ Activo |
| memory | node @modelcontextprotocol/server-memory | memory.jsonl | ✅ Activo |
| exa | node exa-mcp-server | stdio.cjs | ✅ Activo |
| obsidian | node mcp-obsidian | Bóveda E-100 | ✅ Activo |
| notion | npx @notionhq/notion-mcp-server | API remota | ✅ Activo |
| context7 | remote https://mcp.context7.com/mcp | API remota | ✅ Activo |
| todoist | node todoist-mcp | API remota | ✅ Activo |
| obsidian-fs | node server-filesystem | Bóveda E-100 | ✅ Activo |

### MCPs DESHABILITADOS (23)

sqlite, github, puppeteer, browser-mcp, fetch, crawl4ai, whatsapp, sintrazor, gitmcp, sequential-thinking, gmail, google-drive, markdownify, supabase, e2b, mem0, elevenlabs, cloudflare, postgres, dbutils, magic-mcp, docker, youtube, outlook-graph

### Tokens actualizados (esta sesión)

| Servicio | Archivo | Estado | Expiración |
|----------|---------|--------|------------|
| Gmail | google-tokens-gmail.json | ✅ Tokens renovados | 7 días (refresh_token_expires_in: 604799s) |
| Google Drive | google-tokens-drive.json | ⚠️ Pendiente de verificación | — |
| Outlook/Graph | ms-graph-tokens.json | ✅ Tokens presentes | — |
| Notion | OPENAPI_MCP_HEADERS en opencode.json | ✅ Activo | — |
| Todoist | API_KEY en opencode.json | ✅ Activo | — |

---

## 3. Plan de cambios por lotes (lotes pequeños, reversibles)

### LOTE 1 — Verificación de MCPs críticos (lectura solamente)

**Objetivo:** Verificar que los 8 MCPs activos responden correctamente.

**Pasos:**
1. Ejecutar `opencode mcp list` para listar servidores conectados
2. Probar MCP filesystem (leer directorio de Descargas)
3. Probar MCP memory (leer memory.jsonl)
4. Probar MCP exa (búsqueda de prueba)
5. Probar MCP obsidian (listar notas de la bóveda)
6. Probar MCP notion (listar bases de datos)
7. Probar MCP context7 (consulta de documentación)
8. Probar MCP todoist (listar tareas)
9. Probar MCP obsidian-fs (leer archivo de la bóveda)

**Criterio de aceptación:** Todos los 8 MCPs responden sin error.

**Rollback:** No aplica (solo lectura).

**Autorización requerida:** Sí (lectura de configuración y pruebas de conectividad).

---

### LOTE 2 — Prueba de plugins críticos de OpenCode v2.0 (en entorno aislado)

**Objetivo:** Verificar compatibilidad de plugins locales antes de considerar migración definitiva a v2.0.

**Plugins a probar:**
- @opencode-ai/plugin (instalado en v1, versión 1.18.34 en .opencode del proyecto)
- opencode-mermaid-renderer (no instalado en v1)
- opencode-auto-continue (no instalado en v1)
- opencode-omniroute-auth (no instalado en v1)

**Pasos:**
1. Crear copia de seguridad de configuración v1 actual
2. Instalar OpenCode v2.0 en entorno paralelo (no desinstalar v1)
3. Probar cada plugin individualmente
4. Documentar resultados

**Criterio de aceptación:** Los plugins críticos funcionan en v2.0 o se documentan como incompatibles.

**Rollback:** Restaurar opencode.v1.backup.json, desinstalar CLI v2.0.

**Autorización requerida:** Sí (instalación de software).

---

### LOTE 3 — Verificación de Syncthing con celular (acción de Admin)

**Objetivo:** Confirmar que la sincronización entre PC y celular funciona.

**Pasos (ejecutados por Admin):**
1. Abrir Obsidian en el celular
2. Verificar que aparecen notas recientes (ej. `90 SISTEMA/AUDITORIA_AUTORIA_NOTAS_2026-10-29.md`)
3. Editar una nota pequeña en el PC, esperar, verificar que aparece en el celular
4. Editar una nota en el celular, verificar que aparece en el PC

**Criterio de aceptación:** Un archivo se sincroniza y coincide en ambos lados.

**Rollback:** No aplica.

**Autorización requerida:** Acción manual de Admin, no requiere autorización de OpenCode.

---

### LOTE 4 — Reautorización de tokens Gmail y Calendar (esta sesión completada)

**Objetivo:** Mantener vigentes los tokens de OAuth de Google.

**Estado:** ✅ COMPLETADO esta sesión
- Código de autorización canjeado por tokens de acceso y refresh token
- Tokens guardados en `google-tokens-gmail.json`
- Scope: gmail.modify, gmail.settings.basic, calendar.readonly
- Expiración: 1 hora (access_token), 7 días (refresh_token)

**Próxima acción:** Reautorizar antes de los 7 días cuando el refresh_token expire.

**Autorización requerida:** Admin completó el flujo OAuth en el navegador.

---

### LOTE 5 — Limpieza de rutas obsoletas en Obsidian (pendiente de autorización)

**Objetivo:** Actualizar rutas literales obsoletas en 4 archivos identificados.

**Archivos afectados:**
1. `HOME.md`
2. `90 SISTEMA/Vaultorial_Index.md`
3. `90 SISTEMA/Templater_Vaultorial_Mapping.md`
4. `80 OPERATIVO/07 TABLERO/Control Panel.md`

**Pasos:**
1. Leer cada archivo e identificar rutas literales que apuntan a carpetas renombradas
2. Actualizar rutas a la nueva taxonomía (`20 AREAS/20.01 UNIVERSIDAD/...`, `80 OPERATIVO/...`)
3. Verificar que los enlaces `[[wikilinks]]` siguen resolviendo correctamente
4. Commit de cambios en Git

**Criterio de aceptación:** Todas las rutas literales apuntan a carpetas existentes.

**Rollback:** `git reset --hard e3439b2` (último commit conocido bueno).

**Autorización requerida:** Sí (escritura en la bóveda de Obsidian).

---

### LOTE 6 — Migración definitiva a OpenCode v2.0 (pendiente de autorización)

**Objetivo:** Migrar completamente a v2.0 tras verificar compatibilidad.

**Pasos:**
1. Verificar que LOTE 2 pasó (plugins funcionan en v2.0)
2. Respaldar configuración v1 actual
3. Escribir opencode.json con estructura v2.0 (mcp.servers, providers, environment, permissions array)
4. Mover secretos a variables de entorno de Windows
5. Probar `opencode mcp list` en v2.0
6. Probar `opencode` inicia sin errores
7. Desinstalar CLI v2.0 o mantener en paralelo

**Criterio de aceptación:** v2.0 funciona con todos los 8 MCPs activos.

**Rollback:** Restaurar opencode.v1.backup.json, `npm uninstall -g @opencode/cli`.

**Autorización requerida:** Sí (cambio de configuración principal y desinstalación de software).

---

## 4. Copias de seguridad verificables

| Respaldo | Ruta | Contenido | Fecha | Verificado |
|----------|------|-----------|-------|------------|
| Config OpenCode v1 | `C:\Users\Admin\.config\opencode\opencode.v1.backup.json` | Config completa v1 (31 MCPs, 5 providers, plugins, permisos) | 30-oct-2026 | ✅ Creado |
| Bóveda Obsidian | Commit `e3439b2` en rama `cierre-expediente` | 315 archivos, taxonomía unificada | 30-oct-2026 | ✅ Pusheado a GitHub |
| Tokens Gmail | `C:\Users\Admin\.config\opencode\google-tokens-gmail.json` | access_token, refresh_token, scope | 31-oct-2026 | ✅ Canjeado por API |
| Informe auditoría | `90 SISTEMA/E100_Auditoria_Integral_2026-10-30.md` | SHA-256: 86827FD46538CAE7106C1937FF8414965C29D14C0845CD87C87E5F8DB8126EB2 | 31-oct-2026 | ✅ Creado |
| Resumen ejecutivo | `90 SISTEMA/E100_Auditoria_Resumen_Ejecutivo_2026-10-30.md` | SHA-256: 3D98A812EA05EA8E6A8A2A856FD06512EBAD6179E114900A5BEB4E9935C75988 | 31-oct-2026 | ✅ Creado |

---

## 5. Área de prueba no crítica

**Primera área de prueba:** `90 SISTEMA/` (sistema de gobernanza, no conocimiento crítico)

**Por qué:** Los archivos en `90 SISTEMA/` son de gobernanza y documentación. Cualquier error aquí no afecta el conocimiento profundo de la bóveda ni los datos de usuario.

**Segunda área de prueba:** `80 OPERATIVO/07 TABLERO/` (tableros de espejo, solo lectura mental)

**Por qué:** Son espejos de Todoist/Notion, no contienen datos originales críticos.

---

## 6. Procedimiento de reversión

| Escenario | Acción de reversión | Comando |
|-----------|---------------------|---------|
| Config OpenCode v2.0 falla | Restaurar v1 desde backup | `Copy-Item opencode.v1.backup.json opencode.json -Force` |
| CLI v2.0 causa problemas | Desinstalar CLI v2.0 | `npm uninstall -g @opencode/cli` |
| Cambios en Obsidian fallan | Reset a commit conocido bueno | `git reset --hard e3439b2` |
| Tokens Gmail expiran | Usar refresh_token para obtener nuevos | Flujo OAuth nuevamente |
| Plugin v2.0 incompatible | Volver a v1, desinstalar plugin | Restaurar configuración v1 |

---

## 7. Condiciones de parada (detenerse si falla)

**Detener y NO continuar con el lote siguiente si:**
- Cualquier MCP no responde en LOTE 1
- Cualquier plugin crítico no funciona en v2.0 en LOTE 2
- Un archivo de Obsidian no puede leerse después de actualizar rutas en LOTE 5
- v2.0 no inicia o los MCPs no conectan en LOTE 6

---

## 7. Próximos pasos requeridos (autorización de Admin)

| Lote | Acción | ¿Autorizado? |
|------|--------|--------------|
| 1 | Verificar MCPs activos (`opencode mcp list` + pruebas de conectividad) | Pendiente |
| 2 | Probar plugins en v2.0 (instalación en paralelo) | Pendiente |
| 3 | Verificar Syncthing en celular (acción manual de Admin) | Pendiente |
| 4 | Tokens Gmail/Calendar ya renovados | ✅ Completado |
| 5 | Limpiar rutas obsoletas en Obsidian | Pendiente |
| 6 | Migración definitiva a v2.0 | Pendiente |

---

**SHA-256 del plan de Fase 13:** Pendiente de cálculo tras guardar este documento.

**Regla de oro:** No ejecutar un lote posterior hasta validar el anterior. Detenerse si una prueba falla.
