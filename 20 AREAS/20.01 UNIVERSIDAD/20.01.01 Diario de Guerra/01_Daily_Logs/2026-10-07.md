---
tipo: daily
fecha: <% tp.date.now("YYYY-MM-DD") %>
estado: abierto
energia: 0.0
x_ganada: false
tags: [daily]
---

# 📅 <% tp.date.now("dddd MMMM DD, YYYY", 0, tp.file.title, "YYYY-MM-DD") %>

<< [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>|⬅️ Ayer]] | [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>|Mañana ➡️]] >>

---

## 🎯 Foco (Top 3 — si solo haces 3 cosas, estas)
- [ ] 🔥 #1  📅 <% tp.date.now("YYYY-MM-DD") %> ⏫
- [ ] #2 📅 <% tp.date.now("YYYY-MM-DD") %>
- [ ] #3 📅 <% tp.date.now("YYYY-MM-DD") %>

## 🧠 Captura (sin filtrar, se procesa en revisión)
-
-

## 💭 Reflexión (noche, 2 min)
- Gratitud (1):
- Lección (1):

## 🛡️ Cierre E-100
- [ ] Micro-auditoría: evento del día ¿depende de mí? NO → silencio. SÍ → contramedida: ___
- [ ] MCs liquidadas: ___
- [ ] Energía: ___ /1.0 (X exige ≥ 0.7)
- **X de hoy:** ☐ → ☒
- Una línea: ___

## 🔗 Enlaces
- MOCs: [[02_ALEMANIA_ZETTELKASTEN/03_MOC_Aleman/_MOC_ALEMAN|MOC Alemán]] · [[03_PROGRAMACION_Y_LOGICA/03_Snippets_Codigo/_MOC_CODIGO|MOC Código]] · [[01_DIARIO_DE_GUERRA/_MOC_DIARIO|MOC Diario]]
- [[05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/S.O.P. V 5.0]] | [[01_DIARIO_DE_GUERRA/CALENDARIO_DE_VIDA|Vida]] | [[07_TABLERO/TABLERO_SEMANAL|Semana]]

```dataview
TABLE WITHOUT ID file.link AS "Tocada hoy", file.folder AS "Carpeta"
FROM ""
WHERE file.mday = date("<% tp.date.now("YYYY-MM-DD") %>")
SORT file.mtime DESC
LIMIT 10
```
