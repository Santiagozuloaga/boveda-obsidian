---
type: decision-log
tags: [decisiones, e100, notion, 3d2b, admin]
fecha: 2026-10-18
estado: pendiente-de-decision
autor: Admin
---

# DECISIONES PENDIENTES DEL ADMIN — MISIÓN DE RECONCILIACIÓN

> Registro vivo. Ninguna de estas decisiones se ha ejecutado en Notion.
> Notion permanece en **SOLO LECTURA** hasta autorización específica.

---

## D1 — Universo `3d2b` (PRODUCCIÓN vs STAGING)

**Estado:** ✅ FUSIONADO (2026-10-18) · solo PIPELINE escribiria datos

**El hallazgo.** Hay dos juegos de bases con los mismos nombres. Producción
muestra el juego `3d2b38a4-*`, que está **por detrás** en datos:

| Base | Producción (`3d2b`) | Staging | Diferencia |
|---|---|---|---|
| PIPELINE DE ENTREGABLES | **1 fila**, 7 props | `033b…` **12 filas**, 8 props | staging tiene 11 entregables más |
| MONITOR DE INTEGRIDAD 2.0 | **13 props** | `cd1b…` **16 props** | faltan `Dieta`, `NoFap`, `Sueño >7h` |
| Active Recall - Zettel | **6 props** | `2e3b…` **7 props** | falta `Materia` |
| CALENDARIO DE VIDA | `3d3b…` | `046b…` | equivalentes |
| PROYECTO C1 | `3d2b…` 9 filas | `19ab…` 9 filas | equivalentes |
| LOGÍSTICA | `3d2b…` 11 props | `3e5b…` 11 props | equivalentes |

**Por qué bloquea.** La promoción de `THE EGG-NETWORK prueba` a producción
consolidaría la **copia degradada**. Además, `PIPELINE` con 1 fila es
incompatible con la función declarada (seguimiento de entregables).

**OpcionesNIC_ADMIN:**

| Opción | Qué implica | Riesgo |
|---|---|---|
| A. Fusionar staging → producción | Copiar las 12 filas sobre la 1 | Bajo: staging conserva el original |
| B. Archivar `3d2b` | La 1 fila queda en histórico | Bajo |
| C. No hacer nada | Se sigue operando con datos degradados | **Alto** |

**Prerrequisito de A:** revisar visualmente esa única fila de `PIPELINE 3d2b`
y confirmar que no contiene nada que no esté en las 12 de staging.

**Mi recomendación:** A, tras eserequisito.

---

## D2 — Taxonomía de Obsidian — **EJECUTADA** ✅

**Estado:** aplicada el 2026-10-18. Rollback: `git reset --hard 164bc75`

Fusionados el MOC universitario y PARA en un árbol único. **0 notas borradas,
261 renombrados.**

- MOC universitario → `20 AREAS/20.01 UNIVERSIDAD/20.01.01` … `20.01.08`
- `07_TABLERO` + `08 AGENTES` → `80 OPERATIVO/`
- `00_INBOX_TEMPORAL` → fusionado dentro de `00 ENTRADA (Inbox)/`
- `20.01 SOP V2.5` → renombrada a `20.02 SOP V2.5` (colisión de numeración)
- Registrado en `AGENTS.md` (bóveda y proyecto) y en
  `2026-10-18_UNIFICACION_TAXONOMIA_OBSIDIAN.md`

---

## D3 — Gestor de Contraseñas Español

**Estado:** ⛔ PENDIENTE

Base `2f1b38a4…8150` con 9 filas, 11 propiedades, incluida una propiedad
literalmente llamada **`Contraseña`** y otra `Respuesta de Seguridad`.

Notion no cifra ese campo. Si contiene datos reales, están en texto plano.

**Pendiente de Admin:** ¿compruebo si son datos reales o datos de ejemplo de la
plantilla? Solo lectura, sin mostrar valores.

---

## D4 — Qué sale de la navegación operativa

**Estado:** ⛔ PENDIENTE · propuesta reversible

7 candidatos a ocultar **sin borrar nada**:

`Tasks` · `Tasks Manager` ×5 · `Projects`/`Proyectos` · `Hábitos (1)` ·
`Income & Expenses` · `Priority matrix` · `Tareas` ×4

Duplican a Todoist (11 tareas), `PIPELINE` (12 entregables), `MONITOR` (16 props)
y `LOGÍSTICA` (11 props).

**Recomendación:** ocultar de la navegación, **conservar intactos**. Reversible
en un clic, riesgo cero.

---

## Lo que NO se hizo en esta misión

- 0 escrituras en Notion (ni propiedades, ni vistas, ni bases, ni archivos)
- 0 sincronizaciones con Todoist
- 0 borrados en la bóveda
- 0 cambios en proyectos, etiquetas o filtros de Todoist
