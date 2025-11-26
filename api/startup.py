from base_data import criar_usuario, criar_local, criar_default_perfils, init_db
from app.models.perfil import  PERFIL, Base as BasePerfil
# from datetime import datetime

# Nota: Melhorar gerenciamento de erros e logs em produção

try:   
    init_db()
    print("Banco de dados inicializado com sucesso.")
except Exception as e:
    print(f"Erro ao inicializar o banco de dados: {e}")


try:
    criar_default_perfils('ADMIN')
    criar_default_perfils('PROFISSIONAL')
    criar_default_perfils('PACIENTE')
    criar_usuario("Admin", "", "admin@admin.com", "admin123")
    criar_usuario("Profissional", "Teste", "profissional@to.com", "profissional123")
    criar_usuario("Paciente", "Teste", "paciente@to.com", "paciente123")
    criar_local("SP", "São Paulo", "Centro", "Rua A", "100", "Apto 10")
    criar_local("RJ", "Rio de Janeiro", "Copacabana", "Avenida B", "200", "Apto 20")
    criar_local("MG", "Belo Horizonte", "Savassi", "Rua C", "300", "Apto 30")    
except Exception as e:
    print(f"Erro ao inicializar o dados: {e}")
        
        
