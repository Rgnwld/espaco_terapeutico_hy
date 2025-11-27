from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, LargeBinary, ForeignKey
)
from app.models.baseObject import Base
from datetime import datetime

# Base = declarative_base()

class Local(Base):
    __tablename__ = 'local'
    
    id = Column(Integer, primary_key=True)
    estado = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    logradouro = Column(String, nullable=False) 
    numero = Column(String, nullable=True)
    complemento = Column(String, nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    
    __mapper_args__ = {
        "polymorphic_identity": "local",
    }
