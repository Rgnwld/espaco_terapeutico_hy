import jwt
import os
from flask import Blueprint, request, jsonify, g
from db.connection import SessionLocal
from datetime import datetime, timedelta
from app.models.usuario import Usuario
from app.models.log import Log
from app.utils.auth import auth_required
import bcrypt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
login_bp = Blueprint('login', __name__)


@login_bp.before_request
def before_request():
    g.db = SessionLocal()

@login_bp.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@login_bp.route("/", methods=["POST"])
def login():
    db = g.db
    data = request.get_json()
    
    if not SECRET_KEY:
        log_acesso = Log(descricao=f"Usuário: {data['email']} - Problemas com a Senha de Encrypt do Servidor!", tipo="login")
        db.add(log_acesso)
        db.commit()
        return jsonify(message="Problemas com a Senha de Encrypt do Servidor!"), 500
    
    if not data:
        log_acesso = Log(descricao=f"Usuário: {data['email']} - Dados de login não fornecidos!", tipo="login")
        db.add(log_acesso)
        db.commit()     
        return jsonify(message="Dados de login não fornecidos!"), 400
    
    if "email" not in data or "senha" not in data:
        log_acesso = Log(descricao=f"Usuário: {data['email']} - Campos 'email' e 'senha' são obrigatórios!", tipo="login")
        db.add(log_acesso)
        db.commit()
        return jsonify(message="Campos 'email' e 'senha' são obrigatórios!"), 400
    
    
    usuario_existente = db.query(Usuario).filter_by(email=data['email']).first()
    
    if usuario_existente:
        try: 
            print("Verificando senha para o usuário:" + data['senha'] + " com hash: " + usuario_existente.senha)
            senha = bcrypt.checkpw(password=str(data['senha']).encode('utf-8'), hashed_password=usuario_existente.senha.encode('utf-8'))
        except Exception as e:
            log_acesso = Log(descricao=f"Usuário: {data['email']} - Erro ao verificar senha: {str(e)}", tipo="login")
            db.add(log_acesso)
            db.commit()
            return jsonify(message="Erro ao verificar senha!"), 500
        if senha:
            log_acesso = Log(descricao=f"Usuário: {data['email']} - Login Realizado!", tipo="login")
            db.add(log_acesso)
            db.commit() 
            # Gerar o token com expiração
            token = jwt.encode(
                {"user": data["email"], "exp": datetime.utcnow() + timedelta(minutes=30)},
                SECRET_KEY,
                algorithm="HS256"
            )
            return jsonify(token=token), 200

    return jsonify(message="Credenciais inválidas!"), 401

@login_bp.route("/refresh_token", methods=["POST"])
def refresh_token():
    db = g.db
    token = request.headers.get('Authorization')
    print(token)
    
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        new_token = jwt.encode(
            {"user": decoded["user"], "exp": datetime.utcnow() + timedelta(minutes=30)},
            SECRET_KEY,
            algorithm="HS256",
        )
        log = Log(descricao=f"Token atualizado para o usuário: {decoded['user']}", tipo="refresh_token")
        db.add(log)
        db.commit()
        return jsonify(refresh_token=new_token), 200
    except jwt.ExpiredSignatureError:
        return jsonify(message="Token expirado! Faça login novamente."), 401
    except jwt.InvalidTokenError:
        return jsonify(message="Token inválido!"), 401


@login_bp.route("/auth_teste", methods=["POST"])
@auth_required
def teste():
    return jsonify(message="Autenticado com sucesso!"), 200