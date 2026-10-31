# ⏳ PENDIENTES DEL USUARIO (requieren navegador/móvil)

> El agente no puede hacer estos pasos solo. Cuando completes uno, avísame y lo verifico.

## 1. OAuth Gmail + Drive (F13)
1. Abrir la app que usa el MCP `gmail`/`google-drive` y completar el login Google.
2. Verificar que existan `google-tokens-gmail.json` y `google-tokens-drive.json` en `C:\Users\Admin\.config\opencode\`.
3. Avisarme → verifico lectura de bandeja y Drive, luego organizo (F14/F15).

## 2. MCP Microsoft Graph — Outlook (F16)
- Paquete elegido: `@developer.k/ms-graph-mcp` (Outlook + Calendar + ToDo + OneDrive).
- Requiere: registro de app en Azure Portal (ID cliente + tenant) — pasos en tu navegador.
- Tras instalarlo, organizo Outlook con carpetas espejo + reglas.

## 3. WhatsApp QR (F21)
- Arrancar el MCP `whatsapp` y escanear el QR con tu móvil (sesión Baileys).
- Tras el pareo: flujo captura WhatsApp → `00_INBOX_TEMPORAL`.

## 4. YouTube API key (F25)
- Crear key en Google Cloud Console (YouTube Data API v3) y reemplazar `PEGA_TU_API_KEY_YOUTUBE_AQUI` en `opencode.json`.
- Tras eso: activo el MCP e inventario playlists/liked.

## 5. Exports manuales (F26-F28)
- Instagram/Threads: Configuración → Descargar tu información → dejar ZIPs en `01_Proyectos_Agentes\imports\`.
- Google: Takeout de Keep, Fotos (por álbum), marcadores exportados, Saved.
- Nubes: Dropbox (token de app), MEGA (login), Box (export manual).
- Tras cada entrega: ejecuto pipeline ingesta → triage (tu "sí") → materialización → limpieza.

## 6. Exportación urgente Gmail académico (F17, fin de año)
- Cuenta Workspace del colegio (acceso en riesgo). Tras OAuth: inventario por etiquetas → adjuntos útiles a Drive + índice en Obsidian/Notion. Ruido fuera.

## 7. PC + Android (F18-F22)
- PC: estructura `SISTEMA_E100` + limpieza (lo ejecuto cuando digas).
- Android: estructura espejo + vaciado Keep (guía + verificación).
