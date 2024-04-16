from typing import Optional

from sqlmodel import Field, SQLModel


# implementation of the user to be changed when we fully understand OAuth
class UserBase(SQLModel):
    email: str
    public_key: str
    can_create_surveys: bool


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
