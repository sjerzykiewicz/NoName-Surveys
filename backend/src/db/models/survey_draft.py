from typing import Optional

from sqlmodel import Field, SQLModel


class SurveyDraftBase(SQLModel):
    creator: Optional[int] = Field(default=None, foreign_key="user.id")
    title: str
    survey_structure: str
    creation_date: str


class SurveyDraft(SurveyDraftBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
