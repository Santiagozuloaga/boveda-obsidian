---
tipo: fuente
formato: libro
autor: ""
año: ""
titulo: "<% tp.file.title %>"
genero: ""
rating: ""
estado: pendiente
fecha: <% tp.file.creation_date("YYYY-MM-DD") %>
creation_date: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
tags: [fuente, libro]
aliases: ["<% tp.file.title %>"]
---

# 📚 <% tp.file.title %>

> Mínimo viable: 1 tesis + 1 lección + 1 conexión. Lo demás opcional. Método XDA Book + Vaultorial.

| Campo | Detalle |
|---|---|
| **Autor** |  |
| **Género / Tema** |  |
| **Año / Páginas** |  /  |
| **Rating** | ⭐⭐⭐⭐⭐ (1-5) |
| **Fuente** | [[04_LITERATURA_Y_FUENTES/03_Documentacion_Oficial|Doc]] / Zotero:  |

---

## 📌 Tesis del autor (1 línea — XDA)
> ___

## 💡 Lo que ME sirve (mi comprensión, no resumen — 3 bullets max)
- 
- 
- 

## 🧩 3 Lecciones clave (taskforge — accionables)
- [ ] Lección 1: ___ → acción 📅 <% tp.date.now("YYYY-MM-DD") %> ⏫
- [ ] Lección 2: ___ → acción 📅 <% tp.date.now("YYYY-MM-DD") %>
- [ ] Lección 3: ___ → acción 📅 <% tp.date.now("YYYY-MM-DD") %>

## 🧠 Active Recall — 3 Formas (Emowe)
### Forma 1: Toggle > Cover (preguntas cortas)
> Francia → París (oculto)
- Francia
	- París
- Italia
	- Roma
- España
	- Madrid
> Uso: `> + espacio` toggle, `Tab` para anidar respuesta. Colorea verde acierto / rojo fallo.

### Forma 2: Gallery Flashcards con cover
> Vista Gallery con `Cover = propiedad Cover`
- Crea vista Gallery → Properties → Page cover → Fit image
- Cada tarjeta: `title = Pregunta`, `cover = imagen característica` (ej. bandera), abrir = respuesta

### Forma 3: Tema desarrollo con imagen+video
- Toggle nivel superior = índice del tema (ej. POO)
	- Imagen mapa mental
	- Vídeo YouTube embed `/video` + URL
	- Texto / código / PDF Drive URL
> Divide pantalla tablet: izquierda toggle, derecha notas.

## 🗣️ Citas (pocas, con página/minuto — XDA)
> "___" — p. ___
> "___" — p. ___

## 🔗 Conexiones (frase obligatoria: esta fuente cambia ___ porque ___)
- Esta fuente cambia ___ porque ___
- Puente a MOC: [[04_LITERATURA_Y_FUENTES/_MOC_LITERATURA|MOC Literatura]] — por qué importa: ___
- Concepto atómico vinculado: ___ :: ___ #flashcards/Libro

## ✅ Tareas que salen del libro (Tasks 📅⏫🔁)
- [ ] Aplicar lección 1 en proyecto ___ 📅 <% tp.date.now("YYYY-MM-DD", 7) %> ⏫
- [ ] Compartir resumen en ___ 📅 <% tp.date.now("YYYY-MM-DD", 3) %>

## 📝 Notas de lectura (ephemeral → destilado)


---
<!-- Convención tags: #concepto #cita #dato. Temas van en [[links]] y MOCs. Marcar estado: pendiente/leyendo/destilado -->
