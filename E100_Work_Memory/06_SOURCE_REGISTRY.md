# 06_SOURCE_REGISTRY.md — Registro de Fuentes

**Fecha:** 31 de octubre de 2026  
**Usuario:** Admin

## Aplicaciones y documentos canónicos

| ID | Aplicación/Documento | Ruta/Enlace | Accesibilidad | Método de consulta | Última verificación |
|----|---------------------|-------------|---------------|-------------------|---------------------|
| S-01 | OpenCode config v2.0 | `C:\Users\Admin\.config\opencode\opencode.json` | Sí | Lectura directa | 31-oct-2026 |
| S-02 | OpenCode v1 backup | `C:\Users\Admin\.config\opencode\opencode.v1.backup.json` | Sí | Lectura directa | 30-oct-2026 |
| S-03 | Bóveda Obsidian | `C:\Users\Admin\Downloads\syn\Mente Maestra E-100` | Sí | Lectura/escritura | 31-oct-2026 |
| S-04 | GitHub repo | `https://github.com/Santiagozuloaga/boveda-obsidian` | Sí (público) | API GitHub, webfetch | 31-oct-2026 |
| S-05 | Notion API | `https://api.notion.com` | Sí (token configurado) | fetch REST | 31-oct-2026 |
| S-06 | Todoist API | `https://api.todoist.com/api/v1` | Sí (token configurado) | fetch REST | 31-oct-2026 |
| S-07 | Gmail tokens | `C:\Users\Admin\.config\opencode\google-tokens-gmail.json` | Sí | Lectura directa | 31-oct-2026 (renovados) |
| S-08 | Drive tokens | `C:\Users\Admin\.config\opencode\google-tokens-drive.json` | Sí | Lectura directa | 30-oct-2026 |
| S-09 | Outlook/Graph tokens | `C:\Users\Admin\.config\opencode\ms-graph-tokens.json` | Sí | Lectura directa | 30-oct-2026 |
| S-10 | Batería report | `C:\Users\Admin\energy-report-2026-10-30.html` | Sí | Lectura directa | 31-oct-2026 |
| S-11 | Paquete Maestro E-100 | `C:\Users\Admin\Downloads\E100_Paquete_Maestro_Auditoria_Memoria_Hitos_2026-10-22.md` | Sí | Lectura directa | 31-oct-2026 |
| S-12 | NITRO Resolución Sistemática | `C:\Users\Admin\Downloads\E100_NITRO_Resolucion_Sistematica_Problemas.md` | Sí | Lectura directa | 31-oct-2026 |
| S-13 | NITRO Autoejecución | `C:\Users\Admin\Downloads\E100_NITRO_Autoejecucion_Supervisada.md` | Sí | Lectura directa | 31-oct-2026 |

## Documentos canónicos de la bóveda

| ID | Documento | Ruta en bóveda | Tipo |
|----|-----------|----------------|------|
| D-01 | Manual de Organización Digital E-100 | `20 AREAS/20.01 UNIVERSIDAD/20.01.05 Protocolos y Sistemas/01_Constitucion_SOP/MANUAL DE ORGANIZACIÓN DIGITAL E-100.md` | Gobernanza |
| D-02 | S.O.P. V 5.0 | `20 AREAS/20.01 UNIVERSIDAD/20.01.05 Protocolos y Sistemas/01_Constitucion_SOP/S.O.P. V 5.0.md` | Procedimiento |
| D-03 | Contrato Notion-Todoist | `90 SISTEMA/CONTRATO_NOTION_TODOIST.md` | Integración |
| D-04 | Tablero de conteos | `90 SISTEMA/TABLERO_CONTEOS.md` | Métricas base |
| D-05 | Pendientes de Admin | `90 SISTEMA/PENDIENTES_ADMIN_E100.md` | Decisiones pendientes |

## Metodos de consulta

- **OpenCode CLI:** `opencode-cli.exe --version`, `opencode-cli mcp list`
- **Notion API:** `fetch("https://api.notion.com/v1/...")` con Bearer token
- **Todoist API:** `fetch("https://api.todoist.com/api/v1/tasks")` con Bearer token
- **PowerShell:** `Get-FileHash` para SHA-256, `test-path` para existencia de archivos
