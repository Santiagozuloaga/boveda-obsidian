# Plan de Migración OpenCode v1 → v2.0

**Fecha:** 2026-10-18  
**Versión actual:** OpenCode Desktop v1.19.3  
**Versión destino:** OpenCode 2.0 (anomalyco/opencode)  
**Ubicación:** Bóveda Obsidian E-100 — `90 SISTEMA`  
**Estado:** Borrador V01

---

## 1. Resumen Ejecutivo

OpenCode 2.0 es una reescritura estructural completa, no una actualización incremental. La configuración actual de `opencode.json` (v1) **no funciona en v2** sin reescribirla. Este plan detalla los cambios obligatorios, qué se conserva, qué se reescribe y el orden de ejecución para migrar de forma segura sin romper el ecosistema E-100.

**Decisión:** Quedarse en v1 hasta que se disponga de una sesión dedicada. Migración a v2 como proyecto separado con rollback definido.

---

## 2. Estado Actual de tu Configuración v1

### Archivos relevantes
| Ruta | Contenido |
|------|-----------|
| `C:\Users\Admin\.config\opencode\opencode.json` | Config principal (24 KB, 31 MCPs, 5 providers, plugins, permisos, instrucciones) |
| `C:\Users\Admin\.config\opencode\ecc-install-state.json` | Estado de instalación ECC (repoVersion 2.2.2, módulos seleccionados) |
| `C:\Users\Admin\.config\opencode\profiles\` | 3 perfiles: automatizacion, desarrollo, estudio |
| `C:\Users\Admin\.config\opencode\plugins\` | Plugins locales: `btw.js`, `btw.ts`, `ecc-hooks.ts`, `index.ts`, `lib/` |
| `C:\Users\Admin\.config\opencode\node_modules\` | `@opencode-ai/plugin` v1.18.21 instalado |

### MCPs activos (8)
`filesystem`, `memory`, `exa`, `obsidian`, `notion`, `context7`, `todoist`, `obsidian-fs`

### MCPs deshabilitados (23)
`sqlite`, `github`, `puppeteer`, `browser-mcp`, `fetch`, `crawl4ai`, `whatsapp`, `sintrazor`, `gitmcp`, `sequential-thinking`, `gmail`, `google-drive`, `markdownify`, `supabase`, `e2b`, `mem0`, `elevenlabs`, `cloudflare`, `postgres`, `dbutils`, `magic-mcp`, `docker`, `youtube`, `outlook-graph`

### Plugins configurados (5, 4 rotos)
`@opencode-ai/plugin` (instalado), `@xberg-io/opencode-html-to-markdown` (no instalado), `opencode-mermaid-renderer` (no instalado), `opencode-auto-continue` (no instalado), `opencode-omniroute-auth` (no instalado)

### Proveedores configurados
`opencode` (OpenCode Zen), `fcc` (localhost:8082), `gemini`, `qwen`, `omniroute`

### Modelo por defecto
`opencode/nemotron-3-ultra-free`

### Problemas conocidos v1
- 4 de 5 plugins no instalados
- Claves de API en texto plano en `opencode.json` (GitHub PAT, Notion, Exa, Supabase, E2B, Mem0, ElevenLabs, Cloudflare, YouTube, Gemini)
- Estructura `mcp.nombre` obsoleta para v2

---

## 3. Cambios Estructurales v1 → v2.0 (Documentación oficial leída)

| Componente | v1 (actual) | v2.0 (destino) | ¿Compatible? |
|------------|-------------|----------------|--------------|
| MCP servers | `mcp.nombre` directamente | `mcp.servers.nombre` | ❌ No |
| Habilitado | `"enabled": true/false` | `"disabled": true/false` (invertido) | ❌ No |
| Variables de entorno | `"env": {...}` | `"environment": {...}` | ❌ No |
| Proveedores | `"provider": {...}` (singular) | `"providers": {...}` (plural) | ❌ No |
| Campo `npm` en providers | Sí | No existe | ❌ No |
| Permissions | Objeto plano (`read: "allow"`) | Array de reglas (`action`/`resource`/`effect`) | ❌ No |
| Plugins | `"plugin": [...]` | `"plugins": [...]` (objeto con opciones) | ❌ No |
| `$schema` | `https://opencode.ai/config.json` | Mismo | ✅ Sí |
| AGENTS.md / instrucciones | `instructions` | `instructions` | ✅ Sí |
| Secrets | Texto plano en JSON | `{env:NAME}` o `{file:ruta}` | ❌ Debe migrar |
| Plugins locales | Carpeta `plugins/` | `~/.jcode/plugins/` (otro sistema) | ❌ No aplica |

---

## 4. Plan de Migración Paso a Paso

### Fase A — Preparación (sin tocar nada aún)

1. **Respaldar configuración actual**
   - Copiar `C:\Users\Admin\.config\opencode\opencode.json` a `opencode.v1.backup.json`
   - Copiar `ecc-install-state.json` y perfiles
   - Exportar lista de MCPs activos con `opencode mcp list` (si funciona)

2. **Documentar secretos actuales**
   - Identificar todas las claves en texto plano en `opencode.json`
   - Preparar variables de entorno de Windows o archivos `.env` externos
   - Nunca guardar secretos en el nuevo JSON de v2

3. **Verificar requisitos de Windows**
   - OpenCode 2.0 CLI Windows x64: `https://opencode.ai/update/api/latest/cli/opencode/opencode-windows-x64.zip`
   - Desktop Windows x64: `https://opencode.ai/download/stable/windows-x64-nsis`
   - Node.js necesario para MCP servers tipo `npx`

### Fase B — Instalación v2.0 (en paralelo, sin desinstalar v1)

1. **Instalar CLI v2.0**
   ```powershell
   npm install -g @opencode/cli
   ```
   O descargar binario directo desde la URL de actualización.

2. **Instalar Desktop v2.0 (opcional)**
   - Descargar `.exe` desde `/download/stable/windows-x64-nsis`
   - Instalar junto a v1.19.3 (no desinstalar aún)

3. **Verificar instalación**
   ```powershell
   opencode --version
   opencode mcp list
   ```

### Fase C — Reescribir configuración v2.0

Crear nuevo `opencode.json` con estructura v2.0:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "opencode/nemotron-3-ultra-free",
  "shell": "powershell",
  "update": "notify",
  "instructions": [
    "Mǟ�'ǽ�'���TODO CANARY OBLIGATORIO: En CADA respuesta debes mencionar 'Admin'.",
    "REGLA DE MEMORIA: Si el usuario pregunta por configuraciones pasadas, revisa el MCP memory o sqlite antes de responder.",
    "REGLA DE HERRAMIENTAS: Usa sequential-thinking para tareas complejas de desarrollo antes de escribir código.",
    "REGLA DE ENTORNO: Esta PC tiene 12GB de RAM. Evita ejecutar múltiples procesos pesados simultáneamente."
  ],
  "mcp": {
    "timeout": {
      "startup": 30000,
      "catalog": 30000,
      "execution": 43200000
    },
    "servers": {
      "filesystem": {
        "type": "local",
        "command": ["C:\\Program Files\\nodejs\\node.exe", "C:\\Users\\Admin\\AppData\\Roaming\\npm\\node_modules\\@modelcontextprotocol\\server-filesystem\\dist\\index.js", "C:\\Users\\Admin\\Downloads"],
        "disabled": false,
        "environment": {}
      },
      "memory": {
        "type": "local",
        "command": ["C:\\Program Files\\nodejs\\node.exe", "C:\\Users\\Admin\\AppData\\Roaming\\npm\\node_modules\\@modelcontextprotocol\\server-memory\\dist\\index.js"],
        "environment": {
          "MEMORY_FILE_PATH": "C:\\Users\\Admin\\.config\\opencode\\memory.jsonl"
        },
        "disabled": false
      },
      "exa": {
        "type": "local",
        "command": ["C:\\Program Files\\nodejs\\node.exe", "C:\\Users\\Admin\\AppData\\Roaming\\npm\\node_modules\\exa-mcp-server\\dist\\stdio.cjs"],
        "environment": {
          "EXA_API_KEY": "{env:EXA_API_KEY}"
        },
        "disabled": false
      },
      "obsidian": {
        "type": "local",
        "command": ["node", "C:/Users/Admin/AppData/Roaming/npm/node_modules/mcp-obsidian/dist/index.js", "C:\\Users\\Admin\\Downloads\\syn\\Mente Maestra E-100"],
        "disabled": false
      },
      "notion": {
        "type": "remote",
        "url": "https://api.notion.com/mcp",
        "oauth": false,
        "headers": {
          "Authorization": "Bearer {env:NOTION_TOKEN}"
        },
        "disabled": false
      },
      "context7": {
        "type": "remote",
        "url": "https://mcp.context7.com/mcp",
        "oauth": false,
        "headers": {
          "Authorization": "Bearer {env:CONTEXT7_API_KEY}"
        },
        "disabled": false
      },
      "todoist": {
        "type": "local",
        "command": ["node", "C:/Users/Admin/AppData/Roaming/npm/node_modules/todoist-mcp/dist/index.js"],
        "environment": {
          "API_KEY": "{env:TODOIST_API_KEY}"
        },
        "disabled": false
      },
      "obsidian-fs": {
        "type": "local",
        "command": ["node", "C:/Users/Admin/AppData/Roaming/npm/node_modules/@modelcontextprotocol/server-filesystem/dist/index.js", "C:\\Users\\Admin\\Downloads\\syn\\Mente Maestra E-100"],
        "disabled": false
      }
    }
  },
  "providers": {
    "opencode": {
      "models": {
        "nemotron-3-ultra-free": {
          "modelID": "nemotron-3-ultra-free",
          "name": "OpenCode Zen"
        }
      }
    },
    "gemini": {},
    "qwen": {},
    "omniroute": {}
  },
  "permissions": [
    { "action": "read", "resource": "*", "effect": "allow" },
    { "action": "glob", "resource": "*", "effect": "allow" },
    { "action": "grep", "resource": "*", "effect": "allow" },
    { "action": "bash", "resource": "*", "effect": "allow" },
    { "action": "edit", "resource": "*", "effect": "allow" },
    { "action": "write", "resource": "*", "effect": "allow" },
    { "action": "external_directory", "resource": "~/.ssh/**", "effect": "deny" },
    { "action": "external_directory", "resource": "~/.aws/**", "effect": "deny" },
    { "action": "external_directory", "resource": "~/.gnupg/**", "effect": "deny" },
    { "action": "external_directory", "resource": "**/.env", "effect": "deny" },
    { "action": "external_directory", "resource": "**/*.pem", "effect": "deny" },
    { "action": "external_directory", "resource": "**/*.key", "effect": "deny" },
    { "action": "external_directory", "resource": "**/*.p12", "effect": "deny" },
    { "action": "external_directory", "resource": "~/.config/opencode/*.json", "effect": "deny" },
    { "action": "external_directory", "resource": "~/.local/share/opencode/auth.json", "effect": "deny" }
  ],
  "plugins": [
    "@opencode-ai/plugin"
  ],
  "skills": [
    "./team-skills"
  ],
  "commands": {}
}
```

**Notas del nuevo archivo:**
- `provider` → `providers` (plural)
- `enabled` → `disabled` (invertido)
- `env` → `environment`
- Todas las API keys en texto plano → `{env:NOMBRE_VARIABLE}`
- `permissions` es ahora un array de reglas
- `plugin` → `plugins`
- Eliminados: `share`, `small_model`

### Fase D — Variables de entorno de Windows

Crear en PowerShell (persistente):
```powershell
[Environment]::SetEnvironmentVariable("EXA_API_KEY", "tu-clave-aqui", "User")
[Environment]::SetEnvironmentVariable("NOTION_TOKEN", "ntn_...", "User")
[Environment]::SetEnvironmentVariable("CONTEXT7_API_KEY", "ctx7sk-...", "User")
[Environment]::SetEnvironmentVariable("TODOIST_API_KEY", "d076cae34...", "User")
```

O usar archivo `.env` con `{file:ruta}`.

### Fase E — Pruebas y verificación

1. Ejecutar `opencode mcp list` — verificar que los 8 MCPs activos se conecten
2. Ejecutar `opencode` — verificar que inicie sin errores de configuración
3. Probar cada MCP activo individualmente
4. Verificar que los plugins locales de `plugins/` (btw.js, ecc-hooks.ts, etc.) sigan funcionando o migralos a skills de v2

### Fase F — Rollback (si algo falla)

1. Restaurar `opencode.v1.backup.json` a `opencode.json`
2. Desinstalar CLI v2.0: `npm uninstall -g @opencode/cli`
3. Mantener Desktop v1.19.3 como principal
4. Intentar nuevamente después de revisar errores

---

## 5. Qué se conserva y qué se reescribe

| Elemento | Acción | Nota |
|----------|--------|------|
| `opencode.json` | Reescribir completo | Estructura v2 incompatible |
| MCPs activos (8) | Migrar a `mcp.servers` | Reescribir estructura |
| MCPs deshabilitados (23) | Migrar o descartar | Evaluar si se necesitan en v2 |
| Plugins (5) | Reinstalar en v2 | Solo `@opencode-ai/plugin` instalado |
| Plugins locales (`plugins/`) | Revisar compatibilidad | Son de OpenCode v1, pueden no funcionar |
| Perfiles (`profiles/`) | Revisar | Pueden necesitar adaptación |
| `ecc-install-state.json` | No tocar | Estado de ECC, independiente |
| Secretos en texto plano | Mover a variables de entorno | Seguridad obligatoria en v2 |
| AGENTS.md / instrucciones | Conservar | Compatible con v2 |

---

## 6. Riesgos y Mitigaciones

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Perder configuración de MCPs | Alto | Respaldar `opencode.json` antes de tocar |
| Claves expuestas en texto plano | Alto | Mover a `{env:NAME}` antes de migrar |
| Plugins locales dejen de funcionar | Medio | Probar en v2 antes de desinstalar v1 |
| Perder acceso a Notion/Obsidian | Alto | Probar MCP por MCP antes de cerrar v1 |
| No poder hacer rollback | Alto | Mantener v1.19.3 instalado hasta verificar v2 |

---

## 7. Cronología Sugerida

| Día | Acción |
|-----|--------|
| Día 1 | Respaldar configuración, documentar secretos, preparar variables de entorno |
| Día 2 | Instalar CLI v2.0 en paralelo, escribir nuevo `opencode.json` |
| Día 3 | Probar MCPs activos uno por uno, verificar plugins locales |
| Día 4 | Si todo funciona, desinstalar v1 o mantener en paralelo; si falla, rollback |

---

## 7. Checklist Final (antes de declarar éxito)

- [ ] `opencode.json` válido según esquema v2
- [ ] 8 MCPs activos conectados (`opencode mcp list`)
- [ ] No hay claves API en texto plano en el archivo
- [ ] `opencode` inicia sin errores
- [ ] Plugins críticos funcionan
- [ ] Backup de v1 guardado en ubicación segura
- [ ] Documentación de migración actualizada

---

**Nota final:** No desinstales OpenCode v1.19.3 hasta que hayas verificado que v2.0 funciona completamente con tus 8 MCPs activos y tu ecosistema E-100 (Notion, Obsidian, Todoist). Mantén ambas versiones en paralelo durante la transición.

---
*Generado automáticamente basado en documentación oficial de OpenCode v2.0 (opencode.ai/v2/docs) y configuración actual observada.*