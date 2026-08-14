"""App factory: arma la app Flask y conecta Model/View/Controller.

No es parte de M, V ni C en sí mismo — es el cableado de arranque.
"""

from pathlib import Path

from flask import Flask

from src.controllers.rutina_controller import bp as rutina_bp
from src.models.db import init_db
from src.models.dia import NOMBRES_DISPLAY, listar_dias

_VIEWS_DIR = Path(__file__).parent / "views"


def create_app():
    app = Flask(
        __name__,
        template_folder=str(_VIEWS_DIR / "templates"),
        static_folder=str(_VIEWS_DIR / "static"),
    )

    init_db()
    app.register_blueprint(rutina_bp)

    @app.context_processor
    def inject_dias_nav():
        # Disponibles en todas las plantillas para armar la navegación (RF1).
        return {"dias_nav": listar_dias(), "nombres_display": NOMBRES_DISPLAY}

    return app
