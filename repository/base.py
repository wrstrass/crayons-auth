from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import BaseModel


class BaseRepository:
    def __init__(self, Model: BaseModel, session: AsyncSession = Depends(get_session)):
        self.Model = Model
        self._session = session

    async def get_by_id(self, id: int) -> BaseModel:
        return await self._session.scalar(select(self.Model).where(self.Model.id == id))

    async def get_all(self) -> list[BaseModel]:
        return await self._session.scalars(select(self.Model))

    async def update(self, obj: BaseModel) -> BaseModel:
        self._session.add(obj)
        await self._session.commit()
        return obj

    async def delete(self, obj: BaseModel):
        await self._session.delete(obj)
        await self._session.commit()

    async def save(self) -> None:
        await self._session.commit()
