<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# EGG_UX_REPORT — Usabilidad de THE EGG-NETWORK

## 1. Lo que funciona
- Jerarquía clara: 1 `heading_1` + 4 `heading_2` separan las 5 zonas.
- 4 `callout` para imágenes rápidas (Bóveda de Autoridad, Núcleo Emerl, etc.).
- 2 `link_to_page` apuntan directo a las bases de trabajo (CENTRAL y otra).
- Navegación por columnas en UNIVERSIDAD (Estudio | Sistema) funciona.

## 2. Fricciones encontradas
| # | Fricción | Impacto | Severidad |
|---|---|---|---|
| 1 | Los dos `link_to_page` no tienen texto visible en el bloque | El usuario no sabe a dónde lleva sin pasar el ratón | Media |
| 2 | 3 `child_page` con nombres de trabajo interno: `Minimalist Project Manager (1)` | El `(1)` denota creación automática sin renombrar | Baja |
| 3 | Existe `THE EGG-NETWORK prueba` junto a la página real | Ambigüedad: ¿cuál es la canónica? | **Alta** |
| 4 | 6 `paragraph` planos frente a 23 listas | Listas largas se leen peor en párrafo | Baja |
| 5 | `DASHBOARD UNIVERSITARIO` dice V. 5.2 mientras la bóveda define V. 5.3 | Desfase de versión | Media |

## 3. Hallazgo crítico: `THE EGG-NETWORK prueba` es STAGING autorizado
No es duplicado a borrar. Es **STAGING AUTORIZADO** para rediseño de interfaz.
- Función: experimentar con UI/UX, probar layouts, dashboards, navegación, relaciones, vistas.
- Flujo: LAB → EXPERIMENTO → EVALUACIÓN → PATRÓN → DECISIÓN → IMPLEMENTACIÓN SELECTIVA.
- **NO** copiar automáticamente staging → producción.
- **NO** borrar. **NO** fusionar. **NO** promover automáticamente.

## 4. Recomendaciones (pendientes de aplicar)
1. **Resolver la ambigüedad del punto 3**: formalizar `THE EGG-NETWORK prueba` como STAGING con banner visible.
2. Renombrar `Minimalist Project Manager (1)` y quitarle el sufijo `(1)`.
3. Añadir `rich_text` descriptivo a los 2 `link_to_page`.
4. Sincronizar la versión del Dashboard a V. 5.3 (la bóveda define V. 5.3).
5. Añadir banner visible en `THE EGG-NETWORK prueba`: `🧪 STAGING — REDISEÑO UI/UX — NO ES PRODUCCIÓN`.

## 5. No aplicado
Ninguno de los 5 puntos se ejecutó automáticamente: los puntos 2-5 son cambios de contenido que requieren criterio editorial, y el punto 1 es un archivado/renombrado manual que requiere criterio visual.

---

## 4. Navegación móvil vs escritorio
- **Escritorio**: 3 columnas en UNIVERSIDAD, layout completo.
- **Móvil**: columnas se apilan; toggle `Sistema (uso raro)` oculta bases poco usadas.
- **Problema**: `link_to_page` sin texto visible afecta más en móvil.
- **Propuesta**: textos descriptivos en `rich_text` de los `link_to_page`.

## 5. Pruebas de usabilidad pendientes
| Test | Qué verificar | Estado |
|---|---|---|
| TEST 1 | Navegación principal desde HOME a cada zona | Pendiente |
| TEST 2 | Búsqueda semántica (Smart Connections) vs textual | Pendiente |
| TEST 3 | Crear nota desde móvil + sync | Pendiente |
| TEST 4 | Recuperación tras 7 días sin uso | Pendiente |