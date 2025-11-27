from flask import g, jsonify, Blueprint, request
from db.connection import SessionLocal
from app.utils.auth import auth_required
from app.models.local import Local 
from datetime import datetime

local_bp = Blueprint('local', __name__)

# Middleware para iniciar a sessão antes da requisição
@local_bp.before_request
def before_request():
    g.db = SessionLocal()

# Middleware para fechar a sessão após a requisição
@local_bp.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
# Middleware para adicionar cabeçalhos CORS após a requisição
@local_bp.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

@local_bp.route("/<id>", methods=["GET"])
@auth_required
def obter_local(id):
    db = g.db
    _local = db.query(Local).filter(Local.id == id).first()
    if _local:
        return jsonify(
            {
                'id':_local.id,
                'estado':_local.estado,
                'cidade':_local.cidade,
                'bairro':_local.bairro,
                'logradouro':_local.logradouro,
                'numero':_local.numero,
                'complemento':_local.complemento,
                'data_criacao': datetime.now()
             }), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404
    

@local_bp.route("/", methods=["POST"])
def criar_local():
    db = g.db
    data = request.get_json()
    
    if not data or not all(key in data for key in ("estado", "cidade", "bairro", "logradouro",  "numero", "complemento", "data_criacao")):
        return jsonify({"error": "Dados inválidos"}), 400
    
    novo_local = Local(
        estado=data['estado'],
        cidade=data['cidade'],
        bairro=data['bairro'],
        logradouro=data['logradouro'],
        numero=data['numero'],
        complemento=data['complemento'],
        data_criacao=data['data_criacao']
    )
    
    db.add(novo_local)
    db.commit()
    
    #return jsonify({'id': novo_usuario.id, 'nome_completo': novo_usuario.nome_completo, 'email': novo_usuario.email}), 201