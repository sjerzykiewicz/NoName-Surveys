from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
from src.api.models.surveys.survey import Survey
from src.api.models.surveys.survey_draft import (
    SurveyDraftCreate,
    SurveyDraftRead,
)
from src.db.base import get_session
from src.db.models.survey_draft import SurveyDraftBase

router = APIRouter()


@router.get(
    "/all/{user_id}",
    response_description="Get all Survey Drafts",
    response_model=list[SurveyDraftRead],
)
async def get_survey_drafts(
    user_id: int, session: Session = Depends(get_session)
):
    return [
        SurveyDraftRead(
            creator=draft.creator,
            creation_date=draft.creation_date,
            survey_structure=Survey.parse_raw(draft.survey_structure),
        )
        for draft in survey_draft_crud.get_survey_drafts_for_user(
            user_id, session
        )
    ]


@router.post(
    "/create",
    response_description="Create a new Survey Draft",
    response_model=SurveyDraftRead,
)
async def create_survey_draft(
    survey_draft_create: SurveyDraftCreate,
    session: Session = Depends(get_session),
):
    survey_draft_base = SurveyDraftBase(
        creator=survey_draft_create.creator,
        survey_structure=survey_draft_create.survey_structure.model_dump_json(),
    )
    survey_draft = survey_draft_crud.create_survey_draft(
        survey_draft_base, session
    )

    return SurveyDraftRead(
        creator=survey_draft.creator,
        creation_date=survey_draft.creation_date,
        survey_structure=Survey.parse_raw(survey_draft.survey_structure),
    )
