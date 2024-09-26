FROM python:3.9-slim

WORKDIR /app

# Instala las dependencias necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Copia el archivo de requisitos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Comando para ejecutar la aplicación
CMD ["fastapi", "run", "main.py", "--port", "80"]
