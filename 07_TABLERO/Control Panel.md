---
cssclasses: [dashboard]
type: dashboard
tags: [dashboard, kpi, dataview]
obsidianUIMode: preview
---

# 🎛️ Control Panel — KPIs E-100 (niámoš style)

> *Dataview + Tasks + Tracker · Solo lectura · Actualización viva · Pensar aquí, gestionar en Notion, ejecutar en Todoist*

> [!info] Jump — igual que HOME
> [[HOME|🏠 HOME]] · [[07_TABLERO/HOY|HOY]] · [[07_TABLERO/TABLERO_SEMANAL|Semana]] · [[07_TABLERO/Tubería Zettel.canvas|Tubería]] · [[01_DIARIO_DE_GUERRA/CALENDARIO_DE_VIDA|Vida]] · [[90 SISTEMA/Vaultorial_Index|Vaultorial Index]]

## 📊 KPIs — Hoy (niámoš 5 cards)

> [!tip] KPIs vivos (Dataview + Tasks)
> Copia este bloque a HOME si quieres KPIs arriba. Cada número es query, no manual.

| KPI | Valor (auto) | Dónde vive |
|---|---|---|
| **Inbox 48h** | `00_INBOX_TEMPORAL` pendiente de destilar | `[[00_INBOX_TEMPORAL/_MOC_INBOX]]` |
| **Proyectos activos** | contados abajo | `tipo: proyecto + estado: activo` |
| **Tasks hoy** | Tasks due today | Bloque HOME 1 |
| **Energía 14d avg** | Tracker frontmatter `energia:` | `01_DIARIO_DE_GUERRA/01_Daily_Logs` |
| **Dailies este mes** | conteo mes | `Dailies.base` |

```dataview
TABLE WITHOUT ID length(rows) AS "KPI"
FROM "00_INBOX_TEMPORAL"
GROUP BY true
```
*↳ Número de notas en Inbox (debe → 0 cada noche)*

```dataview
TABLE WITHOUT ID length(rows) AS "Activos"
FROM ""
WHERE tipo = "proyecto" AND estado = "activo" AND !contains(file.path, "01_Constitucion_SOP")
GROUP BY true
```

```tasks
not done
due today
path does not include 05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP
short mode
```

*Si no ves Tasks arriba, verifica plugin `obsidian-tasks-plugin` 8.4.0 activo (ver `.obsidian/community-plugins.json` + `data.json` con `useFilenameAsScheduledDate=false`).*

---

## 🚀 Proyectos — Salud (Gantt ready)

```dataview
TABLE WITHOUT ID file.link AS "Proyecto", estado AS "Estado", inicio AS "Inicio", stack AS "Stack", dateformat(file.mtime, "MM-dd") AS "Upd"
FROM "03_PROGRAMACION_Y_LOGICA" OR "10.02 MONOGRAFIA"
WHERE tipo = "proyecto"
SORT estado ASC, file.mtime DESC
```

```dataview
TABLE WITHOUT ID file.link AS "Proyecto", length(filter(file.tasks, (t) => !t.completed)) AS "Tasks abiertas"
FROM "03_PROGRAMACION_Y_LOGICA"
WHERE tipo = "proyecto"
SORT length(filter(file.tasks, (t) => !t.completed)) DESC
LIMIT 7
```

---

## 🎯 Tareas — Deuda total

```tasks
not done
path does not include 05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP
group by due
sort by due
limit 20
short mode
```

```dataview
TASK
WHERE !completed
GROUP BY file.folder
SORT length(rows) DESC
LIMIT 8
```

*↳ Por carpeta — dónde se acumula deuda*

---

## 📝 Actividad — Últimos 14 días

```dataview
TABLE WITHOUT ID file.link AS "Nota", file.folder AS "Carpeta", dateformat(file.mtime, "yyyy-MM-dd HH:mm") AS "Modificado"
FROM ""
SORT file.mtime DESC
LIMIT 14
```

```dataview
TABLE WITHOUT ID file.link AS "Día", energia AS "⚡", x_ganada AS "X", length(file.tasks) AS "#tasks"
FROM "01_DIARIO_DE_GUERRA/01_Daily_Logs"
SORT file.name DESC
LIMIT 14
```

---

## 📈 Energía — Tracker (copia a CALENDARIO_DE_VIDA)

```tracker
searchType: frontmatter
searchTarget: energia
folder: 01_DIARIO_DE_GUERRA/01_Daily_Logs
startDate: 2026-09-01
endDate: 2026-09-30
line:
    title: Energía diaria (0.0–1.0)
    yMin: 0
    yMax: 1
    showPoint: true
    lineColor: "#f0b429"
    pointColor: "#f0b429"
    pointBorderColor: "#0b0b11"
bar:
    title: X ganada (0/1)
    showLegend: false
```

---

## 🔥 Zettelkasten — Pipeline (vaultorial 14 notas demo)

```dataview
TABLE WITHOUT ID file.link AS "MOC", length(rows) AS "Notas vinculadas"
FROM ""
WHERE contains(file.path, "_MOC_")
GROUP BY file.link AS "MOC"
SORT length(rows) DESC
```

```dataview
TABLE WITHOUT ID file.link AS "Nota", file.folder AS "Etapa"
FROM "00_INBOX_TEMPORAL" OR "04_LITERATURA_Y_FUENTES" OR "03_PROGRAMACION_Y_LOGICA" OR "02_ALEMANIA_ZETTELKASTEN"
SORT file.mtime DESC
LIMIT 10
```

*Etapas: `00_INBOX_TEMPORAL` (Fleeting) → `04_LITERATURA_Y_FUENTES` (Literature) → MOCs (Permanent). Ver `90 SISTEMA/Vaultorial_Index.md`.*

---

## 🛡️ Auditoría — Semana (para TABLERO_SEMANAL)

```dataview
TABLE WITHOUT ID file.link AS "Semana", energia AS "Avg Energía", x_ganada AS "X"
FROM "01_DIARIO_DE_GUERRA/04_Revisiones"
WHERE contains(file.name, "W") OR tipo = "revision"
SORT file.name DESC
LIMIT 8
```

> [!example] Checklist dominical (10 min — copia a `PLANTILLA_Revision_Semanal`)
> - [ ] X/7 = __  · Energía avg __ · 1 victoria __ · 1 lección __
> - [ ] Inbox = 0? · Tubería movida? · MOC enlaces +1?
> - [ ] Próximas 3 prioridades con `📅` y `⏫`

---

## 📚 Fuentes — Bookshelf (vaultorial book-notes)

```dataview
TABLE WITHOUT ID file.link AS "📚 Libro", autor AS "Autor", estado AS "Estado", rating AS "★", file.mtime AS "Upd"
FROM "04_LITERATURA_Y_FUENTES"
WHERE tipo = "fuente" AND formato = "libro"
SORT rating DESC, file.mtime DESC
LIMIT 10
```

```dataview
TABLE WITHOUT ID status AS "Estado", length(rows) AS "Libros"
FROM "04_LITERATURA_Y_FUENTES"
WHERE tipo = "fuente"
GROUP BY status AS "status"
SORT length(rows) DESC
```

---

> [!quote] S.O.P. V5.3 — Regla de oro
> **Nada suelto. Cada dato tiene su lugar.** [[05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/S.O.P. V 5.0|S.O.P.]] · [[90 SISTEMA/Vaultorial_Index|Vaultorial 18]] · [[HOME|HOME 3 bloques]]

*Generado 2026-09-19 · Tasks `useFilenameAsScheduledDate=false` · Periodic `daily YYYY-MM-DD @ 01_DIARIO_DE_GUERRA/01_Daily_Logs` `weekly gggg-[W]ww @ 04_Revisiones`*
