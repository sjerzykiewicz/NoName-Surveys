from typing import Optional

from sqlmodel import Field, SQLModel


class RingMemberBase(SQLModel):
    survey_id: Optional[int] = Field(default=None, foreign_key="survey.id")
    user_email: str = Field(default=None, foreign_key="user.email")
    public_key: str = Field(default=None)


class RingMember(RingMemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
