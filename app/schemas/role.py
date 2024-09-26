from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Role_Schema_Response(BaseModel):
    id: int
    name: str
    state: bool
    created_at: datetime
    updated_at: datetime
    
    model_config = {
        "from_attributes": True  
    }

class Role_Schema_Create(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    state: bool
    created_at: Optional[datetime] = datetime.now()

    model_config = {
        "from_attributes": True 
    }


class Role_Schema_Update(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    state: Optional[bool] = None
    updated_at: Optional[datetime] = datetime.now()
    
    model_config = {
        "from_attributes": True
    }

class Role_Schema_Message(BaseModel):
    message: str
    model_config = {
        "from_attributes": True
    }