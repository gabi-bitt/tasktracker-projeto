# Imagem base leve com Python 3.11
FROM python:3.11-slim

# Pasta central de operações dentro do container
WORKDIR /app

# Garante saída imediata (sem buffer) no terminal
ENV PYTHONUNBUFFERED=1

# Copia o código-fonte local para dentro do container
COPY src/ /app/src/

# Comando que dispara a execução da aplicação
CMD ["python", "src/main.py"]
