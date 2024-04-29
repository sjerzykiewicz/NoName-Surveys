from typing import Optional

from sqlmodel import Field, SQLModel


class UserGroupMember(SQLModel, table=True):
    group: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key=True
    )
    user: Optional[int] = Field(default=None, foreign_key="user.id")
