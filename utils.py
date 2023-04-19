from passlib.context import CryptContext
from config import SECRET_KEY


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    return password_context.hash(SECRET_KEY + password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(SECRET_KEY + password, hashed_password)
