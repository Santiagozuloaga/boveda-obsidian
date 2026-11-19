# Hooks — Guía General (E-100)

Índice y referencia rápida de todos los hooks documentados en esta carpeta.

---

## ¿Qué es un Hook?

Un **hook** es un disparador automático: ejecuta código cuando ocurre un evento específico, sin intervención manual.

| Evento típico | Acción automática |
|---|---|
| `SessionStart` | Inicializar estado, cargar config |
| `UserPromptSubmit` | Enriquecer contexto, validar prompt |
| `PreToolUse` | Bloquear/alertar antes de ejecutar herramienta |
| `PostToolUse` | Lint, formatear, guardar side-effects |
| `Stop` / `SubagentStop` | Persistir memoria, limpiar |
| `command:new` / `command:reset` | Guardar sesión anterior |

---

## Hooks Disponibles

### 1. Session Memory Hook (`HOOK.md`)
**Archivo:** `HOOK.md` — Guía completa
**Eventos:** `command:new`, `command:reset`

Guarda el contexto de la sesión al hacer `/new` o `/reset`:
- Busca la sesión anterior
- Extrae los últimos N mensajes (default: 15)
- Genera slug: timestamp o LLM-descriptivo (`llmSlug: true`)
- Guarda en `<workspace>/memory/YYYY-MM-DD-HHMM.md`

Configuración:
```json
{
  "hooks": {
    "internal": {
      "entries": {
        "session-memory": {
          "enabled": true,
          "messages": 25,
          "llmSlug": true
        }
      }
    }
  }
}
```

---

### 2. Components Hooks (`components-hooks.md`)
**Archivo:** `components-hooks.md` — Tabla de componentes y eventos

Wiring en `packages/omo-codex/plugin/hooks/hooks.json`. Cada hook ejecuta:
```
node "${PLUGIN_ROOT}/components/<c>/dist/cli.js" hook <event>
```

| Componente | Eventos Codex | Prueba observable |
|---|---|---|
| `rules` | SessionStart, UserPromptSubmit, PostToolUse `apply_patch`, PostCompact | `additionalContext` con body de regla; cache en `$PLUGIN_DATA/sessions/<id>.json` |
| `ultrawork` | UserPromptSubmit | `<ultrawork-mode>` solo si prompt matchea `/ultrawork|ulw/i` |
| `ulw-loop` | UserPromptSubmit, PreToolUse `create_goal` | Steer JSON; `permissionDecision:"deny"` si keys extra en `create_goal` |
| `comment-checker` | PostToolUse (write/edit/apply_patch) | Warning si archivo tiene comentarios prohibidos |
| `lsp` | PostToolUse (write/edit/apply_patch), PostCompact | LSP diagnostics como `additionalContext` |
| `start-work-continuation` | Stop, SubagentStop | `{"decision":"block",...}` solo si hay estado de continuación |
| `git-bash` | PreToolUse `Bash`, PostCompact | Windows: reminder + marker `$PLUGIN_DATA/git-bash-reminder/<id>.seen` |
| `telemetry` | SessionStart | PostHog event o archivo diagnóstico |
| `bootstrap` | SessionStart | `BOOTSTRAP_RESTART_NOTICE` en primer run |

**Tier de pruebas:**
- **Unit:** `hook-unit-probe.sh` — evento sintético → `dist/cli.js`, assert stdout/disk
- **Live:** `app-server-drive.sh --plugin` — turno real, assert `hook/completed`

---

### 3. Events Hooks (`events-hooks.md`)
**Archivo:** `events-hooks.md` — Implementación interna (err-code, AjvPack)

Código de utilidades para manejo de errores y validación de esquemas en eventos:
- `createError` — wrapper con código y props
- `AjvPack` — validación de esquemas con Ajv

---

### 4. Webhooks Plugin (`webhooks.md`)
**Archivo:** `webhooks.md` — Plugin de entrada HTTP autenticada

Permite que sistemas externos (Zapier, n8n, CI, servicios internos) creen y manejen TaskFlows.

**Configuración:**
```json5
{
  "plugins": {
    "entries": {
      "webhooks": {
        "enabled": true,
        "config": {
          "routes": {
            "zapier": {
              "path": "/plugins/webhooks/zapier",
              "sessionKey": "agent:main:main",
              "secret": { "source": "env", "provider": "default", "id": "OPENCLAW_WEBHOOK_SECRET" },
              "controllerId": "webhooks/zapier",
              "description": "Zapier TaskFlow bridge"
            }
          }
        }
      }
    }
  }
}
```

**Seguridad:**
- Secret compartido por ruta (preferir SecretRef)
- Rate limiting, límite de requests en vuelo, body size guard
- TaskFlows bound a `sessionKey` → autoridad limitada

**Acciones soportadas (POST JSON):**
`create_flow`, `get_flow`, `list_flows`, `find_latest_flow`, `resolve_flow`,
`get_task_summary`, `set_waiting`, `resume_flow`, `finish_flow`, `fail_flow`,
`request_cancel`, `cancel_flow`, `run_task` (runtimes: `subagent`, `acp`)

---

### 5. Webhook Redirect (`webhook.md`)
**Archivo:** `webhook.md` — Redirect a Scheduled Tasks

> "This page moved to [Scheduled Tasks](/automation/cron-jobs#webhooks)"

Ver `cron-jobs` para documentación actual de webhooks programados.

---

## Estructura de Archivos en Esta Carpeta

| Archivo | Tipo | Descripción |
|---|---|---|
| `hooks.md` | **Este índice** | Guía general (reemplaza al corrupto `hooks.md.bak`) |
| `HOOK.md` | Guía | Session Memory Hook |
| `components-hooks.md` | Referencia | Componentes, eventos, pruebas |
| `events-hooks.md` | Código | Utilidades internas (err-code, AjvPack) |
| `webhooks.md` | Guía | Plugin Webhooks completo |
| `webhook.md` | Redirect | Apunta a Scheduled Tasks |

---

## Referencia Rápida de Eventos Codex

| Evento | CamelCase | Snake_case (hooks.json) | CLI kebab |
|---|---|---|---|
| Session Start | `sessionStart` | `session_start` | `hook session-start` |
| User Prompt Submit | `userPromptSubmit` | `user_prompt_submit` | `hook user-prompt-submit` |
| Pre Tool Use | `preToolUse` | `pre_tool_use` | `hook pre-tool-use` |
| Post Tool Use | `postToolUse` | `post_tool_use` | `hook post-tool-use` |
| Stop | `stop` | `stop` | `hook stop` |
| Subagent Stop | `subagentStop` | `subagent_stop` | `hook subagent-stop` |
| Post Compact | `postCompact` | `post_compact` | `hook post-compact` |

---

## Cómo Añadir un Hook Nuevo

1. Crea componente en `packages/omo-codex/plugin/components/<nombre>/`
2. Implementa `dist/cli.js` que acepte `hook <event>` por stdin/stdout
3. Registra en `hooks.json` con matcher snake_case
4. Prueba con `hook-unit-probe.sh` (unit) y `app-server-drive.sh --plugin` (live)

---

> **Nota:** El archivo original `hooks.md` se corrompió (caracteres UTF-8 `EF BF BD` irrecuperables). Se renombró a `hooks.md.bak`. Esta guía lo reemplaza usando el contenido de los demás archivos de hooks de la carpeta.