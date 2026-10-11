<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# EGG_REGRESSION_REPORT — Sin regresiones

## 1. Verificado hoy (2026-10-06)
- Bóveda: **0 borrados**. Solo creaciones y ediciones con snapshot previo.
- `SIM ROBOYORK`: **71/71 tests pasan**, `ruff check .` limpio.
- `data/` de SIM: sin escrituras del restore.
- Los 111 archivos de `recuperadas_20261002` están en `C:\Temp\STAGING_20261004\recuperadas\`, **fuera** de la bóveda.
- `git init` en la bóveda: **EJECUTADO HOY** (2026-10-06).
- Contaminación LAB → producción: ninguna.
- Contaminación staging → producción: ninguna.
- Contaminación histórico → producción: ninguna.

## 2. Notion (cambio real de hoy)
- 10 escrituras de datos, 0 borrados, 0 cambios de estructura.
- 1 página nueva con 35 bloques (`EGG V2 — AUDITORÍA SELECTIVA`).
- Snapshot previo: `notion_pre_selectivo.json`.
- Log de escrituras: `notion_pre_selectivo_aplicado.json`.
- Verificación posterior releída desde la API: CENTRAL 2/2, C1 8/9.

## 3. Diff conceptual
| Antes | Después |
|---|---|
| CENTRAL.Estado vacío en 5/5 | 2 con valor, 3 vacías por falta de datos |
| C1.Progreso % vacío en 9/9 | 8 con valor, 1 intacta (título vacío) |
| THE EGG-NETWORK con 36 hijos | 37 hijos |

## 4. Lo que NO se tocó
PIPELINE (1 fila), MONITOR (13 días viejo), LOGÍSTICA (sin Oct/Nov), `THE EGG-NETWORK prueba`, la fila sin título de C1, y las props no derivables de CENTRAL (Profesor, Horario, Creditos, Nota Actual).

## 5. Rollback
`notion_pre_selectivo.json` contiene los valores previos de las 14 filas tocadas. Cada escritura está en `notion_pre_selectivo_aplicado.json` con timestamp.

## 3. Verificación post-recuperación (2026-10-06)
- Bóveda: 360 archivos, 362 Markdown, 15 plugins activos (Kanban retirado).
- Git: `git init` ejecutado, `.gitignore` configurado.
- Plugins: 15 activos (Kanban/Periodic retirados), Custom Frames configurado.
- Local REST API: activo (puerto 27124, TLS, API key, certs).
- Tests: 71/71 pasan (antes 64).
- Ruff: limpio.
- R4=178 targets, R5=10453 rutas, IDX 33/70→R6+10.

## 4. Lo que NO se tocó (y por qué)
| Elemento | Por qué no se tocó |
|---|---|
| PIPELINE (1 fila) | Requiere datos reales de entregas |
| MONITOR (13 días) | Requiere datos reales diarios |
| LOGÍSTICA (sin Oct/Nov) | Requiere datos financieros reales |
| C1 fila sin título | No se sabe qué representa |
| Props no derivables (Profesor, Horario, Creditos, Nota) | Datos académicos, no derivables |
| THE EGG-NETWORK prueba | STAGING autorizado, no duplicado |
| 15 archivos 0 bytes en Cifrado_Shard | Placeholders intencionales / Meld |

## 5. Rollback disponible
`notion_pre_selectivo.json` contiene los valores previos de las 14 filas tocadas. Cada escritura está en `notion_pre_selectivo_aplicado.json` con timestamp.