from fastapi import APIRouter, Depends, HTTPException


role_router = APIRouter()

@role_router.get("/role")
def get_roles():
    return {"message": "Get all roles"}

@role_router.get("/role/{id}")
def get_role(id: int):
    return {"message": f"Get role with id {id}"}

@role_router.post("/role")
def create_role():
    return {"message": "Create role"}

@role_router.patch("/role/{id}")
def update_role(id: int):
    return {"message": f"Update role with id {id}"}

@role_router.delete("/role/{id}")
def delete_role(id: int):
    return {"message": f"Delete role with id {id}"}

