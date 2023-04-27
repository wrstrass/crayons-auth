from datetime import datetime, timedelta
from fastapi import Depends, Header

from repository import UserRepository, NotUniqueValue
from models import User
from utils import JWTToken
from exceptions import HTTP_401, HTTP_404
from config import JWT_ACCESS_EXPIRE_TIME


async def authenticate(
    access_token: str = Header(),
    user_repository: UserRepository = Depends(UserRepository),
) -> User:
    jwt_token = JWTToken.decode(access_token)
    if jwt_token.created_at + timedelta(minutes=JWT_ACCESS_EXPIRE_TIME) < datetime.now():
        raise HTTP_401(detail="Access Token expired")

    try:
        user = await user_repository.get((User.id == jwt_token.user_id,))
    except NotUniqueValue:
        raise HTTP_401(detail="User Not Found")

    return user
