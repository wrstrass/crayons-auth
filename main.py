from fastapi import FastAPI

PREFIX = "/api/v1/auth"

app = FastAPI(
    docs_url=f"{PREFIX}/docs/",
    redoc_url=f"{PREFIX}/redoc/",
    openapi_url=f"{PREFIX}/openapi.json",
)


@app.post(f"{PREFIX}/register/")
async def register():
    return {"new": "user"}
