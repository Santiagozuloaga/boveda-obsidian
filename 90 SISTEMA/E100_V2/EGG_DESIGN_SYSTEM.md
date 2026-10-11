<!-- E-100 V2 | datos verificados vía Notion REST API el 2026-10-06 | fuente: 90 SISTEMA/E100_V2/ | sin datos inventados -->

# EGG_DESIGN_SYSTEM

## 1. Tokens observados
| Elemento | Convención |
|---|---|
| Prefijo de base | Emoji + nombre en mayúsculas (`AR`, `C1`, `PIPELINE`) |
| Prefijo de base largo | Emoji + descriptor (`MONITOR DE INTEGRIDAD 2.0`) |
| Página | EMOJI + TÍTULO EN MAYÚSCULAS |
| Nombre de fila | español, sin tildes en base de datos (`Programacion`, `Geografia`) |
| Fase o tag | `F1..Fn` con guion y paréntesis (`01_GRAMATICA (12.md)`) |
| Prefijo temporal | `AAAA-MM-DD_` |

## 2. Inconsistencias detectadas (y estado)
1. Las **bases** usan emoji, las **filas** no. No hay convención para filas. → **Pendiente: definir convención filas**.
2. `Programacion` y `Geografia` sin tilde: rompen la búsqueda por acento. → **Corregir a `Programación`, `Geografía`**.
3. `Minimalist Project Manager (1)`: sufijo numérico de creación automática. → **Renombrar**.
4. La versión del Dashboard (V. 5.2) no coincide con la bóveda (V. 5.3). → **Sincronizar a V.5.3**.
5. `THE EGG-NETWORK prueba` existe como STAGING. → **Marcar claramente como STAGING**.

## 3. Propuesta (pendiente de aplicar)
- Nombres de fila con las tildes correctas (`Programación`, `Geografía`, `Matemáticas`, `Física`, `Química`).
- Sufijo numérico solo en borradores, nunca en entregables.
- Versión del sistema en un único lugar: la bóveda es la canónica.
- Banner visible en `THE EGG-NETWORK prueba`: `🧪 STAGING — REDISEÑO UI/UX — NO ES PRODUCCIÓN`.

## 4. Criterio
No se renombró nada. Renombrar en Notion rompe relaciones existentes y las notas ya escritas usan los nombres actuales.
**Regla**: Primero definir convención, luego migrar con script que actualice referencias.

## 5. Lenguaje visual del sistema (Eggman + UNSC)
### Inspiración Eggman
- Laboratorio, ingeniería, radar, maquinaria, terminales, paneles, control central, ingeniería.
- Paleta: `graphite` `#1a1a2e`, `charcoal` `#2d2d44`, `steel` `#3d4a5e`, `dark metal` `#1e1e2e`.
- Acentos: `amber/orange` industrial `#f0b429`, `cyan/blue` tactical `#00bfff`, `warning` restrained `#ff6b6b`.

### Inspiración UNSC
- Consola, protocolos, estados, telemetría, alertas, nomenclatura técnica, jerarquía operacional.
- Tipografía: `JetBrains Mono` / `JetBrains Mono NL` para código/datos; `Inter` / `IBM Plex Sans` para UI.
- Iconografía: `lucide` / `phosphor` (trazo fino, monocromo).

### Paleta conceptual (implementada en `eggman-balance.css`)
| Token | Hex | Uso |
|---|---|---|
| `bg-base` | `#0b0b11` | Fondo principal |
| `fg-primary` | `#ece7dd` | Texto principal (hueso) |
| `accent-gold` | `#f0b429` | Acento principal (oro Eggman) |
| `accent-cyan` | `#6cb2ff` | Acento táctico (UNSC) |
| `accent-red` | `#ff3b3b` | Alerta/Error |
| `muted` | `#6b6b6b` | Texto secundario |
| `border` | `#2a2a3e` | Bordes/divisores |
| `surface` | `#14141a` | Superficies/tarjetas |

## 5. Principios de diseño
1. **Legibilidad > Decoración**: La estética nunca reduce legibilidad.
2. **Función > Forma**: La estética sirve a la función, no al revés.
3. **Consistencia > Originalidad**: Patrones repetibles > unicidad decorativa.
4. **Accesibilidad**: Contraste WCAG AA mínimo. Modo oscuro nativo.
5. **Escalabilidad**: El diseño debe sostener 10x contenido sin rediseño.

## 6. Aplicación por plataforma
### Obsidian
- Aspecto: **LABORATORIO / KNOWLEDGE CORE**.
- Prioridad: legibilidad > velocidad > organización > estética.
- Snippets: `eggman-balance.css`, `dashboard.css`.
- No dashboard gigante.

### Notion (THE EGG-NETWORK)
- Aspecto: **COMMAND CENTER**.
- Jerarquía: COMMAND → OPERATIONS → UNIVERSITY → PROJECTS → MONITORING → ARCHIVE.
- Callouts, paneles, iconografía, estados, vistas, nombres técnicos.
- Sin saturar. Un buen dashboard útil > 5 decorativos.

### Todoist
- Aspecto: TACTICAL EXECUTION.
- Debe ser la interfaz más sencilla.
- Menos decoración. Más: WHAT, WHEN, PRIORITY, STATUS.
- No hacer que cada tarea parezca una misión militar.

## 6. Tokens de diseño (CSS variables)
```css
:root {
  --bg-base: #0b0b11;
  --fg-primary: #ece7dd;
  --accent-gold: #f0b429;
  --accent-cyan: #6cb2ff;
  --accent-red: #ff3b3b;
  --muted: #6b6b6b;
  --border: #2a2a3e;
  --surface: #14141a;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: 'Inter', sans-serif;
}
```

## 6. Principio visual final
> **No uses color para compensar una mala arquitectura. Primero simplifica la información mostrada; después aplica la paleta.**