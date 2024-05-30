from typing import Optional

from sqlmodel import Field, SQLModel


class RingMemberBase(SQLModel):
    survey_id: Optional[int] = Field(
        default=None, foreign_key="survey.id", primary_key=True
    )
    public_key: str


class RingMember(RingMemberBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
