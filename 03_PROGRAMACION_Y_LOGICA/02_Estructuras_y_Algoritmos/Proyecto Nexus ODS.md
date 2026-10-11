---
tipo: proyecto
estado: activo
---

# Proyecto Nexus ODS (importado de Keep — vital)

**Idea:** app Streamlit que mapea cada ODS con datos reales (API Our World in Data) y muestra gráficos por país + noticias ONU por RSS. Caché SQLite, layout sobrio.

## Stack
- `streamlit`, `pandas`, `plotly`, `feedparser`, `requests`, `sqlite3`
- `pip install streamlit pandas plotly feedparser requests`

## Estructura
```
nexus/
  app.py
  data_loader.py   # descarga OWID CSV + guarda en SQLite (tabla owid_cache)
  news.py          # parsea RSS ONU
  nexus.db
```

## Detalle técnico clave
- **Caché SQLite:** antes de descargar, revisa `owid_cache(dataset, descargado)`. Si es de hoy → usa local; si no → descarga y actualiza. Así la app abre rápido.
- **RSS ONU:** `https://news.un.org/feed/subscribe/es/news/all/rss.xml` (español). Si falla → plan B: `https://news.un.org/feed/subscribe/en/news/topic/sustainable-development/rss.xml`.
- **ODS con datos guaranteed:** 3 Salud, 4 Educación, 7 Energía, 13 Clima.

## Insight guardado
> "La app no necesita backend: Streamlit + SQLite local es suficiente. El caché es lo que la hace sentir profesional."

---
*Fuente: 4 notas de Keep (feb 2026) · [[03_PROGRAMACION_Y_LOGICA/03_Snippets_Codigo/_MOC_CODIGO]]*
