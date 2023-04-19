from fastapi import FastAPI

from config import PREFIX
from db import sql_engine
from models import Base
from views import router


app = FastAPI(
    docs_url=f"{PREFIX}/docs/",
    redoc_url=f"{PREFIX}/redoc/",
    openapi_url=f"{PREFIX}/openapi.json",
)


@app.on_event("startup")
async def setup():
    async with sql_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


app.include_router(router)
