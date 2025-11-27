from flask import g, jsonify, Blueprint, request
from db.connection import SessionLocal
from app.utils.auth import auth_required
from app.models.atendimento import Atendimento 
from datetime import datetime

atendimento_bp = Blueprint('atendimento', __name__)

# Middleware para iniciar a sessão antes da requisição
@atendimento_bp.before_request
def before_request():
    g.db = SessionLocal()

# Middleware para fechar a sessão após a requisição
@atendimento_bp.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
# Middleware para adicionar cabeçalhos CORS após a requisição
@atendimento_bp.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

@atendimento_bp.route("/<id>", methods=["GET"])
@auth_required
def obter_local(id):
    db = g.db
    _atendimento = db.query(Atendimento).filter(Atendimento.id == id).first()
    if _atendimento:
        return jsonify(
            {
                'id':_atendimento.id,
                'id_profissional':_atendimento.id_profissional,
                'id_paciente':_atendimento.id_paciente,
                'descricao':_atendimento.descricao,
                'data_atendimento': _atendimento.data_atendimento,
                'data_criacao': datetime.now()
            }), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404
    

@atendimento_bp.route("/", methods=["POST"])
def criar_atendimento():
    db = g.db
    data = request.get_json()
    
    if not data or not all(key in data for key in ("id_profissional", "id_paciente", "descricao", "data_atendimento")):
        return jsonify({"error": "Dados inválidos"}), 400
    
    novo_atendimento = Atendimento(
        id_profissional=data['id_profissional'],
        id_paciente=data['id_paciente'],
        descricao=data['descricao'],
        data_atendimento=data['data_atendimento']
    )
    
    db.add(novo_atendimento)
    db.commit()
    
    return jsonify(novo_atendimento), 201