import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')

def initDb():
    conexao = sqlite3.connect(DATABASE_URL)  # Cria um arquivo chamado meu_banco.db
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios limit 1")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print('Teste:')
        print(usuario)
        
    cursor.close()
    conexao.close()
    
    return "Banco de dados teste!"