---
tipo: proyecto
subtipo: software/learning
estado: activo
inicio: <% tp.file.creation_date("YYYY-MM-DD") %>
creation_date: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
stack: ""
tags: [proyecto, software]
aliases: ["<% tp.file.title %>"]
---

# 🧪 <% tp.file.title %>

> Mínimo viable: 1 objetivo + 1 stack + 1 comando que funciona. XDA Software + vaultorial.

## 🎯 Objetivo (1 línea — E-100)
- 

## 📐 Scope / No-Scope
| Dentro del scope | Fuera del scope |
|---|---|
|  |  |
|  |  |

## 🔑 Keys / Stack (XDA Software — lo que debo saber)
| Concepto | Definición en mis palabras | Link |
|---|---|---|
|  |  | ___ |
|  |  | ___ |

**Stack:** `lenguaje:` ___ | `framework:` ___ | `DB:` ___ | `infra:` ___

## 🔄 Workflows (paso a paso — vaultorial)
1. Setup → ___
2. Build → ___
3. Test → ___
4. Deploy → ___

```mermaid
graph LR
A[Setup] --> B[Build] --> C[Test] --> D[Deploy]
```

## 💻 Commands (código ejecutable — snippets)
```bash
# setup

```
```python
# snippet mínimo reproducible
```
```bash
# test / run
```

## 🐞 Bugs y soluciones (mínimo reproducible — E-100)
| Bug | Causa | Solución | Fecha |
|---|---|---|---|
|  |  |  | <% tp.file.creation_date("YYYY-MM-DD") %> |

## 📓 Aprendizajes / Postmortem (1 victoria + 1 lección)
- **Victoria:** 
- **Lección:** 
- **Próximo experimento:**  📅 <% tp.date.now("YYYY-MM-DD", 7) %> ⏫

## ✅ Tareas del proyecto (Tasks 📅⏫🔁)
- [ ] Setup entorno 📅 <% tp.file.creation_date("YYYY-MM-DD") %> ⏫
- [ ] MVP 1 feature 📅 <% tp.date.now("YYYY-MM-DD", 7) %> 🔼
- [ ] Documentar en [[03_PROGRAMACION_Y_LOGICA/03_Snippets_Codigo/_MOC_CODIGO|MOC Código]] 📅 <% tp.date.now("YYYY-MM-DD", 14) %> 🔁 every 2 weeks

## 🔗 Conexiones (E-100 — frase de enlace)
- Este proyecto conecta con ___ porque ___
- MOC: [[03_PROGRAMACION_Y_LOGICA/03_Snippets_Codigo/_MOC_CODIGO|Programación]] — por qué importa: ___
- Fuente: [[04_LITERATURA_Y_FUENTES/03_Documentacion_Oficial/___|Doc Oficial]]

---
```dataview
TASK FROM "03_PROGRAMACION_Y_LOGICA"
WHERE contains(file.path, this.file.name) OR file.folder = this.file.folder
AND !completed
SORT due ASC
LIMIT 10
```
