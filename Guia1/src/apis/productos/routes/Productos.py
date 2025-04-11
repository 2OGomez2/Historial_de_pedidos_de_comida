from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime

from apis.productos.models.ProductosModels import ProductosModels
from apis.productos.models.entities.Productos import Productos

main = Blueprint('productos_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_producto_by_id(id):
    try:
        producto = ProductosModels.get_producto_by_id(id)
        if producto:
            return jsonify(producto)
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_producto():
    try:
        data = request.get_json()

        required_fields = ['id_categoria', 'nombre_producto', 'descripcion', 'precio']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        producto = Productos(
            id_producto=str(uuid.uuid4()),
            id_categoria=data['id_categoria'],
            nombre_producto=data['nombre_producto'],
            descripcion=data['descripcion'],
            precio=data['precio'],
            disponible=data.get('disponible', True)
        )

        rows_affected = ProductosModels.add_producto(producto)
        return jsonify({"mensaje": "Producto agregado", "filas_afectadas": rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
