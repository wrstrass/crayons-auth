from fastapi import Depends

from models import User
from repository import UserRepository
from schemas import UserSearchSchema


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)) -> None:
        self._user_repository = user_repository

    async def search(self, search_schema: UserSearchSchema) -> list[User]:
        return await self._user_repository.filter((User.username.startswith(search_schema.username),))
