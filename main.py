from fastapi import FastAPI
from app.config.database import engine, Base
from app.routers.role import role_router
from app.routers.person import person_router
from app.middleware.error_handler import custom_validation_error_handler
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.models.role import Role_Model
from app.models.person import Person_Model




app = FastAPI()
app.title = "Manjar Service"
app.version = "0.0.1"

# Crear la base de datos
app.include_router(role_router)
app.include_router(person_router)
Base.metadata.create_all(bind=engine)
app.add_exception_handler(RequestValidationError, custom_validation_error_handler)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


@app.get("/")
def home():
    return {"message": "Welcome Manjar Service"}