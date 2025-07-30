from base_data import criar_admin_user,  criar_default_perfils, init_db

# Nota: Melhorar gerenciamento de erros e logs em produção

try:   
    init_db()
    print("Banco de dados inicializado com sucesso.")
except Exception as e:
    print(f"Erro ao inicializar o banco de dados: {e}")


try:
    criar_default_perfils('ADMIN')
    criar_default_perfils('USER')
    criar_admin_user("Admin", "admin@admin.com", "admin123")
except Exception as e:
    print(f"Erro ao inicializar o dados: {e}")
        
        
