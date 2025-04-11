from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime

from apis.entregas.models.EntregasModels import EntregasModels
from apis.entregas.models.entities.Entregas import Entregas

main = Blueprint('entregas_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_entrega_by_id(id):
    try:
        entrega = EntregasModels.get_entrega_by_id(id)
        if entrega:
            return jsonify(entrega)
        else:
            return jsonify({"error": "Entrega no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_entrega():
    try:
        data = request.get_json()

        required_fields = ['id_pedido', 'fecha_entrega']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        entrega = Entregas(
            id_entrega=str(uuid.uuid4()),
            id_pedido=data['id_pedido'],
            fecha_entrega=data['fecha_entrega']
        )

        rows_affected = EntregasModels.add_entrega(entrega)
        return jsonify({"mensaje": "Entrega registrada", "filas_afectadas": rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
