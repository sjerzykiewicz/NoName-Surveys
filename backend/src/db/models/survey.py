from typing import Optional

from sqlmodel import Field, SQLModel


class SurveyBase(SQLModel):
    title: str
    survey_structure: str
    creator_id: Optional[int] = Field(default=None, foreign_key="user.id")
    deadline: str
    uses_cryptographic_module: bool


class Survey(SurveyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    survey_code: str
