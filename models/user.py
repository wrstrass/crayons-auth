from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    username = Column(String(30), unique=True)
    password = Column(String(70))

    refresh_token = relationship("RefreshToken", back_populates="user")
