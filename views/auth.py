from fastapi import APIRouter, Depends

from schemas import AuthSchema
from services import RegisterService


router = APIRouter()

@router.post(f"/register")
async def register(auth: AuthSchema, service: RegisterService = Depends(RegisterService)):
    return await service.register(auth)
