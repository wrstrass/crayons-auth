from fastapi import APIRouter, Depends, Header

from schemas import AuthSchema
from services import RegisterService, LoginService, TokensService


router = APIRouter()

@router.post(f"/register")
async def register(auth: AuthSchema, service: RegisterService = Depends(RegisterService)):
    return await service.register(auth)

@router.post(f"/login")
async def login(auth: AuthSchema, service: LoginService = Depends(LoginService)):
    return await service.login(auth)

@router.get("/tokens")
async def tokens(refresh_token: str = Header(), service: TokensService = Depends(TokensService)):
    return await service.tokens(refresh_token)
