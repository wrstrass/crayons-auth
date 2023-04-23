from fastapi import APIRouter, Depends

from schemas import AuthSchema
from services import RegisterService, LoginService


router = APIRouter()

@router.post(f"/register")
async def register(auth: AuthSchema, service: RegisterService = Depends(RegisterService)):
    return await service.register(auth)

@router.post(f"/login")
async def login(auth: AuthSchema, service: LoginService = Depends(LoginService)):
    return await service.login(auth)
