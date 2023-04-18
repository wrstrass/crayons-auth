from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    login = Column(String(30))
    password = Column(String(50))

    refresh_token = relationship("RefreshToken", back_populates="user")
