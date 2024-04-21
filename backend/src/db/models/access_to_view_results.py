from typing import Optional

from sqlmodel import Field, SQLModel


class AccessToViewResults(SQLModel, table=True):
    survey_id: Optional[int] = Field(
        default=None, foreign_key="survey.id", primary_key=True
    )
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
