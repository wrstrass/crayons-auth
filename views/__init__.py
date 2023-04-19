from fastapi import APIRouter
from config import PREFIX
from views import auth

router = APIRouter(prefix=PREFIX)
router.include_router(auth.router)
