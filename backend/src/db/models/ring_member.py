from typing import Optional

from sqlmodel import Field, SQLModel


class RingMemberBase(SQLModel):
    survey_id: int = Field(foreign_key="survey.id", nullable=False, index=True)
    user_email: str = Field(foreign_key="user.email", nullable=False)
    public_key: str = Field(default=None)


class RingMember(RingMemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
