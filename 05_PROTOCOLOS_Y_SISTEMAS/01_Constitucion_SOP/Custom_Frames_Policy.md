# Política Custom Frames

- Solo iframes de confianza (HTTPS, sin credenciales en URL).
- Máximo 3 iframes activos simultáneos.
- Revisión cada 30 días: ¿uso real? → si no → desinstalar.
- No almacenar credenciales en URLs.
- Solo iframes de referencia/consulta. Para agentes → Local REST API / MCP.

## Iframes configurados actualmente

1. **AutoCLAW Z.ai** — `https://chat.z.ai` — Chat IA embebido
2. **THE EGG-NETWORK** — `https://notion.so/EGG-NETWORK` — Dashboard Notion
3. **Monitor Local (Grafana)** — `http://localhost:3000` — Desactivado por defecto

## Revisión programada

- Próxima revisión: 30 días desde hoy
- Criterio: ¿uso real en últimos 30 días? → si no → desinstalar
