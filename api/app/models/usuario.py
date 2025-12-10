from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, Table
)
from app.models.baseObject import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class PERFIL(Enum):
    ADMIN = 1
    PROFISSIONAL = 2
    PACIENTE = 3
    
perfil_usuario = Table("perfil_usuario", Base.metadata, Column("perfil_id", Integer, ForeignKey("perfil.id")),  Column("usuario_id", Integer, ForeignKey("usuario.id")))

class Perfil(Base):
    __tablename__ = 'perfil'
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    
    usuarios = relationship("Usuario", back_populates="perfils", secondary=perfil_usuario)

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    data_nascimento = Column(DateTime)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    
    perfils = relationship("Perfil", back_populates="usuarios", secondary=perfil_usuario)
    
    __mapper_args__ = {
        "polymorphic_identity": "usuario",
    }
    
    # __mapper_args__ = {
    #     "polymorphic_on": "perfil",
    # }