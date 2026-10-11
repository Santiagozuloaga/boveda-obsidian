# 🔷 AZURE + GRAPH MCP — Outlook gratis (sin pagar)

> El registro de app en Azure es **gratuito**. Microsoft Graph tiene nivel gratuito suficiente para leer correo, calendario y tareas. Nada aquí requiere suscripción de pago.

## Paso 1 — Registrar la app (tu navegador, ~10 min)
1. Entra a `portal.azure.com` con tu cuenta Microsoft (la del Outlook).
2. **Microsoft Entra ID → App registrations → New registration**.
3. Nombre: `E100-Outlook-MCP`. Tipos de cuenta: **personal Microsoft accounts only** (si tu Outlook es personal) o según tu caso.
4. Redirect URI: `http://localhost` (tipo Public client).
5. Anota: **Application (client) ID** y **Directory (tenant) ID**.

## Paso 2 — Permisos API
1. En la app: **API permissions → Add → Microsoft Graph → Delegated**.
2. Agrega: `Mail.Read`, `Calendars.Read`, `Tasks.Read` (mínimo; agrega `Mail.Send` solo si quieres enviar).
3. **Grant admin consent** si el botón aparece (en cuentas personales basta tu propio consentimiento al loguearte).

## Paso 3 — Avisarme
Pásame el **client ID** y **tenant ID** (el secret NO lo pegues en chat si es confidencial; lo configuro por otro medio). Yo:
1. Instalo `@developer.k/ms-graph-mcp` global.
2. Agrego el bloque `outlook-graph` a `opencode.json` (con tu confirmación).
3. Verifico lectura de bandeja y organizo con carpetas espejo + reglas (F16).

## Costos reales (honesto)
| Concepto | Costo |
|---|---|
| Registro de app Azure | Gratis |
| Microsoft Graph (uso personal normal) | Gratis |
| Lo que SÍ costaría | Planes Microsoft 365 de pago (no necesarios), WhatsApp Business API oficial (no la usamos; usamos Baileys gratis) |

## Alternativa $0 inmediata
Reenvío automático Outlook → Gmail (2 min en tu navegador, sin registros). Si prefieres esto, dímelo y te doy los pasos.
