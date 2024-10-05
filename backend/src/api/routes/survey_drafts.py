from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
from src.api.models.surveys.survey import SurveyStructure
from src.api.models.surveys.survey_draft import (
    SurveyDraftCreate,
    SurveyDraftFetchOutput,
    SurveyDraftHeadersOutput,
    SurveyDraftUserActions,
)
from src.api.models.users.user import User
from src.db.base import get_session
from src.db.models.survey_draft import SurveyDraftBase

router = APIRouter()


@router.post(
    "/all",
    response_description="Get all Survey Drafts Headers of a user",
    response_model=list[SurveyDraftHeadersOutput],
)
async def get_survey_drafts(user_input: User, session: Session = Depends(get_session)):
    user = user_crud.get_user_by_email(user_input.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    return [
        SurveyDraftHeadersOutput(
            id=survey_draft.id,
            title=SurveyStructure.model_validate_json(
                survey_draft.survey_structure
            ).title,
            creation_date=survey_draft.creation_date,
        )
        for survey_draft in survey_draft_crud.get_not_deleted_survey_drafts_for_user(
            user.id, session
        )
    ]


@router.post(
    "/fetch",
    response_description="Fetch a survey draft by id",
    response_model=SurveyDraftFetchOutput,
)
async def get_survey_draft(
    survey_draft_fetch: SurveyDraftUserActions,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_draft_fetch.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    survey_draft = survey_draft_crud.get_not_deleted_survey_draft_by_id(
        survey_draft_fetch.id, session
    )
    if survey_draft is None:
        raise HTTPException(status_code=404, detail="Survey Draft does not exist")

    if survey_draft.creator_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="User does not have access to this Survey Draft",
        )

    return SurveyDraftFetchOutput(
        survey_structure=SurveyStructure.model_validate_json(
            survey_draft.survey_structure
        )
    )


@router.post(
    "/delete",
    response_description="Delete a survey draft",
    response_model=dict,
)
async def delete_survey_draft(
    survey_draft_delete: SurveyDraftUserActions,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_draft_delete.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    survey_draft = survey_draft_crud.get_not_deleted_survey_draft_by_id(
        survey_draft_delete.id, session
    )
    if survey_draft is None:
        raise HTTPException(status_code=404, detail="Survey Draft does not exist")

    if survey_draft.creator_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="User does not have access to this Survey Draft",
        )

    survey_draft_crud.delete_survey_draft_by_id(survey_draft_delete.id, session)

    return {"message": "Survey Draft deleted successfully"}


@router.post(
    "/create",
    response_description="Create a new SurveyStructure Draft",
    response_model=int,
)
async def create_survey_draft(
    survey_draft_create: SurveyDraftCreate,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_draft_create.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    try:
        survey_draft_create.survey_structure.validate()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    created_survey_draft = survey_draft_crud.create_survey_draft(
        SurveyDraftBase(
            creator_id=user.id,
            survey_structure=survey_draft_create.survey_structure.model_dump_json(),
            is_deleted=False,
        ),
        session,
    )

    return created_survey_draft.id
