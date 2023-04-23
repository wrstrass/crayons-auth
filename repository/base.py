from typing import Iterable
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import BaseModel


class NotUniqueValue(Exception):
    pass

class BaseRepository:
    def __init__(self, Model: BaseModel, session: AsyncSession):
        self.Model = Model
        self._session = session

    async def get_by_id(self, id: int) -> BaseModel:
        return await self._session.scalar(select(self.Model).where(self.Model.id == id))

    async def get_all(self) -> list[BaseModel]:
        return await self._session.scalars(select(self.Model))
    
    async def filter(self, clauses: Iterable) -> list[BaseModel]:
        query = select(self.Model)
        for clause in clauses:
            query = query.where(clause)
        values = await self._session.scalars(query)
        return values.all()

    async def get(self, clauses: Iterable) -> BaseModel:
        values = await self.filter(clauses)
        if len(values) != 1:
            raise NotUniqueValue
        return values[0]

    async def update(self, obj: BaseModel) -> BaseModel:
        self._session.add(obj)
        await self._session.commit()
        return obj

    async def delete(self, obj: BaseModel):
        await self._session.delete(obj)
        await self._session.commit()

    async def save(self) -> None:
        await self._session.commit()
