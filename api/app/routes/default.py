from flask import g, jsonify, Blueprint, request
from db.connection import SessionLocal
from app.models.usuario import Usuario
from app.utils.auth import auth_required

api_bp = Blueprint('api', __name__)

@api_bp.before_request
def before_request():
    g.db = SessionLocal()

@api_bp.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
@api_bp.route("/usuarios", methods=["GET"])
@auth_required
def listar_usuarios():
    db = g.db  
    usuarios = db.query(Usuario).all()
    return jsonify([{'id':u.id, 'nome':u.nome_completo, 'email': u.email, 'perfil': u.perfil} for u in usuarios]), 200
