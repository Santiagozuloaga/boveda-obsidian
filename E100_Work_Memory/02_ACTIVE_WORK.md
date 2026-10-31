# 02_ACTIVE_WORK.md — Trabajos Abiertos

**Fecha:** 31 de octubre de 2026  
**Objetivo:** Completar la auditoría E-100 y ejecutar pruebas E2E autorizadas

## Trabajo en curso

### Prueba E2E-01: Flujo Todoist → HOY.md ✅ PASADA

**Objetivo:** Verificar que las 11 tareas abiertas de Todoist aparecen en el tablero HOY.md de Obsidian.

**Resultado:** Las 11 tareas de Todoist coinciden exactamente con HOY.md (títulos, proyectos, prioridades, vencimientos). La tarea "Export Gmail academico" muestra vencimiento 2026-11-30.

**Evidencia:** HOY.md leído y comparado con respuesta de API de Todoist.

**Estado:** Completado y verificado

---

### Prueba E2E-02: Flujo Notion Bandeja → consumo → Estado "Consumido" ✅ PASADA

**Objetivo:** Verificar que cambiar el estado de una entrada en Notion Bandeja de Aprendizaje se refleja correctamente.

**Resultado:** Entrada `409b38a4-c0ce-8153-a284-d76dd5c34bd6` ("Dativ vs. Akkusativ: Verbs with 2 cases") cambiada de "Sin leer" → "Consumido". lastEditedTime actualizado a 2026-10-31T05:39:00.000Z. Verificado mediante lectura posterior de la página.

**Evidencia:** PATCH a Notion API (status 200) + lectura posterior confirmando estado "Consumido".

**Estado:** Completado y verificado

---

### Prueba E2E-03: Tarea `Export Gmail academico` ✅ PASADA

**Objetivo:** Verificar que la tarea `Export Gmail academico (Workspace en riesgo)` tiene vencimiento 2026-11-30 y está activa.

**Resultado:** Tarea ID `6hRJqrx922hRHWj2` confirmada en API de Todoist: due date 2026-11-30, checked=false, priority=4, etiqueta "alta".

**Evidencia:** Respuesta de API de Todoist (status 200, 11 tareas totales).

**Estado:** Completado y verificado

