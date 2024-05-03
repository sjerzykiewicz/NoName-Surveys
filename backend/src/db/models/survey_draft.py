from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class SurveyDraftBase(SQLModel):
    creator: int = Field(foreign_key="user.id", nullable=False)
    title: str
    survey_structure: str


class SurveyDraft(SurveyDraftBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: str = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
