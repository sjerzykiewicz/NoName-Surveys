from secrets import randbelow
from typing import Optional

from sqlmodel import Field, SQLModel


# TODO: change to a secure way of generating survey codes
def generate_survey_code():
    return "".join(str(randbelow(10)) for _ in range(6))


class SurveyBase(SQLModel):
    deadline: str
    uses_cryptographic_module: bool
    survey_structure_id: int = Field(
        foreign_key="surveydraft.id", nullable=False
    )


class Survey(SurveyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    survey_code: str = Field(default_factory=generate_survey_code, unique=True)
