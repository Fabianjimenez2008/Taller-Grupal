"""Modelo Comida: CRUD de comidas colgadas de la rutina de un día.

Cubre RF1-RF8 de la especificación 003: alta/edición/baja/listado ordenado
por día, tipo restringido a un enum fijo, y se permite más de una comida
del mismo tipo por día (RF8) porque no hay restricción de unicidad por tipo.
"""

from .db import get_connection
from .dia import obtener_rutina_id

TIPOS_VALIDOS = ["desayuno", "almuerzo", "cena", "snack"]

NOMBRES_DISPLAY_TIPO = {
    "desayuno": "Desayuno",
    "almuerzo": "Almuerzo",
    "cena": "Cena",
    "snack": "Snack",
}


def listar_por_dia(nombre_dia):
    """RF5: comidas de un día, en el orden en que fueron cargadas."""
    rutina_id = obtener_rutina_id(nombre_dia)
    if rutina_id is None:
        return []
    conn = get_connection()
    filas = conn.execute(
        "SELECT * FROM comida WHERE rutina_id = ? ORDER BY orden ASC, id ASC",
        (rutina_id,),
    ).fetchall()
    conn.close()
    return [dict(f) for f in filas]


def crear(nombre_dia, nombre, tipo):
    """RF3/RF4/RF8: agrega una comida nueva al final del día; no valida
    unicidad de tipo (se permite más de una comida del mismo tipo)."""
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"Tipo de comida inválido: {tipo}")
    rutina_id = obtener_rutina_id(nombre_dia)
    if rutina_id is None:
        raise ValueError(f"Día inválido: {nombre_dia}")
    conn = get_connection()
    siguiente_orden = conn.execute(
        "SELECT COALESCE(MAX(orden), 0) + 1 AS n FROM comida WHERE rutina_id = ?",
        (rutina_id,),
    ).fetchone()["n"]
    cur = conn.execute(
        "INSERT INTO comida (rutina_id, nombre, tipo, orden) VALUES (?, ?, ?, ?)",
        (rutina_id, nombre, tipo, siguiente_orden),
    )
    conn.commit()
    nuevo_id = cur.lastrowid
    conn.close()
    return nuevo_id


def obtener(comida_id):
    conn = get_connection()
    fila = conn.execute(
        "SELECT * FROM comida WHERE id = ?", (comida_id,)
    ).fetchone()
    conn.close()
    return dict(fila) if fila else None


def actualizar(comida_id, nombre, tipo):
    """RF4/RF7: edita una comida existente in place (sin historial)."""
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"Tipo de comida inválido: {tipo}")
    conn = get_connection()
    conn.execute(
        "UPDATE comida SET nombre = ?, tipo = ? WHERE id = ?",
        (nombre, tipo, comida_id),
    )
    conn.commit()
    conn.close()


def eliminar(comida_id):
    """RF4: borra una comida del día correspondiente."""
    conn = get_connection()
    conn.execute("DELETE FROM comida WHERE id = ?", (comida_id,))
    conn.commit()
    conn.close()
