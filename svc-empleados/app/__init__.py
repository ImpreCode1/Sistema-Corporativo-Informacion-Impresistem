"""
Aplicación principal de Flask para la API de Empleados.

Este módulo define la función `create_app` que configura e inicializa
la aplicación Flask con la configuración, extensiones y rutas necesarias.
"""

from flask import Flask
from app.extensions import db
# from app.routes.clientes import clientes
from app.routes.auth import auth
from app.routes.empleados import empleados


def create_app(config_class):
    """
    Fábrica de aplicación para crear una instancia de Flask.

    Args:
        config_class: Clase de configuración que contiene variables como
                      URI de la base de datos, claves secretas, etc.

    Returns:
        app (Flask): Instancia de la aplicación Flask completamente configurada.
    """
    # Crear la instancia de Flask
    app = Flask(__name__)
    
    # Cargar configuración desde la clase proporcionada
    app.config.from_object(config_class)
    
    # Inicializar extensiones (por ahora solo SQLAlchemy)
    db.init_app(app)
    
    # Crear tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()
        
    # Registrar Blueprints (modularización de rutas)
    app.register_blueprint(auth)
    app.register_blueprint(empleados)
    # app.register_blueprint(clientes)  # Si decides activarlo en el futuro
    
    # Ruta raíz para prueba de funcionamiento
    @app.route("/")
    def home():
        """Ruta raíz que confirma que la API está corriendo."""
        return {"msg": "API de Empleados corriendo"}

    return app
