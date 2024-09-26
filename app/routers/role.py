from fastapi import APIRouter, HTTPException,status
from sqlalchemy.exc import SQLAlchemyError

from app.services.role import RoleService
from app.config.database import Session
from app.schemas.role import Role_Schema_Response,Role_Schema_Create,Role_Schema_Update,Role_Schema_Message

database = Session()
role_service = RoleService(database)
role_router = APIRouter()


@role_router.get("/role", tags=["role"], response_model=list[Role_Schema_Response], status_code=status.HTTP_200_OK)
async def get_roles() -> any:
    try:
    
        roles = role_service.service_get_all()
        return roles
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")

@role_router.get("/role/{id}", tags=["role"], response_model=Role_Schema_Response, status_code=status.HTTP_200_OK)
async def get_role(id: int) -> any:
    try:
        role = role_service.service_get_by_id(id)
        if role is None:
            raise HTTPException(status_code=404, detail="Role not found")
        return role
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Error al acceder a la base de datos")

@role_router.get("/role/search/{role_name}", tags=["role"], response_model=Role_Schema_Response, status_code=status.HTTP_200_OK)
async def search_role(role_name: str) -> any:
    try:
        role_search_by_name = role_service.service_search_by_name(role_name)
        if role_search_by_name is None:
            raise HTTPException(status_code=404, detail="Role not found")
        return role_search_by_name
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")


@role_router.post("/role", tags=["role"],response_model=Role_Schema_Response, status_code=status.HTTP_201_CREATED)
async def create_role(role: Role_Schema_Create) -> any:
    
    try:
        role_search_by_name = role_service.service_search_by_name(role.name)
        if role_search_by_name:
            raise HTTPException(status_code=400, detail="Role already exists")
        
        add_role = role_service.service_create(role)
        return add_role
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")



@role_router.patch("/role/{id}", tags=["role"],response_model=Role_Schema_Response, status_code=status.HTTP_200_OK)

async def update_role(id: int, role: Role_Schema_Update) -> any:
    try:
        
        role_id = role_service.service_get_by_id(id)
        if role_id is None:
            raise HTTPException(status_code=404, detail="Role not found")

        if role.name is not None:
            role_search_by_name = role_service.service_search_by_name(role.name)
            if role_search_by_name:
                raise HTTPException(status_code=400, detail="Role with this name already exists")

        update_role = role_service.service_update(id, role)
        return update_role
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")


@role_router.delete("/role/{id}", tags=["role"],response_model=Role_Schema_Message, status_code=status.HTTP_200_OK)
async def delete_role(id: int):
    try:
        role_search_by_id = role_service.service_get_by_id(id)
        if role_search_by_id is None:
            raise HTTPException(status_code=404, detail="Role not found")
        
        role_service.service_delete(id)
        return {"message": "Role deleted successfully of id {}".format(id)}
    
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Internal server error")
