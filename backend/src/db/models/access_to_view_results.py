from typing import Optional

from sqlmodel import Field, SQLModel


class AccessToViewResultsBase(SQLModel):
    survey_id: int = Field(foreign_key="survey.id", nullable=False, index=True)
    user_id: int = Field(foreign_key="user.id", nullable=False, index=True)


class AccessToViewResults(AccessToViewResultsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
