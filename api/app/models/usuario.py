from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    # perfil = Column(Integer, ForeignKey("perfil.id")) 
    
    __mapper_args__ = {
        "polymorphic_identity": "usuario",
    }
    
    # __mapper_args__ = {
    #     "polymorphic_on": "perfil",
    # }



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
# Exemplo de atendimento (1 profissional -> N pacientes)
# -------------------------------
class Atendimento(Base):
    __tablename__ = 'atendimento'

    id = Column(Integer, primary_key=True)
    numero_atendimento = Column(String, unique=True, nullable=False)
    id_profissional = Column(Integer, ForeignKey('profissional.id'), nullable=False)
    id_paciente = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    descricao = Column(String)
    data_atendimento = Column(DateTime, default=datetime.utcnow)
    
    profissional = relationship("Profissional", backref="atendimento")
    paciente = relationship("Paciente", backref="atendimento")