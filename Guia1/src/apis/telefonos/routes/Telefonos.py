from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime

from apis.telefonos.models.TelefonosModels import TelefonosModels
from apis.telefonos.models.entities.Telefonos import Telefonos

main = Blueprint('telefonos_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_telefono_by_id(id):
    try:
        telefono = TelefonosModels.get_telefono_by_id(id)
        if telefono:
            return jsonify(telefono)
        else:
            return jsonify({"error": "Teléfono no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_telefono():
    try:
        data = request.get_json()
        required_fields = ['nombre', 'numero_telefono']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        telefono = Telefonos(
            id_telefono=str(uuid.uuid4()),
            nombre=data['nombre'],
            numero_telefono=data['numero_telefono'],
            fecha_creacion=datetime.now()
        )

        rows_affected = TelefonosModels.add_telefono(telefono)
        return jsonify({"mensaje": "Teléfono agregado", "filas_afectadas": rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
