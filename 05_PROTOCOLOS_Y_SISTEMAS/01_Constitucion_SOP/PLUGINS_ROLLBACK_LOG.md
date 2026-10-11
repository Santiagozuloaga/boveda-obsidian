# PLUGINS_ROLLBACK_LOG.md

## Registro de cambios de plugins E-100

### 2026-10-06 — Auditoría post-recuperación

| Plugin | Acción | Estado anterior | Estado nuevo | Motivo | Rollback |
|--------|--------|-----------------|--------------|--------|----------|
| obsidian-kanban | DESINSTALADO | Activo en JSON | Retirado + movido a .trash/ | Duplicado por Canvas nativo; sin mantenedor; UX rota | Carpeta en `.trash/obsidian-kanban-20261006` |
| obsidian-custom-frames | CONFIGURADO | Activo sin config | Activo + config + política | Iframes útiles: Z.ai, Notion EGG-NETWORK, monitor local | Revisión 30 días |
| periodic-notes | CONSERVADO | Retirado (docs) | ACTIVO · INFRAESTRUCTURA CENTRAL | Motor Daily/Semanal/Mensual/Anual + score X ↔ CALENDARIO_DE_VIDA | — |
| obsidian-kanban | MOVIDO A .trash | Activo | Movido a `.trash/obsidian-kanban-20261006` | Duplicado por Canvas nativo; sin mantenedor | Carpeta en `.trash/obsidian-kanban-20261006` |

### Rollback disponible

Si se necesita revertir:
- **Kanban**: restaurar carpeta desde `.trash/obsidian-kanban-20261006` → `.obsidian/plugins/obsidian-kanban/` + añadir a `community-plugins.json`
- **Custom Frames**: eliminar `data.json` y entradas en docs
- **Periodic Notes**: mantener activo (no tocado)

### Próxima revisión: 2026-11-05

| Plugin | Criterio | Acción si no cumple |
|--------|----------|---------------------|
| Custom Frames | Uso real en 30 días | Desinstalar |
| Notebook Navigator | Uso real navegación MOC | Desinstalar |
| Smart Connections | Búsqueda semántica útil | Desinstalar |
| QuickAdd | Captura rápida real | Desinstalar |
