from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import BaseModel


class RefreshToken(BaseModel):
    __tablename__ = "refresh_token"

    created_at = Column(DateTime)
    user_id = Column(ForeignKey("user.id", ondelete="CASCADE"), unique=True)

    user = relationship("User", back_populates="refresh_token")
