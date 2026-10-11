# E-100 ARCHITECTURE RECONCILIATION AUDIT (solo lectura — cambia NADA)
Fecha: 2026-09-28 · Fuentes: informe Claude + auditoría Todoist + inspección directa API + certificación Obsidian.

## 1. Matriz fuente de verdad (propuesta, decide Admin)

| Función | Obsidian | Notion antiguo | Notion LAB | Todoist | Fuente propuesta |
|---|---|---|---|---|---|
| Materias | conocimiento MOC | CENTRAL (2 filas, XP/Nivel/rollups) | Cursos (4 filas, Tipo/Créditos) | — | CENTRAL = estado/notas; Cursos = operación semestral. Convivencia con enlace, no fusión |
| Entregables | contexto/borradores | PIPELINE (1 fila prueba) | Assignments (3 filas, rel Curso) | 11 acciones reales | PIPELINE = estado; Assignments = tracking; Todoist = acción. Tres capas, un dato enlazado |
| Exámenes | notas/post-mortem | — (vacío) | Exámenes (2 filas, Peso) | recordatorio | LAB Exámenes = fuente (sin contraparte antigua) |
| Hábitos | conocimiento | MONITOR (1 demo) | Hábitos (2 filas, Racha) | 0 recurrentes | LAB Hábitos = fuente operativa; MONITOR = energía/estado |
| Calendario | notas diarias | CALENDARIO DE VIDA | Calendario Semestre (1 fila) | fechas | CALENDARIO DE VIDA = vida; Semestre = académico. Separar por dominio |
| Proyectos | conocimiento | Orden/PIPELINE/C1 | — | acciones | Notion = estado; Todoist = acción; Obsidian = contexto |
| Finanzas | — | LOGÍSTICA (real) | — | — | LOGÍSTICA única fuente |
| Repaso | SR plugin | AR Zettel (3) | — | — | Obsidian SR = conocimiento; AR = seguimiento. No duplicar tarjetas |

## 2. Verificaciones propias contra el documento
- **9 bloques "desconocidos"/truncated en EGG**: SON mis 9 link_to_page al LAB [VERIFICADO por API]. No es corrupción. Verificación visual pendiente (browser, 5 min).
- **Etiquetas Todoist**: el documento menciona "seis etiquetas huérfanas"; mi auditoría API encontró 0 labels en la cuenta. Discrepancia [NO VERIFICADO] — pedir evidencia o descartar.
- **Kanban/Custom Frames**: Kanban retirado con rollback disponible [VERIFICADO]; Custom Frames activo [ACTIVO]. Decisiones ya tomadas, no pendientes.
- **NEXUS**: archivado (recuperable 30d), no eliminado [VERIFICADO]. "No encontrado como activo" = correcto por diseño.
- **06_OPERACIONES**: NO existe en vault [VERIFICADO]. Permanece PROPUESTA condicionada.
- **Gate extra DEDUPLICATION**: adoptado. Nuevo orden 15 gates (doc §10).

## 3. Decisión requerida de Admin (una por fila de la matriz)
¿Fusión, enlace o separación por cada solapamiento? Mi recomendación: ENLACE (links), nunca fusión ni borrado.

## 4. APROBACIÓN Admin 2026-09-28
Matriz aprobada con criterio ENLACE. Ejecutado: 9 links LAB->UNIVERSIDAD + 6 bloques inversos (H2 + 5 links a CENTRAL/MONITOR/LOGISTICA/AR/PIPELINE) en LAB. Cero fusiones, cero borrados.

## 5. CAPA C — plantillas externas (auditoría 2026-09-28)
| Plantilla | Estado | Clasificación propuesta |
|---|---|---|
| Student OS Starter | Duplicada real, con refs PRO/upsell | REFERENCIA (no tocar; decidir si se pela PRO o se archiva) |
| Minimalist Project Manager | Duplicada real | REFERENCIA/COMPLEMENTO visual |
| Second Brain PARA | Duplicada real (3 pgs + 2 DBs) | REFERENCIA (espejo Obsidian pendiente) |
| LAB 9 DBs | Datos DEMO etiquetados con banner | LABORATORIO |
| CENTRAL/PIPELINE/MONITOR/LOGISTICA/AR | Datos reales | FUENTE DE VERDAD |
Enlaces link_to_page verificados 11/11 por API (el lector externo los muestra unknown por limitación suya, no rotos).
## 6. Dashboard Universitario
Toggles vacíos = estado PRE-EXISTENTE restaurado 1:1 (borrado accidental + restauración verificada). No es obra incompleta: así estaba.

## 7. FUENTE DE VERDAD OPERATIVA (cierre 2026-09-29, ejecutado)
| Par | FUENTE | COMPLEMENTO | LAB/REF |
|---|---|---|---|
| CENTRAL vs Cursos | CENTRAL (notas/XP/rollups reales) | Cursos (operación semestral) | LAB |
| PIPELINE vs Assignments | PIPELINE (estado entregables) | Assignments (tracking) + Todoist (acción) | LAB |
| MONITOR vs Hábitos | MONITOR (energía/estado) | Hábitos (rachas) | LAB |
| CALENDARIO DE VIDA vs Calendario Semestre | VIDA=personal, SEMESTRE=académico (dominios separados) | — | LAB |
| ACTIVE RECALL vs Clases/Lectures | AR (seguimiento) + Obsidian SR (conocimiento) | Lectures (contexto clase) | LAB |
| Finanzas | LOGÍSTICA única | — | — |
| Student OS/Minimalist/SecondBrain | REFERENCIA externa intacta | Maqueta visual | REF |
Dashboard 10/11 toggles poblados con links verificados; Rutina 30-30-30 sin target (BLOQUEO: requiere decisión humana). LAB 16/16 filas DEMO=True + banner.
