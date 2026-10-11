# 2026-10-06 — Configuración IA 3000: OmniRoute + DSH + Claude Code

## Índice

1. [OmniRoute](#1-omniroute)
2. [Claude Code vía OmniRoute](#2-claude-code-vía-omniroute)
3. [DSH (DeepSeek Harness)](#3-dsh-deepseek-harness)
4. [Obsidian](#4-obsidian)
5. [Estado de proveedores](#5-estado-de-proveedores-hoy)
6. [Tareas pendientes](#6-tareas-pendientes)

---

## 1. OmniRoute

- **Gateway local** que unifica +170 proveedores de IA. Sin él no andan Claude Code ni DSH con tu key.
- **Dashboard/API:** `http://localhost:20128` (API: `/v1/models`, `/v1/chat/completions`).
- **Base de datos activa:** `%APPDATA%\omniroute\storage.sqlite` (23 conexiones, 3 keys: Opencode, Claude code, qwen).
- **Arrancado:** `omniroute serve --daemon --no-open` (puerto 20128, escucha).
- **Datos clave:** `~/.config/opencode/opencode.json` → provider `omniroute` (`baseURL`, key en `~/.local/share/opencode/auth.json`).
- **Cmd útil:** `omniroute status`, `omniroute doctor`, `omniroute stop`.
- **Contraseña dashboard:** ninguna set. La ventana pide una API key activa (la misma de auth.json).
- **Error histórico del día:** el CLI creó una base vacía en `C:\Users\Admin\.omniroute` por falta de `DATA_DIR`. Usar siempre `$env:DATA_DIR="$env:APPDATA\omniroute"` antes de comandos del CLI.

## 2. Claude Code vía OmniRoute

- **Settings:** `C:\Users\Admin\.claude\settings.json`:
  - `env.ANTHROPIC_BASE_URL`: `http://localhost:20128/v1`
  - `env.ANTHROPIC_AUTH_TOKEN`: `sk-cc17f5131cd2c7b4-04fdfc-74b1d88c`
  - `env.CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`: `1`
  - `model`: `auto/best-fast`
- **Perfiles generados:** `~/.claude/profiles/<name>/` (30 nombres, ej. `kr-claude-sonnet-4-5`, `cfp-deepseek-ai-deepseek-v4-flash-0731`, `auto-best-fast`).
- **Lanzar con perfil:** `omniroute launch --profile auto-best-fast --api-key "..."`.
- **Verificado:** `claude -p "ok"` y DSH vía mismo gateway responden. Error de `/model auto/best-coding` ignorado con `auto/best-fast` (catalog discovery).
- **Variables locales:** `ANTHROPIC_API_KEY` debe quedar vacía/unset salvo que use gateway.

## 3. DSH (DeepSeek Harness)

- **Instalado:** `dsh` v0.1.5-rc.1, paquete npm `@deepseek-ai/dsh`.
- **Modo:** headless / web / tui / sdk / acp vía `--profile`.
- **Settings:** `~/.dsh/settings.yaml`:
  - `llm-pi-ai.providers.omniroute-deepseek`: `apiKeyEnv: OMNIROUTE_API_KEY`, `baseURL: http://localhost:20128/v1`, modelo activo `cfp/deepseek-ai/deepseek-v4-flash-0731`
  - `agent-default-model`: provider `omniroute-deepseek`, model `cfp/deepseek-ai/deepseek-v4-flash-0731`
- **Variable de entorno:** `OMNIROUTE_API_KEY` guardada a nivel Usuario. Nueva terminal ya la ve.
- **Comando probado:** `dsh --profile headless "Responde con solo la palabra: ok"` → responde.
- **Web UI:** `dsh web` → `http://127.0.0.1:3080` (modelos, workspace, plugins).
- **Models page / API key:** la key de OmniRoute se usa también para `llm-pi-ai` providers.

## 4. Obsidian

- **Bóveda:** `C:\Users\Admin\Downloads\syn\Mente Maestra E-100` (PARA + M.O.C. universitario).
- **Apertura fix:** en Windows + Obsidian 1.13.7, el arranque normal (sin flags) crashea con `0x80000003`. Argumento necesario: `--no-sandbox`.
- **Acceso configurado:** `OneDrive\Desktop\Obsidian - Republica.lnk` → `Obsidian.exe --no-sandbox`. Si tarda, ver plugins pesados (REST API with MCP 6.3s, Kanban 5.5s, Omnisearch 4.2s, Style Settings 3.6s, Smart Connections 3.4s).

## 5. Estado de proveedores (2026-10-06)

| Provider | Estado | Nota |
|----------|--------|------|
| `llm7` | disable | `is_active=0` |
| `kiro` | banned | OAuth expiró 14/09 |
| `opencode-zen` | 403 | solo Opus 5, restricted |
| `openrouter` | 429 cooldown | sin cuota |
| `moonshot` | 402 | credits exhausted |
| `cfp` (DeepSeek) | **OK** | `deepseek-v4-flash-0731` responde |
| `glm`/`zai` | FALLO | comprobado directo: 500 o timeout |
| `auto/best-fast` | **OK parcial** | routing fallback 404→429→200 |

## 6. Tareas pendientes

- [ ] Borrar base duplicada accidental: `C:\Users\Admin\.omniroute\storage.sqlite` y sus `-shm/-wal`. **¡Confirmar antes!**
- [ ] Reconectar Kiro y/orecargar OpenRouter en Providers → volver a Claude completo vía Claude Code.
- [ ] Desabilitar plugins Obsidian pesados para reducir startup.
- [ ] Revisar `dsh web` plugins: Local REST API, Kanban, Omnisearch, Smart Connections.
