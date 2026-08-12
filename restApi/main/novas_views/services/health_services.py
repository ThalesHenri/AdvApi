import time
from django.db import connection
from main.models import Cliente, Processo, Tarefas  # Ajuste o import do app se necessário

# Guarda o momento em que a aplicação iniciou
START_TIME = time.time()

class HealthService:
    @staticmethod
    def check_system_health() -> dict:
        db_ok = True
        clientes_count = 0
        processos_ativos = 0
        tarefas_em_aberto = 0

        try:
            # Força o teste de conexão ativa com o banco de dados
            connection.ensure_connection()
            
            # Métricas baseadas nas suas models reais
            clientes_count = Cliente.objects.count()
            processos_ativos = Processo.objects.filter(status='ativo').count()
            tarefas_em_aberto = Tarefas.objects.filter(concluida=False, deletada=False).count()
            
        except Exception:
            db_ok = False

        return {
            "is_healthy": db_ok,
            "data": {
                "status": "UP" if db_ok else "DOWN",
                "database": "OK" if db_ok else "ERROR",
                "metrics": {
                    "total_clientes": clientes_count if db_ok else 0,
                    "processos_ativos": processos_ativos if db_ok else 0,
                    "tarefas_em_aberto": tarefas_em_aberto if db_ok else 0,
                },
                "uptime_seconds": round(time.time() - START_TIME, 2)
            }
        }