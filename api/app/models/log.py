from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime
)
from datetime import datetime
from app.models.baseObject import Base

class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    data_log = Column(DateTime, default=datetime.utcnow)