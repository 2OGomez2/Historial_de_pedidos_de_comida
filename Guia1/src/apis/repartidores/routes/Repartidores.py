from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime

from apis.repartidores.models.RepartidoresModels import RepartidoresModels
from apis.repartidores.models.entities.Repartidores import Repartidores

main = Blueprint('repartidores_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_repartidor_by_id(id):
    try:
        repartidor = RepartidoresModels.get_repartidor_by_id(id)
        if repartidor:
            return jsonify(repartidor)
        else:
            return jsonify({"error": "Repartidor no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_repartidor():
    try:
        data = request.get_json()
        required_fields = ['nombre_repartidor', 'telefono', 'dui']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        repartidor = Repartidores(
            id_repartidor=str(uuid.uuid4()),
            nombre_repartidor=data['nombre_repartidor'],
            telefono=data['telefono'],
            dui=data['dui'],
            activo=data.get('activo', True)
        )

        rows_affected = RepartidoresModels.add_repartidor(repartidor)
        return jsonify({"mensaje": "Repartidor agregado", "filas_afectadas": rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
