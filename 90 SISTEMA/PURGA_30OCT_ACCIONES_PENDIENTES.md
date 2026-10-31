# PURGA 30-OCT — Acciones pendientes de ejecución local (ventana 4AM, PC)

> Generado por Vibe durante la Purga del 30-oct-2026. Decisiones ya confirmadas por Santiago en la corrida.
> Regla de congelamiento vigente: esto se ejecuta tal cual; lo que falle se documenta, no se repara.

## Estado de borradas

- Borrados vía API en la corrida (2): 2026-09-23.md y 2026-09-24.md en 01_Daily_Logs.
- Restantes (52): 11 dailies de prueba + 41 docs OpenClaw/plantillas agente. El conector GitHub tarda ~2 min por archivo, así que van por git local en UN commit.

## Comando único (ejecutar en el clon local)

```bash
git rm "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-09-26.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-09-27.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-09-29.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-09-30.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-01.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-02.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-04.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-05.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-06.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-07.md" \
  "01_DIARIO_DE_GUERRA/01_Daily_Logs/2026-10-10.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/ahooks.js.LICENSE.txt" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/api-usage-costs.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/bootstrapping.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/claude-max-api-proxy.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/clawbot.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/clawdock.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/clawflow.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/clawhub.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/components-hooks.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/events-hooks.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/group-messages.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/hooks.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/imessage.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/incident-response.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/incident-retro-setup.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/intent-clear.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/manifest.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/memory-usage.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/message-composition.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/message-presentation.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/message.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/messages.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/migrate-claude.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/migrating-claude.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/openclaw-sdk-api-design.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/openclaw-sdk.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/openclaw.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/partial-runtime-evidence.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/soul.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/usage-tracking.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/usage.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/webhook.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/webhooks.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/zalouser.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/IDENTITY.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/IDENTITY.dev.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/USER.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/USER.dev.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/SOUL.dev.md" \
  "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/BOOT.md"
git commit -m 'Purga 30-oct: borrar 11 dailies de prueba + 41 docs OpenClaw/plantillas agente (confirmado)'
git push origin main
```

## Por qué cada bloque

- Dailies (11): confirmados por Santiago como archivos de prueba. Se conservan 2026-09-11.md (real) y 2026-09-20.md (parcial).
- OpenClaw (34): documentación verbatim de OpenClaw/omo-codex mal ubicada en 01_Constitucion_SOP desde el fork original.
- Plantillas agente (7): IDENTITY.md, IDENTITY.dev.md, USER.md, USER.dev.md, SOUL.dev.md, soul.md, BOOT.md — son plantillas del agente OpenClaw, no contenido de Santiago.

## NO borrar (quedan para revisión del 30-nov)

- AI_POLICY.md (adaptada de uv, tiene valor propio), BOOTSTRAP.md, CLAUDE.md, HANDOFF.md, HOOK.md, DEVELOPMENT-STATUS.md, EVIDENCE.md, COMPARACION_session_memory_vs_memory.md, CONTINUITY_ses_2c60.md, THREAT_MODEL.md, THREAT-MODEL-ATLAS.md, CONTRIBUTING-THREAT-MODEL.md. Ambiguos: verificar autoría antes de tocar.

## Otros pendientes de esta purga

- 2026-W41.md: sin llenar, ubicar y decidir (rellenar o borrar).
- Bitacora de guerra.md vs Bitácora de guerra 1.md en 01_DIARIO_DE_GUERRA: duplicadas, consolidar en una.
- REPO PÚBLICO (CRÍTICO): GitHub Settings → Danger Zone → Change visibility → Private. El repo expone Keep Incidentes Feb-2026, informes Emerl y respuestas de auditorías.
- Después de las borradas: syncthing puede marcar conflictos; revisar .stfolder antes de aceptar.
