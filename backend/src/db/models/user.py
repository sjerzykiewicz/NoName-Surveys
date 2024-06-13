from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str = Field(unique=True)


class UserWithKey(UserBase):
    public_key: str = Field(default="")


class User(UserWithKey, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
    can_create_surveys: bool = Field(default=True)
