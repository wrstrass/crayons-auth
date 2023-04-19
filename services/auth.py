from fastapi import Depends

from repository import UserRepository
from schemas import AuthSchema
from models import User
from utils import hash_password
from exceptions import HTTP_403


class RegisterService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)) -> None:
        self._user_repository = user_repository

    async def register(self, auth: AuthSchema) -> int:
        user = User(**auth.dict())
        user.password = hash_password(user.password)

        try:
            user = await self._user_repository.update(user)
            return user.id
        except Exception as exc:
            raise HTTP_403(detail=str(exc))
