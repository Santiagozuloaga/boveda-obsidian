![Obsidian](https://img.shields.io/badge/Obsidian-000000?style=for-the-badge&logo=obsidian&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![PARA](https://img.shields.io/badge/M%C3%A9todo-PARA-blue?style=for-the-badge)
![Español](https://img.shields.io/badge/idioma-español-red?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

# 🧠 Mente Maestra E-100 — Segundo Cerebro (Obsidian)

> **Pensar aquí · Gestionar en Notion · Ejecutar en Todoist**  
> Bóveda de conocimiento personal bajo el método **PARA** y el sistema de organización digital **E-100**.  
> Segunda cabeza privada: notas atómicas, interconexión total (`[[enlaces]]`), Zettelkasten académico y protocolo E-100.

---

## 📖 Tabla de Contenidos

- [¿Qué es esta bóveda?](#-qué-es-esta-bóveda)
- [Estructura PARA](#-estructura-para)
- [MOC Universitario (20 AREAS / 20.01 UNIVERSIDAD)](#-moc-universitario)
- [La Trinidad de Herramientas](#-la-trinidad-de-herramientas)
- [Flujo de Trabajo E-100](#-flujo-de-trabajo-e-100)
- [Reglas de Oro](#-reglas-de-oro)
- [Nomenclatura ISO-SAGE](#-nomenclatura-iso-sage)
- [Cómo clonar y usar en GitHub](#-cómo-clonar-y-usar-en-github)
- [`.gitignore` sugerido](#-gitignore-sugerido)
- [Filtros (intocables)](#-filtros-intocables)
- [Licencia](#-licencia)
- [Autor](#-autor)

---

## 📖 ¿Qué es esta bóveda?

Este repositorio es el **segundo cerebro personal** en formato Markdown/Obsidian. No es un gestor de tareas (eso es Todoist), ni una base operativa (eso es Notion), ni un campo de pruebas. Es el lugar donde se **piensa, se conecta ideas y se destila conocimiento**.

Está sincronizada con:
- **Notion** (`THE EGG-NETWORK`) — procesos, calendarios, sistemas, bases de datos operativas.
- **Todoist** — tareas pequeñas diarias y entregables con fecha.
- **Obsidian** (esta bóveda) — conocimiento profundo, Zettelkasten, método PARA.

---

## 🗂️ Estructura PARA

| Carpeta | Propósito |
|---------|-----------|
| `00 ENTRADA (Inbox)/` | Captura rápida. Regla 48h: todo lo que entra aquí se procesa, destila o se descarta en 48 horas. |
| `10 PROYECTOS/` | Proyectos activos con fecha de inicio y fin. |
| `20 AREAS/` | Áreas de responsabilidad permanente. Contiene el MOC universitario. |
| `30 RECURSOS/` | Material de referencia, libros, papers, documentación. |
| `40 ARCHIVOS X/` | Archivo muerto / proyectos completados. |
| `80 OPERATIVO/` | Estado vivo: tableros (`HOY`, `TABLERO_SEMANAL`), agentes, tubería Zettel. No es conocimiento, es operación. |
| `90 SISTEMA/` | Gobernanza, contratos, plantillas, memoria colectiva, informes de auditoría. |

---

## 🎓 MOC Universitario (20 AREAS / 20.01 UNIVERSIDAD)

El conocimiento académico vive dentro de `20 AREAS`, no en la raíz:

```
20.01.01 Diario de Guerra/        → dailies, post-mortem, shard
20.01.02 Alemán Zettelkasten/     → gramática, vocabulario, MOC (meta C1)
20.01.03 Programación y Lógica/   → matemáticas, física, estructuras, snippets
20.01.04 Literatura y Fuentes/    → papers, resúmenes, documentación
20.01.05 Protocolos y Sistemas/   → constitución SOP, PRNA, auditorías
20.01.06 Fe y Filosofía/          → escrituras, reflexiones, principios
20.01.07 Repaso STEM/             → repaso científico-técnico
20.01.08 Monografía/              → tesis Santiago Zuloaga Daza
```

Índices operativos en `80 OPERATIVO/07 TABLERO/` y `80 OPERATIVO/08 AGENTES/`.

---

## 🏛️ La Trinidad de Herramientas

| Herramienta | Rol | Ubicación |
|-------------|-----|-----------|
| **Notion** | Centro de operaciones "THE EGG-NETWORK" | Procesos, calendarios, BDs |
| **Obsidian** | Cerebro de Acero | Esta bóveda (`Mente Maestra E-100`) |
| **Todoist** | Arma de corto alcance | Tareas pequeñas de hoy |

> **Regla de oro:** Notion para gestionar, Obsidian para pensar, Todoist para ejecutar hoy. Nada suelto: cada dato tiene su lugar.

---

## 🔄 Flujo de Trabajo E-100

```
CAPTURA (5 seg, cero fricción)
  idea → 00_INBOX_TEMPORAL → cerrar
              ↓ (revisión semanal, 15 min)
PROCESAMIENTO
  SÍ → destilar (palabras propias + 4 props + 2–3 [[ ]]) → mover a MOC
  NO → borrar
              ↓
CONEXIÓN
  cada nota nueva enlaza 2–3 notas/MOCs previos
  MOC = índice curado a mano
              ↓
ESTUDIO (Active Recall + Spaced Repetition)
  flashcards → SR o Anki 10 min/día
              ↓
EXPRESIÓN
  examen · código que corre · ensayo · clase explicada sin mirar
```

**Ritual semanal (obligatorio):** domingo 15 min — vaciar Inbox + semanal (score, victoria, lección, prioridades).

---

## 📜 Reglas de Oro

1. **Conceptos atómicos**: 1 nota = 1 idea.
2. **Interconexión total**: cada nota nueva enlaza 2–3 notas/MOCs previos con `[[enlaces]]`.
3. **LaTeX obligatorio** en ecuaciones.
4. **Explicar código con palabras propias**, no pegar bloques sin contexto.
5. **Frontmatter mínimo**: `tipo, estado, fecha, materia` (+ dominio según plantilla).
6. **Plantillas** solo vía Templater.
7. **NO destruir**: nada se borra, renombra o mueve sin evidencia + autorización.
8. **Fuente de verdad**: archivos reales > cualquier informe.

---

## 🏷️ Nomenclatura ISO-SAGE

```
[AAAA-MM-DD]_[PROYECTO]_[DESCRIPCIÓN]_V[XX]
```

Ejemplo: `2026-11-18_E100_Inicio_Boveda_V01.md`

---

## 📦 Cómo clonar y usar en GitHub

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/mente-maestra-e100.git
cd mente-maestra-e100

# Abrir en Obsidian como bóveda
# → Obsidian → Abrir bóveda como carpeta → seleccionar esta carpeta
```

> **Nota:** Esta bóveda está diseñada para Obsidian Desktop. Las funciones de Dataview, Templater y canvas requieren instalar esos plugins en Obsidian.

---

## `.gitignore` sugerido

```gitignore
# Obsidian
.obsidian/
*.sync-conflict-*
.DS_Store
Thumbs.db

# E-100 / Sistema
90 SISTEMA/Backup_*
90 SISTEMA/*.lock
*.env
*.key
*.pem

# Temporales
*.tmp
*.log
```

> **Advertencia:** No subas archivos con tokens, API keys, contraseñas o información personal (`90 SISTEMA/`, `00 ENTRADA/` sin revisar).

---

## 🛡️ Filtros (intocables sin autorización)

- `20 AREAS/20.01 UNIVERSIDAD/20.01.05 Protocolos y Sistemas/01_Constitucion_SOP/00_ARCHIVO_HISTORICO/` — historia, no se toca.
- Tokens, API keys y archivos de configuración — solo lectura salvo orden directa.
- Archivos que el usuario tenga abiertos en Obsidian en ese momento.

---

## 📄 Licencia

MIT License — Uso personal. Segunda cabeza privada de **Santiago Zuloaga Daza (Admin)**.

---

## 👤 Autor

**Admin** (Santiago Zuloaga Daza)  
Sistema de Organización Digital E-100  
Última actualización: 14 de noviembre de 2026

---

> [!note] **Referencia completa:** `90 SISTEMA/MANUAL DE ORGANIZACIÓN DIGITAL E-100.md`
