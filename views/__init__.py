from fastapi import APIRouter
from config import PREFIX
from views import auth, user

router = APIRouter(prefix=PREFIX)
router.include_router(auth.router)
router.include_router(user.router)
