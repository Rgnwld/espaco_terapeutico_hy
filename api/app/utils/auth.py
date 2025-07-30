from flask import g, jsonify, request
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

# Decorador para verificar se o usuário está autenticado
def auth_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify(message="Token de autenticação ausente!"), 401
        
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            g.user = decoded["user"]
        except jwt.ExpiredSignatureError:
            return jsonify(message="Token expirado! Faça login novamente."), 401
        except jwt.InvalidTokenError:
            return jsonify(message="Token inválido!"), 401
        return f(*args, **kwargs)
    return decorated