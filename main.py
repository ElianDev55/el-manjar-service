from fastapi import FastAPI
from app.config.database import Session, engine, Base
from app.models.role import Role
from app.routers.role import role_router


app = FastAPI()
app.title = "Manjar Service"
app.version = "0.0.1"

# Crear la base de datos
app.include_router(role_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to Manjar Service"}