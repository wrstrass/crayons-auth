from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from repository import BaseRepository
from db import get_session
from models.refresh_token import RefreshToken


class RefreshTokenRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(Model=RefreshToken, session=session)
