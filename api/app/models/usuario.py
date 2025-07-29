from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, LargeBinary, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class TIPO_USUARIO(Enum):
    ADMIN = 1
    USER = 2

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    perfil = Column(Integer)  # Discriminator para herança

class Admin(Usuario):
    __tablename__ = 'admins'
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    nivel_de_acesso = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def validate_acao(self, func):
        # Validação com base no nível de acesso
        if self.nivel_de_acesso >= 5:
            return func()
        else:
            return "Acesso negado"


class Paciente(Usuario):
    __tablename__ = 'pacientes'
    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    data_nascimento = Column(DateTime)
    genero = Column(String)
    historico_medico = Column(LargeBinary)
    documentacao = Column(LargeBinary)

    __mapper_args__ = {
        'polymorphic_identity': 'paciente'
    }

    def marcarConsulta(self):
        return f"Consulta marcada para o paciente {self.nome}"


class ProfissionalDeSaude(Base):
    __tablename__ = 'profissionais'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    documentacao = Column(LargeBinary)

    def solicitarExame(self):
        return f"Exame solicitado por {self.nome}"