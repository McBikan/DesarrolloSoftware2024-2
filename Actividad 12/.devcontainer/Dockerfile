FROM python:3.9

# Instalar dependencias adicionales
RUN apt-get update && apt-get install -y \
    curl \
    git

# Instalar dependencias de Python
WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt
