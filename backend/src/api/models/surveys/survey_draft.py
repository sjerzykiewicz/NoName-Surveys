from datetime import datetime

from pydantic import field_validator

from src.api.models.base import Base
from src.api.models.surveys.survey import SurveyStructure


class SurveyDraftAction(Base):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v) -> str:
        return Base.validate_email(v)


class SurveyDraftCreate(SurveyDraftAction):
    title: str
    survey_structure: SurveyStructure

    @field_validator("title")
    def validate_survey_title(cls, v) -> str:
        if v is None or v == "":
            raise ValueError("survey title must be provided")
        return v


class SurveyDraftHeadersOutput(Base):
    id: int
    title: str
    creation_date: datetime


class SurveyDraftUserActions(SurveyDraftAction):
    id: int


class SurveyDraftUserActionDelete(SurveyDraftAction):
    ids: list[int]

    @field_validator("ids")
    def validate_ids(cls, v) -> list[int]:
        if v is None or len(v) == 0:
            raise ValueError("ids must be provided and not empty")
        return v


class SurveyDraftFetchOutput(Base):
    title: str
    survey_structure: SurveyStructure
