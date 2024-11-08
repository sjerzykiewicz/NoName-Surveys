from datetime import datetime
from typing import Optional

import pytz
from sqlalchemy.dialects.postgresql import TEXT
from sqlmodel import Column, Field, SQLModel

tz = pytz.timezone("Europe/Warsaw")


class SurveyDraftBase(SQLModel):
    creator_id: int = Field(foreign_key="user.id", nullable=False)
    survey_structure: str = Field(sa_column=Column(TEXT))
    title: str = Field(nullable=False)
    is_deleted: bool


class SurveyDraft(SurveyDraftBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    creation_date: str = Field(
        default_factory=lambda: datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    )
