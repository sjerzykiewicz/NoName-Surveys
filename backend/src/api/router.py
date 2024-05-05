from fastapi import APIRouter

from src.api.routes import answers, survey_drafts, surveys, users

api_router = APIRouter()
api_router.include_router(answers.router, prefix="/answers", tags=["answers"])
api_router.include_router(
    survey_drafts.router, prefix="/survey-drafts", tags=["survey-drafts"]
)
api_router.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
