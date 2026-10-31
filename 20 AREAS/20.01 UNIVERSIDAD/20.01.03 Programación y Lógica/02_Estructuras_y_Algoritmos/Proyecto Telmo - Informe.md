---
tipo: proyecto
estado: activo
fecha: 2026-09-24
---

# 📋 Proyecto Telmo - Informe

**Fecha:** 2026-09-24
**Curso:** Digital House — Estructuras de Datos en Python (Proyecto integrador)
**Código fuente:** `C:\Users\Admin\Downloads\01_Proyectos_Agentes\telmo_asistente_colab.py` (631 líneas)
**Apuntes:** [[Asistente Virtual Telmo - Apuntes]]

---

## 1. Objetivo

Completar el esqueleto del asistente virtual "Telmo" (OpenClaw no; chatbot bancario de consola) para Google Colab: buscar usuario por DNI y ofrecer 5 operaciones — saldo, facturas vencidas, pago, sucursales y turnos — con personalidad "Ejecutiva Estructurada" (`[TELMO]` + español neutro).

## 2. Funciones implementadas

| Función | Qué hace |
|---|---|
| `buscarUsuarioPorDni(nro)` | Búsqueda lineal en `usuarios`; retorna dict o `None` |
| `consultarSaldo(usuario)` | Imprime cuenta, titular y saldo |
| `consultarFacturas(usuario)` | Lista servicio/vencimiento/valor + total; mensaje si no hay |
| `pagarFacturas(usuario)` | Solo paga si `Saldo >= total`; descuenta, vacía lista, emite comprobante `T-XXXX` |
| `consultarSucursales()` | Recorre dict `sucursales` por zona |
| `sacarTurno()` | Valida zona/sucursal, genera fecha (evita finde) + hora 9-17 + código |
| `main()` | Pide DNI con `try/except`, saluda, menú `while` 1-5 con validación, pregunta `SI/NO`, despedida |

## 3. Pruebas ejecutadas (todas OK)

1. **Flujo Shelby** (`38729016` → 1 → SI → 2 → SI → 3 → NO): saldo $27545 → pago $5870 → nuevo saldo $21675, facturas en 0.
2. **Pago insuficiente Marcelo** (`26344067`): deuda $4921 > saldo $3790 → "Saldo insuficiente", datos intactos.
3. **Opción inválida + sucursales** (`9` → `4`): aviso de opción + listado de 4 zonas.
4. **Turno** (Iván `14327165` → Caba → Palermo): `Turno confirmado | 30-09-2026 11:00 | Código: T-2158`.
5. **Bordes:** DNI `0` → "No encontré ese DNI"; DNI `abc` → "DNI inválido" sin crash.

## 4. Errores encontrados y corrección

- **VSC reportaba 9+ errores:** diagnóstico con `flake8` → 0 errores reales (E9/F), 141 avisos de estilo (E122/E128 indentación de datos heredada del pegado, E302 líneas en blanco, E501 líneas largas).
- **Fix:** reindentado de `usuarios`/`sucursales` a 4 espacios, doble línea entre funciones, `print` partidos. Resultado: `flake8 → 0`.
- **Colab `SyntaxError`:** título pegado como celda de código sin `#` → solución: celda Markdown o comentar con `#`.

## 5. Estado final

- ✅ 5/5 tareas de la rúbrica (slides 2-5)
- ✅ Nombres de función intactos según consigna
- ✅ Solo construcciones del curso (listas, dicts, `for`/`while`, `if`, `f-strings`/`str()`, `try/except`)
- ✅ Listo para pegar en Colab en 3 celdas (datos → funciones → `main`)

## 6. Próximos pasos

- [ ] Pegar en Colab y correr de arriba abajo (`Shift+Enter`)
- [ ] Capturas: pago exitoso, pago insuficiente y turno para la entrega
- [ ] `Reiniciar entorno` y re-correr antes de entregar (evita saldos en 0 por pruebas)
