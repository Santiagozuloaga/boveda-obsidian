# 📱 ANDROID — Espejo del ecosistema (sin pagar)

> El celular es captura + consulta. Lo pesado vive en el PC.

## 1. Estructura espejo (archivos)
- Replicar en almacenamiento interno: `SISTEMA_E100/00_INBOX/` (buzón), `10_PROYECTOS/`, `20_AREAS/`.
- Regla: lo que entra al móvil y no se procesa en 48h se revisa el domingo o se borra.

## 2. Captura rápida (3 segundos)
- **Google Keep** = buzón temporal. Se vacía cada noche hacia Obsidian (`00_INBOX_TEMPORAL`) o Todoist.
- **Todoist app** = tareas del día (proyectos 🎓🇩🇪📚💪 ya creados, sincronizan solos).
- **Cámara** = pizarrón/apuntes → álbum "U" → fin de semana a Drive espejo + Bóveda de Evidencias si aplica.

## 3. Sync
- **Syncthing Android** ↔ PC: carpeta de la bóveda (solo lectura en el móvil si quieres evitar conflictos; escritura solo en PC).
- **Notion + Todoist apps**: sesión iniciada, widgets de HOY en pantalla principal.
- **WhatsApp**: tras el pareo QR, los mensajes clave se reenvían al flujo del agente.

## 4. Limpieza mensual (con la Purga del 31)
1. Keep vacío (todo transferido o borrado).
2. Descargas del móvil vacías.
3. Fotos: álbum "U" procesado, resto a su álbum o fuera.
4. Revisar apps sin uso >60 días.

## 5. Lo que NO va en el móvil
- Tokens, keys, `opencode.json` (solo PC).
- Edición de la bóveda (el móvil es espejo de lectura + captura).
