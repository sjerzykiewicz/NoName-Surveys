import re
from datetime import datetime

from pydantic import BaseModel, ValidationInfo, field_validator

from src.api.models.surveys.survey import SurveyStructure


class SurveyDraftCreate(BaseModel):
    user_email: str
    survey_structure: SurveyStructure

    @field_validator("user_email")
    def validate_user_email(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("email must be provided")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class SurveyDraftHeadersOutput(BaseModel):
    id: int
    title: str
    creation_date: datetime

    class Config:
        extra = "forbid"


class SurveyDraftUserActions(BaseModel):
    user_email: str
    id: int

    @field_validator("user_email")
    def validate_user_email(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("email must be provided")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class SurveyDraftFetchOutput(BaseModel):
    survey_structure: SurveyStructure

    class Config:
        extra = "forbid"
