from datetime import datetime
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from repository import BaseRepository, NotUniqueValue
from db import get_session
from models.refresh_token import RefreshToken


class RefreshTokenRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(Model=RefreshToken, session=session)

    async def issue(self, user_id: int) -> RefreshToken:
        try:
            refresh_token = await self.get((RefreshToken.user_id == user_id,))
        except NotUniqueValue:
            refresh_token = RefreshToken(
                user_id = user_id,
            )

        refresh_token.created_at = datetime.now()
        await self.update(refresh_token)
        return refresh_token
