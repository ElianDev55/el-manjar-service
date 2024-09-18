from app.config.database import Base
import datetime
from sqlalchemy import Column, Integer, String, Boolean

class Role_Model(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    state = Column(Boolean, default=True)
    created_at = Column(String, default=datetime.datetime.now())
    updated_at = Column(String, default=datetime.datetime.now())
