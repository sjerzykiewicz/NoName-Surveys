from typing import Optional

from sqlalchemy.dialects.postgresql import TEXT
from sqlmodel import Column, Field, SQLModel


class AnswerBase(SQLModel):
    survey_id: int = Field(foreign_key="survey.id")
    answer: str = Field(sa_column=Column(TEXT))
    y0: str = Field(default="")


class Answer(AnswerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
