from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey
)
from app.models.baseObject import Base
from datetime import datetime
from app.models.usuario import Usuario

# -------------------------------
# Exemplo de atendimento
# -------------------------------

class Atendimento(Base):
    __tablename__ = 'atendimento'

    id = Column(Integer, primary_key=True)
    numero_atendimento = Column(String, unique=True, nullable=False)
    profissional_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    paciente_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    data_atendimento = Column(DateTime, nullable=False)
    descricao = Column(String)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    
    # id_profissional = relationship("Usuario", back_populates="atendimento")
    # id_paciente = relationship("Usuario", back_populates="atendimento")