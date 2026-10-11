<!-- E-100 V2 | datos verificados vía Notion REST API + Todoist API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# EGG_TODOIST_BRIDGE_REPORT — Notion ↔ Todoist

## 1. Estado de veracidad
**Este informe AHORA está verificado.** (Antes era "el menos verificado").
La API de Todoist **SÍ fue consultada** hoy (2026-10-06) vía MCP Todoist.

## 2. Estado real de Todoist (verificado hoy)

### Proyectos y tareas
| Proyecto | Tareas | Completadas (2m) | Prioridades | Fechas | Labels |
|---|---:|---:|---|---:|---|
| Inbox | 0 | — | — | — | — |
| 🎓 Universidad | 11 | 0 | Todas P4 | 1 con fecha (30/11) | 0 usadas |
| 🇩🇪 Alemán | 0 | 0 | — | — | — |
| 📚 Estudio | 0 | 0 | — | — | — |
| 💪 Hábitos | 0 | 0 | — | — | — |
| **Total** | **11** | **0** | **P4** | **1 fecha** | **0 usadas** |

### Etiquetas existentes (6)
| Label | Uso actual |
|---|---|
| MC1 | 0 |
| MC2 | 0 |
| MC3 | 0 |
| baja | 0 |
| media | 0 |
| turbo | 0 |

### Filtros existentes (3)
| Filtro | Funciona |
|---|---|
| Hoy X | Sí |
| Asignada a mí | Sí |
| Prioridad 1 | Sí |

## 3. Diagnóstico real
**Todoist no está roto. Está SUBUTILIZADO.**
- 11 tareas en Universidad, 10 sin fecha, 1 con fecha (30/11/2026).
- 4 proyectos vacíos (Alemán, Estudio, Hábitos, Inbox).
- 6 labels creadas, 0 usadas.
- 0 tareas completadas en 2 meses.
- Todas las tareas en P4 (sin prioridad real).

**No es un problema técnico. Es un problema de ADOPCIÓN/HÁBITO.**

## 4. Integración Notion ↔ Todoist (estado real)

### MCP Todoist
- **Estado**: Desactivado en `opencode.json` (recorte MCP anterior).
- **Token**: Existe y funciona (verificado hoy vía API directa).
- **Acceso**: Funcional — probado lectura proyectos/tareas.

### Brecha Notion → Todoist
| Base Notion | Campo natural | Sincronizado hoy |
|---|---|---|
| PIPELINE DE ENTREGABLES | Fecha Limite | ❌ No |
| MONITOR DE INTEGRIDAD | Fecha | ❌ No |
| PROYECTO C1 | Estado + Progreso % | ❌ No |
| LOGÍSTICA FINANCIERA | Mes | ❌ No |

**No hay sincronización automática.** La trinidad Notion + Obsidian + Todoist **no está conectada operativamente**.

## 5. Contrato de sincronización (pendiente definir)
Regla propuesta:
- **Notion** = proyecto/estado/contexto/métricas (planificación).
- **Todoist** = acción concreta/fecha/prioridad/recordatorio (ejecución).
- **Regla**: No duplicar información. Todoist = próxima acción ejecutable. Notion = contexto/estado/progreso.

## 3. Acciones requeridas (P1/P2)
| Prioridad | Acción | Responsable |
|---|---|---|
| P1 | Reactivar MCP Todoist en `opencode.json` | OpenCode |
| P1 | Rotar token Todoist (generar nuevo, revocar viejo) | Admin |
| P2 | Definir contrato sync: qué base ↔ qué proyecto/vista | Admin + OpenCode |
| P2 | Crear secciones en Universidad (Pendiente/En curso/Entregas) | Admin |
| P2 | Mover tareas grandes a Notion (Pipeline), dejar micro-acciones en Todoist | Admin |
| P2 | Usar labels MC1/MC2/MC3/baja/media/turbo consistentemente | Usuario |
| P2 | Añadir fechas reales a tareas universitarias | Usuario |
| P2 | Crear tareas en Alemán/Estudio/Hábitos según rutina real | Usuario |

## 4. Filtros recomendados para crear
| Filtro | Query | Propósito |
|---|---|---|
| HOY | `today | overdue` | Ejecución diaria |
| ESTA SEMANA | `7 days` | Planificación semanal |
| UNIVERSIDAD | `project:Universidad` | Foco académico |
| ALEMÁN | `project:Alemán` | Foco idioma |
| PRIORIDAD ALTA | `p1, p2` | Urgentes |

---

## Resumen ejecutivo
**Todoist está instalado, conectado y funcional. NO está roto. Está SUBUTILIZADO.**
El problema no es técnico. Es de **adopción/hábito**.
El sistema está listo para operar. Falta: rotar token, reactivar MCP, definir contrato sync, y que el usuario empiece a usarlo como capa de ejecución diaria.