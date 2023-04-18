from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class RefreshToken(BaseModel):
    __tablename__ = "refresh_token"

    token = Column(String(50))
    user_id = Column(ForeignKey("user.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="refresh_token")
