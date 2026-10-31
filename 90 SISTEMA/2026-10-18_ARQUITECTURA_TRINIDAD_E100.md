---
type: arquitectura
tags: [e100, notion, todoist, obsidian, trinidad, reconciliacion]
fecha: 2026-10-18
estado: vigente
fuente: MISION_E100_RECONCILIACION (Notion+Todoist+Obsidian, solo lectura)
---

# ARQUITECTURA DE LA TRINIDAD — E-100

> Documento canónico de la distribución de responsabilidades. Actualizado tras la
> reconciliación del 18-10-2026 (lectura completa de Notion, Todoist y Obsidian).

---

## 1. PRINCIPIO

| Sistema | Es el dueño de | NO es el dueño de |
|---|---|---|
| **Todoist** | Tareas accionables, fechas, prioridades, recordatorios, recurrencia, cumplimiento real | Contexto, entregables, finanzas |
| **Notion** | Estructura, proyectos, entregables, hitos, paneles, supervisión, **visor de Todoist** | Microtareas, conocimiento profundo |
| **Obsidian** | Conocimiento reusable, zettelkasten, protocolos, documentación, repaso | Gestión de tareas, estado operativo |

**Regla que resuelve el 90 % de las contradicciones:** si un dato es una acción
concreta con verbo y resultado, vive en Todoist. Si es un entregable, vive en
Notion. Si es conocimiento, vive en Obsidian.

**Nada de copia completa.** La Bandeja de Aprendizaje es bandeja de resultados
automáticos, no de conocimiento: lo que se consume va a Obsidian o a Todoist, y
lo que no, se descarta.

---

## 2. INVENTARIO REAL (verificado por API, 0 errores)

### Notion — 1.576 objetos · 115 bases · 1.183 filas
- Dos universos EGG: producción `2eeb38a4…` y staging `ac9b38a4…` (banner STAGING).
- 10 páginas raíz + 13 bases sueltas a nivel raíz.
- 25 grupos de nombres duplicados → 56 bases con el mismo nombre.
- **80 relaciones verificadas, 0 rotas.**

### Todoist — 5 proyectos · 6 etiquetas · 11 tareas
| Proyecto | Tareas |
|---|---|
| Universidad | **11 (todas)** |
| Inbox / Alemán / Estudio / Hábitos | 0 |

- Prioridades: P1=2 · P2=5 · P3=4. Con fecha: **1 de 11**. Vencidas: 0.
- Etiquetas: `MC1` `MC2` `MC3` `baja` `media` `alta`.
- Sin filtros verificables por API (404 en `/api/v1/filters`).

### Obsidian — 445 notas · 999 archivos auxiliares
- Taxonomía **unificada el 18-10-2026**: un solo árbol (PARA arriba, MOC
  universitario dentro de `20 AREAS/20.01 UNIVERSIDAD/`).
- Núcleos: `90 SISTEMA` (170) · `20.01.05 Protocolos` (125) · `01 Diario de Guerra` (42).

---

## 3. CONTRADICCIONES DETECTADAS Y RESUELTAS

| # | Contradicción | Resolución |
|---|---|---|
| C1 | `PIPELINE` producción con 1 fila vs 12 en staging | **Fusionado** el 18-10: 11 filas creadas, 0 borradas, 0 modificadas |
| C2 | `MONITOR` producción con 13 props vs 16 en staging | Diferencia de **esquema**, no de datos → pendiente de decisión |
| C3 | Taxonomía doble en la bóveda (PARA + MOC) | **Unificada** en un árbol (261 renombrados, 0 borrados) |
| C4 | 21 plugins de Obsidian desactivados | **Restaurados** (ver `SALUD_DEL_ECOSISTEMA`) |
| C5 | `Inteligencia de Campo` (destino de 3 de 5 metas del MAPA) | **No existe** en Notion ni Obsidian → pendiente de decisión |

---

## 4. LA BANDEJA DE APRENDIZAJE — AUDITORÍA

`Bandeja de Aprendizaje` (`bd8b76fb-1a2d-4f58-b7c1-ef9575e59bc9`), 5 propiedades:
`Titulo` · `Notas` · `Recibido` · `Estado` (Sin leer / Consumido / Descartado) ·
`Origen` (Alemán · Matemáticas · Programación · Radar · Crítica · Alemania · Inglés).

**26 entradas. Reparto: `Sin leer` 15 · `Descartado` 11 · `Consumido` 0.**

| Problema | Evidencia |
|---|---|
| Llega el **prompt**, no el resultado | 4 entradas son el texto de la automatización (`Actúa como un tutor de alemán…`) |
| La pasada del 18-10 16:56 **descartó resultados legítimos** | `Microservicios: modular apps`, `Anmeldung: Primer paso alemán!`, `New AI learning tools`, `No piensa sin IA?` pasaron de `Sin leer` a `Descartado` |
| 4 duplicados exactos | mismos títulos, 2 entradas cada uno |
| 18 de 26 sin origen trazable | solo los 8 *backfill* del 17-10 tienen `Notas` con el correo de origen |

**Regla aplicable:** *"Si la bandeja no se consume, se resta antes de sumar"*
→ con 0 consumidas, la decisión del 30-nov debe ser **reducir**, no añadir.

---

## 5. CLASIFICACIÓN DE COMPONENTES (resumen)

| Categoría | Nº | Ejemplos |
|---|---|---|
| CONSERVAR OPERATIVO | 24 | CENTRAL ACADÉMICA, PIPELINE, C1, MONITOR, LOGÍSTICA, BÓVEDA, RADAR TEMPORAL, ORDEN DE BATALLA, INVASIÓN SEMANAL, ARSENAL DE MATERIAS |
| CONSERVAR COMO ÍNDICE | 4 | `Resources` (1 de 4), Active Recall (→ Obsidian), `HOY.md`/`TABLERO_SEMANAL.md` |
| REUTILIZAR DISEÑO | 2 | patrón Minimalist PM (`Start/End Date` + `Progress` + `Task Remaining`) para RADAR TEMPORAL |
| MANTENER EN LABORATORIO | 13 | set universitario ×2, Student OS, `Tasks Manager` ×5, `Resources` ×3, `Notes`/`Meeting`/`Areas` |
| CANDIDATO A RETIRAR DE LA NAVEGACIÓN | 7 | `Tasks`, `Projects`, `Hábitos (1)`, `Income & Expenses`, `Priority matrix`, `Tareas` ×4 |
| SIN EQUIVALENTE | 3 | `Daily entries`, `Unified Database`, `Registro del sueño` |
| NO VERIFICADO | 4 | vistas, `aaaa`, filtros de Todoist, historial de ejecuciones |

---

## 6. VISOR DE TODOIST EN NOTION (diseño)

Flujo unidireccional, **solo lectura**:

```
Todoist ──GET /api/v1/tasks (cada 15 min)──► caché local ──upsert──► base Notion
```

- **Clave de deduplicación:** `Tarea ID` (texto), nunca editado.
- **Campos:** `Tarea ID` · `Tarea` · `Proyecto` · `Prioridad` · `Fecha límite` ·
  `Vencida` (fórmula) · `Etiquetas` · `Completada` · `Última sincronización`.
- **Nunca borra:** si una tarea desaparece, se marca y se deja para revisión manual.
- **Coste:** 4 llamadas/hora → 0 €. Límite oficial no publicado; terceros sitúan
  450–1000 req/15 min → margen de dos órdenes de magnitud.
- **Si falla:** el panel conserva la última foto buena y muestra su antigüedad.

**Lo que sí se puede mostrar con los datos verificados:** Hoy · Próximas ·
Vencidas · Por proyecto · Prioritarias. El cruce con entregables académicos
debe hacerse **por nombre**, no por ID (regla ya escrita en `CONTRATO_NOTION_TODOIST.md`).

> **Bloqueante:** hoy el destino (la Bandeja) es visible pero **Vibe escribe en otro
> espacio** y la base tiene 0 consumidas. Sin destino auditable no hay métrica
> de consumo, y sin métrica no hay Purga posible.

---

## 7. PENDIENTES DE DECISIÓN (.Admin)

1. **Universo `3d2b`** — fusionado en PIPELINE. ¿Se archiva el resto de duplicados
   (CENTRAL, MONITOR, CALENDARIO, HARDWARE) o se conservan?
2. **Esquema de MONITOR** — ¿se crean `Dieta`, `NoFap`, `Sueño >7h`,
   `Cumplimiento Hábitos` en producción para igualar a staging?
3. **"Inteligencia de Campo"** — 3 de 5 metas del MAPA apuntan a algo inexistente.
4. **F2 de la Bandeja** — el Organizador sigue descartando resultados válidos.
5. **`YA ENTREGADOS` vacío** en el prompt del Radar de Recursos → duplicados semanales.
6. **Colisión de las 17:00** — la carta de alemán llega a la misma hora que el
   bloque de consumo (17:00-18:00).
7. **Slots de Vibe** — "3 de 5 en uso" vs "quedan 2 libres" (incoherencia interna).

---

## 8. LIMITACIONES DE ESTA AUDITORÍA

- Sin acceso a los paneles de Grok ni de Vibe → **0 de 9 automatizaciones** verificables
  en ejecución. El conteo de 9 es una afirmación documental, no un hecho comprobado.
- Los **filtros de Todoist** no son verificables por API (404).
- Las **vistas** (Timeline, Tablero, In Progress, Feed) no son accesibles por API.
- La base `aaaa` sigue sin fuente de datos accesible (es una vista enlazada).
- No hay historial de ejecuciones en ninguna de las tres apps.
- Google emite los refresh tokens de Gmail/Drive con **7 días de vida** → sin
  reautorización semanal, el flujo Grok→Vibe→Notion se cae solo.
