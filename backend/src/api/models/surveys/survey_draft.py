from pydantic import BaseModel

from src.api.models.surveys.survey import Survey


class SurveyDraftCreate(BaseModel):
    creator: int
    title: str
    creation_date: str

    survey_structure: Survey

    class Config:
        extra = "forbid"
