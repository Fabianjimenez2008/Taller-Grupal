# Taller-Grupal
Esta es la clase 1 de reposición de Git Hub

## App de gimnasio: rutinas semanales

Metodología **Spec-Driven Development** — ver [`especificaciones/`](especificaciones/)
(constitución del proyecto + especificación 001). Arquitectura **MVC**
(`src/models/`, `src/views/`, `src/controllers/`), dependencias con **uv**.

### Correr la app

```bash
uv sync
uv run main.py
```

Abrir http://127.0.0.1:5000 — navegá entre lunes y viernes, y cargá/editá/
eliminá ejercicios de cada rutina. Los datos quedan en `gimnasio.db`
(SQLite, ignorado por git).
