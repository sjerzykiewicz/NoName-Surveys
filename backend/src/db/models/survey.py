from typing import Optional

from sqlmodel import Field, SQLModel


class SurveyBase(SQLModel):
    deadline: str
    uses_cryptographic_module: bool


class Survey(SurveyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    survey_code: str
    survey_structure: Optional[int] = Field(
        default=None, foreign_key="survey_draft.id"
    )
