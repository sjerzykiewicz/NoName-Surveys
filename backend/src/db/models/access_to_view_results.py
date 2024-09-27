from typing import Optional

from sqlmodel import Field, SQLModel


class AccessToViewResultsBase(SQLModel):
    survey_id: Optional[int] = Field(default=None, foreign_key="survey.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class AccessToViewResults(AccessToViewResultsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
