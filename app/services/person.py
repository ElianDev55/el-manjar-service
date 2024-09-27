from app.models.person import Person_Model
from app.models.role import Role_Model
from app.schemas.person import Person_Schema_Response, Person_Schema_Create, Person_Schema_Update
from sqlalchemy.orm import Session

class PersonService:

    def __init__(self, db: Session) -> None:
        self.db = db

    def service_get_all(self) -> list[Person_Schema_Response]:
        try:
            result = self.db.query(Person_Model).order_by(Person_Model.id).all()
            return result
        except Exception as e:
            print(e)
            raise ValueError("An error occurred while getting the persons") from e

    def service_get_by_id(self, id: int) -> Person_Schema_Response:
        try:
            result = self.db.query(Person_Model).filter(Person_Model.id == id).first()
            return result
        except Exception as e:
            raise ValueError("An error occurred while getting the role") from e

    def service_search_by_name(self, person_name) -> Person_Schema_Response:
        try:
            person_name = person_name.dict()
            result = self.db.query(Person_Model).filter(
                Person_Model.first_name == person_name["first_name"],
                Person_Model.middle_name == person_name["middle_name"],
                Person_Model.first_surname == person_name["first_surname"],
                Person_Model.second_surname == person_name["second_surname"]
            ).first()
            
            if(result):
                role_data = self.db.query(Role_Model).filter(Role_Model.id == result.role_id).first()
                result.role = role_data

            return result
        
        except Exception as e:
            raise ValueError("An error occurred while searching the person")

    def service_create(self, person: Person_Schema_Create) -> Person_Schema_Response :
        try:
            new_person = Person_Model(**person.model_dump(exclude_unset=True))
            self.db.add(new_person)
            self.db.commit()
            self.db.refresh(new_person)
            service_search_by_name = self.service_search_by_name(person)
            return service_search_by_name
        except Exception as e:
            self.db.rollback()
            print(e)
            raise ValueError("An error occurred while creating the person") from e

    def service_update(self, id: int, person: Person_Schema_Update) -> Person_Schema_Response:
        try:

            person_dic = person.model_dump(exclude_unset=True)
            self.db.query(Person_Model).filter(Person_Model.id == id).update(person_dic)
            self.db.commit()
            person_updated = self.db.query(Person_Model).filter(Person_Model.id == id).first()
            return person_updated
        
        except Exception as e:
            self.db.rollback()
            raise ValueError("An error occurred while updating the person") from e
    
    def service_delete(self, id: int) -> bool:
        try:
            self.db.query(Person_Model).filter(Person_Model.id == id).delete()
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise ValueError("An error occurred while deleting the person") from e