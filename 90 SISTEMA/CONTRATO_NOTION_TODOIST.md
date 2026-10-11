# Contrato Notion ↔ Todoist — canónico v1 (2026-10-11)

> Fuente maestra única de la relación entre sistemas. No duplica datos,
> declara reglas. Estado verificado por API el 2026-10-11.

## Funciones
- **Notion (gestiona):** contexto, proyectos, estado, finanzas, seguimiento
  (EGG-NETWORK producción + prueba staging).
- **Todoist (ejecuta):** acciones ejecutables, fechas, prioridades,
  recordatorios. 11 abiertas (P1×2/P2×5/P3×4), 10 sin fecha.

## Fuentes maestras por dato
| Dato | Maestra | La otra |
|---|---|---|
| Proyectos y estado | Notion | Solo referencia |
| Tareas accionables/fechas/prioridades | Todoist | Solo espejo lectura (HOY/TABLERO) |
| Finanzas, C1, Monitor | Notion | No se duplican |

## Reglas
1. Vinculación tarea→proyecto por nombre explícito, no por ID frágil.
2. Cambios se hacen en la maestra; el espejo se regenera, no se edita.
3. Completadas viven en su sistema; no se borran para "limpiar".
4. Eliminaciones y conflictos: se documentan, no se sincronizan a ciegas.
5. Puente actual: MANUAL + asistido (OpenCode vía API directa). MCPs
   notion/todoist configurados pero sin cargar en sesión — NO tocar config.
6. No existe sincronización automática. No afirmarla hasta probarla.
7. Automatización futura: solo tras respaldos + pruebas + autorización.

## Verificación 2026-10-11
Notion: PIPELINE 12, MONITOR 0, C1 9 (conteos exactos). Todoist: 11/11
abiertas. Staging con banner STAGING·NO OPERATIVO (verificado en bloques).
