import os
import datetime
import jwt
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Define un Blueprint de Flask para el módulo de autenticación
auth = Blueprint("auth", __name__)

# Claves y credenciales tomadas de variables de entorno
SECRET_KEY = os.getenv("SECRET_KEY")
API_USER = os.getenv("API_USER")
API_PASSWORD = os.getenv("API_PASSWORD")

@auth.route("/login", methods=["POST"])
def login():
    """
    Ruta de inicio de sesión.

    Esta ruta permite autenticar a un usuario mediante un nombre de usuario y contraseña.
    Si las credenciales son válidas, devuelve un token JWT con una validez de 10 horas.

    Request (JSON):
        {
            "user": "<nombre_de_usuario>",
            "password": "<contraseña>"
        }

    Response (200 OK):
        {
            "token": "<jwt_token>"
        }

    Response (401 Unauthorized):
        {
            "error": "Credenciales inválidas"
        }
    """
    data = request.json

    # Verifica que los datos estén presentes y coincidan con las credenciales del entorno
    if not data or data.get("user") != API_USER or data.get("password") != API_PASSWORD:
        return jsonify({"error": "Credenciales inválidas"}), 401
    
    # Genera un token JWT con expiración de 10 horas
    token = jwt.encode(
        {
            "user": data["user"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=10)
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({"token": token})
