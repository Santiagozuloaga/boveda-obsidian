<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# E100_RECOVERY_PROTOCOL

## 1. Regla
Nada entra en la bóveda sin estar limpio y revisado. Lo dudoso va a staging.

## 2. Rutas
| Ruta | Qué es |
|---|---|
| `C:\Temp\STAGING_20261004\` | staging de todo el trabajo de recuperación |
| `...\recuperadas\` | 111 `.md` dudosos extraídos de la bóveda |
| `...\hashes\` | manifiestos, snapshots, scripts y logs |
| `...\hashes\omniroute_backup\` | backup previo al reset de OmniRoute |

## 3. Pipeline
1. **Staging**: extraer a `imports\<fuente>-<fecha>\`. Nunca directo a la bóveda.
2. **Triage**: tabla de qué se conserva y qué se descarta. Por defecto se descarta: el minimalismo es la regla.
3. **Materializar**: una nota índice por lote. Solo lo excepcional merece nota atómica.
4. **Limpiar**: ZIP crudo a `backups\`, borrar staging, reportar.

## 4. Estado actual (2026-10-06)
| Etapa | Cantidad |
|---|---|
| Movidos a staging | 111 |
| Descorruptos | 65 |
| Ya estaban limpios | 5 |
| **Pendientes** | **41** |

Los 41 están listados en `hashes/recup_raros.txt` y ordenados por lotes en `hashes/recup_indice_lotes.md`.

## 5. Filtros intocables
- `05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/00_ARCHIVO_HISTORICO`: historia, no se toca.
- Tokens, API keys y `opencode.json`: solo lectura sin orden directa.
- Archivos abiertos en Obsidian en ese momento.

## 6. Debilidad actual
**`git init` en la bóveda: EJECUTADO HOY (2026-10-06).** El snapshot de Notion era un JSON suelto. Con control de versiones, un error de escritura se puede deshacer. **Riesgo reducido.**

## 7. Estado de sincronización
- SyncTrayzor 2.2.0 instalado, no corriendo.
- Syncthing config con 4 carpetas (vault `mente-maestra-e100`) y 2 dispositivos (PC + V2202).
- Pruebas A–D pendientes con móvil.
- SYNC ≠ ACTIVE.

## 8. Pruebas de sincronización (pendientes)
TEST A: PC → crear/modificar nota → móvil recibe.
TEST B: Móvil → modificar nota → PC recibe.
TEST C: Móvil → crear archivo → PC recibe.
TEST D: Provocar conflicto controlado → verificar resolución/recuperación.

## 9. Política de Git
- Antes de `git init`: verificar que no existen secretos.
- `.gitignore` debe cubrir: `.obsidian/workspace.json`, `.obsidian/plugins/*/data.json`, `*.log`, `.pyc`, `__pycache__/`, `.trash/`, `hashes/`, `C:\Temp\STAGING*/`.
- Primer commit: estado post-recuperación, sin secretos.
- Rama `main` protegida, `develop` para trabajo en curso.

## 9. Recuperación desde Drive
Si falla todo: descargar `Mente Maestra E-100(1).zip` → descomprimir → `git init` → restaurar.