from app.config.database import Base
import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Person_Model(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    middle_name = Column(String(50))
    first_surname = Column(String(50))
    second_surname = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    address = Column(String(50))
    state = Column(Boolean, default=True)
    created_at = Column(String, default=datetime.datetime.now())
    updated_at = Column(String, default=datetime.datetime.now())
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role_Model", back_populates="person", lazy="joined")