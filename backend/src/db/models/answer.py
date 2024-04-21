from typing import Optional

from sqlmodel import Field, SQLModel


class Answer(SQLModel, table=True):
    survey_id: Optional[int] = Field(
        default=None, foreign_key="survey.id", primary_key=True
    )
    answer: str
    y0: str
