from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.services.answers_service as service
from src.api.models.surveys.answer import (
    SurveyAnswerBase,
    SurveyAnswersFetchInput,
    SurveyAnswersFetchOutput,
)
from src.db.base import get_session
from src.services.utils.exceptions import (
    DuplicateAnswerException,
    InvalidSignatureException,
    InvalidSurveyStructureException,
    SurveyDraftNotFoundException,
    SurveyNotFoundException,
    UserAccessException,
    UserNotFoundException,
)

router = APIRouter()


@router.post(
    "/fetch",
    response_description="Fetch answers for a survey",
    response_model=list[SurveyAnswersFetchOutput],
)
async def get_survey_answers_by_code(
    survey_fetch: SurveyAnswersFetchInput,
    session: Session = Depends(get_session),
):
    try:
        return service.get_survey_answers_by_code(survey_fetch, session)
    except (
        UserNotFoundException,
        SurveyNotFoundException,
        SurveyDraftNotFoundException,
        UserAccessException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/fill",
    response_description="Save answers for a survey",
    response_model=dict,
)
async def save_survey_answer(
    survey_answer: SurveyAnswerBase,
    session: Session = Depends(get_session),
):
    try:
        return service.save_survey_answer(survey_answer, session)
    except (
        UserNotFoundException,
        SurveyNotFoundException,
        UserAccessException,
        InvalidSurveyStructureException,
        DuplicateAnswerException,
        InvalidSignatureException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))
