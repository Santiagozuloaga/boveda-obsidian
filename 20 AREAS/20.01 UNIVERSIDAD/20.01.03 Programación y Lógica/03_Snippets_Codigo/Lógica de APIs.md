# 💻 LÓGICA DE APIs

**Concepto atómico:** Cómo se comunican programas entre sí por HTTP.

---

## 🧠 CONCEPTOS
- **Endpoint:** URL donde se hace la petición
- **Métodos:** GET (leer), POST (crear), PUT (actualizar), DELETE (borrar)
- **JSON:** Formato de intercambio de datos

## 📝 PYTHON (requests)
```python
import requests

resp = requests.get("https://api.ejemplo.com/datos")
datos = resp.json()
print(datos)
```

## 🔗 CONEXIONES
- Procesa [[Estructuras de Datos]] (JSON → diccionario)
- Usa [[Bucles For-While]] para recorrer resultados

---

**Explicación propia:** Una API es como pedir algo en una ventanilla: le dices qué quieres (endpoint + método) y te devuelve el resultado en una caja (JSON).