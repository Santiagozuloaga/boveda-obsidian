# 🤖 PROTOCOLO JARVIS: INTEGRACIÓN DEL AGENTE IA CON LA BÓVEDA

**Objetivo:** Que un agente IA local (estilo JARVIS) actúe como segundo cerebro autónomo sobre la bóveda.

---

## 🧠 POR QUÉ OBSIDIAN ES EL HOGAR DEL JARVIS

1. **Acceso directo al filesystem:** Texto plano .md, lectura/escritura en milisegundos.
2. **Estructura semántica `[[ ]]`:** La IA navega la red de conceptos como una red neuronal.
3. **Privacidad absoluta:** Los datos nunca salen de la máquina.

---

## 🔌 CAPAS DE CONEXIÓN

### A. Capa de Lectura (RAG Local)
- El agente escanea carpetas (ej. `03_PROGRAMACION_Y_LOGICA`), busca el .md del concepto y responde usando TUS palabras.

### B. Capa de Escritura Autónoma
- El agente puede crear/modificar archivos en carpetas específicas:
 - **Inbox:** ideas rápidas → `00_INBOX_TEMPORAL/YYYY-MM-DD_idea.md`
 - **Diario:** resumen de progreso → `01_DIARIO_DE_GUERRA/`
 - **Código:** snippets explicados → `03_PROGRAMACION_Y_LOGICA/03_Snippets_Codigo/`

---

## 📦 REQUISITOS DEL BACKEND IA
- **Python File System (os/pathlib):** listar, leer, escribir .md
- **Búsqueda (grep / vector search):** encontrar notas en el Zettelkasten
- **Frontmatter limpio:** toda nota nueva con `date: YYYY-MM-DD`, `tags: [...]`

---

## ⚡ REGLAS PARA EL AGENTE
1. **Leer antes de escribir** (evitar conflictos).
2. **Nunca borrar** sin confirmación de Admin.
3. **Respetar la estructura M.O.C.** (cada dato en su zona).
4. **Conectar** toda nota nueva con `[[ ]]` — nunca dejar puntos aislados.
5. **Frontmatter obligatorio** en notas de conocimiento.

---

**Conclusión:** Obsidian da la memoria al JARVIS; Admin da la dirección táctica. Juntos forman el Cerebro de Acero.