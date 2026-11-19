# 03_DECISIONS.md — Decisiones E-100

**Fecha:** 31 de octubre de 2026  
**Usuario:** Admin

| ID | Decisión | Fecha | Fuente de autorización | Justificación | Sistemas afectados |
|----|----------|-------|------------------------|---------------|-------------------|
| D-01 | Migrar OpenCode a v2.0 con secretos en variables de entorno | 30-oct-2026 | Admin (orden directa: "me obligaron a migrar") | Estructura v1 incompatible con v2.0 | opencode.json, variables de entorno Windows |
| D-02 | Restaurar OpenCode v1 después de probar v2.0 | 30-oct-2026 | Admin (orden directa: "lo original que estaba funcionando") | v1 es lo que funciona estable en este entorno | opencode.json v1 restaurado |
| D-03 | Dejar repositorio GitHub público | 31-oct-2026 | Admin ("deja quieto lo del repositorio") | No cambiar visibilidad sin orden explícita | SantiagoZuloaga/boveda-obsidian |
| D-04 | No reemplazar batería | 31-oct-2026 | Admin ("déjalo quieto" sobre batería) | No intervenir sin orden específica | Batería del laptop |
| D-05 | Ejecutar operaciones no destructivas con autorización inmediata | 31-oct-2026 | Admin ("tienes un sí inmediato para toda operación no destructiva") | Agilizar ejecución de auditorías | Todos los sistemas |
| D-06 | Escribir en Obsidian (memoria de trabajo + pruebas E2E) | 31-oct-2026 | Admin ("Tienes autorización para lo de Obsidian y las pruebas") | Crear memoria de trabajo y ejecutar pruebas E2E | Bóveda Obsidian, E100_Work_Memory/ |
| D-07 | Renovar tokens Gmail/Calendar | 31-oct-2026 | Admin (canjeó código de autorización OAuth) | Tokens expirados, necesario para flujo Grok→Vibe→Notion | google-tokens-gmail.json |
