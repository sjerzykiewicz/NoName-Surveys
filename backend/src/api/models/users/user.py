from pydantic import BaseModel


class User(BaseModel):
    email: str

    class Config:
        extra = "forbid"


class UserWithInfo(User):
    public_key: str

    class Config:
        extra = "forbid"
