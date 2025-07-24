from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)

# Testar a conexão
def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * from usuarios limit 1"))
        print(result.fetchone())
        return "Conexão bem-sucedida!"

def connection_decorator(func):
    def wrapper(*args, **kwargs):
        with engine.connect() as connection:
            return func(connection, *args, **kwargs)
    return wrapper