from flask import g, jsonify, Blueprint, request
from db.connection import SessionLocal
from app.models.usuario import Usuario, TIPO_USUARIO
from app.utils.senha import hash_senha
from app.utils.auth import auth_required

usuario_bp = Blueprint('usuario', __name__)

# Middleware para iniciar a sessão antes da requisição
@usuario_bp.before_request
def before_request():
    g.db = SessionLocal()

@usuario_bp.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
@usuario_bp.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

@usuario_bp.route("/<id>", methods=["GET"])
@auth_required
def obter_usuario(id):
    db = g.db
    u = db.query(Usuario).filter(Usuario.id == id).first()
    if u:
        return jsonify({'id':u.id, 'nome':u.nome, 'email': u.email}), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404
    

@usuario_bp.route("/", methods=["POST"])
@auth_required
def criar_usuario():
    db = g.db
    data = request.get_json()
    
    if not data or not all(k in data for k in ("nome", "email", "senha")):
        return jsonify({"error": "Dados inválidos"}), 400
    
    usuario_existente = db.query(Usuario).filter_by(email=data['email']).first()
    
    if usuario_existente:
        return jsonify({"error": "Usuário já existe"}), 400
    
    novo_usuario = Usuario(
        nome=data['nome'],
        email=data['email'],
        senha=hash_senha(data['senha']),
        tipo=TIPO_USUARIO.USER
    )
    
    db.add(novo_usuario)
    db.commit()
    
    return jsonify({'id': novo_usuario.id, 'nome': novo_usuario.nome, 'email': novo_usuario.email}), 201