"""
Módulo de configuración de la aplicación Flask.

Carga las variables de entorno desde un archivo `.env` y define una clase
de configuración que puede ser utilizada por la aplicación para acceder
a parámetros como claves secretas, la URI de la base de datos, etc.
"""

import os
from dotenv import load_dotenv

# Carga las variables del archivo .env en el entorno
load_dotenv()

class Config:
    """
    Clase de configuración base para la aplicación Flask.

    Atributos:
        SECRET_KEY (str): Clave secreta usada por Flask para sesiones y seguridad.
        SQLALCHEMY_DATABASE_URI (str): URI de la base de datos para SQLAlchemy.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Desactiva señales innecesarias de SQLAlchemy.
        JWT_SECRET_KEY (str): Clave secreta usada para firmar tokens JWT.
        UPLOAD_FOLDER (str): Ruta absoluta al directorio donde se almacenan archivos subidos.
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecret")
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "upload")
