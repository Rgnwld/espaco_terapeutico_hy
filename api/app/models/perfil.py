from enum import Enum
from sqlalchemy import (
    Column, Integer, String, DateTime, LargeBinary, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class PERFIL(Enum):
    ADMIN = 1
    USER = 2

class Perfil(Base):
    __tablename__ = 'perfil'
    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)