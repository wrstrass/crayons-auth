from pydantic import BaseModel


class UserSearchSchema(BaseModel):
    username: str


class UserSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
