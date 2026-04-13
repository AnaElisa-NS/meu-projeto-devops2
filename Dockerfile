# Usa imagem oficial do Python
FROM python:3.11

# Define diretório dentro do container
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Comando para executar o programa
CMD ["python", "main.py"]