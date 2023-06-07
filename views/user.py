from fastapi import APIRouter, Depends
from schemas import UserSearchSchema, UserSchema
from services import UserService


router = APIRouter(prefix="/user")

@router.post(f"/search")
async def search(search_schema: UserSearchSchema, service: UserService = Depends(UserService)) -> list[UserSchema]:
    return await service.search(search_schema)

@router.get("/{user_id}")
async def get_by_id(user_id: int, service: UserService = Depends(UserService)) -> str:
    return await service.get_by_id(user_id)
