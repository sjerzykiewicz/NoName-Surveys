from typing import Optional

from sqlmodel import Field, SQLModel


# THIS MODEL WILL BE USED LATER ON IN THE PROJECT
class UserGroup(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creator_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    name: str
