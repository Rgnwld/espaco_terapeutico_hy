from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Usuario  # Assumindo que está em models.py
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def hash_senha(senha: str):
    # Exemplo simples de hash – use bcrypt/scrypt em produção!
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_admin(_user, _email, _senha):
    session = SessionLocal()
    try:
        usuario_existente = session.query(Usuario).filter_by(email=_email).first()
        
        if not usuario_existente:
            admin = Usuario(
                nome=_user,
                email=_email,
                senha=hash_senha(_senha),
                tipo='admin'
            )
            session.add(admin)
            session.commit()
            print("Usuário admin criado com sucesso.")
        else:
            print("Usuário admin já existe.")
    finally:
        session.close()

if __name__ == "__main__":
    criar_admin()
