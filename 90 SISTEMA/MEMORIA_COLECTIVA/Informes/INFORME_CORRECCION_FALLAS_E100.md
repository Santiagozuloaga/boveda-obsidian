# INFORME_CORRECCION_FALLAS_E100
**Fecha:** 2026-09-26 | **Backup:** `BAK_VAULT_E100_PRE_CORRECCION` (344/344) | **Fuente de verdad:** bóveda abierta (no ZIP)

## 1. Estado inicial
Bóveda post-reconciliación: 140 notas, 15 plugins, sintaxis única, HOME 61/Daily 46, Canvas nativos, memoria colectiva + 95 sesiones.

## 2. Fallas confirmadas
| # | Falla | Evidencia |
|---|---|---|
| 1 | LanguageTool `staticLanguage` duplicado (`es-ES` + `auto`) | data.json líneas 3 y 10; parser usa última → efectivo `auto` ≠ intención |
| 2 | `PLANTILLA_Post_Mortem_Examen` con `{{materia}}`/`{{fecha}}` inválidos | plantilla mapeada; ni core ni Templater procesan esas claves |
| 3 | Proyectos reales sin frontmatter (Nexus ODS, Telmo) | archivos con código/fechas reales, 0 metadata → invisibles en dashboards |

## 3. Fallas descartadas
- `#U00xx` en filesystem/contenido: 0 casos. Nombres reales (`Cálculo`, `Relativsätze`, `Tubería`) sanos.
- `{{}}` en MEMORIA e INFORME LIQUIDACIÓN: meta-documentación y formulario sin uso, no sintaxis operativa.
- Trigger Templater: causa fuera de alcance headless (requiere test en vivo ya instruido).

## 4. Fallas históricas
Instrucciones ELIMINAR Gem/NEXUS (2 docs ya con banner SUPERADO). Otros 4 docs solo describen historia con su corrección inline: sin banner adicional.

## 5. Templater
6 mappings reales = documentados (ARQUITECTURA coincide). TEST3 eliminado por Admin tras test. Flujo manual vigente.

## 6. Daily Notes
23 (limpia, manual Admin), 24 (regenerada slim correcta), 26 (0b, NO rellenada por orden expresa).

## 7. LanguageTool
✅ CORREGIDO Y VERIFICADO: eliminada 2ª clave; efectivo `es-ES` (JSON válido). Probar corrección en español dentro de Obsidian (humano).

## 8. Nombres de archivo
4 testigos con tildes/diéresis correctos. Veredicto: #U00xx solo existe en exportaciones ZIP. NO RENOMBRAR.

## 9. Dataview
Queries sanas. Novedad: Nexus/Telmo ahora califican en "Proyectos — Salud" y "Activos" (verificar en UI).

## 10. Tracker
Sin cambios (ya correcto). Re-verificar render tras reinicio (humano).

## 11. Proyectos
Nexus ODS (Streamlit ODS, vital) + Telmo (integrador 24/09, 631 líneas): reales y activos por evidencia → frontmatter mínimo añadido. Sin datos fabricados.

## 12. Central Académica
Sin cambios (calcula igual). NO TOCAR por estética.

## 13. Monitor de Integridad
Sin cambios (0.71 + barras verificados). Pendiente: reload visual humano.

## 14. Canvas
Sin cambios (refs válidas, visual confirmado). NO RECONSTRUIR.

## 15. Documentación
2 banners previos vigentes. 4 docs con menciones ELIMINAR evaluados: describen historia con corrección inline → sin banner extra. Criterio documentado.

## 16. Cambios realizados
1. `data.json` LanguageTool: −1 línea duplicada (backup rollback).
2. Post_Mortem: `{{materia}}`→`___`, `{{fecha}}`→fecha Templater.
3. Nexus ODS + Telmo: frontmatter `tipo/estado(+fecha)` antepuesto, contenido intacto.

## 17. Archivos modificados
3 archivos. Ninguna eliminación, ningún renombre, ningún dato creado.

## 18. Pruebas realizadas
JSON válido post-fix · frontmatter sin duplicar (assert) · renders UI pendientes de humano (Tracker, queries con nuevos proyectos, LanguageTool es-ES).

## 19. Problemas restantes
Trigger muerto (workaround vigente) · 26 vacía (intencional) · MONITOR reload · rotar secrets · MONOGRAFIA vacía con MOC listo.

## 20. Estado para auditoría de Devin
🟡 LISTA: backup + informe + evidencia por falla. Devin debe probar en vivo: LanguageTool es-ES, queries Proyectos con Nexus/Telmo, render Tracker/Dataview/Canvas, trigger, fórmulas Notion.
