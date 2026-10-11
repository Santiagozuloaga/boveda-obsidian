---
tags: [agente, opencode]
status: activo
---

# OpenCode — constructor principal

- **Rol:** implementa, ejecuta, verifica, documenta. Orquesta subagentes.
- **Acceso:** filesystem PC, bash, APIs REST (Notion/Todoist), ADB, git.
- **Verificado 2026-10-07/11:** RCS 265 tests verdes; cirugía Syncthing
  (cifrado fantasma, fsPath, marcadores); APIs Notion/Todoist en vivo;
  vault pusheada a GitHub (573 archivos, sin secretos).
- **Límites:** MCPs notion/todoist/obsidian no cargan en su sesión
  (usa APIs directas); no toca secretos (documenta, no rota sin orden).
- **Cuándo usarlo:** todo trabajo de ejecución en PC.
