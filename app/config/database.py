import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Variables de entorno para la base de datos
POSTGRES_DB = os.getenv('POSTGRES_DB_NAME')
POSTGRES_USER = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')


# Crear la URL de conexión a PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

try:
    # Crear el motor de SQLAlchemy
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

    # Crear una fábrica de sesiones
    Session = sessionmaker(bind=engine)

    # Crear la base de datos
    Base = declarative_base()

    print("Conexión a la base de datos exitosa")

except Exception as e:
    print(f"Error al conectar a la base de datos: {type(e).__name__}: {e}")