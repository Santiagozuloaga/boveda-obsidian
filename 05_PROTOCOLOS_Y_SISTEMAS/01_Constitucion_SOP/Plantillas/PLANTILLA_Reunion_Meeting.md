---
tipo: reunion
fecha: <% tp.file.creation_date("YYYY-MM-DD") %>
creation_date: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
hora: ""
ubicacion: ""
estado: pendiente
tags: [reunion]
aliases: ["<% tp.file.title %>"]
---

# 🤝 <% tp.file.title %> — <% tp.file.creation_date("YYYY-MM-DD") %>

> Mínimo viable: 1 propósito + 1 decisión + 1 acción con dueño y fecha. XDA Meeting.

## 📋 Overview (XDA)
| Campo | Detalle |
|---|---|
| **Fecha / Hora** | <% tp.file.creation_date("YYYY-MM-DD") %> / ___ |
| **Ubicación** |  (presencial / Meet / Teams) |
| **Asistentes** |  ,  ,  |
| **Propósito** |  (1 línea) |
| **Facilitador** |  |

## 🎯 Agenda (timeboxed)
1. [ ] Tema 1 ( ___ min) — dueño: ___
2. [ ] Tema 2 ( ___ min) — dueño: ___
3. [ ] Tema 3 ( ___ min)

## 📝 Notas (captura rápida — ephemeral)
- 
- 


## ✅ Decisiones tomadas
| # | Decisión | Por qué | Impacto |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |

## 📌 Action Items (taskforge Tasks 📅⏫🔁 — tabla + checkboxes)
| ✅ | Tarea | Dueño | Vence | Prioridad | Recurrencia |
|---|---|---|---|---|---|
| [ ] |  | @___ | 📅 <% tp.date.now("YYYY-MM-DD", 1) %> | ⏫ |  |
| [ ] |  | @___ | 📅 <% tp.date.now("YYYY-MM-DD", 3) %> | 🔼 | 🔁 every week |

> Sintaxis Tasks: `- [ ] tarea 📅 YYYY-MM-DD ⏫` donde ⏫=alta 🔼=media 🔽=baja ⏬=mínima 🔁=recurrencia 🏁=fecha inicio

- [ ] Enviar minuta a @___ 📅 <% tp.date.now("YYYY-MM-DD") %> ⏫
- [ ] Seguimiento decisión #1 📅 <% tp.date.now("YYYY-MM-DD", 7) %> 🔁 every 2 weeks

## 🔗 Conexiones & Follow-up
- Proyecto vinculado: [[10.02 MONOGRAFIA/_MOC_MONOGRAFIA|Monografía]] / [[03_PROGRAMACION_Y_LOGICA/_MOC_CODIGO]]
- Próxima reunión: [[<% tp.date.now("YYYY-MM-DD", 7) %>|Revisión]]
- Notas relacionadas: ___ porque ___

---
```dataview
TASK
WHERE file.name = this.file.name
AND !completed
SORT priority DESC
```
