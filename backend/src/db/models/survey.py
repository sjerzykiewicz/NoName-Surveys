from datetime import datetime
from typing import Optional

import pytz
from sqlmodel import Field, SQLModel

tz = pytz.timezone("Europe/Warsaw")


class SurveyBase(SQLModel):
    creator_id: int = Field(foreign_key="user.id", nullable=False)
    uses_cryptographic_module: bool
    survey_structure_id: int = Field(foreign_key="surveydraft.id", nullable=False)
    survey_code: str = Field(unique=True)


class Survey(SurveyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
    deadline: str = Field(default="")
    creation_date: str = Field(
        default_factory=lambda: datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    )
