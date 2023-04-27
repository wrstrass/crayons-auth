from datetime import datetime
import jwt
from passlib.context import CryptContext

from models import RefreshToken
from config import SECRET_KEY
from exceptions import HTTP_401


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    return password_context.hash(SECRET_KEY + password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(SECRET_KEY + password, hashed_password)


class JWTToken:
    user_id: int
    created_at: datetime

    def __init__(self, user_id: int, created_at: datetime = None) -> None:
        self.user_id = user_id
        if type(created_at) != datetime:
            created_at = datetime.now()
        self.created_at = created_at

    @classmethod
    def from_orm(cls, model: RefreshToken) -> "JWTToken":
        return JWTToken(
            model.user_id,
            model.created_at,
        )

    def encode(self) -> str:
        return jwt.encode(
            {
                "user_id": self.user_id,
                "created_at": self.created_at.timestamp(),
            },
            SECRET_KEY,
            algorithm="HS256",
        )

    @staticmethod
    def decode(token: str) -> "JWTToken":
        try:
            token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.DecodeError:
            raise HTTP_401(detail="Invalid JWT")
        token["created_at"] = datetime.fromtimestamp(token["created_at"])
        return JWTToken(**token)
