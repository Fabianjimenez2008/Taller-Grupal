"""Modelo Ejercicio: CRUD de ejercicios dentro de la rutina de un día.

Cubre RF4-RF8: alta/edición/baja/listado ordenado, y el hecho de que editar
o eliminar reemplaza el estado del día sin dejar historial (RF8) porque
sólo existe una fila por ejercicio, sin versionado.
"""

from .db import get_connection
from .dia import obtener_rutina_id


def listar_por_dia(nombre_dia):
    """RF6: ejercicios de un día, en el orden en que fueron cargados."""
    rutina_id = obtener_rutina_id(nombre_dia)
    if rutina_id is None:
        return []
    conn = get_connection()
    filas = conn.execute(
        "SELECT * FROM ejercicio WHERE rutina_id = ? ORDER BY orden ASC, id ASC",
        (rutina_id,),
    ).fetchall()
    conn.close()
    return [dict(f) for f in filas]


def crear(nombre_dia, nombre, series, repeticiones, peso=None, descanso=None, notas=None):
    """RF4/RF5: agrega un ejercicio nuevo al final de la rutina del día."""
    rutina_id = obtener_rutina_id(nombre_dia)
    if rutina_id is None:
        raise ValueError(f"Día inválido: {nombre_dia}")
    conn = get_connection()
    siguiente_orden = conn.execute(
        "SELECT COALESCE(MAX(orden), 0) + 1 AS n FROM ejercicio WHERE rutina_id = ?",
        (rutina_id,),
    ).fetchone()["n"]
    cur = conn.execute(
        """
        INSERT INTO ejercicio
            (rutina_id, nombre, series, repeticiones, peso, descanso, notas, orden)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (rutina_id, nombre, series, repeticiones, peso, descanso, notas, siguiente_orden),
    )
    conn.commit()
    nuevo_id = cur.lastrowid
    conn.close()
    return nuevo_id


def obtener(ejercicio_id):
    conn = get_connection()
    fila = conn.execute(
        "SELECT * FROM ejercicio WHERE id = ?", (ejercicio_id,)
    ).fetchone()
    conn.close()
    return dict(fila) if fila else None


def actualizar(ejercicio_id, nombre, series, repeticiones, peso=None, descanso=None, notas=None):
    """RF5/RF8: edita un ejercicio existente in place (sin historial)."""
    conn = get_connection()
    conn.execute(
        """
        UPDATE ejercicio
        SET nombre = ?, series = ?, repeticiones = ?, peso = ?, descanso = ?, notas = ?
        WHERE id = ?
        """,
        (nombre, series, repeticiones, peso, descanso, notas, ejercicio_id),
    )
    conn.commit()
    conn.close()


def eliminar(ejercicio_id):
    """RF5: borra un ejercicio de la rutina de su día."""
    conn = get_connection()
    conn.execute("DELETE FROM ejercicio WHERE id = ?", (ejercicio_id,))
    conn.commit()
    conn.close()
