# 🤖 Asistente Virtual Telmo - Apuntes

**Concepto atómico:** Chatbot de autogestión bancaria que aplica listas de diccionarios, búsqueda lineal, bucle `while` con menú e `input()`.

**Fuente:** Proyecto integrador Digital House — Estructuras de Datos en Python. Código: `telmo_asistente_colab.py` (631 líneas, 7 funciones).

---

## 🧠 1. Lista de diccionarios (`usuarios`)

Cada usuario es un `dict` con `FacturasAdeudadas` = lista de `dicts` anidados.

```python
usuarios = [
    {
        "Nombre": 'Marcelo',
        "Apellido": 'Cortés',
        "Dni": 26344067,
        "Cuenta": '409662-9',
        "FacturasAdeudadas": [
            {"Servicio": 'Electricidad', "Vencimiento": '25-02-2023', "Valor": 2747},
        ],
        "Saldo": 3790,
    },
]
```

**Explicación propia:** Es una tabla disfrazada — la lista es la tabla, cada dict una fila y cada clave una columna. Para agregar un usuario nuevo basta un `.append()`.

## 🔎 2. Búsqueda lineal (`buscarUsuarioPorDni`)

```python
def buscarUsuarioPorDni(nroBuscado):
    for u in usuarios:
        if u['Dni'] == nroBuscado:
            return u
    return None
```

**Idea clave:** Recorre hasta encontrar coincidencia; si termina el `for`, retorna `None`. Costo $O(n)$. El `None` obliga al que llama a validar antes de usar el resultado.

## 💰 3. Pago con guarda (`pagarFacturas`)

```python
total = sum(f['Valor'] for f in facturas)
if usuario['Saldo'] >= total:
    usuario['Saldo'] -= total
    usuario['FacturasAdeudadas'] = []  # se borran al pagar
```

**Idea clave:** Patrón guarda — primero el caso vacío (`return` temprano), luego la condición de saldo. La mutación (`-=`, `= []`) modifica el dict original porque los dicts se pasan por referencia.

## 🔁 4. Menú con `while` + validación (`main`)

```python
continuar = "SI"
while continuar == "SI":
    opcion = input("...1-5...").strip()
    if opcion not in ["1", "2", "3", "4", "5"]:
        print("[TELMO] Opción inválida...")
    elif opcion == "1":
        consultarSaldo(usuarioActual)
    # ...
    continuar = input("¿Deseas otra operación? (SI/NO): ").strip().upper()
```

**Idea clave:** `.strip().upper()` normaliza el input para que `si`, ` SI ` también valgan. El `try/except ValueError` al convertir el DNI evita que el programa crashee con letras.

## 🎲 5. Turnos con `random` + `datetime` (`sacarTurno`)

```python
dias = random.randint(1, 10)
fecha = datetime.date.today() + datetime.timedelta(days=dias)
while fecha.weekday() >= 5:  # 5=sábado, 6=domingo
    fecha = fecha + datetime.timedelta(days=1)
hora = random.randint(9, 17)
```

**Idea clave:** `timedelta` desplaza la fecha y el `while` la empuja a lunes si cae en finde. `.title()` + comparación en minúsculas hace la validación de sucursal insensible a mayúsculas.

## 🧹 6. Calidad estilo_VSC

- 141 avisos `flake8` (E122/E128/E501/E302) → 0 tras reindentar datos a 4 espacios, doble línea entre funciones y partir `print` largos.
- 0 errores reales (`E9/F`): el código siempre ejecutó; los avisos eran solo formato heredado del pegado original.

---

## 🔗 CONEXIONES

- Base teórica en [[Estructuras de Datos]]
- Bucles en [[Bucles For-While]]
- Informe del proyecto: [[Proyecto Telmo - Informe]]

---

**Explicación propia:** Telmo es un CRUD mínimo sin base de datos — la "base" es la lista en memoria, el "read" es la búsqueda lineal y el "delete" es vaciar la lista de facturas al pagar.
