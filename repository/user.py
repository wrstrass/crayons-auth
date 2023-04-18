from sqlalchemy import select

from repository import BaseRepository
from models.user import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(Model=User)

    async def get_by_login(self, login: str) -> User:
        return await self._session.scalar(select(User).where(User.login == login))
