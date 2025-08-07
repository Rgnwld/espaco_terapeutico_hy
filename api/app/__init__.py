from flask import Flask, Blueprint, request, Response
from app.routes.default import api_bp 
from app.routes.usuario import usuario_bp
from app.routes.login import login_bp

def create_app():
    app = Flask(__name__)
    # Importa e registra os blueprints personalizados
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(usuario_bp, url_prefix='/api/usuario/')
    app.register_blueprint(login_bp, url_prefix='/api/login/')
    
    @app.after_request
    def handle_options(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
        return response 
    
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            res = Response()
            res.headers['X-Content-Type-Options'] = '*'
            return res
    
    return app
