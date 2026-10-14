# CAMBIOS_EJECUTADOS_E100.md — v1.0 2026-10-14 (misión cierre; rama cierre-expediente)

| Archivo(s) | Motivo | Método | Prueba | Reversión |
|---|---|---|---|---|
| `01_DIARIO_DE_GUERRA/01_Daily_Logs/Sin título.md` eliminado | Vacío 0B accidental | `git rm` | vscan: 0 accidentales restantes | `git checkout HEAD -- <ruta>` (historial) |
| `04_LITERATURA_Y_FUENTES/_MOC_LITERATURA.md` creado | 3 links sin destino | MOC mínimo (subdirs reales) | refs resuelven | borrar archivo |
| `07_TABLERO/HOY.md`, `TABLERO_SEMANAL.md` | Espejo viejo (27-sep) | `sync-tablero.py` (mejorado: fechas Notion) | 11/12/2/4 en vivo; detectó renombre real | `git checkout -- 07_TABLERO` |
| `90 SISTEMA/sync-tablero.py` mejorado | Sufijos de fecha se perdían | +prop date en query | fechas → presentes | `git checkout --` |
| `.git/hooks/pre-commit` chmod +x | Bypass anómalo 17:05 (causa probable: bit ejecutable) | sh chmod +x | bloqueo+exit 1 ×2 | reinstalar desde `90 SISTEMA/hooks/` |
| ebb1842 (commit prueba con zip) | Hook no disparó 17:05, causa no determinada | `reset --soft HEAD~1` + unstage (rama local, sin push) | `git log` sin ebb1842; zip en ningún árbol | N/A (nunca salió del clon) |
| `04…/_MOC_LITERATURA.md` línea MOC_FUENTES | Texto provisorio | edit (verificado existente) | ls-files | — |

Cero escrituras en Notion/Todoist (solo lectura API). Cero cambios en staging. Nada commiteado a main (rama + PR).
