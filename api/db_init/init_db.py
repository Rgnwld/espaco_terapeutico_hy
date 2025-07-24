from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.environ.get('DATABASE_URL')

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
