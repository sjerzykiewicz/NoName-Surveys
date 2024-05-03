from pydantic import BaseModel

from src.api.models.surveys.survey import Survey


class SurveyDraftCreate(BaseModel):
    creator: int
    title: str

    survey_structure: Survey

    class Config:
        extra = "forbid"


class SurveyDraftRead(SurveyDraftCreate):
    creator: int
    title: str
    creation_date: str

    survey_structure: Survey

    class Config:
        extra = "forbid"
