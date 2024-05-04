from pydantic import BaseModel

from src.api.models.surveys.survey import Survey


class SurveyDraftCreate(BaseModel):
    creator: int
    survey_structure: Survey

    class Config:
        extra = "forbid"


class SurveyDraftRead(SurveyDraftCreate):
    creator: int
    creation_date: str
    survey_structure: Survey

    class Config:
        extra = "forbid"
