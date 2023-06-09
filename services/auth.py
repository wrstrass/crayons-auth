from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.responses import JSONResponse

from repository import NotUniqueValue, UserRepository, RefreshTokenRepository
from schemas import AuthSchema
from models import User, RefreshToken
from utils import hash_password, verify_password, JWTToken
from exceptions import HTTP_401, HTTP_403, HTTP_404
from config import JWT_REFRESH_EXPIRE_TIME


class RegisterService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)) -> None:
        self._user_repository = user_repository

    async def register(self, auth: AuthSchema) -> int:
        user = User(**auth.dict())
        user.password = hash_password(user.password)

        try:
            user = await self._user_repository.update(user)
            return {}
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
            refresh_token = await self.refresh_token_repository.issue(user.id)

            response = JSONResponse(content={})
            response.set_cookie("access", JWTToken(user.id).encode())
            response.set_cookie("refresh", JWTToken.from_orm(refresh_token).encode())
            return response


class TokensService:
    def __init__(
        self,
        repository: RefreshTokenRepository = Depends(RefreshTokenRepository),
    ) -> None:
        self.repository = repository

    async def tokens(self, refresh_token: str) -> JSONResponse:
        jwt_token = JWTToken.decode(refresh_token)
        if jwt_token.created_at + timedelta(minutes=JWT_REFRESH_EXPIRE_TIME) < datetime.now():
            raise HTTP_401(detail="Refresh Token expired")

        try:
            token = await self.repository.get((
                RefreshToken.user_id == jwt_token.user_id,
                RefreshToken.created_at == jwt_token.created_at,
            ))
        except NotUniqueValue:
            raise HTTP_401()

        token.created_at = datetime.now()
        await self.repository.update(token)

        response = JSONResponse(content={})
        response.set_cookie("access", JWTToken(token.user_id).encode())
        response.set_cookie("refresh", JWTToken.from_orm(token).encode())
        return response
