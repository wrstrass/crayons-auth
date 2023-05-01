from fastapi import APIRouter, Depends, Header

from dependencies import authenticate
from models import User
from schemas import AuthSchema, UserSchema
from services import RegisterService, LoginService, TokensService


router = APIRouter(prefix="/auth")

@router.post(f"/register")
async def register(auth: AuthSchema, service: RegisterService = Depends(RegisterService)):
    return await service.register(auth)

@router.post(f"/login")
async def login(auth: AuthSchema, service: LoginService = Depends(LoginService)):
    return await service.login(auth)

@router.get("/tokens")
async def tokens(refresh_token: str = Header(), service: TokensService = Depends(TokensService)):
    return await service.tokens(refresh_token)

@router.get("/me")
async def me(user: User = Depends(authenticate)):
    return UserSchema.from_orm(user)
