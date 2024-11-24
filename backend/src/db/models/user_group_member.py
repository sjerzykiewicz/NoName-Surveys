from typing import Optional

from sqlmodel import Field, SQLModel


class UserGroupMemberBase(SQLModel):
    group_id: int = Field(foreign_key="usergroup.id", nullable=False, index=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)


class UserGroupMember(UserGroupMemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
