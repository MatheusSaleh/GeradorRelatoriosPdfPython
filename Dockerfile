# Base Debian com Python 3.11
FROM python:3.11-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2 \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    python3-dev \
    pkg-config \
    libglib2.0-0 \
    fonts-dejavu-core \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências Python
RUN pip install --no-cache-dir fastapi uvicorn jinja2 weasyprint

# Expõe porta do FastAPI
EXPOSE 8000

# Comando para rodar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
