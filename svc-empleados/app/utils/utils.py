from functools import wraps
from flask import request, jsonify
import jwt
import os

# Obtiene la clave secreta desde variables de entorno
SECRET_KEY = os.getenv("SECRET_KEY")

def token_requerido(f):
    """
    Decorador que protege rutas mediante autenticación JWT.

    Este decorador verifica que la solicitud incluya un token JWT válido
    en el encabezado Authorization. Si el token no está presente, es inválido
    o ha expirado, se devuelve un error 401.

    Ejemplo de encabezado requerido:
        Authorization: Bearer <token>

    Uso:
        @app.route("/ruta-protegida")
        @token_requerido
        def ruta_protegida():
            ...

    Returns:
        JSON con error 401 si el token no es válido o falta.
        Ejecuta la función protegida si el token es válido.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Obtiene el encabezado Authorization
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token requerido"}), 401

        try:
            # Extrae el token del esquema "Bearer <token>"
            token_parts = token.split(" ")
            if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
                raise ValueError("Formato de token inválido")

            jwt.decode(token_parts[1], SECRET_KEY, algorithms=["HS256"])

        except Exception as e:
            # No se detalla el error por seguridad
            return jsonify({"error": "Token inválido o expirado"}), 401

        # Token válido: continúa con la ejecución de la función original
        return f(*args, **kwargs)

    return wrapper