from flask import Blueprint, jsonify, request
import uuid
from apis.estados.models.EstadosModels import EstadosModels
from apis.estados.models.entities.Estados import Estados

main = Blueprint('estados_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_estado_by_id(id):
    try:
        estado = EstadosModels.get_estado_by_id(id)
        if estado:
            return jsonify(estado)
        else:
            return jsonify({"error": "Estado no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_estado():
    try:
        data = request.get_json()

        required_fields = ['nombre_estado', 'descripcion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        estado = Estados(
            id_estado=str(uuid.uuid4()),
            nombre_estado=data['nombre_estado'],
            descripcion=data['descripcion']
        )

        rows_affected = EstadosModels.add_estado(estado)
        return jsonify({"mensaje": "Estado agregado", "filas_afectadas": rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
