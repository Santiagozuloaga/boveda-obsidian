---
type: log
tags: [taxonomia, migracion, e100, obsidian]
fecha: 2026-10-18
estado: aplicado
rollback: git reset --hard 164bc75
---

# UNIFICACIÓN DE TAXONOMÍA DE OBSIDIAN — 2026-10-18

> **Decisión de Admin:** no se elimina nada; se fusiona el MOC universitario y PARA
> creando una taxonomía única. Nada se borró: 226 notas se movieron.

## Problema

La bóveda tenía **dos árboles conviviendo**:

| Sistema | Notas | Raíz |
|---|---|---|
| PARA | ~40 | `00 ENTRADA` · `10 PROYECTOS` · `20 AREAS` · `30 RECURSOS` · `40 ARCHIVOS X` · `90 SISTEMA` |
| MOC universitario | ~226 | `00_INBOX_TEMPORAL` … `10.02 MONOGRAFIA`, todos en raíz |

Consecuencia: al buscar no se sabía en qué carpeta mirar. El 92 % del contenido
(226 de 245 notas gestionadas) estaba en el MOC, que de facto ya mandaba.

## Taxonomía resultante (UNA sola)

```
00 ENTRADA (Inbox)          captura; contiene 00_INBOX_TEMPORAL (regla 48h)
10 PROYECTOS
20 AREAS                    contenedor de areas de vida
   20.01 UNIVERSIDAD        ← MOC universitario absorbido
      20.01.01 Diario de Guerra        42 notas
      20.01.02 Alemán Zettelkasten     10
      20.01.03 Programación y Lógica   11
      20.01.04 Literatura y Fuentes     6
      20.01.05 Protocolos y Sistemas   125
      20.01.06 Fe y Filosofía           4
      20.01.07 Repaso STEM              7
      20.01.08 Monografía               1
   20.02 SOP V2.5                      17  (ya existía)
   20.04 Informes GEMS                 18  (ya existía)
30 RECURSOS
40 ARCHIVOS X
80 OPERATIVO              ← NUEVO: estado vivo, no conocimiento
   07 TABLERO                              8
   08 AGENTES                             11
90 SISTEMA                              170  (governance, contratos, memoria)
```

**Criterio:** PARA manda en el nivel superior (áreas de vida).
El MOC universitario es *contenido de un área*, no una estructura paralela.
Tableros y registro de agentes no son conocimiento → `80 OPERATIVO`.

## Mapa de movimientos (226 notas)

| Origen | Destino | Notas |
|---|---|---|
| `01_DIARIO_DE_GUERRA` | `20 AREAS/20.01 UNIVERSIDAD/20.01.01 Diario de Guerra` | 42 |
| `02_ALEMANIA_ZETTELKASTEN` | `…/20.01.02 Alemán Zettelkasten` | 10 |
| `03_PROGRAMACION_Y_LOGICA` | `…/20.01.03 Programación y Lógica` | 11 |
| `04_LITERATURA_Y_FUENTES` | `…/20.01.04 Literatura y Fuentes` | 6 |
| `05_PROTOCOLOS_Y_SISTEMAS` | `…/20.01.05 Protocolos y Sistemas` | 125 |
| `06_FE_Y_FILOSOFIA` | `…/20.01.06 Fe y Filosofía` | 4 |
| `09 REPASO STEM` | `…/20.01.07 Repaso STEM` | 7 |
| `10.02 MONOGRAFIA` | `…/20.01.08 Monografía` | 1 |
| `07_TABLERO` | `80 OPERATIVO/07 TABLERO` | 8 |
| `08 AGENTES` | `80 OPERATIVO/08 AGENTES` | 11 |
| `00_INBOX_TEMPORAL` | `00 ENTRADA (Inbox)/00_INBOX_TEMPORAL` | 1 |

## Verificación

- Notas antes: **445** · después: **445** · movidas verificadas: **226/226**
- **0 notas borradas.** Total cuadra exactamente.
- Rollback: `git reset --hard 164bc75` (rama `cierre-expediente`)

## Efecto secundario detectado y corregido

El movimiento **rompió Templater**: su configuración real apuntaba a carpetas
inexistentes. Corregido el 2026-10-18:

| Archivo | Cambio |
|---|---|
| `.obsidian/plugins/templater-obsidian/data.json` | `templates_folder` + 6 `folder_templates` reescritos |
| `.obsidian/daily-notes.json` | `folder` de notas diarias reescrito |

Backups: `data.json.bak-taxonomia-20261018` · `daily-notes.json.bak-taxonomia-20261018`

También se recreó `20.01.04 Literatura y Fuentes/02_Resumenes`, que el trigger
referenciaba pero **nunca existió** (0 notas, carpeta ausente).

## Enlaces

- Los `[[wikilinks]]` de Obsidian resuelven por nombre de archivo → **no se rompieron**.
- Rutas **literales** sí quedaron obsoletas en: `90 SISTEMA/Vaultorial_Index.md`,
  `90 SISTEMA/Templater_Vaultorial_Mapping.md`, `HOME.md`,
  `80 OPERATIVO/07 TABLERO/Control Panel.md`. **Pendiente de actualizar.**
- Informes históricos en `90 SISTEMA/MEMORIA_COLECTIVA/Informes/` conservan sus
  rutas originales **a propósito**: son registro del pasado, no referencias activas.

## Rollback

```powershell
cd "C:\Users\Admin\Downloads\syn\Mente Maestra E-100"
git reset --hard 164bc75
```

## Ver también

[[CONTRATO_NOTION_TODOIST]] · [[LAYOUT_IDEAL_EGG_NETWORK]] · [[ARQUITECTURA_SEGUNDO_CEREBRO]]

---

# PENDIENTE — DECISIÓN DEL ADMIN: UNIVERSO NOTION `3d2b`

> Registrado aquí por decisión de Admin. **No se ha escrito nada en Notion.**

Notion sigue en **solo lectura**. Se documenta, no se ejecuta.

## Qué es

Dos juegos de bases con los mismos nombres. Producción usa el universo `3d2b38a4-*`;
staging tiene las bases reales.

| Base | Producción `3d2b` | Staging | Diferencia |
|---|---|---|---|
| PIPELINE DE ENTREGABLES | **1 fila** (7 props) | **12 filas** (8 props) | staging tiene 11 entregables más |
| MONITOR DE INTEGRIDAD 2.0 | 13 props | 16 props | faltan `Dieta`, `NoFap`, `Sueño >7h` |
| Active Recall - Zettel | 6 props | 7 props | falta `Materia` |
| CALENDARIO DE VIDA | 1 fila | 1 fila | equivalentes |
| PROYECTO C1 | 9 filas | 9 filas | equivalentes |
| LOGÍSTICA | 1 fila, 11 props | 1 fila, 11 props | equivalentes |
| BÓVEDA / HARDWARE | 0 filas | 0 filas | ambas vacías |

## Por qué bloquea

Producción está mostrando la copia **degradada**. Mientras siga así, se opera
sobre 11 entregables que no están a la vista.

## Opciones (ninguna ejecutada)

| Opción | Implicación | Riesgo |
|---|---|---|
| **A. Fusionar** staging → producción | Copiar 12 filas reales sobre 1 | Bajo: staging conserva el original |
| **B. Archivar** `3d2b` tal cual | La 1 fila queda como histórico | Bajo |
| **C. Dejar como está** | Se sigue con datos degradados | **Alto** |

**Recomendación: A**, previa revisión de la única fila de `3d2b` para confirmar
que no contiene algo ausente en las 12. Esa revisión es de lectura y la puede
hacer Admin o un agente.

## Condición para promover el diseño de prueba

`THE EGG-NETWORK prueba` solo puede promoverse cuando **staging supere a producción
en datos**. Hoy **no se cumple**. Por eso la promoción sigue bloqueada.