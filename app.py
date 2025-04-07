from flask import Flask
from .app import app_routes  # <- Aqui está o ajuste

app = Flask(__name__)

# Registrar as rotas do Blueprint
app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)
