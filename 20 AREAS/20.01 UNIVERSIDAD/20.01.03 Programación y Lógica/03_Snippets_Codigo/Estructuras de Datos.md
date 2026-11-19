# 💻 ESTRUCTURAS DE DATOS

**Concepto atómico:** Formas de organizar y almacenar datos para acceso y modificación eficiente.

---

## 🧠 TIPOS CLAVE
- **Listas/Arrays:** Secuencia ordenada, acceso por índice $O(1)$
- **Diccionarios/Hash:** Clave→valor, búsqueda $O(1)$ promedio
- **Pilas (Stack):** LIFO (Last In, First Out)
- **Colas (Queue):** FIFO (First In, First Out)
- **Árboles:** Jerarquía (ej. árbol binario)

## 📝 PYTHON
```python
# Lista
numeros = [1, 2, 3]
numeros.append(4)

# Diccionario
alumno = {"nombre": "Santiago", "promedio": 4.5}
print(alumno["promedio"])
```

## 🔗 CONEXIONES
- Los [[Bucles For-While]] recorren estas estructuras
- Base para [[Lógica de APIs]]

## 🎒 ANALOGÍA: LA MOCHILA

> Imagina tu mochila como una lista. Puedes meter varios lápices, colores y gomas (son "elementos" o ítems). Si alguien pide "¿dónde está el azul?", simplemente buscas la posición 2 (el segundo lápiz). No hace falta que revises todo el contenido uno por uno.

```python
# Registro de gastos diarios de comida
gastos = ["pan", "leche", "huevos"]
print(gastos[1])   # "leche" — el segundo elemento (índice 1)

# Ejemplo completo
amigos = ["Ana", "Pedro", "Lucía"]
amigos.append("Diego")
print("¡Hola!", amigos)
```

- **Índice base 0:** `gastos[0]` es "pan", `gastos[1]` es "leche". El primero es `[0]`.
- **Acceso O(1):** por índice se llega directo, no hay que recorrer la lista.
- **`.append(x)`** añade al final.

*Origen: lección recuperada de la Bandeja de Aprendizaje (Automation Grok, 18-oct-2026), restaurada el 31-oct.*

---

**Explicación propia:** Un diccionario es como un armario con etiquetas: buscas por etiqueta (clave), no revisando todo el contenido.

**Explicación propia (listas):** Una lista es una mochila con ranuras numeradas: si sabes el número, agarras el objeto sin revolver todo. El diccionario es el armario con etiquetas; la lista es el cajón con posiciones. En la lista preguntas "¿cuál es el elemento número 3?"; en el diccionario, "¿qué hay en la ranura *carrera*?".