# AdvApi

# ApiAdv

## Descrição
A **ApiAdv** é uma aplicação desenvolvida em Django para gerenciar um escritório de advocacia. Ela permite a administração de clientes, casos, prazos, documentos e equipe jurídica de forma eficiente e segura.

## Tecnologias Utilizadas
- **Linguagem:** Python 3+
- **Framework:** Django + Django REST Framework
- **Banco de Dados:** PostgreSQL
- **Autenticação:** Token-based Authentication (JWT)
- **Outras Tecnologias:** Celery, Redis, Docker

## Funcionalidades Principais
- **Gestão de Clientes:** Cadastro, edição e listagem de clientes.
- **Casos Jurídicos:** Acompanhamento de processos, status e atribuição de advogados.
- **Prazos e Agendamentos:** Gerenciamento de compromissos e audiências.
- **Documentação:** Upload e organização de arquivos jurídicos.
- **Usuários e Permissões:** Perfis de administrador, advogados e assistentes.

## Instalação

### Pré-requisitos
- Python 3+
- PostgreSQL
- Docker (opcional)

### Passos
1. Clone este repositório:
   ```sh
   git clone https://github.com/seuusuario/apiadv.git
   cd apiadv
   ```
2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure o banco de dados no `.env` e aplique as migrações:
   ```sh
   python manage.py migrate
   ```
5. Crie um superusuário para acessar o painel de administração:
   ```sh
   python manage.py createsuperuser
   ```
6. Execute o servidor:
   ```sh
   python manage.py runserver
   ```

## Uso
Após iniciar o servidor, acesse a API em `http://127.0.0.1:8000/` e a interface administrativa em `http://127.0.0.1:8000/admin/`.

## Documentação da API
A documentação interativa pode ser acessada via Swagger ou Redoc:
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- Redoc: `http://127.0.0.1:8000/api/redoc/`

## Contribuição
1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature-nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça um push (`git push origin feature-nova-funcionalidade`)
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.


