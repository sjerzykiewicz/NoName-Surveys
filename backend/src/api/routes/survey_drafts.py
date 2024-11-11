from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
from src.api.models.surveys.survey import SurveyStructure
from src.api.models.surveys.survey_draft import (
    SurveyDraftCreate,
    SurveyDraftFetchOutput,
    SurveyDraftHeadersOutput,
    SurveyDraftUserActionDelete,
    SurveyDraftUserActions,
)
from src.api.models.users.user import User
from src.db.base import get_session

router = APIRouter()


LIMIT_OF_ACTIVE_SURVEY_DRAFTS = 50
PAGE_SIZE = 10


@router.post(
    "/all/{page}",
    response_description="Get all Survey Drafts Headers of a user",
    response_model=list[SurveyDraftHeadersOutput],
)
async def get_survey_drafts(
    page: int, user_input: User, session: Session = Depends(get_session)
):
    if page < 0:
        raise HTTPException(status_code=400, detail="Invalid page number")

    user = user_crud.get_user_by_email(user_input.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    return [
        SurveyDraftHeadersOutput(
            id=survey_draft.id,
            title=survey_draft.title,
            creation_date=survey_draft.creation_date,
        )
        for survey_draft in survey_draft_crud.get_not_deleted_survey_drafts_for_user(
            user.id, page * PAGE_SIZE, PAGE_SIZE, session
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
        title=survey_draft.title,
        survey_structure=SurveyStructure.model_validate_json(
            survey_draft.survey_structure
        ),
    )


@router.post(
    "/delete",
    response_description="Delete a survey draft",
    response_model=dict,
)
async def delete_survey_drafts(
    survey_draft_delete: SurveyDraftUserActionDelete,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_draft_delete.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    deleted_survey_drafts = survey_draft_crud.delete_survey_drafts(
        user.id, survey_draft_delete.ids, session
    )

    if len(deleted_survey_drafts) != len(survey_draft_delete.ids):
        raise HTTPException(
            status_code=404,
            detail="Some of the survey drafts do not exist or are already deleted",
        )

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

    survey_drafts_count = (
        survey_draft_crud.get_count_of_not_deleted_survey_drafts_for_user(
            user.id, session
        )
    )
    if survey_drafts_count >= LIMIT_OF_ACTIVE_SURVEY_DRAFTS:
        raise HTTPException(
            status_code=400,
            detail=f"User cannot have more than {LIMIT_OF_ACTIVE_SURVEY_DRAFTS} active survey drafts",
        )

    try:
        survey_draft_create.survey_structure.validate()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    created_survey_draft = survey_draft_crud.create_survey_draft(
        user.id,
        survey_draft_create.title,
        survey_draft_create.survey_structure.model_dump_json(),
        False,
        session,
    )

    return created_survey_draft.id


@router.post(
    "/count",
    response_description="Number of survey drafts of a user",
    response_model=int,
)
async def count_survey_drafts(
    user_input: User, session: Session = Depends(get_session)
):
    user = user_crud.get_user_by_email(user_input.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    return survey_draft_crud.get_count_of_not_deleted_survey_drafts_for_user(
        user.id, session
    )
