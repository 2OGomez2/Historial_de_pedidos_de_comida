from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime

from apis.comentarios.models.ComentariosModels import ComentariosModels
from apis.comentarios.models.entities.Comentarios import Comentarios

main = Blueprint('comentarios_blueprint', __name__)


@main.route('/<id>', methods=['GET'])
def get_comentario_by_id(id):
    try:
        comentario = ComentariosModels.get_comentario_by_id(id)
        if comentario:
            return jsonify(comentario)
        else:
            return jsonify({"error": "Comentario no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_comentario():
    try:
        data = request.get_json()

        required_fields = ['id_pedido', 'id_cliente', 'texto', 'calificacion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        comentario = Comentarios(
            id_comentario=str(uuid.uuid4()),
            id_pedido=data['id_pedido'],
            id_cliente=data['id_cliente'],
            texto=data['texto'],
            fecha=datetime.now(),
            calificacion=data['calificacion']
        )

        rows_affected = ComentariosModels.add_comentario(comentario)
        return jsonify({'mensaje': 'Comentario agregado', 'filas_afectadas': rows_affected}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500