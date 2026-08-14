"""Capa Model: conexión y esquema de la base de datos SQLite.

Implementa RF1/RF2/RF3: los 5 días fijos (lunes a viernes) y su rutina
1 a 1 se crean al iniciar la app; nunca se crean/exponen sábado o domingo.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent.parent / "gimnasio.db"

DIAS_VALIDOS = ["lunes", "martes", "miercoles", "jueves", "viernes"]


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Crea las tablas si no existen y siembra los 5 días (RF1) con su
    rutina 1 a 1 (RF3), sin duplicar en corridas sucesivas."""
    conn = get_connection()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS dia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS rutina (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dia_id INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (dia_id) REFERENCES dia(id)
        );

        CREATE TABLE IF NOT EXISTS ejercicio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rutina_id INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            series INTEGER NOT NULL,
            repeticiones INTEGER NOT NULL,
            peso TEXT,
            descanso TEXT,
            notas TEXT,
            orden INTEGER NOT NULL,
            FOREIGN KEY (rutina_id) REFERENCES rutina(id) ON DELETE CASCADE
        );
        """
    )
    for nombre in DIAS_VALIDOS:
        conn.execute("INSERT OR IGNORE INTO dia (nombre) VALUES (?)", (nombre,))
    conn.commit()

    for nombre in DIAS_VALIDOS:
        dia = conn.execute(
            "SELECT id FROM dia WHERE nombre = ?", (nombre,)
        ).fetchone()
        conn.execute(
            "INSERT OR IGNORE INTO rutina (dia_id) VALUES (?)", (dia["id"],)
        )
    conn.commit()
    conn.close()
