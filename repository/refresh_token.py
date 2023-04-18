from sqlalchemy import select

from repository import BaseRepository
from models.refresh_token import RefreshToken


class RefreshTokenRepository(BaseRepository):
    def __init__(self):
        super().__init__(Model=RefreshToken)

    async def get_by_token(self, token: str) -> RefreshToken:
        return await self._session.scalar(select(RefreshToken).where(RefreshToken.token == token))
