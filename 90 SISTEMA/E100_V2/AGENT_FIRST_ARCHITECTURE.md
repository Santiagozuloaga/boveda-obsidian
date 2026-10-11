<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# AGENT_FIRST_ARCHITECTURE

## 1. Principio
La bóveda es la fuente de verdad. Notion y Todoist son vistas. Ningún agente escribe en la bóveda sin snapshot.

## 2. Reglas que ya se aplican
1. **Lectura primero**: explorar antes de proponer.
2. **Escritura solo tras «sí» explícito**.
3. **Destructivo prohibido sin «sí» literal**: borrar requiere confirmación.
4. **Todo cambio reversible**: snapshot antes de escribir.
5. **Staging para lo dudoso**: `C:\Temp\STAGING_20261004\`, no la bóveda.

## 3. Verificado hoy (2026-10-06)
- Los 10 cambios en Notion se hicieron con snapshot previo y log de escritura.
- Los 111 archivos dudosos NO entraron a la bóveda: siguen en staging.
- El token de Notion se movió del código al registro antes de escribir.
- **git init** en la bóveda: **EJECUTADO HOY** (ver `E100_RECOVERY_PROTOCOL.md`).
- **Tokens rotados**: 3 tokens rotados (Notion, Todoist, Local REST API).
- **Recovery protocol**: `E100_RECOVERY_PROTOCOL.md` actualizado con estado actual.

## 4. Violaciones de este patrón detectadas (y corregidas)
| Violación | Dónde | Corrección |
|---|---|---|
| Token de Notion hardcodeado | `temp_rec/notion_pull.py`, `notion_audit.py` | movido a `HKCU\Environment\NOTION_TOKEN` |
| Informes con datos sin fuente | 11 informes V2 | regenerados con datos de API |
| `git init` no existía | Bóveda sin control de versiones | **EJECUTADO HOY** |
| 3 tokens pasaron por chat/código | Notion, Todoist, Local REST API | **ROTADOS HOY** |

## 3. Modelo de agente asíncrono
Un agente que llega al sistema debe poder descubrir SIN PREGUNTAR:
- **IDENTIDAD**: qué es el proyecto/entidad.
- **OBJETIVO**: qué se intenta lograr.
- **ESTADO**: actual (operativo/parado/bloqueado).
- **FUENTE DE VERDAD**: dónde vive el dato canónico.
- **DOCUMENTACIÓN**: dónde están las decisiones/reglas.
- **TAREAS**: qué hay pendiente/en progreso/completado.
- **ARCHIVOS**: dónde están los archivos relevantes.
- **EVIDENCIA**: hashes, logs, tests.
- **BLOQUEOS**: qué está atascado y por qué.
- **ÚLTIMA ACTUALIZACIÓN**: timestamp.
- **SIGUIENTE ACCIÓN**: qué toca ahora.

## 4. Modelo de subagentes (orquestación)
OpenCode actúa como **ORQUESTADOR**. Delegación obligatoria cuando exista capacidad:

| Subagente | Responsabilidad | Modifica |
|---|---|---|
| EGG-ARCHITECT | Auditar arquitectura Notion | No |
| EGG-UX | Auditar UX/UI Notion | No |
| EGG-DATA | Auditar bases de datos | No |
| EGG-OBSIDIAN-BRIDGE | Puente Notion ↔ Obsidian | No |
| EGG-TODOIST-BRIDGE | Puente Notion ↔ Todoist | No |
| AGENT-FIRST-ARCHITECT | Diseño para agentes asíncronos | No |
| DESIGN-SYSTEM | Patrones reutilizables LAB | No |
| QUALITY/REGRESSION | Auditoría post-cambios | No |
| RCS-GAME-ENGINE | Recursos, estados, puntuación | Sí |
| RCS-EVENT-ENGINE | Random, eventos, efecto dominó | Sí |
| RCS-PERSISTENCE | CSV, historial, persistencia | Sí |
| RCS-REPORTING | Markdown + HTML + exportación | Sí |
| RCS-UX | Consola, navegación, demo | Sí |
| RCS-QA | Tests y pruebas de integración | Puede corregir |
| RCS-SECURITY | Credenciales, archivos, errores | No (al principio) |
| RCS-DEMO | Guion de demostración | No |
| RCS-DOCUMENTATION | README, explicación técnica | No |
| RCS-RELEASE | Empaquetado, verificación final | Solo release |

## 3. Protocolo de continuidad (OBLIGATORIO)
- **NUNCA** reiniciar el proyecto desde cero.
- **NUNCA** descartar trabajo previo sin evidencia de que es basura.
- **NUNCA** tratar una inferencia como hecho.
- **SIEMPRE** leer contexto completo antes de actuar.
- **SIEMPRE** preservar histórico, incluso si parece obsoleto.
- **SIEMPRE** distinguir: HECHO / VERIFICADO / INFERIDO / NO VERIFICADO / HISTÓRICO / TEST / DEMO / STAGING.

## 4. Regla de evidencia
Cada hallazgo debe clasificarse:
- [VERIFICADO] — evidencia directa reproducible.
- [INFERIDO] — evidencia apunta, pero no concluyente.
- [NO VERIFICADO] — no hay evidencia suficiente.
- [HISTÓRICO] — información antigua, no necesariamente vigente.
- [TEST/DEMO] — prueba controlada.
- [STAGING] — experimental, no producción.

Nunca presentar una inferencia como hecho.
Si una herramienta no interpreta correctamente un objeto de Notion, no concluyas automáticamente que el objeto está roto. Verifica por otra vía disponible.

## 5. Modelo de recuperación (continuidad)
Si un agente falla:
1. Determinar qué información se perdió.
2. Qué trabajo sí completó.
3. Qué evidencia queda.
4. Qué información se perdió.
5. Si otro agente puede continuar.
6. Si OpenCode debe asumir la tarea.

El sistema debe conservar evidencia para que otro agente continúe sin reconstruir mentalmente todo el trabajo anterior.

## 5. Principio final
La prioridad no es "ganar" una auditoría. La prioridad es mantener la integridad de E-100.
- NO INVENTAR.
- NO DESTRUIR.
- NO OCULTAR.
- NO SUPONER.
- NO REPETIR SIN NECESIDAD.
- NO SOBREINGENIERIZAR.
- NO FALSIFICAR RESULTADOS.
- NO CONFUNDIR AUSENCIA DE DATOS CON ERROR.
- NO CONFUNDIR HISTORIAL CON INSTRUCCIÓN ACTUAL.
- NO CONFUNDIR API CON UI.
- NO CONFUNDIR AUDITORÍA CON PASIVIDAD.

VERIFICAR. INVESTIGAR. AYUDAR. RESCATAR CUANDO SEA NECESARIO. CORREGIR DE FORMA SEGURA. VOLVER A VERIFICAR. DOCUMENTAR. MANTENER CONTINUIDAD.