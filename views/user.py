from fastapi import APIRouter, Depends
from schemas import UserSearchSchema, UserSchema
from services import UserService


router = APIRouter(prefix="/user")

@router.post(f"/search")
async def search(search_schema: UserSearchSchema, service: UserService = Depends(UserService)) -> list[UserSchema]:
    return await service.search(search_schema)
