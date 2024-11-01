# Usando a imagem oficial do Python
FROM python:3.8.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY flaskr/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=flaskr/app.py
ENV FLASK_ENV=development  

# Para modo de desenvolvimento; altere para 'production' em produção

# Expõe a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
