from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, LargeBinary, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    nome_completo = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    perfil = Column(Integer, foreign_key="perfil.id")  # usado para diferenciar o tipo de usuário

    __mapper_args__ = {
        "polymorphic_identity": "usuario",
    }

# -------------------------------
# Subclasse Paciente (herda Usuario)
# -------------------------------
class Paciente(Usuario):
    __tablename__ = 'paciente'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    data_nascimento = Column(DateTime)
    genero = Column(String)
    
    __mapper_args__ = {
        "polymorphic_identity": "paciente",
    }

# -------------------------------
# Subclasse Profissional (herda Usuario)
# -------------------------------
class Profissional(Usuario):
    __tablename__ = 'profissional'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    especialidade = Column(String)
    
    __mapper_args__ = {
        "polymorphic_identity": "profissional",
    }

# -------------------------------
# Exemplo de relacionamento (1 profissional -> N pacientes)
# -------------------------------
class Relacionamento(Base):
    __tablename__ = 'relacionamento'

    id = Column(Integer, primary_key=True)
    id_profissional = Column(Integer, ForeignKey('profissional.id'), nullable=False)
    id_paciente = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    
    profissional = relationship("Profissional", backref="relacionamentos")
    paciente = relationship("Paciente", backref="relacionamentos")