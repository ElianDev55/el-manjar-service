from app.models.role import Role_Model
from app.schemas.role import Role_Schema
from sqlalchemy.orm import Session

class RoleService:

    def __init__(self, db: Session) -> None:
        self.db = db

    def service_get_all(self) -> list[Role_Schema]:
        result = self.db.query(Role_Model).all()
        return [Role_Schema.from_orm(role) for role in result]
    
    def service_get_by_id(self, id: int) -> Role_Schema:
        result = self.db.query(Role_Model).filter(Role_Model.id == id).first()
        return Role_Schema.from_orm(result)
        
    
    def service_search_by_name(self, role: Role_Schema) -> Role_Schema:
        result = self.db.query(Role_Model).filter(Role_Model.name == role.name).first()
        return Role_Schema.from_orm(result)

    def service_create(self, role: Role_Schema) -> Role_Schema:
        try:
            new_role = Role_Model(**role.dict(exclude_unset=True))
            self.db.add(new_role)
            self.db.commit()
            self.db.refresh(new_role) 
            return Role_Schema.from_orm(new_role)
        
        except Exception as e:
            self.db.rollback()
            raise e