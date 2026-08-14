# Constitución del proyecto

Reglas de fondo que aplican a **todas** las especificaciones de este repositorio,
de aquí en adelante. Cada especificación individual describe el QUÉ; esta
constitución define el CÓMO técnico y el proceso.

## Metodología: Spec-Driven Development (SDD)

- Todo desarrollo parte de una especificación escrita **antes** que el código.
- Cada especificación nueva se guarda en la carpeta `especificaciones/`,
  numerada secuencialmente: `NNN-nombre-corto-en-kebab-case.md`.
- Flujo de trabajo: **Especificar → Planificar → Implementar → Validar contra
  la especificación**.
- Cada especificación se desarrolla en su propia rama creada desde `main`:
  `spec/NNN-nombre-corto`.
- El código implementado debe poder trazarse de vuelta a los requisitos
  funcionales (RF-N) de su especificación.

## Arquitectura de código: MVC

- **Model**: entidades de datos y lógica de persistencia/negocio.
- **View**: presentación / interfaz de usuario (plantillas, respuestas al
  cliente).
- **Controller**: recibe las peticiones/acciones, coordina Model y View.
- Estructura de carpetas esperada en cada implementación:
  ```
  src/
    models/
    views/
    controllers/
  ```

## Gestión de dependencias: uv

- Se usa [`uv`](https://docs.astral.sh/uv/) (Astral) para el entorno virtual
  y la gestión de dependencias Python.
- Todo proyecto implementado incluye `pyproject.toml` gestionado con
  `uv add` / `uv remove` / `uv sync`.
- No se usa `pip`, `venv` manual ni `poetry` directamente.
- Ejecución de la app y comandos siempre vía `uv run ...`.

## Convenciones de cada especificación

Cada archivo en `especificaciones/` sigue esta estructura mínima:

- Estado (Borrador / Aprobada / Implementada)
- Rama asociada
- Fecha
- Contexto
- Objetivo
- Alcance (y fuera de alcance)
- Historias de usuario
- Requisitos funcionales (RF-N)
- Entidades de datos (Modelo)
- Criterios de aceptación
- Preguntas abiertas (si quedan)

## Índice de especificaciones

| # | Especificación | Estado | Rama |
|---|---|---|---|
| 001 | [App de gimnasio: rutinas semanales](001-app-gimnasio-rutinas-semanales.md) | Cerrada | `spec/001-app-gimnasio-rutinas-semanales` |
| 002 | [Fondo oscuro](002-fondo-oscuro.md) | Cerrada | `spec/002-fondo-oscuro` |
| 003 | [Apartado de comidas por día](003-comidas-por-dia.md) | Borrador | `spec/003-comidas-por-dia` |
