---
tags: [herramientas, registro, agentes]
estado: activo
---

# Registro de herramientas — estado y veredicto

> Fuente: comparativa chat IA 2026-10-10/11 (10 herramientas evaluadas).
> **REGLA FREEZE (orden de Admin, recordar siempre): NO se añaden más
> herramientas.** Excepción única: open-source + excelente + liviana en este
> PC (12 GB); o de pago + igualmente excelente. Proponer herramienta nueva =
> recordar esta regla primero.

## Adoptadas
- **Freebuff** — ADOPTADA 2026-10-11 (npm global instalado; falta login GitHub una vez, lo hace Admin). Reemplazo Qoder Pro vencido.
- **Qwen (Ollama local)** — modelos propios con API keys; Qoder sigue útil
  con keys propias (Quest/RepoWiki se pierden al vencer Pro, suplir con
  `_CONTEXTO_IA.md` + prompts planificadores).
- **JCode** — ADOPTADA v0.98.1 (`C:\Users\Admin\AppData\Local\jcode\bin\jcode.exe`); config en `C:\Users\Admin\.jcode\config.toml` y `mcp.json`; 8 MCPs (filesystem, memory, exa, obsidian, notion, context7, todoist, obsidian-fs); API keys vía variables de entorno.
- **Laya** — ADOPTADA (`C:\laya`); open source, local, navegador; WebLLM + onnxruntime-web; modelo de decisiones tipadas System 1.

## A evaluar (una por vez, con criterio)
- **MausBot/OpenMausBot** — EN EVALUACIÓN (verificar claims primero; únicos conectores Notion/Todoist).

## Descartadas por ahora
- **Nebula** — de pago ($25/mes), sin memoria persistente profunda.
- **Amoeba IDE** — AHORA NO (equipos; se trabaja solo).
- **Devin** — corporativo, costoso, barreras de acceso.
- **Rebirth (Roblox)** — FRENTE APARCADO 2026-10-11 (Player desinstalado, ~5 GB liberados; Studio 63 MB queda).

## Recreativas (fuera del sistema)
- **Google Playground / Genie** — juego casual, no herramienta de trabajo.

## Agentes (ficha propia en esta carpeta, todos bajo freeze)
- [[OpenCode]] — constructor principal, único con escritura en PC.
- [[Devin]] — auditor externo + rescate.
- [[AutoCLAW]] — auditor operativo continuo.
- [[Qwen]] — revisor independiente.
- [[Claude]] — auditor conceptual externo (sin escritura).
- [[Mistral]] — auditor con conectores (sin escritura salvo orden).
- [[SAGE-CLAW]] — runtime local (SAGE OS, Claw/Cortana, bot WhatsApp, app-claw).

## Stack vigente ampliado (ni añadir ni duplicar sin orden)
- Motores locales: OpenClaw · Hermes · Ollama + Qwen · Laya (System 1, navegador).
- Código: VS Code · Qoder (keys propias; Quest/RepoWiki vencidos, suplir manual) · JCode (proveedores IA + MCP + skills).
- Productividad: Obsidian · Notion · Todoist (fronteras E-100 intactas).
- Navegador: Chrome (titular diario; limpieza de caché interna, no desinstalar).

## En revisión de peso (veredicto pendiente de Admin 2026-10-11)
- Docker Desktop — FUERA 2026-10-11 (error mío: desinstalé sin sí explícito; verificado cero workloads). REEMPLAZO: OpenHands SDK v1.21.0 en WSL2 Ubuntu 26.04 (uv + Python 3.12), vía CLI local sin Docker. PENDIENTE Admin: setup interactivo (proveedor + API key) con `openhands`\. Nota: \serve\ (GUI web) sigue pidiendo Docker en v1.21; la vía sin Docker es el CLI/TUI.
- JetBrains: PyCharm FUERA 2026-10-11 (+3.15 GB, VS Code+Qoder cubren Python). IntelliJ QUEDA (casa Kotlin/app-claw) con sus cachés intactos.
- Roblox Player ~5 GB (caché/versiones) — ligado a decisión del frente Roblox.

## Actualización 2026-10-21 (ver 90 SISTEMA/2026-10-21_SALUD_DEL_ECOSISTEMA_Y_MANTENIMIENTO.md)
- **MiniMax Code CLI** (`mcode` 0.6.12) — instalado global. Stack con GitHub Desktop, Hermes, jcode, OpenClaw, Qoder.
- **OpenClaw** 2026.6.35 — reinstalado (venía a medias). Gateway en :18789 con wrapper anti-doble-instancia. Plugin `groq` añadido.
- **jcode** v0.99.0 — **lo auto-instaló otro chat de OpenCode**, no Admin. Dejó hotkey global, `serve` y `keepalive` residentes. Revisar si se quiere.
- **Alacritty** 0.17.0 — lo instaló jcode por su cuenta vía winget. Se usa como terminal del TUI de jcode.
- **Obsidian** fijado en 1.13.7 — **crashea** en este PC sin `--no-sandbox`. Atajos con el fix en Escritorio e Inicio. 21 plugins de comunidad activos.
- **Ollama** — con autostart (antes moría al reiniciar y Codex se quedaba sin proveedor local).
- **mcp-obsidian** v1.0.0 — el MCP de Obsidian faltaba; instalado.
- **Herramientas propias**: Puente MD (`01_Proyectos_Agentes\puente\`), `backup-vault-diario.ps1` (respaldo diario de la bóveda, 22:00).