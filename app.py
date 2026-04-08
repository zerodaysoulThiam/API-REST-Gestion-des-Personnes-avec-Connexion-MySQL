from flask import Flask, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from routes import people_bp
import os

# ============================================================
# app.py — Flask + Swagger UI integre
# ============================================================

app = Flask(__name__)

# --- Enregistrer les routes CRUD ---
app.register_blueprint(people_bp)

# --- Swagger UI ---
# L'interface sera accessible sur http://localhost:5000/swagger
SWAGGER_URL  = '/swagger'          # URL de l'interface Swagger UI
API_URL      = '/swagger.json'     # URL du fichier de spec JSON

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API Repertoire de Personnes"}
)
app.register_blueprint(swaggerui_blueprint)

# --- Servir le fichier swagger.json depuis le dossier local ---
@app.route('/swagger.json')
def swagger_json():
    return send_from_directory(os.path.dirname(__file__), 'swagger.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
