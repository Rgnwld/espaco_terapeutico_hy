from base_data import criar_usuario, criar_default_perfils, init_db
from app.models.perfil import  PERFIL, Base as BasePerfil

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
    criar_usuario("Admin", "admin@admin.com", "admin123", PERFIL.ADMIN.value)
    criar_usuario("Profissional", "profissional@to.com", "profissional123", PERFIL.PROFISSIONAL.value)
    criar_usuario("Paciente", "paciente@to.com", "paciente123", PERFIL.PACIENTE.value)
except Exception as e:
    print(f"Erro ao inicializar o dados: {e}")
        
        
