---
tipo: informe
fecha: 2026-10-29
autor: Vibe (Mistral)
estado: activo
tags: [auditoria, autoria, e100]
---

# AUDITORÍA DE AUTORÍA — Notas IA vs. notas propias (2026-10-29)

**Auditor:** Vibe/Mistral vía API de GitHub. **Método:** inventario completo del repo + lectura de ~90 notas completas + contraste con el reporte forense del 06-oct (522 archivos / 362 md locales). **Alcance:** todas las carpetas excepto `.obsidian`.

## 1. Cifras totales

| Métrica | Valor |
|---|---|
| Archivos en el repo (sin .obsidian) | ≈455 |
| Notas .md | ≈420 |
| Notas con contenido real | ≈350 (83%) |
| Vacías a propósito (0 B, cifrado GEM) | 30 |
| Daily logs creados / con contenido real | 14 / 2 |
| Plantillas base (sin contenido por diseño) | ≈25 |

## 2. Clasificación de autoría (sobre el total de notas)

| Clase | Notas (aprox.) | % | Qué es |
|---|---|---|---|
| Sistema/IA (generadas por agentes) | ~250 | 60% | Informes E-100, MOCs, dashboards, protocolos, sesiones SES-*, registros de agentes, planes |
| Co-creadas (IA estructura + contenido de Santiago) | ~60 | 14% | Zettel alemán, snippets de código, matemáticas, auditorías éticas (respuestas), Vision MIT-KOSPIE |
| Terceros importados | ~45 | 11% | Documentación OpenClaw/ClawHub, AI_POLICY (adaptada de uv), papers |
| Santiago (autoría propia) | ~8 | 2% | Manifiesto, Keep Incidentes, bitácoras, daily logs reales |
| Vacías / plantillas | ~57 | 13% | GEM cifradas 0 B, plantillas base, dailies sin llenar |

**Lectura honesta:** solo ~2% de la bóveda es escritura pura de Santiago; otro ~14% es co-creada. El resto es salida del sistema (informes, registro, estructura) o material importado. La bóveda hoy documenta el sistema más de lo que almacena pensamiento propio.

## 3. Las que son TUYAS (autoría dominante)

- `06_FE_Y_FILOSOFIA/Manifiesto Santi 2.0.md` — credo personal.
- `01_DIARIO_DE_GUERRA/Keep Incidentes Feb-2026.md` — importado de tu Google Keep.
- `01_DIARIO_DE_GUERRA/Bitacora de guerra.md` y `Bitácora de guerra 1.md` (duplicadas exactas, 1 línea c/u).
- `01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-09-11.md` (única daily completamente real) y `2026-09-20.md` (parcial).
- Tus respuestas dentro de las ~35 "Auditoría ética y nocturna" (estructura plantilla IA, respuestas humanas).
- `07_TABLERO/Pruebas Plugins.md` (tus marcas de verificación).
- `10.02 MONOGRAFIA` (los PDF son tu tesis; el MOC solo la indexa).

## 4. Co-creadas (IA armó la forma; tú pusiste el fondo)

- `02_ALEMANIA_ZETTELKASTEN` completo (8 Zettel con "EJEMPLO PROPIO" + 2 MOC): generadas en sesiones con IA a partir de TU material de Drive (`imports/drive`).
- `03_PROGRAMACION_Y_LOGICA`: Asistente Virtual Telmo (tu proyecto), Derivadas SAGE-X (tu archivo), 4 snippets, Cálculo Diferencial.
- `06_FE_Y_FILOSOFIA/Vision MIT-KOSPIE.md` ("investigación Pi/Gemini + contexto propio"), Doctrina del Log v2.
- `04_LITERATURA_Y_FUENTES`: Marco Rap Fuente, Playlist Emowe Triage.
- `09 REPASO STEM` (7 notas): generadas por Mistral en la auditoría del 11-oct con tus datos; formalmente IA.

## 5. IA pura (sistema)

- `90 SISTEMA` casi entero: informes E-100, EGG_* (10), WORKFLOW, ARQUITECTURA, respaldo Notion (8), MEMORIA_COLECTIVA (127: 96 sesiones SES-* + 27 informes + índices).
- `08 AGENTES` (11).
- `07_TABLERO`: HOY y TABLERO_SEMANAL (script sync-tablero.py), Control Panel, CHECKLIST ("Hecho por la IA"), ESTADO_OBSIDIAN, MAPA_FRENTES (propuesta IA).
- Todos los `_MOC_*` (≈15) y scaffolds: HOME, AGENTS, CALENDARIO_DE_VIDA, S.O.P. V 5.0.
- Informes GEMS (Emerl ×2): roleplay de agente redactado sobre tu contexto.
- `E100_CURRENT_STATE_REPORT.md` (raíz, forense del 06-oct).
- `20 AREAS/Costos-Tramites-Alemania.md` (pegado de tabla IA, formato roto).

## 6. Terceros MAL UBICADOS (acción requerida)

~40 archivos de documentación del proyecto open-source OpenClaw/omo-codex (`hooks.md`, `message.md`, `webhooks.md`, `clawhub.md`, `openclaw-sdk.md`, `soul.md`, `manifest.md`, `usage.md`, `api-usage-costs.md`, `THREAT-MODEL-ATLAS.md`, `DEVELOPMENT-STATUS.md`, …) viven dentro de `05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP`. No son IA ni tuyos: contaminan la carpeta Constitución. Recomendación: mover a `40 ARCHIVOS X/_docs_openclaw/` o similar. `AI_POLICY.md` es plantilla adaptada de uv.

## 7. Vacíos, plantillas y duplicados

- 30 notas 0 B: informes GEM "cifrados" (15 en 03_Cifrado_Shard + 15 en 20.04 INFORMES GEMS; confirmados intencionales por el reporte del 06-oct).
- 12 de 14 daily logs: plantillas sin llenar (4 con Templater sin renderizar: `<% tp.date.now %>` visible).
- `04_Revisiones/2026-W41.md`: plantilla sin llenar.
- 18 plantillas en `01_Constitucion_SOP/Plantillas` + 7 en `90 SISTEMA/90.01 TEMPLATES`.
- Duplicados: Bitácora ×2, Plantilla informes GEM ×2, Emerl ×2 (dos carpetas), `_HISTORICO_V1` ×3 (marcadores intencionales), Auditorías éticas duplicadas entre 01_Constitucion y SOP V2.5/AUDITORIAS (mismo contenido, dos ubicaciones).

## 8. Hallazgo crítico: material sensible en repo público

Este repositorio es PÚBLICO y contiene material personal y familiar de alta sensibilidad: la bitácora de incidentes domésticos importada de Keep, los informes del gem "Emerl" con detalles de conflictos familiares, y las respuestas personales de las auditorías éticas. Este informe no reproduce nada de eso, pero la recomendación es directa: hacer el repo privado o sacar del repo público al menos `01_DIARIO_DE_GUERRA` (Keep Incidentes y 03_Cifrado_Shard). Decisión del Admin.

## 9. Método y límites

- Inventario completo vía API de GitHub (sin `.obsidian`); ~90 notas leídas completas; el resto clasificado por carpeta, tamaño y señales de estructura (frontmatter, formato Zettel, "Fuente:", "Hecho por la IA", Templater sin renderizar).
- Contraste: 362 md locales el 06-oct vs ≈420 en GitHub hoy; el delta son sobre todo las 96 sesiones SES-* y notas nuevas de octubre.
- Margen de error: ±10 notas en las clases 1-3; los conteos de vacíos y plantillas son exactos.
