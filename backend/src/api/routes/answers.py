from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.services.answers_service as service
from src.api.models.surveys.answer import (
    SurveyAnswerBase,
    SurveyAnswersFetchInput,
    SurveyAnswersFetchOutput,
)
from src.db.base import get_session

router = APIRouter()


@router.post(
    "/fetch",
    response_description="Fetch answers to a given survey",
    response_model=list[SurveyAnswersFetchOutput],
)
async def get_survey_answers_by_code(
    survey_fetch: SurveyAnswersFetchInput,
    session: Session = Depends(get_session),
):
    return service.get_survey_answers_by_code(survey_fetch, session)


@router.post(
    "/fill",
    response_description="Fill out a survey",
    response_model=dict,
)
async def save_survey_answer(
    survey_answer: SurveyAnswerBase,
    session: Session = Depends(get_session),
):
    return service.save_survey_answer(survey_answer, session)
