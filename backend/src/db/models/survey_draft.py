from typing import Optional

from sqlmodel import Field, SQLModel


class SurveyDraft(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creator: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    title: str
    survey_structure: str
    creation_date: str
