from datetime import datetime
from typing import Optional

import pytz
from sqlalchemy.dialects.postgresql import TIMESTAMP
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
    start_date: Optional[datetime] = Field(
        sa_column=Field(TIMESTAMP(timezone=True), nullable=True), default=None
    )
    deadline_date: Optional[datetime] = Field(
        sa_column=Field(TIMESTAMP(timezone=True), nullable=True), default=None
    )
    creation_date: datetime = Field(
        sa_column=Field(TIMESTAMP(timezone=True)),
        default_factory=lambda: datetime.now(tz),
    )
