from pydantic import BaseModel

from src.api.models.surveys.survey import SurveyStructure


class SurveyStructureDraft(BaseModel):
    user_email: str
    survey_structure: SurveyStructure

    class Config:
        extra = "forbid"


class SurveyStructureDraftRead(SurveyStructureDraft):
    creation_date: str

    class Config:
        extra = "forbid"
