from flask import g, jsonify, Blueprint, request
from db.connection import SessionLocal
from app.models.usuario import Usuario, PERFIL
from app.utils.senha import hash_senha
from app.utils.auth import auth_required
from datetime import datetime

usuario_bp = Blueprint('usuario', __name__)

# Middleware para iniciar a sessão antes da requisição
@usuario_bp.before_request
def before_request():
    g.db = SessionLocal()

# Middleware para fechar a sessão após a requisição
@usuario_bp.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
        
# Middleware para adicionar cabeçalhos CORS após a requisição
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
        return jsonify({'id':u.id, 'nome':u.nome, 'sobrenome':u.sobrenome, 'email': u.email}), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404
    

@usuario_bp.route("/", methods=["POST"])
def criar_usuario():
    db = g.db
    data = request.get_json()
    campos_obrigatorios = ["nome", "sobrenome", "email", "senha", "data_nascimento"]
    _data_nascimento = None
    
    if not data or not all(key in data for key in campos_obrigatorios):
        nao_encontrados = []
        for key in campos_obrigatorios:
            if key not in data:
                nao_encontrados.append(key)
        return jsonify({"error": "Existem campos obrigatorios faltando: " + ", ".join(nao_encontrados)}), 400
    
    usuario_existente = db.query(Usuario).filter_by(email=data['email']).first()
    
    if usuario_existente:
        return jsonify({"error": "Usuário já existe"}), 400
    
    if (data['email'].count('@') != 1 or data['email'].count('.') == 0 
        or data['email'].index('@') > data['email'].rindex('.') 
        or data['email'].startswith('@') or data['email'].endswith('@')  
        or data['email'].startswith('.') or data['email'].endswith('.')
        or data['email'].__contains__(' ')):
        return jsonify({"error": "Email em formato inválido."}), 400
    
    if len(data['senha']) < 6:
        return jsonify({"error": "Senha deve ter pelo menos 6 caracteres."}), 400
    
    if data['nome'].strip() == "" or data['sobrenome'].strip() == "":
        return jsonify({"error": "Nome e sobrenome não podem ser vazios."}), 400
    
    if data['nome'].isalpha() == False or data['sobrenome'].isalpha() == False:
        return jsonify({"error": "Nome e sobrenome devem conter apenas letras."}), 400
    
    if data['nome'].__contains__(' ') or data['sobrenome'].__contains__(' '):
        return jsonify({"error": "Nome e sobrenome não podem conter espaços."}), 400
    
    if data['data_nascimento']:
        try:
            _data_nascimento = datetime.strptime(data['data_nascimento'], "%d/%m/%Y")
        except ValueError:
            return jsonify({"error": "Data de nascimento em formato inválido. Use DD/MM/AAAA."}), 400
    
    novo_usuario = Usuario(
        nome=data['nome'],
        sobrenome=data['sobrenome'],
        email=data['email'],
        senha=hash_senha(data['senha']),
        data_nascimento=_data_nascimento
    )
    
    db.add(novo_usuario)
    db.commit()
    
    return jsonify({'id': novo_usuario.id, 'nome': novo_usuario.nome, 'sobrenome': novo_usuario.sobrenome, 'email': novo_usuario.email, 'data_nascimento': novo_usuario.data_nascimento, 'data_criacao' : novo_usuario.data_criacao}), 201