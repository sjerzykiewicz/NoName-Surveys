from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.services.survey_draft_service as service
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


@router.post(
    "/all/{page}",
    response_description="Get all Survey Drafts Headers of a user",
    response_model=list[SurveyDraftHeadersOutput],
)
async def get_survey_drafts(
    page: int, user_input: User, session: Session = Depends(get_session)
):
    return service.get_survey_drafts(page, user_input.user_email, session)


@router.post(
    "/fetch",
    response_description="Fetch a survey draft by id",
    response_model=SurveyDraftFetchOutput,
)
async def get_survey_draft(
    survey_draft_fetch: SurveyDraftUserActions,
    session: Session = Depends(get_session),
):
    survey_draft = service.get_survey_draft(
        survey_draft_fetch.id, survey_draft_fetch.user_email, session
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
    service.delete_survey_drafts(
        survey_draft_delete.user_email, survey_draft_delete.ids, session
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
    return service.create_survey_draft(survey_draft_create, session)


@router.post(
    "/count",
    response_description="Number of survey drafts of a user",
    response_model=int,
)
async def count_survey_drafts(
    user_input: User, session: Session = Depends(get_session)
):
    return service.count_survey_drafts(user_input.user_email, session)
