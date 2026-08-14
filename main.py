"""Punto de entrada de la app. Ejecutar con: uv run main.py"""

from src.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
