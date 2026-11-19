# ✅ Pruebas de plugins (marca con x)

> Paleta = Ctrl+P · Lectura = icono libro · Reporta número + error.

## Estado
- [x] 1. Tracker — gráfico en `CALENDARIO_DE_VIDA` con punto 0.7
- [x] 2. Spaced Repetition — paleta buscar `spaced` → `Revisar tarjetas de todas las notas` ✅ (verificado 2026-09-13, mazos con 5 tarjetas)
- [x] 3. Dataview — `HOY` lectura → tabla Rayos-X con 2026-09-11
- [x] 4. Kanban — arrastrar tarjeta Inbox→MOC y persiste + negro aplicado
- [ ] 5. Templater — paleta *Insert template* → crea con fecha
- [x] 6. Homepage — reiniciar app → grafo primero
- [x] 7. Periodic Notes — weekly configurado por Admin (2026-09-13)
- [ ] 8. Omnisearch — Ctrl+Shift+F `Klausur` → MOC + daily
- [x] 9. LanguageTool — funciona; fijado a español `es-ES` en `data.json` (2026-09-13)
- [x] 10. Style Settings — vacío confirmado (esperado con EvilRed)
- [x] 11. Meld — pide contraseña ✅ (clave Admin: 123 — sin recupero si se pierde)
- [x] 12. Zotero — BBT sirviendo `ready` ✅ (habilitado + verificado por API, 2026-09-13) + `data.json` ✅; confirma en Obsidian: `Ctrl+P` → `Import notes`
- [x] 13. YT Transcript — funciona ✅; idioma preferido fijado a `es` (2026-09-13)
- [ ] 14. Custom Frames — panel leo.org
- [x] 15. Text Extractor — funciona ✅ (palabra `Buenrostro`, verificado 2026-09-13)
- [x] 16. Excel→md — funciona ✅
- [x] 17. Dailies.base — funciona ✅

## Fallos (anota aquí número + texto exacto)
- 7: en paleta `Periodic` solo aparecen `Open today's daily note` y `Switch active calendar set`; no existe `Open weekly note` (week `{}` vacío en `data.json`).
- 9: LanguageTool no subraya — pendiente verificar si es falta de auto-check o límite de cuenta gratuita (lo básico NO pide premium).
- 12: `Import notes` exige Better BibTeX — INSTALADO en perfil Zotero (2026-09-13, compatible Zotero 10). Falta: reinicia Zotero y prueba `Ctrl+P` → `Import notes`.
