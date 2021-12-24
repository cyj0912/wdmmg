from .app import app
from flask import g
import sqlite3
from sqlite3.dbapi2 import Connection


def get_db() -> Connection:
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
