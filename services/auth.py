from fastapi import Depends
from fastapi.responses import JSONResponse

from repository import NotUniqueValue, UserRepository, RefreshTokenRepository
from schemas import AuthSchema
from models import User, RefreshToken
from utils import hash_password, verify_password, JWTToken
from exceptions import HTTP_403, HTTP_404


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


class LoginService:
    def __init__(
        self,
        user_repository: UserRepository = Depends(UserRepository),
        refresh_token_repository: RefreshTokenRepository = Depends(RefreshTokenRepository),
    ) -> None:
        self.user_repository = user_repository
        self.refresh_token_repository = refresh_token_repository

    async def login(self, auth: AuthSchema) -> JSONResponse:
        try:
            user = await self.user_repository.get((User.username == auth.username,))
        except NotUniqueValue:
            raise HTTP_404()

        if not verify_password(auth.password, user.password):
            raise HTTP_403(detail="Wrong Password")
        else:
            try:
                refresh_token = await self.refresh_token_repository.get((RefreshToken.user_id == user.id,))
                print(refresh_token)
            except NotUniqueValue:
                refresh_token = RefreshToken(
                    user_id = user.id,
                )

            jwt_token = JWTToken(user.id)
            refresh_token.created_at = jwt_token.created_at
            await self.refresh_token_repository.update(refresh_token)

            response = JSONResponse(content={})
            response.set_cookie("access", jwt_token.encode())
            response.set_cookie("refresh", JWTToken(user.id).encode())
            return response
