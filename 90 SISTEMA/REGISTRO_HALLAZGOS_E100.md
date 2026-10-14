# REGISTRO_HALLAZGOS_E100.md — v1.0 2026-10-14 (canónico; una fila por hallazgo)

| ID | Pri | Hallazgo | Fuente/evidencia | Responsable | Acción | Estado | Prueba aceptación |
|---|---|---|---|---|---|---|---|
| H-01 | P0 | Hook no bloqueó commit zip 17:05 (ebb1842) | EN VIVO: `git show ebb1842` contenía test-block2.zip | OpenCode | Reset --soft+unstage (rama no pusheada); chmod +x al hook; re-prueba | CORREGIDO Y VERIFICADO | Bloqueo + exit 1 reproducido 2× post-fix |
| H-02 | P2 | `Daily Sin título.md` vacío accidental | EN ARCHIVOS: 0 bytes | OpenCode | `git rm` | CORREGIDO Y VERIFICADO | vscan 31→30 vacíos (remedido 14-oct: 15 Shard + 15 GEMS + 0 accid. = 30; método: Get-ChildItem -Recurse Length -eq 0 excluyendo .git/.obsidian/.trash/.stversions/.smart-env/.stfolder) |
| H-03 | P2 | `_MOC_LITERATURA` inexistente (×3 refs) | EN ARCHIVOS: scan links | OpenCode | MOC mínimo con subdirs reales | CORREGIDO Y VERIFICADO | 3 refs resuelven |
| H-04 | — | Links `___`/vacíos/tp-tokens (×45) | EN ARCHIVOS | — | Reclasificado: ruido de plantillas, NO defecto | NO DEFECTO | — |
| H-05 | P2 | Notas Derivadas/Cinemática/Álgebra sin crear | EN ARCHIVOS | Admin (contenido) | Registrar como contenido futuro (plan STEM existe) | PENDIENTE DE DECISIÓN | — |
| H-06 | P1 | Dupes Devin/OpenCode (08 vs MEMORIA_COLECTIVA) | EN ARCHIVOS | Admin | Definir canónico (propuesta: 08 AGENTES) | PENDIENTE DE DECISIÓN | — |
| H-07 | P3 | Ramas remotas stale ×3 | EN VIVO: `git branch -a` | Admin | Borrar tras verificar merges | PENDIENTE DE DECISIÓN | — |
| H-08 | P2 | Frontmatter 57% ausente | EN ARCHIVOS: 246 notas | Admin+OpenCode | Campaña por lotes (MOCs primero) | EN PROGRESO (sin lote ejecutado) | ≥80% MOCs/informes |
| H-09 | P1 | Sync app apagada hoy | EN VIVO: 0 procesos | — | Estado documentado; A–D 11-oct vigente | NO VERIFICADO (hoy) | re-probes con móvil |
| H-10 | P0 | P0 seguridad aplazado | Decisión Admin 14-oct | Admin | Rotar key, privado, purga (cuando ordene) | APLAZADO (no resuelto) | — |

Cierre global techo: LISTO CON LIMITACIONES (P0 abierto impide LISTO).
