# 1. Usa uma imagem base com Python
FROM python:3.11-slim

# 2. Define o diretório onde o código da app vai ficar dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências
COPY requirements.txt .

# 4. Instala as dependências do projeto
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copia o restante do código da aplicação para dentro do container
COPY . .

# 6. Expõe a porta 8000 (a porta padrão do runserver)
EXPOSE 8000



# 7. Define o comando padrão para issniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
