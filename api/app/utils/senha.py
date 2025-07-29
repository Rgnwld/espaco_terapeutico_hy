import bcrypt
def hash_senha(senha: str):
    # Usando bcrypt para hash de senha
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bytes, salt)
    return hashed.decode('utf-8')