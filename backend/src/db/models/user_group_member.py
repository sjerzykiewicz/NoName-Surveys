from typing import Optional

from sqlmodel import Field, SQLModel


class UserGroupMemberBase(SQLModel):
    group_id: Optional[int] = Field(default=None, foreign_key="usergroup.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class UserGroupMember(UserGroupMemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
