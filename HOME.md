---
cssclasses: [dashboard, banner]
banner: "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1200&h=280&fit=crop"
obsidianUIMode: preview
---

# 🏠 HOME — Puerta del Segundo Cerebro

> [!quote] **Pensar aquí. Gestionar en Notion. Ejecutar en Todoist.**

> [!info] 🧭 **Navegación**
> **Tablero:** [[07_TABLERO/HOY|HOY]] · [[07_TABLERO/TABLERO_SEMANAL|Semana]] · [[07_TABLERO/Tubería Zettel.canvas|Tubería]] • **Vida:** [[01_DIARIO_DE_GUERRA/CALENDARIO_DE_VIDA|Vida]] · [[01_DIARIO_DE_GUERRA/_MOC_DIARIO|Diario]]
> **MOCs:** [[02_ALEMANIA_ZETTELKASTEN/03_MOC_Aleman/_MOC_ALEMAN|🇩🇪 Alemán C1]] · [[03_PROGRAMACION_Y_LOGICA/03_Snippets_Codigo/_MOC_CODIGO|💻 Código]] · [[03_PROGRAMACION_Y_LOGICA/01_Matematicas_y_Fisica/_MOC_CIENCIAS|🔬 Ciencias]] · [[04_LITERATURA_Y_FUENTES/01_Papers_e_Investigacion/_MOC_FUENTES|📚 Fuentes]] · [[06_FE_Y_FILOSOFIA/_MOC_FE|✝️ Fe]] · [[05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/_MOC_PROTOCOLOS|⚙️ Protocolos]] • **Inbox:** [[00_INBOX_TEMPORAL/_MOC_INBOX|📥 Inbox 48h]]

> [!tip] ⚡ **Acciones — 1 clic**
> `Ctrl+P` → **Daily notes: Open today's daily note** · **Templater: Insert template** (`Apunte` / `Libro` / `Reunión`) · **Random note** · buscar `Ctrl+Shift+F`
> *Captura en [[00_INBOX_TEMPORAL/_MOC_INBOX|Inbox]] → destila 1/día → mueve a MOC con `[[link]]`*

---

## 📅 Hoy

```dataview
TABLE WITHOUT ID file.link AS "📅 Hoy", energia AS "Energía", x_ganada AS "X"
FROM "01_DIARIO_DE_GUERRA/01_Daily_Logs"
WHERE file.name = string(date(today))
LIMIT 1
```

> Si no existe daily hoy: `Ctrl+P` → *Daily notes: Open today's daily note* (Templater aplica la plantilla V2 solo).

---

## 🚀 Proyectos activos

```dataview
TABLE WITHOUT ID file.link AS "Proyecto", estado AS "Estado"
FROM ""
WHERE tipo = "proyecto" AND estado = "activo" AND !contains(file.path, "01_Constitucion_SOP")
SORT file.mtime DESC
LIMIT 10
```

*Flujo: [[07_TABLERO/Tubería Zettel.canvas|Tubería]] (Inbox → MOC → Evergreen)*

---

## 📝 Reciente

```dataview
TABLE WITHOUT ID file.link AS "Nota", dateformat(file.mtime, "yyyy-MM-dd") AS "Tocada"
FROM ""
WHERE file.name != "HOME"
SORT file.mtime DESC
LIMIT 7
```

---

> [!quote] 🔒 Regla de oro E-100
> **Notion para gestionar · Obsidian para pensar · Todoist para ejecutar hoy.** [[05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/S.O.P. V 5.0|S.O.P. V5.3]]
