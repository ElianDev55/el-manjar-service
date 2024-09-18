from fastapi import APIRouter, HTTPException
from app.services.role import RoleService
from app.config.database import Session
from app.schemas.role import Role_Schema
from fastapi.responses import JSONResponse

dabase = Session()
role_service = RoleService(dabase)
role_router = APIRouter()


@role_router.get("/roles", tags=["roles"], response_model=list[Role_Schema])
def get_roles() -> list[Role_Schema]:
        roles = role_service.service_get_all()
        return roles


@role_router.get("/role/{id}",tags=["roles"], response_model=Role_Schema)
def get_role(id: int) -> Role_Schema:

    role = role_service.service_get_by_id(id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@role_router.post("/role",tags=["roles"], response_model=Role_Schema)
def create_role(role: Role_Schema):
    
    role_search = role_service.service_search_by_name(role)
    if role_search:
        raise HTTPException(status_code=400, detail="Role already exists")
    
    
    add_role =  role_service.service_create(role)
    return JSONResponse(status_code=201 ,content={
        "message": "Role created successfully",
        "data": add_role
    })

@role_router.patch("/role/{id}")
def update_role(id: int):
    return {"message": f"Update role with id {id}"}

@role_router.delete("/role/{id}")
def delete_role(id: int):
    return {"message": f"Delete role with id {id}"}
