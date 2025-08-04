FROM python:3.10-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto para o contêiner
COPY . /app/

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta que o Django usará
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]