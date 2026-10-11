# PROMPT PARA OPENCODE - TAREAS PENDIENTES E-100
**Fecha:** 2026-09-23 | **Sistema:** E-100 v5.3 | **Vault:** Mente Maestra E-100 | **Workspace:** THE EGG-NETWORK
**Contexto:** Reconciliación completada por OpenCode (INFORME_RECONCILIACION_E100.md)
**Auditorías previas:** Devin V1/V2, OpenCode Reconciliación

---

## 📋 RESUMEN DE ESTADO ACTUAL

### ✅ COMPLETADO por OpenCode (Reconciliación):
- hideLegend corregido → showLegend en Control Panel.md
- Contaminación de plantillas corregida en queries de proyectos
- 15 archivos placeholders restaurados (links de _INFORMES_GEMS.md)
- GEMs clasificados como [PENDIENTE CONTEXTO] (NO inventados)
- NEXUS clasificado como [PENDIENTE CONTEXTO] (NO inventado)
- Active Recall 3 pages CONFIRMADAS vía API

### ⚠️ PENDIENTE - Requiere intervención del usuario:

---

## 🎯 OBJETIVO PRINCIPAL

Completar todas las tareas pendientes que requieren verificación visual en UI y confirmación del usuario, siguiendo principios del MASTER PROMPT (NO DESTRUCCIÓN, NO INVENTAR, CLASIFICACIÓN DE EVIDENCIA).

---

## 📋 TAREAS PENDIENTES - PRIORIDAD ALTA

### TAREA 1: Confirmación del usuario sobre GEMs

**Ubicación:** THE EGG-NETWORK → MANDO → MC1/MC2

**Pregunta al usuario:**
> "En MANDO MC1/MC2 aparecen 'Gem E-123 OMEGA' y 'Gem E-001 ULTRON'. Según _ELENCO_GEMS.md, estos son tus modos mentales reales. ¿Es la redacción actual en Notion la vigente, o requiere corrección?"

**Acción:**
- Esperar respuesta del usuario
- Si usuario dice "es vigente": NO modificar
- Si usuario dice "requiere corrección": preguntar qué corregir
- Documentar la decisión

**Clasificación esperada:** [VERIFICADO] después de confirmación del usuario

---

### TAREA 2: Confirmación del usuario sobre NEXUS

**Ubicación:** THE EGG-NETWORK → MEJORA E-100

**Pregunta al usuario:**
> "En MEJORA E-100 aparece 'NEXUS importado - 3 reglas operativas'. La importación ocurrió (2 DBs existen: TAREAS COLABORATIVAS y TASK MANAGER). ¿Existe un workspace Notion literal llamado 'NEXUS', o es un nombre de ejemplo que debería eliminarse?"

**Acción:**
- Esperar respuesta del usuario
- Si usuario dice "existe workspace NEXUS": mantener referencia
- Si usuario dice "es ejemplo": eliminar callout o marcar como histórico
- Documentar la decisión

**Clasificación esperada:** [VERIFICADO] después de confirmación del usuario

---

### TAREA 3: Verificación visual de Active Recall 3 pages

**Ubicación:** Notion → BD Active Recall - Zettel Cards

**Estado actual:**
- ✅ 3 pages existen vía API (¿Capital de Francia?, ¿Capital de Italia?, ¿Qué es POO?)
- ✅ 7 props existen (Cover, Dificultad, Materia, Pregunta, Próximo Repaso, Respuesta, Tipo)
- ⚠️ Render visual NO verificado

**Instrucción al usuario:**
> "Abre la BD Active Recall - Zettel Cards en Notion. Verifica que las 3 pages (Francia-París, Italia-Roma, POO Mapa Mental) se renderizan correctamente en UI. Toma capturas de pantalla de cada page con sus props visibles."

**Acción:**
- Esperar capturas del usuario
- Si se renderizan correctamente: clasificar como [VERIFICADO]
- Si NO se renderizan: investigar causa
- Documentar el resultado

**Clasificación esperada:** [VERIFICADO] después de capturas

---

### TAREA 4: Verificación visual de Tracker gráfico

**Ubicación:** Obsidian → Control Panel.md → sección "Energía — Tracker"

**Estado actual:**
- ✅ hideLegend corregido → showLegend por OpenCode
- ✅ Plugin Tracker activo en UI
- ⚠️ Render visual NO verificado

**Instrucción al usuario:**
> "Reabre Obsidian. Ve a Control Panel.md en Preview Mode. Verifica si el gráfico Tracker (energía/x_ganada) se renderiza correctamente. Toma captura de pantalla."

**Acción:**
- Esperar captura del usuario
- Si se renderiza correctamente: clasificar como [VERIFICADO]
- Si NO se renderiza: investigar si requiere reiniciar Obsidian o configuración adicional
- Documentar el resultado

**Clasificación esperada:** [VERIFICADO] después de captura

---

### TAREA 5: Verificación visual de Dataview queries

**Ubicación:** Obsidian → HOME.md y Control Panel.md

**Estado actual:**
- ✅ Sintaxis queries sanas (verificado por OpenCode)
- ✅ hideLegend corregido
- ⚠️ Render visual NO verificado
- "No results" = ausencia de datos, no queries rotas

**Instrucción al usuario:**
> "Reabre Obsidian. Ve a HOME.md y Control Panel.md en Preview Mode. Verifica si las Dataview queries se renderizan correctamente. Toma capturas de:
> - HOME.md: HOY (0) y ENERGIA
> - HOME.md: Proyectos activos
> - HOME.md: Reciente
> - Control Panel.md: KPIs (Inbox count, Proyectos activos, Tasks hoy, Energía 14d avg, Dailies este mes)
> - Control Panel.md: Proyectos — Salud
> - Control Panel.md: Tasks abiertas
> - Control Panel.md: Actividad — Últimos 14 días"

**Acción:**
- Esperar capturas del usuario
- Clasificar cada query:
  - Si renderiza datos: [VERIFICADO]
  - Si muestra "No results": [VERIFICADO] (ausencia de datos es normal)
  - Si muestra error: [REQUIERE CORRECCIÓN]
- Documentar el resultado por query

**Clasificación esperada:** [VERIFICADO] para todas las queries (sintaxis sana, solo datos faltantes)

---

### TAREA 6: Verificación visual de Canvas

**Ubicación:** Obsidian (si existe Canvas en la bóveda)

**Estado actual:**
- ⚠️ No se menciona en informes, requiere verificación

**Instrucción al usuario:**
> "Reabre Obsidian. ¿Existen archivos Canvas en la bóveda? Si existen, verifica si se renderizan correctamente en UI. Toma captura de pantalla."

**Acción:**
- Esperar respuesta/captura del usuario
- Si no existen Canvas: marcar como [NO APLICABLE]
- Si existen y renderizan: [VERIFICADO]
- Si existen y NO renderizan: [REQUIERE CORRECCIÓN]

**Clasificación esperada:** [VERIFICADO] o [NO APLICABLE]

---

## 📋 TAREAS PENDIENTES - PRIORIDAD MEDIA

### TAREA 7: Verificación visual de props Notion

**Ubicación:** Notion → CENTRAL ACADÉMICA

**Estado actual:**
- ✅ Props existen en código: Total, Completadas, Progress, Barra, XP, Nivel
- ⚠️ Render visual NO verificado

**Instrucción al usuario:**
> "Abre CENTRAL ACADÉMICA en Notion. Verifica que las props se renderizan correctamente:
> - Total (number)
> - Completadas (number)
> - Progress (formula = Completadas/Total)
> - Barra (formula de barras de progreso █████░░░░░░░)
> - XP (formula = round(Progress*1000))
> - Nivel (formula = I/II/III)
> Toma captura de pantalla de al menos 1 entry con todas las props visibles."

**Acción:**
- Esperar captura del usuario
- Si se renderizan correctamente: [VERIFICADO]
- Si NO se renderizan: investigar causa
- Documentar el resultado

**Clasificación esperada:** [VERIFICADO] después de captura

---

### TAREA 8: Verificación visual de fórmulas Notion - MONITOR

**Ubicación:** Notion → MONITOR DE INTEGRIDAD 2.0

**Estado actual:**
- ✅ Props existen en código: Hecho Hoy, Racha Actual, Racha Máx, Cumplimiento %, Barra Streak
- ⚠️ Render visual NO verificado
- ⚠️ OpenCode reportó que Barra Streak mostraba `????` (emoji 🔥 corrompido)

**Instrucción al usuario:**
> "Abre MONITOR DE INTEGRIDAD 2.0 en Notion. Verifica que las props se renderizan correctamente:
> - Hecho Hoy (checkbox)
> - Racha Actual
> - Racha Máx
> - Cumplimiento % (formula = Racha Actual / Racha Máx)
> - Barra Streak (formula con emojis 🔥🔥🔥)
> CRÍTICO: ¿Los emojis 🔥 aparecen correctamente o muestran '????'?
> Toma captura de pantalla."

**Acción:**
- Esperar captura del usuario
- Si emojis 🔥 aparecen: [VERIFICADO]
- Si emojis muestran `????`: [REQUIERE CORRECCIÓN] - editar fórmula en UI
- Documentar el resultado

**Clasificación esperada:** [VERIFICADO] o [REQUIERE CORRECCIÓN]

---

### TAREA 9: Verificación visual de fórmulas Notion - LOGÍSTICA

**Ubicación:** Notion → LOGÍSTICA FINANCIERA

**Estado actual:**
- ✅ Props existen en código: Presupuesto, Gastado, Restante
- ⚠️ Render visual NO verificado

**Instrucción al usuario:**
> "Abre LOGÍSTICA FINANCIERA en Notion. Verifica que las props se renderizan correctamente:
> - Presupuesto
> - Gastado
> - Restante (formula = Presupuesto - Gastado)
> Toma captura de pantalla de al menos 1 entry (ejemplo Septiembre)."

**Acción:**
- Esperar captura del usuario
- Si se renderizan correctamente: [VERIFICADO]
- Si NO se renderizan: investigar causa
- Documentar el resultado

**Clasificación esperada:** [VERIFICADO] después de captura

---

### TAREA 10: Probar plantilla Daily Note con Templater

**Ubicación:** Obsidian → 01_DIARIO_DE_GUERRA/01_Daily_Logs

**Estado actual:**
- ✅ Plantilla PLANTILLA_Daily_Note.md existe (108 líneas)
- ✅ Templater activo en UI
- ✅ Folder template configurado
- ⚠️ Ejecución real NO verificada

**Instrucción al usuario:**
> "Reabre Obsidian. Crea una nueva nota en 01_DIARIO_DE_GUERRA/01_Daily_Logs (puedes usar Ctrl+N en esa carpeta).
>
> CAPTURA 1 (ANTES): Inmediatamente después de crear, antes de que Templater se ejecute. Deberías ver placeholders como <% tp.date.now... %>.
>
> CAPTURA 2 (DESPUÉS): Deja que Templater se ejecute automáticamente (trigger_on_file_creation: true). Verifica que:
> - Fecha se reemplaza con fecha real (ejemplo: Wednesday September 23, 2026)
> - Navegación ayer/mañana aparece con links
> - Secciones de la plantilla se renderizan
>
> Toma ambas capturas para comparar."

**Acción:**
- Esperar 2 capturas del usuario
- Si ANTES tiene placeholders y DESPUÉS tiene fecha real: [VERIFICADO]
- Si Templater NO se ejecuta: [REQUIERE CORRECCIÓN] - verificar configuración trigger
- Documentar el resultado

**Clasificación esperada:** [VERIFICADO] después de capturas

---

## 📋 TAREAS PENDIENTES - PRIORIDAD BAJA

### TAREA 11: Verificar secciones vacías en Control Panel

**Ubicación:** Obsidian → Control Panel.md

**Estado actual:**
- Zettelkasten pipeline: 0 datos (8 MOCs existen, pero query requiere `tipo: zettel` o `#zettel`)
- Bookshelf: 0 datos (requiere `tipo: libro` o `#libro`)
- Auditoría: 0 datos (requiere `tipo: auditoria` o `#auditoria`)

**Instrucción al usuario:**
> "En Control Panel.md, las secciones Zettelkasten, Bookshelf y Auditoría muestran 'No results'. ¿Deseas:
> a) Crear notas con las props/tags correctas para que estas queries retornen datos?
> b) Eliminar estas secciones si no las necesitas?
> c) Mantener como estructura para futuro uso?"

**Acción:**
- Esperar decisión del usuario
- Documentar la decisión
- Ejecutar según elección del usuario

**Clasificación esperada:** [VERIFICADO] después de decisión del usuario

---

## 📊 FORMATO DE RESPUESTA ESPERADO

OpenCode debe responder con:

# INFORME DE ESTADO - OPENCODE TAREAS PENDIENTES

## 1. CONFIRMACIONES DEL USUARIO
- GEMs: [Es vigente / Requiere corrección / Pendiente]
- NEXUS: [Existe workspace / Es ejemplo / Pendiente]

## 2. VERIFICACIONES VISUALES
- Active Recall 3 pages: [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]
- Tracker gráfico: [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]
- Dataview queries: [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]
- Canvas: [VERIFICADO / NO APLICABLE / PENDIENTE]

## 3. VERIFICACIONES NOTION
- CENTRAL ACADÉMICA props: [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]
- MONITOR fórmulas (🔥 emojis): [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]
- LOGÍSTICA props: [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]

## 4. TEMPLATER DAILY NOTE
- Ejecución: [VERIFICADO / REQUIERE CORRECCIÓN / PENDIENTE]
- Capturas: [Recibidas / Pendientes]

## 5. SECCIONES VACÍAS
- Decisión del usuario: [Crear datos / Eliminar secciones / Mantener]

## 6. PRÓXIMOS PASOS
- Qué requiere intervención adicional
- Qué puede completar OpenCode directamente
- Qué requiere nueva auditoría

---

## 🔗 REFERENCIAS

- **MASTER PROMPT:** `90 SISTEMA/MEMORIA_COLECTIVA/Informes/MASTER_PROMPT_AUDITORIA_RECUPERACION.md`
- **Auditoría V2:** `90 SISTEMA/MEMORIA_COLECTIVA/Informes/AUDITORIA_COMPLETA_MASTER_PROMPT_V2.md`
- **Datos Contexto:** `90 SISTEMA/MEMORIA_COLECTIVA/Informes/AUDITORIA_DATOS_REQUIEREN_CONTEXTO.md`
- **Reconciliación:** `90 SISTEMA/MEMORIA_COLECTIVA/Informes/INFORME_RECONCILIACION_E100.md`
- **Paquete ChatGPT:** `90 SISTEMA/MEMORIA_COLECTIVA/Informes/PAQUETE_COMPLETO_CHATGPT.md`

---

**FIN DEL PROMPT PARA OPENCODE**
