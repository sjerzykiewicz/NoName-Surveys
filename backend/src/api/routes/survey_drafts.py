from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
from src.api.models.surveys.survey import SurveyStructure
from src.api.models.surveys.survey_draft import (
    SurveyStructureDraft,
    SurveyStructureDraftRead,
)
from src.api.models.users.user import User
from src.db.base import get_session
from src.db.models.survey_draft import SurveyDraftBase

router = APIRouter()


@router.post(
    "/all",
    response_description="Get all SurveyStructure Drafts of a user",
    response_model=list[SurveyStructureDraftRead],
)
async def get_survey_drafts(
    user_input: User, session: Session = Depends(get_session)
):
    user = user_crud.get_user_by_email(user_input.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    return [
        SurveyStructureDraftRead(
            user_email=user_input.user_email,
            survey_structure=SurveyStructure.model_validate_json(
                survey_draft.survey_structure
            ),
            creation_date=survey_draft.creation_date,
        )
        for survey_draft in survey_draft_crud.get_survey_drafts_for_user(
            user.id, session
        )
    ]


@router.post(
    "/create",
    response_description="Create a new SurveyStructure Draft",
    response_model=SurveyStructureDraftRead,
)
async def create_survey_draft(
    survey_draft_create: SurveyStructureDraft,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_draft_create.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    try:
        survey_draft_create.survey_structure.validate()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    survey_draft = survey_draft_crud.create_survey_draft(
        SurveyDraftBase(
            creator_id=user.id,
            survey_structure=survey_draft_create.survey_structure.model_dump_json(),
        ),
        session,
    )

    return SurveyStructureDraftRead(
        user_email=survey_draft_create.user_email,
        survey_structure=survey_draft_create.survey_structure,
        creation_date=survey_draft.creation_date,
    )
