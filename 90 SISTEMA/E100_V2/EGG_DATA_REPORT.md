<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# EGG_DATA_REPORT — Estado de las bases

## 1. Inventario verificado
| Base | Props | Filas | Estado |
|---|---|---|---|
| CENTRAL ACADÉMICA | 15 | 5 | Funcional, con huecos |
| Active Recall (AR) | 7 | 6 | Funcional |
| PROYECTO C1 | 7 | 9 | 1 objetivo + 8 KR |
| PIPELINE DE ENTREGABLES | 8 | 1 | **Insuficiente** |
| MONITOR DE INTEGRIDAD | 13 | 1 | **Parado** |
| LOGÍSTICA FINANCIERA | 11 | 1 | **Incompleto** |
| BÓVEDA DE EVIDENCIAS | 9 | 0 | **Vacía** |
| MANTENIMIENTO DE HARDWARE | 8 | 0 | **Vacía** |
| RADAR TEMPORAL | 6 | 2 | **1 fila TEST** |
| ARSENAL DE MATERIAS | 6 | 6 | Funcional |
| ORDEN DE BATALLA | 7 | 4 | Histórico/Parcial |
| LOG DE INTERFERENCIA | 8 | 0 | **Vacía** |
| CALENDARIO DE VIDA | 4 | 1 | **Encoding roto** |
| ACTIVE RECALL | 7 | 6 | Funcional |

## 2. CENTRAL ACADÉMICA — 5 filas
| Materia | Nivel | Completadas/Total | Barra |
|---|---|---|---|
| Programacion | III | 6/8 | 75% |
| Geografia | II | 3/10 | 30% |
| Matematicas | I | sin datos | 0% |
| Quimica | I | sin datos | 0% |
| Fisica | I | sin datos | 0% |

3 de 5 materias tienen `Total` y `Completadas` vacíos. Sin esos números el porcentaje y la barra mienten: dicen 0% cuando en realidad se desconoce. **No inventar datos**: solo Programación y Geografía tienen actividad real.

## 3. PROYECTO C1 — 9 filas
8 Key Results con `Estado` = `Pendiente`:
B2 (Avanzado), B1 (Intermedio), A2 (Elemental), Relativsätze, Passiv, Konjunktiv II, Dativ, Akkusativ.
+ 1 fila **sin título** (`3dcb38a4-c0ce-81c3-...`), no se modificó.
Todos los `Progreso %` estaban vacíos; se rellenaron a 0 (ver trazabilidad).
**Agregados 3 KRs del roadmap real**: A2, B1, B2 (pendientes). A1 está "En progreso" (excluido).

## 4. PIPELINE DE ENTREGABLES — el problema real
Única fila: `Parcial de Cálculo (prueba)`, Estado `ENTREGADO`, nota 4.5, ponderada 0.9, peso 20%.
Pero CENTRAL declara **8 entregas en Programacion** y **10 en Geografia**.
El pipeline no refleja la realidad de la uni. O se migran las entregas reales, o se acepta que el pipeline es un experimento abandonado.
**Decisión**: Pipeline debe reflejar entregas reales de CENTRAL. No inventar datos.

## 5. MONITOR DE INTEGRIDAD — parado
Única fila: `2026-09-19 Demo`. Estado: «PELIGRO CRÍTICO».
Cumplimiento 0.71, Barra 4/5, Racha 5.
Campos `Energía`, `Horas de Sueño`, `Vector de Ataque Externo` y `Traducción Shard` vacíos.
**13 días de retraso** respecto a la fecha de esta auditoría.
**Bug de encoding**: `🔥` se muestra como `????` en API. Revisar encoding de propiedad.

## 6. LOGÍSTICA FINANCIERA — incompleto
Única fila `Septiembre 2026`: Gastado 1200, Presupuesto 5000, Ahorro Acumulado 5604, Restante 3800, Meta 11208.
Faltan las filas de **Octubre** y **Noviembre 2026**.
Campos `Ingreso`, `Progreso Sperrkonto`, `Gastos Universitarios` y `Notas` vacíos.
**No inventar octubre/noviembre**: solo registrar cuando haya datos reales.

## 6. CALENDARIO DE VIDA — encoding roto
Propiedades con caracteres rotos: `D�a`, `Energ�a`, `Micro-auditor�a`.
3 propiedades con mojibake en API. Verificar si es solo representación API o dato corrupto en Notion.
**No renombrar hasta determinar causa**.

## 7. RADAR TEMPORAL — dato TEST
Contiene fila `aaa` → clasificar como **TEST DATA EN PRODUCCIÓN**. No borrar, marcar.

## 7. BÓVEDA DE EVIDENCIAS / MANTENIMIENTO / ARSENAL / ORDEN / LOG / CALENDARIO
- BÓVEDA DE EVIDENCIAS: 0 filas — **vacía legítima** (no hay evidencias que registrar).
- MANTENIMIENTO DE HARDWARE: 0 filas — **vacía legítima**.
- ARSENAL DE MATERIAS: 6 filas — funcional.
- ORDEN DE BATALLA: 4 filas — histórico/parcial (feb 2026). Requiere limpieza.
- LOG DE INTERFERENCIA: 0 filas — vacía legítima.
- CALENDARIO DE VIDA: 1 fila TEST-VERIFY → dato TEST.

## 8. Active Recall — Zettel Cards
6 tarjetas totales (3 originales + 3 nuevas).
Nuevas: Física (Q=mcΔT + 1ª ley), Química (nomenclatura IUPAC dienos/trienos), Matemáticas (dominio/rango función racional).
Relaciones `Materia` → páginas reales de CENTRAL ACADÉMICA (no texto).

## 9. Campos vacíos por base (resumen)
| Base | Campos con celdas vacías |
|---|---|
| CENTRAL | Profesor (5/5), Horario Tutorias (5/5), Estado (3/5), Total (3/5), Creditos (5/5), Nota Actual (5/5) |
| AR | Dificultad (3/6), Tipo (3/6), Proximo Repaso (3/6) |
| C1 | Progreso % (9/9), Fecha (9/9), Tipo (9/9), Notas (9/9) |
| PIPELINE | Tipo (1/1), Fecha Limite (1/1) |
| MONITOR | Energía, Vector, Estado, Sueño, Traducción (todas) |
| LOGÍSTICA | Ingreso, Progreso, Meta, Notas, Gastos Uni (todas) |
| CALENDARIO | Encoding roto (3 props) |

## 9. Nota metodológica
`Profesor`, `Horario Tutorias`, `Creditos` y `Nota Actual` están vacías en las 5 materias. No se rellenaron: son datos académicos que no se pueden derivar. **No inventar datos académicos**.

---

## 10. Resumen de acciones requeridas (P0/P1)

| Prioridad | Acción | Responsable |
|---|---|---|
| P0 | Corregir encoding Calendario de Vida | OpenCode (Notion API) |
| P1 | Migrar Pipeline con entregas reales de Central | Usuario + OpenCode |
| P1 | Reactivar Monitor con datos reales diarios | Usuario |
| P1 | Completar Logística Financiera (Oct/Nov + campos vacíos) | Usuario |
| P1 | Corregir encoding Calendario (API vs dato) | OpenCode/Notion |
| P1 | Limpiar ORDEN DE BATALLA (histórico vs activo) | Usuario + OpenCode |
| P1 | Marcar datos TEST/DEMO claramente | OpenCode |
| P2 | Poblar Proyecto C1 con 3 KRs roadmap (A2/B1/B2) | Hecho |
| P2 | Active Recall: 3 tarjetas nuevas (Física, Química, Matemáticas) | Hecho |
| P2 | Central: agregar Física/Química/Matemáticas (solo título) | Hecho |
| P3 | Estandarizar nombres (tildes, sin sufijos numéricos) | Pendiente |
| P3 | Unificar versión Dashboard (V.5.3) | Pendiente |