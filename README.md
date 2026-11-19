# Mente Maestra E-100 — Especificación Operativa para Agentes de IA

> **Repositorio:** `Santiagozuloaga/boveda-obsidian`  
> **Rama:** `cierre-expediente`  
> **Propósito:** Especificación técnica y reglas de operación para agentes de IA que lean, escriban o modifiquen esta bóveda de Obsidian.  
> **Dueño:** Santiago Zuloaga Daza (Admin)  
> **Última actualización:** 2026-11-14

---

## 1. ¿Qué es este repositorio?

Esta bóveda es el **segundo cerebro personal** bajo el sistema de organización digital **E-100**. No es una carpeta de notas sueltas; es un sistema con gobernanza, protocolos y separación de responsabilidades.

La bóveda opera bajo el método **PARA** (Proyectos, Áreas, Recursos, Archivos) extendido con una capa operativa (`80 OPERATIVO`) y una capa de sistema (`90 SISTEMA`). Toda la configuración de gobernanza vive en `90 SISTEMA`.

### La Trinidad de Herramientas

| Herramienta | Rol | Alcance en este repositorio |
|-------------|-----|-----------------------------|
| **Notion** | Centro de operaciones "THE EGG-NETWORK" | Procesos, calendarios, bases de datos, sistemas de gestión. **No vive aquí.** |
| **Obsidian** | Cerebro de Acero — conocimiento profundo | **Este repositorio.** Zettelkasten, método PARA, notas atómicas. |
| **Todoist** | Arma de corto alcance | Tareas pequeñas de hoy. **No vive aquí.** |

**Regla de oro:** Notion para gestionar, Obsidian para pensar, Todoist para ejecutar hoy. Nada suelto: cada dato tiene su lugar.

---

## 2. Estructura de Carpetas (PARA + Capas Operativa y Sistema)

| Carpeta | Propósito | Acceso de agente |
|---------|-----------|------------------|
| `00 ENTRADA (Inbox)/` | Captura rápida. Regla 48h: todo lo que entra se procesa, destila o se descarta en 48 horas. | ✅ Leer y escribir con precaución. No eliminar sin autorización. |
| `10 PROYECTOS/` | Proyectos activos con fecha de inicio y fin. | ✅ Leer. Escribir solo si el proyecto está activo. |
| `20 AREAS/` | Áreas de responsabilidad permanente. Contiene el MOC universitario en `20.01 UNIVERSIDAD/`. | ✅ Leer. Escribir solo en áreas asignadas. |
| `30 RECURSOS/` | Material de referencia, libros, papers, documentación. | ✅ Leer. No modificar contenido de referencia sin autorización. |
| `40 ARCHIVOS X/` | Archivo muerto / proyectos completados. | ✅ Leer solamente. **No escribir ni eliminar.** |
| `80 OPERATIVO/` | Estado vivo: tableros (`HOY`, `TABLERO_SEMANAL`), agentes, tubería Zettel. No es conocimiento, es operación. | ⚠️ Escribir con extrema precaución. Es el motor del sistema. |
| `90 SISTEMA/` | Gobernanza, contratos, plantillas, memoria colectiva, informes de auditoría. | ⚠️ Leer siempre antes de operar. Escribir solo con autorización explícita de Admin. |

### 20 AREAS / 20.01 UNIVERSIDAD (MOC Académico)

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

## 3. Reglas de Gobernanza para Agentes (OBLIGATORIAS)

Estas reglas son **inalienables**. Cualquier agente que opere sobre este repositorio debe cumplirlas sin excepción.

### 3.1. Reglas Absolutas

1. **NO destruir.** No borrar, renombrar o mover nada sin evidencia + autorización de Admin. Gems, NEXUS, históricos e informes viejos: intactos siempre.
2. **NO inventar.** Datos, resultados, sesiones ni contenido. Lo no verificado se marca, no se rellena.
3. **Mínimo viable.** Un cambio pequeño con prueba supera una reforma. Prohibido sobreingenierizar.
4. **Fuente de verdad:** archivos y configuración reales > cualquier informe (incluidos los de `90 SISTEMA/`).
5. **Fronteras:** Obsidian piensa · Notion gestiona · Todoist ejecuta. No duplicarlas aquí.

### 3.2. Filtros Intocables (sin autorización explícita de Admin)

- `20 AREAS/20.01 UNIVERSIDAD/20.01.05 Protocolos y Sistemas/01_Constitucion_SOP/00_ARCHIVO_HISTORICO/` — historia, no se toca.
- Tokens, API keys y archivos de configuración (`opencode.json`, `.env`) — solo lectura salvo orden directa.
- Archivos que Admin tenga abiertos editando en Obsidian en ese momento.

### 3.3. Frontmatter Mínimo

Cada nota nueva debe incluir, como mínimo:

```yaml
---
tipo: <tipo_de_nota>
estado: <estado>
fecha: <AAAA-MM-DD>
materia: <materia>
dominio: <dominio_opcional>
---
```

Campos válidos para `estado`: `semilla`, `en_proceso`, `madura`, `archivada`.

### 3.4. Nomenclatura ISO-SAGE

Todos los archivos deben seguir el formato:

```
[AAAA-MM-DD]_[PROYECTO]_[DESCRIPCIÓN]_V[XX]
```

Ejemplo: `2026-11-18_E100_Inicio_Boveda_V01.md`

### 3.5. Interconexión Total (Zettelkasten)

- **1 nota = 1 idea** (conceptos atómicos).
- Cada nota nueva debe enlazar **2–3 notas o MOCs previos** usando `[[enlaces wiki]]`.
- El Graph View es métrica de calidad: una nota sin enlaces es una nota huérfana y debe revisarse.
- **LaTeX obligatorio** en ecuaciones.
- **Explicar código con palabras propias**, no pegar bloques sin contexto.

---

## 4. Protocolo de Operación para Agentes

### 4.1. Antes de escribir cualquier cosa

1. Leer `AGENTS.md` en la raíz del repositorio.
2. Leer `90 SISTEMA/WORKFLOW_E100.md` para entender el ciclo Captura → Procesamiento → Conexión → Estudio → Expresión.
3. Identificar en qué capa PARA pertenece la nota que va a crear.
4. Verificar que no exista ya una nota sobre el mismo tema (buscar en el grafo o con búsqueda de Obsidian).

### 4.2. Ciclo de vida de una nota

```
CAPTURA (5 seg, cero fricción)
  idea → 00_INBOX_TEMPORAL → cerrar
              ↓ (revisión semanal, 15 min)
PROCESAMIENTO
  SÍ → destilar: palabras propias + 4 props + 2–3 [[enlaces]] → mover a su MOC
  NO → borrar (coleccionar ≠ aprender)
              ↓
CONEXIÓN
  cada nota nueva enlaza 2–3 notas/MOCs previos
  MOC = índice curado a mano, no lista auto
              ↓
ESTUDIO (Active Recall + Spaced Repetition)
  flashcards → #flashcards/... → SR o Anki 10 min/día
              ↓
EXPRESIÓN
  examen · código que corre · ensayo/tesis · clase explicada sin mirar
```

### 4.3. Ritual semanal (único mantenimiento obligatorio)

Domingo 15 min: vaciar Inbox + semanal (score, victoria, lección, prioridades). Sin esto, el sistema decae en ~6 meses.

---

## 5. Árbol de Directorios Clave (referencia rápida)

```
Mente Maestra E-100/
├── README.md                      ← Este archivo (especificación para agentes)
├── AGENTS.md                      ← Reglas de comportamiento para OpenCode
├── HOME.md                        → Página de inicio de Obsidian (dashboard)
├── who i am.md                    → Identidad del dueño
├── E100_CURRENT_STATE_REPORT.md   → Estado actual del sistema
├── e100.ico
│
├── 00 ENTRADA (Inbox)/            → Captura (regla 48h)
│   ├── _MOC_INBOX.md
│   └── Sin título.md
│
├── 10 PROYECTOS/                  → Proyectos activos
│   └── _HISTORICO_V1.md
│
├── 20 AREAS/                      → Áreas de responsabilidad
│   ├── 20.01 UNIVERSIDAD/         → MOC universitario (Zettelkasten académico)
│   │   ├── 20.01.01 Diario de Guerra/
│   │   ├── 20.01.02 Alemán Zettelkasten/
│   │   ├── 20.01.03 Programación y Lógica/
│   │   ├── 20.01.04 Literatura y Fuentes/
│   │   ├── 20.01.05 Protocolos y Sistemas/
│   │   ├── 20.01.06 Fe y Filosofía/
│   │   ├── 20.01.07 Repaso STEM/
│   │   └── 20.01.08 Monografía/
│   ├── 20.02 SOP V2.5/
│   └── 20.04 INFORMES GEMS/
│
├── 30 RECURSOS/                   → Material de referencia
├── 40 ARCHIVOS X/                 → Archivo muerto (solo lectura)
│
├── 80 OPERATIVO/                  → Estado vivo (tableros, agentes)
│   ├── 07 TABLERO/                → HOY.md + TABLERO_SEMANAL.md
│   └── 08 AGENTES/                → HERRAMIENTAS.md + registro de herramientas
│
└── 90 SISTEMA/                    → Gobernanza y memoria
    ├── WORKFLOW_E100.md           → Flujo completo del sistema
    ├── Vaultorial_Index.md
    ├── Templater_Vaultorial_Mapping.md
    ├── TABLERO_CONTEOS.md
    ├── CONTRATO_NOTION_TODOIST.md
    ├── CAMBIOS_EJECUTADOS_E100.md
    ├── E100_Auditoria_Integral_2026-10-30.md
    ├── documentacion_interna/
    ├── MEMORIA_COLECTIVA/         → Informes y auditorías
    └── Backup_AutoClaw_2026-11-06/
```

---

## 6. Qué NO Hacer (Lista de Bloqueo)

| Acción | Por qué está prohibida |
|--------|----------------------|
| `git add .` sin revisar `90 SISTEMA/` | Puede subir tokens o claves accidentalmente |
| Borrar notas de `40 ARCHIVOS X/` | Es archivo muerto; solo lectura |
| Renombrar carpetas de nivel raíz | Rompe todos los enlaces `[[ ]]` existentes |
| Escribir en `01_Constitucion_SOP/00_ARCHIVO_HISTORICO/` | Es historia, no se toca |
| Crear notas sin frontmatter mínimo | Rompe la consistencia del sistema |
| Crear notas sin enlaces entrantes o salientes | Viola la interconexión total |

---

## 7. Cómo Contribuir (para agentes)

1. **Fork** este repositorio si vas a hacer cambios experimentales.
2. Lee `AGENTS.md` y `90 SISTEMA/WORKFLOW_E100.md` antes de tocar cualquier archivo.
3. Crea una rama descriptiva: `feature/<descripcion-corta>`.
4. Escribe notas siguiendo nomenclatura ISO-SAGE y frontmatter mínimo.
5. Asegúrate de que cada nota nueva tenga 2–3 enlaces `[[ ]]` a notas existentes.
6. Abre un Pull Request describiendo qué cambiaste y por qué.
7. Admin revisará y fusionará solo si cumple las reglas de gobernanza.

---

## 8. Contacto y Autoridad

- **Dueño:** Santiago Zuloaga Daza (Admin)
- **Palabra clave Canary:** `Admin` (debe aparecer en toda respuesta del agente)
- **Repositorio:** `https://github.com/Santiagozuloaga/boveda-obsidian`
- **Rama principal:** `cierre-expediente`

---

> [!note] **Referencia completa:** `90 SISTEMA/MANUAL DE ORGANIZACIÓN DIGITAL E-100.md`  
> [!warning] **Este documento es para agentes de IA.** Si eres humano, lee `HOME.md` para la experiencia de usuario.
