from fastapi import APIRouter, HTTPException,status, Query
from sqlalchemy.exc import SQLAlchemyError
from app.services.person import PersonService
from app.config.database import Session
from app.schemas.person import Person_Schema_Response, Person_Schema_Create, Person_Schema_Message,Person_Schema_Query_Search_Name,Person_Schema_Update
from typing import Annotated, Literal

database = Session()
person_service = PersonService(database)
person_router = APIRouter()




@person_router.get("/person", tags=["person"], response_model=list[Person_Schema_Response], status_code=status.HTTP_200_OK)
async def get_persons():
    try:
        persons = person_service.service_get_all()
        return persons
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")

@person_router.get("/person/{id}", tags=["person"], response_model=Person_Schema_Response, status_code=status.HTTP_200_OK)
async def get_role(id: int) -> any:
    try:
        person = person_service.service_get_by_id(id)
        if person is None:
            raise HTTPException(status_code=404, detail="Role not found")
        return person
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error al acceder a la base de datos")

@person_router.get("/person/search/", tags=["person"])
async def search_person(person_name: Annotated[Person_Schema_Query_Search_Name, Query()]) -> Person_Schema_Response :
    try:
        person_name = person_service.service_search_by_name(person_name)
        if person_name is None:
            raise HTTPException(status_code=404, detail="Person not found")
        return person_name
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")


@person_router.post("/person", tags=["person"],response_model=Person_Schema_Response, status_code=status.HTTP_201_CREATED)
async def create_role(person: Person_Schema_Create) -> any:
    
    try:
        role_search_by_name = person_service.service_search_by_name(person)
        if role_search_by_name:
            raise HTTPException(status_code=400, detail="Person already exists")
        
        add_person= person_service.service_create(person)
        return  add_person
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")



@person_router.patch("/person/{id}", tags=["person"],response_model=Person_Schema_Response, status_code=status.HTTP_200_OK)

async def update_role(id: int,  person: Person_Schema_Update) -> any:
    try:
        
        person_id = person_service.service_get_by_id(id)
        if person_id is None:
            raise HTTPException(status_code=404, detail="Person not found")

        update_role = person_service.service_update(id, person)
        return update_role
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")


@person_router.delete("/person/{id}", tags=["person"],response_model=Person_Schema_Message, status_code=status.HTTP_200_OK)
async def delete_role(id: int):
    try:
        person_search_by_id = person_service.service_get_by_id(id)
        if person_search_by_id is None:
            raise HTTPException(status_code=404, detail="Person not found")
        
        person_service.service_delete(id)
        return {"message": "Person deleted successfully of id {}".format(id)}
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")
