from pydantic import BaseModel

from src.api.models.surveys.survey import SurveyStructure


class SurveyStructureDraftCreate(BaseModel):
    creator: int
    survey_structure: SurveyStructure

    class Config:
        extra = "forbid"


class SurveyStructureDraftRead(SurveyStructureDraftCreate):
    creator: int
    creation_date: str
    survey_structure: SurveyStructure

    class Config:
        extra = "forbid"
