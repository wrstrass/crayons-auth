from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import config


sql_engine = create_async_engine(
    f"{config.DB}+{config.DB_DRIVER}://"
    + f"{config.DB_USER}:{config.DB_PASSWORD}@"
    + f"{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    echo=True,
    future=True,
)
print(sql_engine)


async_session = sessionmaker(
    sql_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
