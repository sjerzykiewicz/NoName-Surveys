from typing import Optional

from sqlmodel import Field, SQLModel


# THIS MODEL WILL BE USED LATER ON IN THE PROJECT
class UserGroupMember(SQLModel, table=True):
    group_id: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key=True
    )
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
