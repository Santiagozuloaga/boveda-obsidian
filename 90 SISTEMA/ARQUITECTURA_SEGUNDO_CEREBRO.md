# 🏛️ ARQUITECTURA DEL SEGUNDO CEREBRO E-100
**Versión:** 2.0 | **Fecha:** 2026-09-23 | **Estado:** VERIFICADO en uso

## Qué es
Obsidian es donde Admin **aprende, piensa, conecta, investiga, documenta, escribe, recupera y reutiliza**. No gestiona (Notion), no ejecuta el día (Todoist).

## Reglas (todas las que hay)
1. **Captura sin decidir**: idea → `00_INBOX_TEMPORAL`, sin carpeta ni tags obligatorios.
2. **Nota útil = 4 props + palabras propias + 2–3 `[[ ]]`**. Sin eso, es borrador.
3. **1 MOC por materia/proyecto** como índice curado (Alemán C1, Código, Ciencias, Fuentes, Diario, Fe, Protocolos).
4. **Frontmatter mínimo**: `tipo, materia, fecha, estado` (+ lo que el Tracker exige en dailies). Tags ≤ 8 funcionales.
5. **Todo template se inserta vía Templater** (`Ctrl+P` → *Templater: Insert template*). No existe otro mecanismo.
6. **Dailies**: creación vía core Daily notes + *Insert template* manual (determinístico; el auto-trigger está inactivo, ver memoria §16-17). Weeklies manuales desde plantilla.
7. **Revisión semanal 15 min**: Inbox → MOC o borrar. Inbox que no se vacía es basurero.
8. **Gamificación opcional y subordinada**: XP/niveles/rachas motivan, nunca obligan.

## Carpetas (7, planas, buckets estables)
`00_INBOX_TEMPORAL` · `01_DIARIO_DE_GUERRA` · `02_ALEMANIA_ZETTELKASTEN` · `03_PROGRAMACION_Y_LOGICA` · `04_LITERATURA_Y_FUENTES` · `05_PROTOCOLOS_Y_SISTEMAS` · `06_FE_Y_FILOSOFIA` · `07_TABLERO` · `10.02 MONOGRAFIA` · `90 SISTEMA`

## Tipos de notas y plantillas
| Tipo | Plantilla | Dónde nace |
|---|---|---|
| daily | PLANTILLA_Daily_Note | auto (core + Templater) |
| apunte | PLANTILLA_Apunte | Inbox (auto) |
| clase | PLANTILLA_Clase | manual Templater |
| vocabulario | PLANTILLA_Vocabulario_Aleman | `02_.../02_Vocabulario` (auto) |
| fuente/libro | PLANTILLA_Fuente / Libro | Papers/Resúmenes (auto) |
| reunión | PLANTILLA_Reunion_Meeting | manual Templater |
| proyecto | PLANTILLA_Proyecto / Proyecto_Software | manual Templater |
| semanal/mensual/anual | PLANTILLA_Revision_Semanal... | manual Templater |
| MOC/ensayo | PLANTILLA_MOC / Ensayo | manual Templater |

## HOME
Mapa, no consola: navegación + hoy + proyectos activos + reciente. Lo administrativo vive en `Control Panel`.

## Paleta aprobada (intacta)
Fondo `#0b0b11` · Oro `#f0b429` · Hueso `#ece7dd` · Platino `#c9cdd4` · Rojo `#ff3b3b` · Azul `#6cb2ff`. Semántica, no decorativa.

## Constitución de frontmatter (mínima, derivada de queries reales)
- Núcleo (toda nota útil): `tipo, estado, fecha, materia`.
- Dailies (+Tracker): `energia, x_ganada, tags:[daily]`.
- Dominio: libros `autor/año/rating/formato`, proyectos `inicio/stack`, reuniones `hora/ubicacion`.
- Regla: ningún campo que ningún query, template o flujo consuma.
