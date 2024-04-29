from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
from src.db.base import get_session
from src.db.models.survey_draft import SurveyDraftBase, SurveyDraft

router = APIRouter()


@router.get(
    "/all",
    response_description="Get all Survey Drafts",
    response_model=list[SurveyDraft],
)
async def get_user(session: Session = Depends(get_session)):
    return survey_draft_crud.get_survey_drafts(session)


@router.post(
    "/create",
    response_description="Create a new Survey Draft",
    response_model=SurveyDraftBase,
)
async def create_user(
    survey_draft_create: SurveyDraftBase, session: Session = Depends(get_session)
):
    return survey_draft_crud.create_survey_draft(survey_draft_create, session)
