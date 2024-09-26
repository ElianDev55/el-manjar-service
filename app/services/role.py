from app.models.role import Role_Model
from app.schemas.role import Role_Schema_Response, Role_Schema_Create, Role_Schema_Update
from sqlalchemy.orm import Session

class RoleService:

    def __init__(self, db: Session) -> None:
        self.db = db

    def service_get_all(self) -> list[Role_Schema_Response]:
        try:
            result = self.db.query(Role_Model).order_by(Role_Model.id).all()
            return result
        except Exception as e:
            raise ValueError("An error occurred while getting the roles") from e

    def service_get_by_id(self, id: int) -> Role_Schema_Response:
        try:
            result = self.db.query(Role_Model).filter(Role_Model.id == id).first()
            return result
        except Exception as e:
            raise ValueError("An error occurred while getting the role") from e

    def service_search_by_name(self, role_name: str) -> Role_Schema_Response:
        try:
            result = self.db.query(Role_Model).filter(Role_Model.name == role_name).first()
            return result
        except Exception as e:
            raise ValueError("An error occurred while searching the role") from e

    def service_create(self, role: Role_Schema_Create) -> Role_Schema_Response:
        try:
            new_role = Role_Model(**role.model_dump(exclude_unset=True))
            self.db.add(new_role)
            self.db.commit()
            self.db.refresh(new_role)
            service_search_by_name = self.service_search_by_name(role.name)
            return service_search_by_name

        except Exception as e:
            self.db.rollback()
            raise ValueError("An error occurred while creating the role") from e

    def service_update(self, id: int, role: Role_Schema_Update) -> Role_Schema_Response:
        try:

            role_dic = role.model_dump(exclude_unset=True)
            self.db.query(Role_Model).filter(Role_Model.id == id).update(role_dic)
            self.db.commit()
            role_updated = self.db.query(Role_Model).filter(Role_Model.id == id).first()
            
            return role_updated
        
        except Exception as e:
            self.db.rollback()
            raise ValueError("An error occurred while updating the role") from e
    
    def service_delete(self, id: int) -> bool:
        try:
            self.db.query(Role_Model).filter(Role_Model.id == id).delete()
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise ValueError("An error occurred while deleting the role") from e