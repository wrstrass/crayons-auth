from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from repository import BaseRepository
from db import get_session
from models.user import User


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(Model=User, session=session)

    async def get_by_username(self, username: str) -> User:
        return await self._session.scalar(select(User).where(User.username == username))
