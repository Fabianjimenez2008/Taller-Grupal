# Taller Grupal

Este repositorio sigue **Spec-Driven Development**. Antes de tocar código,
leer:

- [`especificaciones/CONSTITUCION.md`](especificaciones/CONSTITUCION.md) —
  metodología, arquitectura (MVC) y gestión de dependencias (`uv`).
- `especificaciones/NNN-*.md` — cada especificación individual (el índice
  está al final de la constitución).

Reglas rápidas:

- Toda especificación nueva se guarda en `especificaciones/`, numerada
  (`NNN-nombre-corto.md`), y se trabaja en una rama `spec/NNN-nombre-corto`
  creada desde `main`.
- El código se organiza en Model / View / Controller (`src/models/`,
  `src/views/`, `src/controllers/`).
- Las dependencias Python se gestionan con `uv` (`uv add`, `uv sync`,
  `uv run`), nunca con `pip`/`venv`/`poetry` directamente.
