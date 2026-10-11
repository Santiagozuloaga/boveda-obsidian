---
type: map
tags: [templater, vaultorial, sistema]
cssclasses: [dashboard]
---

# 🔧 Templater — Vaultorial Mapping (E-100)

> *Trigger activo: `trigger_on_file_creation: true` · `auto_jump_to_cursor: true` · 6 folder_templates · Carpeta base: `05_PROTOCOLOS_Y_SISTEMAS`*

## 📂 JSON real → `.obsidian/plugins/templater-obsidian/data.json`

```json
{
  "trigger_on_file_creation": true,
  "auto_jump_to_cursor": true,
  "enable_folder_templates": true,
  "folder_templates": [
    { "folder": "01_DIARIO_DE_GUERRA/01_Daily_Logs", "template": "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/Plantillas/PLANTILLA_Daily_Note.md" },
    { "folder": "04_LITERATURA_Y_FUENTES/02_Resumenes", "template": "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/Plantillas/PLANTILLA_Libro_Book_Notes.md" },
    { "folder": "00_INBOX_TEMPORAL", "template": "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/Plantillas/PLANTILLA_Apunte.md" },
    { "folder": "01_DIARIO_DE_GUERRA/02_Post_Mortem_Examenes", "template": "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/Plantillas/PLANTILLA_Post_Mortem_Examen.md" },
    { "folder": "04_LITERATURA_Y_FUENTES/01_Papers_e_Investigacion", "template": "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/Plantillas/PLANTILLA_Fuente.md" },
    { "folder": "01_DIARIO_DE_GUERRA/04_Revisiones", "template": "05_PROTOCOLOS_Y_SISTEMAS/01_Constitucion_SOP/Plantillas/PLANTILLA_Revision_Semanal.md" }
  ]
}
```

## 🔗 Origen Vaultorial (18 MIT)

| Vaultorial | Plantilla E-100 | Carpeta destino |
|---|---|---|
| `daily-note-template` + `weekly-note-template` | `PLANTILLA_Daily_Note.md` + `PLANTILLA_Revision_Semanal.md` | `01_DIARIO_DE_GUERRA/01_Daily_Logs` + `04_Revisiones` |
| `book-notes-template` | `PLANTILLA_Libro_Book_Notes.md` | `04_LITERATURA_Y_FUENTES/02_Resumenes` |
| `zettelkasten-starter-vault` (Fleeting) | `PLANTILLA_Apunte.md` | `00_INBOX_TEMPORAL` |
| `project-management-template` + `kanban-template` | `PLANTILLA_Proyecto_Software.md` | `03_PROGRAMACION_Y_LOGICA` |
| `moc-template` | `PLANTILLA_Vocabulario_Aleman.md` | `02_ALEMANIA_ZETTELKASTEN` |
| `student-vault` | `PLANTILLA_Post_Mortem_Examen.md` | `01_DIARIO_DE_GUERRA/02_Post_Mortem_Examenes` |
| `cornell-notes-template` | `PLANTILLA_Fuente.md` | `04_LITERATURA_Y_FUENTES/01_Papers_e_Investigacion` |
| `habit-tracker` + `daily-planner-template` | `PLANTILLA_Revision_Semanal.md` / `PLANTILLA_Mensual.md` | `01_DIARIO_DE_GUERRA/04_Revisiones` |

*Ver índice completo 18 con links y zips en [[Vaultorial_Index|Vaultorial_Index.md]] — no se copia zip, solo referencia.*

## ✅ Pruebas (marca al pasar)

- [ ] Crear `00_INBOX_TEMPORAL/Test_Apunte.md` → aplica `PLANTILLA_Apunte` + cursor en `<% tp.file.cursor(1) %>`
- [ ] Crear `01_DIARIO_DE_GUERRA/01_Daily_Logs/2099-01-01.md` → aplica Daily V2
- [ ] Crear `03_PROGRAMACION_Y_LOGICA/Test_Proj.md` → aplica `PLANTILLA_Proyecto_Software` con Gantt
- [ ] ~~Periodic `Open today's daily note` → respeta `YYYY-MM-DD` y plantilla Daily V2~~ (HISTÓRICO: Periodic retirado 2026-09-23; vía canónica core Daily Notes + Templater)

---
*Sincronizado con `Vaultorial_Index.md` y `.obsidian/plugins/templater-obsidian/data.json` — 2026-09-19*
