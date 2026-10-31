---
type: registro
tags: [e100, mantenimiento, ejecutores, electron, windows, obsidian, openclaw, tareas]
fecha: 2026-10-21
estado: vigente
---

# SALUD DEL ECOSISTEMA Y MANTENIMIENTO — E-100

> Bitácora técnica de los ejecutores: qué estaba roto, por qué y cómo quedó.
> Todo lo de aquí es **verificado por API o por log de Windows**, no por suposición.

---

## 1. EL HALLAZGO PRINCIPAL: ELECTRON CRASHEA EN ESTE PC

**Síntoma:** `0x80000003` (STATUS_BREAKPOINT) dentro del propio `Obsidian.exe`,
en **cada arranque limpio**. Mismo fallo en `GitHubDesktop.exe` (17-10).

**Causa:** el **sandbox de Chromium** falla en esta máquina. No es la app, ni la
bóveda, ni los plugins.

**Lo que se descartó (por eliminación):**

| Sospecha | Cómo se descartó |
|---|---|
| Bóveda, plugins, config, perfil, registro | probado con bóveda vacía y perfil nuevo → seguía |
| Versión | 1.12.7, 1.13.7 y 1.14.4 crasheaban las tres |
| GPU / ANGLE | probado con `--use-angle=swiftshader` |
| Red / actualizador | probado bloqueando GitHub (`--host-resolver-rules`) |
| CPU (AVX2) | **hipótesis falsa**: el campo `Flags` de WMI venía vacío; el i3-1005G1 sí tiene AVX2 |
| Defender, IFEO, DLLs, AppInit_DLLs | sin nada; sin eventos de bloqueo |
| Otros apps Electron | Qoder, TRAE, AutoClaw y Alacritty arrancan **bien** → no es un problema general de Electron |

**Solución:** `--no-sandbox --disable-features=RendererCodeIntegrity`.

**Atajos creados (usar estos, no el icono anclado):**
- Escritorio e Inicio: `Obsidian - E-100.lnk` → `Obsidian.exe --no-sandbox --disable-features=RendererCodeIntegrity "C:\Users\Admin\Downloads\syn\Mente Maestra E-100"`
- Escritorio e Inicio: `GitHub Desktop.lnk` → mismos flags.

> **Pendiente:** la 1.14.4 **sigue crasheando** aunque lleve los flags. Se fijó
> Obsidian en **1.13.7** (funciona). Cuando salga una 1.14.5+ corregida, actualizar.

---

## 2. EJECUTORES: ESTADO ANTES Y DESPUÉS

| Ejecutor | Antes | Ahora | Arreglo |
|---|---|---|---|
| Tarea `E100-Backup-Boveda` | 🔴 `0xFFFD0000` (script inexistente) | ✅ `0x0` | Se creó `scripts\backup-vault-diario.ps1` (478 archivos → 10,3 MB, poda a 7 copias) |
| Tarea `OpenClaw Gateway` | 🔴 `0xC000013A` (chocaba de puerto) | ✅ `0x0` | Wrapper `~\.openclaw\gateway-safe.cmd` anti-doble-instancia + versión del launcher a 2026.6.35 |
| Tarea `AutoClaw Launch At Login` | 🔴 `0xCFFFFFFF` | ⚠️ **requiere admin** | La acción tenía comillas literales en `Execute`; además su `.exe` declara `requireAdministrator` → necesita `RunLevel Highest` |
| Tareas OneDrive ×3 | 🔴 `0x80070002` (OneDrive no instalado) | ✅ deshabilitadas | — |
| Tareas `WarrantyChecker` ×2 (HP) | 🔴 `0x8007042B` | ✅ deshabilitadas | El software ya no existe |
| Clave `Run` de OneDrive | 🔴 apuntaba a binario inexistente | ✅ eliminada | — |
| Tarea `npm-openclaw-install` | 🗑️ andamiaje temporal | ✅ eliminada | — |
| MCP `obsidian` | 🔴 paquete ausente | ✅ funciona | `npm i -g mcp-obsidian` (v1.0.0) |
| MCP `notion` | 🔴 `server unavailable` | ✅ funciona | Era transitorio: `npx` sin cachear |
| Ollama | 🔴 parado y **sin autostart** | ✅ activo con atajo de inicio | Ahora mismo escucha en 11434 |
| 21 plugins de Obsidian | 🔴 desactivados (`[]`) | ✅ restaurados | Volvieron a su estado commiteado |

### Comandos para lo que exige administrador
```powershell
# 1) AutoClaw con RunLevel Highest
Start-Process powershell -Verb RunAs -ArgumentList '-NoProfile','-ExecutionPolicy','Bypass','-File "C:\Users\Admin\Downloads\01_Proyectos_Agentes\_mision_e100\fix-autoclaw-elevated.ps1"'

# 2) Tareas HP residuales
Start-Process powershell -Verb RunAs -ArgumentList '-NoProfile','-Command','Disable-ScheduledTask -TaskPath ''\Hewlett-Packard\HP Support Assistant\'' -TaskName WarrantyChecker; Disable-ScheduledTask -TaskPath ''\Hewlett-Packard\HP Support Assistant\'' -TaskName WarrantyChecker_DeviceScan'
```

---

## 3. CRASHES REGISTRADOS (14 días) Y SU ORIGEN

| App | Eventos | Módulo | Código | Estado |
|---|---|---|---|---|
| `Obsidian.exe` | 5 (18-10) + 6 (hoy) | Obsidian.exe | `0x80000003` | ✅ resuelto con `--no-sandbox` |
| `GitHubDesktop.exe` | 2 (17-10) | sí mismo | `0x80000003` | ✅ resuelto con `--no-sandbox` |
| `CodexSandboxService.OpenAI.Codex` | 7 (11→16-10) | — | — | Servicio **deshabilitado**; el paquete MSIX de Codex ya no existe |
| `AutoClaw.exe` | 2 hangs | — | — | ⚠️ pendiente del fix de RunLevel |
| `msedge.exe`, `ChatGPT Classic.exe` | 1 hang cada uno | — | — | Residuo, sin impacto |

---

## 4. HERRAMIENTAS INSTALADAS EN ESTA SESIÓN

| Herramienta | Versión | Estado | Nota |
|---|---|---|---|
| **MiniMax Code CLI** (`mcode`) | 0.6.12 | ✅ | `npm i -g @minimax-ai/code`. Ya tiene sitio en tu stack (la Cola Post-Purga lo propone para repos) |
| **OpenClaw** | 2026.6.35 | ✅ gateway en :18789 | Reinstalado (el paquete estaba a medias: sin `node_modules` ni shims) |
| `@openclaw/groq-provider` | 2026.6.35 | ✅ | El plugin de Groq faltaba; instalado |
| **jcode** | v0.99.0 | ⚠️ | **Lo auto-instaló otro chat de OpenCode**, no tú. Se auto-configuró: hotkey global de Windows, `serve` y `keepalive` resident |
| **Alacritty** | 0.17.0 | ✅ | **Lo instaló jcode por su cuenta** vía `winget install -e --id Alacritty.Alacritty`. Es el terminal que jcode usa para su TUI |
| **mcp-obsidian** | 1.0.0 | ✅ | Faltaba el paquete |
| **Ollama** | — | ✅ | Con autostart |

> **Sobre jcode:** es un binario de 124 MB que se auto-instala, deja 3 procesos
> residentes, registra un **hotkey global** y ejecuta `winget` **con privilegios de
> administrador** por su cuenta. No es malware, pero conviene saberlo.

---

## 5. TRAMPAS DEL ENTORNO (para no volver a tropezar)

| Trampa | Detalle |
|---|---|
| **Tokens de Google caducan a los 7 días** | `refresh_token_expires_in: 604799`. Gmail y Drive quedaron **revocados** (`invalid_grant`). Hay que reautorizar cada semana o usar una app en modo *testing* (30 días) |
| **`Mv` es un alias de PowerShell** | Define tus funciones con otro nombre: `Move-Item`, `Rename-Item`… el alias gana a la función |
| **`Get-ChildItem -Include` no filtra** | Necesita ruta con comodín o `-Recurse`; si no, devuelve 0 filas |
| **Matar procesos por nombre es peligroso** | Barrí y maté `OpenCode.exe`, que hospeda la sesión. Mata por PID |
| **`Get-CimInstance Win32_Processor.Flags` puede venir vacío** | No lo tomes como "feature ausente" |
| **La API de Notion no expone vistas** | `2022-06-28` no tiene endpoints de vistas; `2026-03-11` sí, pero solo crea `table`, `form` y `dashboard`. **Timeline es imposible por API** |
| **La API v2 de Todoist está deprecada** | Usa `/api/v1/` y devuelve `{"results":[…]}` |
| **`--include` / rutas con acentos** | En PowerShell, acentos mal codificados crean carpetas duplicadas con doble codificación UTF-8 |

---

## 6. HERRAMIENTAS PROPIAS CREADAS

| Herramienta | Qué hace |
|---|---|
| **Puente MD** (`01_Proyectos_Agentes\puente\`) | Escribes la pregunta en `cola.md` (en VS Code), guardas, y el agente responde **en el mismo archivo**. El watcher detecta el bloque, lo copia al portapapeles y lo pega en la terminal de OpenCode. Activar: `.\activar.ps1` · Apagar: `.\desactivar.ps1` |
| **`scripts\backup-vault-diario.ps1`** | Respaldo diario de la bóveda (22:00, tarea programada `E100-Backup-Boveda`): zip con 7 copias podadas |
| **`convertir-estacion3-docx.ps1`** | MD → DOCX + PDF con interlineado 1,5, títulos en negrita y acotaciones en cursiva (usa Word COM) |

---

## 7. ESPACIO EN DISCO

| Momento | Libre |
|---|---|
| Inicio de la sesión | 12,99 GB |
| Cachés, updaters, versiones de Minecraft, gradle, npm, uv, SquirrelTemp, WER, Chrome, VS Code, TEMP, jcode viejo | **20,67 GB** |

Objetivo de 20 GB **cumplido**. `.ollama` (11,6 GB) son **modelos**, no caché: no se tocan.
