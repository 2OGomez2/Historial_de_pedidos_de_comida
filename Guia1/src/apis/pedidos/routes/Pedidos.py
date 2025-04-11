from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime

from apis.pedidos.models.PedidosModels import PedidosModels
from apis.pedidos.models.entities.Pedidos import Pedidos

main = Blueprint('pedidos_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_pedido_by_id(id):
    try:
        pedido = PedidosModels.get_pedido_by_id(id)
        if pedido:
            return jsonify(pedido)
        else:
            return jsonify({"error": "Pedido no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_pedido():
    try:
        data = request.get_json()

        required_fields = ['id_cliente', 'id_estado', 'id_repartidor', 'direccion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        pedido = Pedidos(
            id_pedido=str(uuid.uuid4()),
            id_cliente=data['id_cliente'],
            fecha_pedido=datetime.now(),
            id_estado=data['id_estado'],
            id_repartidor=data['id_repartidor'],
            direccion=data['direccion']
        )

        rows_affected = PedidosModels.add_pedido(pedido)
        return jsonify({"mensaje": "Pedido registrado", "filas_afectadas": rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500