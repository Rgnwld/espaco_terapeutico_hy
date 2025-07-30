from base_data import criar_admin_user,  criar_default_perfils

# Nota: Melhorar gerenciamento de erros e logs em produção

try:
    criar_default_perfils('ADMIN')
    criar_default_perfils('USER')
    criar_admin_user("Admin", "admin@admin.com", "admin123")
except Exception as e:
    print(f"Erro ao inicializar o dados: {e}")
        
        
