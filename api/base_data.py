from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.usuario import Usuario, Base as BaseUsuario
from app.models.perfil import Perfil, Base as BasePerfil
from app.models.log import Log, Base as BaseLog
from app.utils.senha import hash_senha  # Importando a função de hash de senha
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    engine = create_engine(DATABASE_URL)

    BaseUsuario.metadata.create_all(engine)
    BasePerfil.metadata.create_all(engine)
    BaseLog.metadata.create_all(engine)

def criar_default_perfils(_descricao):
    session = SessionLocal()
    try:
        perfil_existente = session.query(Perfil).filter_by(descricao=_descricao).first()
        
        if not perfil_existente:
            perfil = Perfil(
                descricao=_descricao,
            )
            session.add(perfil)
            session.commit()
            print("Perfil criados com sucesso.")
        else:
            print("Perfil:" + _descricao +  " já gerado.")
            print(perfil_existente.id)
    except Exception as e:
        print(f"Erro ao criar perfil: {e}")
        session.rollback()
    finally:
        session.close()
        
def criar_usuario(_user, _email, _senha, _perfil):
    session = SessionLocal()
    try:
        usuario_existente = session.query(Usuario).filter_by(email=_email).first()
        
        if not usuario_existente:
            admin = Usuario(
                nome_completo=_user,
                email=_email,
                senha=hash_senha(_senha),
                perfil=_perfil
            )
            session.add(admin)
            session.commit()
            print("Usuário criado com sucesso.")
        else:
            print("Usuário já existe.")
    finally:
        session.close()