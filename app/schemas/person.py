from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas.role import Role_Schema_Response



class Person_Schema_Response(BaseModel):
    id: int
    first_name: str
    middle_name: str
    first_surname: str
    second_surname: str
    phone: str
    email: str
    address: str
    state: bool
    created_at: str
    updated_at: str
    role: Role_Schema_Response

    model_config = {
        "from_attributes": True  
    }



class Person_Schema_Create(BaseModel):
    first_name: str
    middle_name: str
    first_surname: str
    second_surname: str
    phone: str
    email: str
    address: str
    state: bool
    role_id: int

    model_config = {
        "from_attributes": True 
    }

class Person_Schema_Update(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    first_surname: Optional[str] = None
    second_surname: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    state: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    role: Optional[int] = None
    
    model_config = {
        "from_attributes": True
    }


class Person_Schema_Query_Search_Name(BaseModel):
    first_name: str 
    middle_name: str 
    first_surname: str 
    second_surname: str
    
    model_config = {
        "from_attributes": True 
    }

class Person_Schema_Message(BaseModel):
    message: str
    model_config = {
        "from_attributes": True
    }