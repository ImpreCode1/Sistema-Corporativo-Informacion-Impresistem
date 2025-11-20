"""
Inicialización de extensiones para la aplicación Flask.

Este módulo define las extensiones que serán utilizadas en la aplicación
y que deben ser inicializadas posteriormente dentro de la función `create_app`.
"""

from flask_sqlalchemy import SQLAlchemy

# Inicializa la extensión SQLAlchemy sin aplicarla aún a la app
db = SQLAlchemy()
