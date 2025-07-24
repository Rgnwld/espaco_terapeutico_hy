from init_db import init_db
from base_data import criar_admin 

# Nota: Melhorar gerenciamento de erros e logs em produção

try:
    init_db()
except Exception as e:
    print(f"Erro ao inicializar o banco de dados: {e}")

try:
    criar_admin("Admin", "admin@admin.com", "admin123")
except Exception as e:
    print(f"Erro ao inicializar o dados: {e}")
        
        
