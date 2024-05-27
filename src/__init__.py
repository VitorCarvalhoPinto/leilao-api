from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app, origins='http://localhost:3000')

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes .tipos_routes import tipo as tipos_routes
    from .routes .banco_routes import banco as banco_routes
    from .routes .leilao_routes import leilao as leilao_routes
    from .routes .cliente_routes import clientes as cliente_routes
    from .routes .entidade_routes import entidade as entidade_routes
    from .routes .entidade_cliente_routes import entidadecliente as entidade_cliente_routes
    app.register_blueprint(tipos_routes)
    app.register_blueprint(banco_routes)
    app.register_blueprint(leilao_routes)
    app.register_blueprint(cliente_routes)
    app.register_blueprint(entidade_routes)
    app.register_blueprint(entidade_cliente_routes)

    return app