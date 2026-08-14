"""Modelo Dia: los 5 días fijos de entrenamiento (RF1, RF2).

No existe (ni se puede crear) día para sábado o domingo: la lista de días
válidos es fija y cerrada.
"""

from .db import DIAS_VALIDOS, get_connection

NOMBRES_DISPLAY = {
    "lunes": "Lunes",
    "martes": "Martes",
    "miercoles": "Miércoles",
    "jueves": "Jueves",
    "viernes": "Viernes",
}


def listar_dias():
    """Los 5 días fijos, en orden lunes -> viernes (RF1)."""
    return DIAS_VALIDOS


def existe_dia(nombre_dia):
    """RF2: valida que el día pedido sea uno de los 5 hábiles soportados."""
    return nombre_dia in DIAS_VALIDOS


def obtener_rutina_id(nombre_dia):
    """Id de la rutina única (RF3) asociada a un día."""
    conn = get_connection()
    fila = conn.execute(
        """
        SELECT rutina.id FROM rutina
        JOIN dia ON dia.id = rutina.dia_id
        WHERE dia.nombre = ?
        """,
        (nombre_dia,),
    ).fetchone()
    conn.close()
    return fila["id"] if fila else None
