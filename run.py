from flask import Flask
from dotenv import load_dotenv
import os

from app.auth.auth_routes import auth_routes
from app.app_routes import app_routes  # Certo: import do módulo dentro da pasta routes
from app.extensions import db, cors

load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configurações do app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///fila.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "meusegredosecreto123")

    # Inicialização das extensões
    db.init_app(app)
    cors.init_app(app)

    # Registro dos Blueprints
    app.register_blueprint(auth_routes)
    app.register_blueprint(app_routes)

    # Criação das tabelas do banco
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
