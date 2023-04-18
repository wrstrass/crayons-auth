from fastapi import FastAPI, Request
from db import sql_engine
from models import Base

PREFIX = "/api/v1/auth"


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


@app.post(f"{PREFIX}/register/")
async def register(req: Request):
    req = await req.json()
    print(req)
    return req
