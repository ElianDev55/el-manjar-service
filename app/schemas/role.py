from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Role_Schema(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=50)
    state: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
