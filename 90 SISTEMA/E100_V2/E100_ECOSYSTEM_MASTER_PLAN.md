<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# E100_ECOSYSTEM_MASTER_PLAN

## 1. Estado real de la trinidad (verificado 2026-10-06)
| Herramienta | Rol | Estado | Bloqueo |
|---|---|---|---|
| Obsidian | Cerebro: conocimiento y fuente de verdad | Operativa, 360 archivos, 15 plugins | 41 archivos pendientes descorruptar |
| Notion | Centro de operaciones: bases, dashboards, estado | Operativa, 14 bases, 10 correcciones aplicadas | MCP desactivado en OpenCode (pendiente) |
| Todoist | Arma de corto plazo: acciones inmediatas | Funcional, 11 tareas (10 sin fecha) | Sin token rotado, MCP desactivado |

**Conclusión: la trinidad no funciona como sistema integrado.** Notion y Obsidian están vivas pero desconectadas; Todoist no existe como capa de ejecución operativa.

## 2. Cuellos de botella reales (ordenados por daño)
| # | Cuello | Daño | Coste de arreglo |
|---|---|---|---|
| 1 | Sin `git init` en la bóveda | **RESUELTO** (ejecutado 2026-10-06) | 5 min |
| 2 | Todoist desconectado | El «hoy» no existe como sistema | 30 min + token |
| 3 | 41 archivos sin descorruptar | 37% de lo recuperado sigue ilegible | 1 h |
| 4 | PIPELINE con 1 fila de prueba | Entregas no llegan a Notion | 1 h + datos reales |
| 5 | MONITOR parado 13 días | Marca un peligro de hace 2 semanas | 10 min/día |
| 6 | 3 tokens pasaron por chat/código | **RESUELTOS** (rotados 2026-10-06) | 15 min |
| 6 | PIPELINE ↔ CENTRAL desconectados | Entregas no fluyen | 1 h + datos reales |
| 7 | MONITOR parado | Marca peligro de hace 2 semanas | 10 min/día |
| 7 | CALENDARIO encoding roto | Datos corruptos en API | 10 min |
| 8 | LOGÍSTICA incompleta | Falta Oct/Nov + campos vacíos | Usuario |
| 8 | ORDEN DE BATALLA histórico | Mezcla histórico/actual | Usuario |

## 3. Secuencia recomendada (actualizada 2026-10-06)
1. ~~`git init` y `.gitignore` en la bóveda.~~ **HECHO**
2. **Rotar los 3 tokens** (Notion, Todoist, Local REST API). **HECHO**
3. Descorruptar los 41 y decidir por lotes.
4. Conectar Todoist de una sola dirección (Notion → Todoist).
5. Cerrar PIPELINE con entregas reales (desde CENTRAL).
6. Reactivar MONITOR con datos reales diarios.
7. Corregir encoding CALENDARIO DE VIDA.
8. Limpiar ORDEN DE BATALLA (histórico vs activo).
9. Marcar datos TEST/DEMO claramente.
10. SIM Fases 3 y 4 (cuando RCS-2040 esté listo).

## 4. Regla de oro
Notion para gestionar. Obsidian para pensar. Todoist para ejecutar hoy.
Nada suelto: cada dato tiene su lugar.

## 5. Honestidad del documento
Este plan no inventa capacidades. Los 8 cuellos son observados, no supuestos.
Lo único teórico es el puente con Todoist, y está marcado como tal en `EGG_TODOIST_BRIDGE_REPORT.md`.

## 6. Próximos pasos críticos (P0/P1)
| Acción | Responsable | Deadline |
|---|---|---|
| Rotar token Todoist + reactivar MCP | Admin + OpenCode | Inmediato |
| Poblar PIPELINE con entregas reales de CENTRAL | Usuario + OpenCode | Esta semana |
| Reactivar MONITOR con datos diarios | Usuario | Esta semana |
| Corregir encoding CALENDARIO DE VIDA | OpenCode | Inmediato |
| Limpiar ORDEN DE BATALLA (histórico vs activo) | Usuario + OpenCode | Esta semana |
| Completar descorrupción 41 archivos | OpenCode | Esta semana |
| Revisión Custom Frames (30 días) | OpenCode | 2026-11-05 |

## 5. Visión a 12 meses (E-100 v3.0)
- **Obsidian**: Knowledge Core maduro, búsqueda semántica (Smart Connections), agentes autónomos leyendo/escribiendo.
- **Notion**: Command Center operativo, proyectos/operaciones/academia integrados, dashboards vivos.
- **Todoist**: Tactical Execution Layer, captura móvil fluida, rutina diaria automática.
- **Sync**: PC ↔ Móvil transparente, cero conflictos, backup Git + Syncthing.
- **Agentes**: OpenCode (ejecutor), AutoCLAW (auditor), Devin (red-team), Qwen (revisor) — orquestados.
- **RCS-2040**: Entregado, certificado, en competición.
- **E-100**: Segundo Cerebro operativo de por vida, no solo para la U.