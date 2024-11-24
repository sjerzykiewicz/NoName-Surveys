from typing import Optional

from sqlmodel import Field, SQLModel


class UserGroupBase(SQLModel):
    creator_id: Optional[int] = Field(foreign_key="user.id", nullable=False, index=True)
    name: str = Field(nullable=False, index=True)


class UserGroup(UserGroupBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
