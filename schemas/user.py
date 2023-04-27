from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str

    class Config:
        orm_mode = True
