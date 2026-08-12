import json
from django.core.management.base import BaseCommand
from django.test import Client
from main.models import Advogado  # Ajuste o import do app se necessário

class Command(BaseCommand):
    help = 'Executa o menu interativo de testes do sistema'

    def handle(self, *args, **options):
        self.testar_fluxo_autenticacao_completo()

    def testar_fluxo_autenticacao_completo(self):
        print("\n==================================================")
        print("      INICIANDO TESTE DE FLUXO DE LOGIN & JWT")
        print("==================================================")
        
        client = Client()
        email_teste = "advogado.teste@escritorio.com"
        senha_teste = "SenhaSegura@1234"
        
        # Passo 0: Garantir que o advogado de teste existe
        print("\n[Passo 0] Verificando/Criando Advogado de Teste...")
        advogado, criado = Advogado.objects.get_or_create(
            email=email_teste,
            defaults={
                "nome": "Doutor Teste da Silva",
                "telefone": "(83) 98888-7777",
                "oab": "PB99999"
            }
        )
        if criado or not advogado.check_password(senha_teste):
            advogado.set_password(senha_teste)
            advogado.save()
            print(f"-> Advogado '{email_teste}' criado/atualizado com sucesso.")
        else:
            print(f"-> Advogado '{email_teste}' já existente pronto para uso.")

        # Passo 1: Requisitar o Token CSRF ('csrf/' mapeado no seu urls.py)
        # Nota: Se suas URLs estão sob um prefixo como '/api/', ajuste para '/api/csrf/'
        print("\n[Passo 1] Requisitando Token CSRF...")
        response_csrf = client.get('/api/csrf/') 
        
        if response_csrf.status_code != 200:
            print(f"[ERRO] Falha ao obter o cookie CSRF. Status: {response_csrf.status_code}")
            print(f"Detalhes: {response_csrf.content.decode()}")
            return
        
        csrf_token = client.cookies.get('csrftoken')
        if not csrf_token:
            print("[ERRO] O cookie 'csrftoken' não foi retornado.")
            return
        print(f"[SUCESSO] Cookie CSRF obtido com sucesso: {csrf_token.value[:10]}...")

        # Passo 2: Efetuar Login ('token/' mapeado no seu urls.py)
        print("\n[Passo 2] Efetuando Login (CustomTokenObtainPairView)...")
        payload_login = {
            "email": email_teste,
            "password": senha_teste
        }
        
        response_login = client.post(
            '/api/token/',
            data=json.dumps(payload_login),
            content_type='application/json',
            HTTP_X_CSRFTOKEN=csrf_token.value
        )
        
        print(f"-> Status HTTP do Login: {response_login.status_code}")
        
        if response_login.status_code != 200:
            print(f"[ERRO] O login falhou! Resposta: {response_login.content.decode()}")
            return
        
        access_cookie = client.cookies.get('access_token')
        refresh_cookie = client.cookies.get('refresh_token')
        
        if not access_cookie or not refresh_cookie:
            print("[ERRO] O login retornou 200, mas os cookies HttpOnly não foram definidos.")
            return
        
        print("[SUCESSO] Login realizado com cookies HttpOnly gerados!")

        # Passo 3: Testar Renovação de Token ('token/refresh/' mapeado no seu urls.py)
        print("\n[Passo 3] Testando Renovação de Token (CustomTokenRefreshView)...")
        response_refresh = client.post(
            '/api/token/refresh/',
            HTTP_X_CSRFTOKEN=csrf_token.value
        )
        
        print(f"-> Status HTTP do Refresh: {response_refresh.status_code}")
        
        if response_refresh.status_code == 200:
            print("[SUCESSO] Token renovado com sucesso utilizando o cookie de refresh!")
        else:
            print(f"[ERRO] Falha ao renovar o token: {response_refresh.content.decode()}")
            return

        print("\n==================================================")
        print("   FLUXO DE AUTENTICAÇÃO VALIDADO COM SUCESSO! ✅")
        print("==================================================")