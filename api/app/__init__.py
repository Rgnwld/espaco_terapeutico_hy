from flask import Flask, Blueprint
from app.routes.default import api_bp 
from app.routes.usuario import usuario_bp
from app.routes.login import login_bp

def create_app():
    _app = Flask(__name__)
    
    # Importa e registra os blueprints personalizados
    _app.register_blueprint(api_bp, url_prefix='/api')
    _app.register_blueprint(usuario_bp, url_prefix='/api/usuario')
    _app.register_blueprint(login_bp, url_prefix='/api/login')
    
    return _app
