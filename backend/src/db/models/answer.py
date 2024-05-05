from typing import Optional

from sqlmodel import Field, SQLModel


class AnswerBase(SQLModel):
    survey_id: int = Field(foreign_key="survey.id")
    answer: str
    y0: str = Field(default="")


class Answer(AnswerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
