import re
from datetime import datetime

from pydantic import BaseModel, ValidationInfo, field_validator

from src.api.models.surveys.survey import SurveyStructure


class SurveyDraftAction(BaseModel):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("email must be provided")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class SurveyDraftCreate(SurveyDraftAction):
    title: str
    survey_structure: SurveyStructure

    @field_validator("title")
    def validate_survey_title(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("survey title must be provided")
        return v

    class Config:
        extra = "forbid"


class SurveyDraftHeadersOutput(BaseModel):
    id: int
    title: str
    creation_date: datetime

    class Config:
        extra = "forbid"


class SurveyDraftUserActions(SurveyDraftAction):
    id: int

    class Config:
        extra = "forbid"


class SurveyDraftUserActionDelete(SurveyDraftAction):
    ids: list[int]

    @field_validator("ids")
    def validate_ids(cls, v, info: ValidationInfo) -> list[int]:
        if v is None or len(v) == 0:
            raise ValueError("ids must be provided and not empty")
        return v

    class Config:
        extra = "forbid"


class SurveyDraftFetchOutput(BaseModel):
    title: str
    survey_structure: SurveyStructure

    class Config:
        extra = "forbid"
