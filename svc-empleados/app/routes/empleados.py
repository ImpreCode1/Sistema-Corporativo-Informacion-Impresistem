import os
from flask import Blueprint, request, jsonify, Response
from dotenv import load_dotenv
from app.utils.utils import token_requerido

load_dotenv()

empleados = Blueprint("empleados", __name__)

# =========================
# Obtener todos los empleados
# =========================
@empleados.route("/empleados", methods=["GET"])
@token_requerido
def obtener_empleados():
    """
    Devuelve todos los empleados en formato JSON.
    """
    # TODO: Reemplazar con consulta real a la base de datos
    empleados = []  # Lista simulada
    return jsonify(empleados), 200

# =========================
# Obtener un empleado por ID
# =========================
@empleados.route("/empleados/<int:id_empleado>", methods=["GET"])
@token_requerido
def obtener_empleado(id_empleado):
    """
    Devuelve los datos de un empleado específico por ID.
    """
    # TODO: Reemplazar con búsqueda real
    empleado = {"id": id_empleado}  # Simulación
    return jsonify(empleado), 200

# =========================
# Crear un nuevo empleado
# =========================
@empleados.route("/empleados", methods=["POST"])
@token_requerido
def crear_empleado():
    """
    Crea un nuevo empleado.
    """
    data = request.json
    # TODO: Validar y guardar datos en la base de datos
    return jsonify({"mensaje": "Empleado creado", "data": data}), 201

# =========================
# Actualizar un empleado
# =========================
@empleados.route("/empleados/<int:id_empleado>", methods=["PUT"])
@token_requerido
def actualizar_empleado(id_empleado):
    """
    Actualiza los datos de un empleado existente.
    """
    data = request.json
    # TODO: Buscar empleado y actualizar campos
    return jsonify({"mensaje": f"Empleado {id_empleado} actualizado", "data": data}), 200

# =========================
# Eliminar un empleado
# =========================
@empleados.route("/empleados/<int:id_empleado>", methods=["DELETE"])
@token_requerido
def eliminar_empleado(id_empleado):
    """
    Elimina un empleado por ID.
    """
    # TODO: Eliminar empleado de la base de datos
    return jsonify({"mensaje": f"Empleado {id_empleado} eliminado"}), 200

# =========================
# Importar empleados desde CSV
# =========================
@empleados.route("/empleados/importar", methods=["POST"])
@token_requerido
def importar_empleados():
    """
    Importa empleados desde un archivo CSV.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Archivo CSV no proporcionado"}), 400

    archivo = request.files['file']

    # TODO: Procesar el archivo CSV y guardar datos
    return jsonify({"mensaje": "Importación completada"}), 201

# =========================
# Exportar empleados a CSV
# =========================
@empleados.route("/empleados/exportar", methods=["GET"])
@token_requerido
def exportar_empleados():
    """
    Exporta los empleados a un archivo CSV.
    """

    # TODO: Obtener empleados reales
    empleados_simulados = [
        {"id": 1, "nombre": "Empleado A", "correo": "a@correo.com"},
        {"id": 2, "nombre": "Empleado B", "correo": "b@correo.com"}
    ]

    def generar_csv():
        encabezado = "id,nombre,correo\n"
        yield encabezado
        for e in empleados_simulados:
            fila = f'{e["id"]},{e["nombre"]},{e["correo"]}\n'
            yield fila

    return Response(
        generar_csv(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=empleados.csv"}
    )
