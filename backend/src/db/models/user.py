from datetime import datetime
from typing import Optional

import pytz
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlmodel import Field, SQLModel

tz = pytz.timezone("Europe/Warsaw")


class UserBase(SQLModel):
    email: str = Field(unique=True)


class UserWithKey(UserBase):
    public_key: str = Field(default="")
    key_creation_date: Optional[datetime] = Field(
        sa_column=Field(TIMESTAMP(timezone=True), nullable=True),
        default=None,
    )


class User(UserWithKey, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
    can_create_surveys: bool = Field(default=True)
