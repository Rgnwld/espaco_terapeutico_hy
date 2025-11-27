from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, insert
from app.models.baseObject import Base
from app.models.usuario import Usuario, Perfil, perfil_usuario
from app.models.local import Local
from app.models.atendimento import Atendimento
from app.utils.senha import hash_senha  # Importando a função de hash de senha
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    engine = create_engine(DATABASE_URL)
    
    Base.metadata.create_all(engine)

def criar_perfils(_descricao):
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
        
def criar_perfil_usuario(_perfil, _usuario):
    session = SessionLocal()
    try:
        perfil_usuario_existente = session.query(perfil_usuario).filter_by(perfil_id=_perfil, usuario_id=_usuario).first()

        if not perfil_usuario_existente:
            session.execute(perfil_usuario.insert().values(perfil_id=_perfil, usuario_id=_usuario))
            session.commit()
            print("Perfil-Usuario criado com sucesso.")
        else:
            print("Perfil-Usuario já gerado.")
    except Exception as e:
        print(f"Erro ao criar perfil: {e}")
        session.rollback()
    finally:
        session.close()
        
def criar_usuario(_nome, _sobrenome, _email, _senha, _data_nascimento):
    session = SessionLocal()
    try:
        usuario_existente = session.query(Usuario).filter_by(email=_email).first()
        
        if not usuario_existente:
            _usuario = Usuario(
                nome=_nome,
                sobrenome=_sobrenome,
                email=_email,
                senha=hash_senha(_senha),
                data_nascimento=_data_nascimento,
            )
            session.add(_usuario)
            session.commit()
            print("Usuário criado com sucesso.")
        else:
            print("Usuário já existe.")
    finally:
        session.close()
        
def criar_local(_estado, _cidade, _bairro, _logradouro, _numero, _complemento):
    session = SessionLocal()
    try:
        _local = Local(
            estado=_estado,
            cidade=_cidade,
            bairro=_bairro,
            logradouro=_logradouro,
            numero=_numero,
            complemento=_complemento,
        )
        session.add(_local)
        session.commit()
        print("Local criado com sucesso.")
    finally:
        session.close()
    
def criar_atendimento(_profissional, _paciente, _data_atendimento: datetime,_descricao):
    session = SessionLocal()
    try:
        _atendimento = Atendimento(
            numero_atendimento="ATEND-00" + str(_profissional) + "00" + str(_paciente) + "00" + str(_data_atendimento.year) + str(_data_atendimento.month) + str(_data_atendimento.day) + str(_data_atendimento.hour) + str(_data_atendimento.minute) + str(datetime.now().strftime("%f")),
            paciente_id=_profissional,
            profissional_id=_paciente,
            data_atendimento=_data_atendimento,
            descricao=_descricao,
        )
        session.add(_atendimento)
        session.commit()
        print("Atendimento criado com sucesso.")
    finally:
        session.close()