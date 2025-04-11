from flask import Blueprint, jsonify, request
import uuid #que lo usarmemos para generarlos en Postgres
from apis.categorias.models.CategoriasModels import CategoriasModels
from apis.categorias.models.entities.Categorias import Categorias
from datetime import datetime #para manejar las fechas

main = Blueprint('categoria_blueprint', __name__)

@main. route('/<id>', methods=[ 'GET' ])
def get_categorias_by_id(id):
    try:
        categorias = CategoriasModels.get_categorias_by_id(id)
        if categorias:
             return jsonify(categorias)
        else:
             return jsonify({"error": "Empleado no encontrado"}), 404
    except Exception as ex:
     return jsonify({"error": str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_categoria():
    try:
        data = request.get_json()
        required_fields = ['nombre_categoria', 'descripcion']
        missing_fields = [field for field in required_fields if field not in data]            
        if missing_fields:
               return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        
        categorias = Categorias(
            id_categoria=categoria_id, # type: ignore
            nombre_categoria=data.get('nombre_categoria' ),
            descripcion=data.get('descripcion')
        )
        CategoriasModels.add_categoria(categorias)

        return jsonify({"message": "Categoria agregada", "id": categoria_id}), 201 # type: ignore

    except Exception as ex:
            return jsonify({"error": str(ex)}), 500

@main.route('/update/<id>', methods=['PUT' ])
def update_categoria(id): 
    try:
        data = request.get_json()
        existing_categoria = CategoriasModels.get_categoria_by_id(id)
        if not existing_categoria:
            return jsonify({"error": "Categoria no encontrada"}), 404
        required_fields = ['nombre_categoria', 'descripcion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}),500
        
        categorias = Categorias(
            id_categoria=id,
            nombre_categoria=data.get('nombre_categoria'),
            descripcion=data.get('descripcion'),
        )
        affected_rows = CategoriasModels. update_categoria(categorias)
        if affected_rows == 1:
            return jsonify({"message": "Empleado actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el empleado"}), 400
    except Exception as ex:
            return jsonify({"error": str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE' ])
def delete_categoria(id):
    try:
        categorias = Categorias(
            id_categoria=id,
            nombre_categoria="", 
            descripcion=""
        )
        affected_rows = CategoriasModels. delete_categoria(categorias)
        if affected_rows == 1:
            return jsonify({"message": f"Categoria {id} eliminada"}), 200
        else:
            return jsonify({"error": "Categoria no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
