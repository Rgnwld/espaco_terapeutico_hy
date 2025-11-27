from base_data import criar_usuario, criar_local, criar_perfil_usuario, criar_perfils, init_db, criar_atendimento
from datetime import datetime
# from datetime import datetime

# Nota: Melhorar gerenciamento de erros e logs em produção

try:   
    init_db()
    print("Banco de dados inicializado com sucesso.")
except Exception as e:
    print(f"Erro ao inicializar o banco de dados: {e}")


try:
    criar_perfils('ADMIN')
    criar_perfils('PROFISSIONAL')
    criar_perfils('PACIENTE')
    criar_usuario("Admin", "", "admin@admin.com", "admin123", datetime(1990, 2, 1))
    criar_usuario("Profissional", "Teste", "profissional@to.com", "profissional123",   datetime(1990, 3, 1))
    criar_usuario("Paciente", "Teste", "paciente@to.com", "paciente123", datetime(1990, 1, 1))
    criar_perfil_usuario(1, 1)  # ADMIN para o usuário 1
    criar_perfil_usuario(2, 2)  # PROFISSIONAL para o usuário 2
    criar_perfil_usuario(3, 3)  # PACIENTE para o usuário
    criar_local("SP", "São Paulo", "Centro", "Rua A", "100", "Apto 10")
    criar_local("RJ", "Rio de Janeiro", "Copacabana", "Avenida B", "200", "Apto 20")
    criar_local("MG", "Belo Horizonte", "Savassi", "Rua C", "300", "Apto 30")    
    criar_atendimento(2, 3, datetime(2024, 6, 15, 10, 0),  "Consulta inicial",)
    print("Dados iniciais criados com sucesso.")
except Exception as e:
    print(f"Erro ao inicializar o dados: {e}")
        
        
