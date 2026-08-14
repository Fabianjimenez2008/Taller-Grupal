"""Controller: recibe las peticiones HTTP de comidas y coordina Model <-> View.

Vista separada de la rutina de ejercicios (RF9 de la especificación 003):
rutas propias bajo /dia/<nombre_dia>/comidas.
"""

from flask import Blueprint, abort, redirect, render_template, request, url_for

from src.models import comida as comida_model
from src.models import dia as dia_model

bp = Blueprint("comida", __name__)


def _datos_form():
    return {
        "nombre": request.form["nombre"].strip(),
        "tipo": request.form["tipo"],
    }


@bp.route("/dia/<nombre_dia>/comidas")
def ver_comidas(nombre_dia):
    # RF2 (spec 001): sólo existen lunes..viernes; cualquier otro valor es 404.
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    comidas = comida_model.listar_por_dia(nombre_dia)
    return render_template(
        "comidas.html",
        dia=nombre_dia,
        comidas=comidas,
        tipos=comida_model.TIPOS_VALIDOS,
        nombres_display_tipo=comida_model.NOMBRES_DISPLAY_TIPO,
    )


@bp.route("/dia/<nombre_dia>/comidas/agregar", methods=["POST"])
def agregar_comida(nombre_dia):
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    comida_model.crear(nombre_dia, **_datos_form())
    return redirect(url_for("comida.ver_comidas", nombre_dia=nombre_dia))


@bp.route("/dia/<nombre_dia>/comidas/<int:comida_id>/editar", methods=["GET", "POST"])
def editar_comida(nombre_dia, comida_id):
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    comida = comida_model.obtener(comida_id)
    if comida is None:
        abort(404)

    if request.method == "POST":
        comida_model.actualizar(comida_id, **_datos_form())
        return redirect(url_for("comida.ver_comidas", nombre_dia=nombre_dia))

    return render_template(
        "editar_comida.html",
        dia=nombre_dia,
        comida=comida,
        tipos=comida_model.TIPOS_VALIDOS,
        nombres_display_tipo=comida_model.NOMBRES_DISPLAY_TIPO,
    )


@bp.route("/dia/<nombre_dia>/comidas/<int:comida_id>/eliminar", methods=["POST"])
def eliminar_comida(nombre_dia, comida_id):
    if not dia_model.existe_dia(nombre_dia):
        abort(404)
    comida_model.eliminar(comida_id)
    return redirect(url_for("comida.ver_comidas", nombre_dia=nombre_dia))
