from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime
)
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    data_log = Column(DateTime, default=datetime.utcnow)