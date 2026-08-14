"""Controller: recibe las peticiones HTTP y coordina Model <-> View.

Ninguna consulta SQL ni lógica de presentación vive acá: sólo orquestación
(RF1-RF8 de la especificación 001).
"""

from flask import Blueprint, abort, redirect, render_template, request, url_for

from src.models import dia as dia_model
from src.models import ejercicio as ejercicio_model

bp = Blueprint("rutina", __name__)


def _datos_form():
    return {
        "nombre": request.form["nombre"].strip(),
        "series": int(request.form["series"]),
        "repeticiones": int(request.form["repeticiones"]),
        "peso": request.form.get("peso", "").strip() or None,
        "descanso": request.form.get("descanso", "").strip() or None,
        "notas": request.form.get("notas", "").strip() or None,
    }


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/dia/<nombre_dia>")
def ver_dia(nombre_dia):
    # RF2: sólo existen lunes..viernes; cualquier otro valor es 404.
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    ejercicios = ejercicio_model.listar_por_dia(nombre_dia)
    return render_template("dia.html", dia=nombre_dia, ejercicios=ejercicios)


@bp.route("/dia/<nombre_dia>/agregar", methods=["POST"])
def agregar_ejercicio(nombre_dia):
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    ejercicio_model.crear(nombre_dia, **_datos_form())
    return redirect(url_for("rutina.ver_dia", nombre_dia=nombre_dia))


@bp.route("/dia/<nombre_dia>/ejercicio/<int:ejercicio_id>/editar", methods=["GET", "POST"])
def editar_ejercicio(nombre_dia, ejercicio_id):
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    ejercicio = ejercicio_model.obtener(ejercicio_id)
    if ejercicio is None:
        abort(404)

    if request.method == "POST":
        ejercicio_model.actualizar(ejercicio_id, **_datos_form())
        return redirect(url_for("rutina.ver_dia", nombre_dia=nombre_dia))

    return render_template("editar.html", dia=nombre_dia, ejercicio=ejercicio)


@bp.route("/dia/<nombre_dia>/ejercicio/<int:ejercicio_id>/eliminar", methods=["POST"])
def eliminar_ejercicio(nombre_dia, ejercicio_id):
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    ejercicio_model.eliminar(ejercicio_id)
    return redirect(url_for("rutina.ver_dia", nombre_dia=nombre_dia))
