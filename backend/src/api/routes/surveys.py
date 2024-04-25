from fastapi import APIRouter

from src.api.models.survey import Survey

router = APIRouter()


@router.get(
    "/",
    response_description="List all surveys",
)
def list_surveys():
    return {"message": "List all surveys"}


@router.post("/create", response_description="Create a new survey")
async def create_survey(survey_create: Survey):
    return survey_create
