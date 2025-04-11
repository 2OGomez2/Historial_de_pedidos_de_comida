from flask import Flask
from flask_cors import CORS
from config.config import app_config

from apis.categorias.routes import Categorias
from apis.repartidores.routes import Repartidores
from apis.entregas.routes import Entregas
from apis.clientes.routes import Clientes
from apis.productos.routes import Productos
from apis.estados.routes import Estados
from apis.facturas.routes import Facturas
from apis.comentarios.routes import Comentarios
from apis.telefonos.routes import Telefonos
from apis.notificaciones.routes import Notificaciones


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(app_config['development'])

    # Registrar Blueprints
    app.register_blueprint(Repartidores.main, url_prefix='/api/repartidores')
    app.register_blueprint(Clientes.main, url_prefix='/api/clientes')
    app.register_blueprint(Productos.main, url_prefix='/api/productos')
    app.register_blueprint(Estados.main, url_prefix='/api/estados')
    app.register_blueprint(Facturas.main, url_prefix='/api/facturas')
    app.register_blueprint(Categorias.main, url_prefix='/api/categorias')
    app.register_blueprint(Entregas.main, url_prefix='/api/entregas')
    app.register_blueprint(Comentarios.main, url_prefix='/api/comentarios')
    app.register_blueprint(Telefonos.main, url_prefix='/api/telefonos')
    app.register_blueprint(Notificaciones.main, url_prefix='/api/notificaciones')

    # Manejo de errores
    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return "<h1>Página no encontrada</h1>", 404

    @app.errorhandler(500)
    def error_servidor(error):
        return "<h1>Error interno del servidor</h1>", 500

    @app.route('/')
    def principal():
        return "<h1>Bienvenido a mi aplicación con Flask</h1>"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
