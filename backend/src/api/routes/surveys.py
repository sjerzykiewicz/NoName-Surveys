from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.services.survey_service as service
from src.api.models.surveys.survey import (
    ShareSurveyActions,
    SurveyEnableDisableAction,
    SurveyHeadersOutput,
    SurveyInfoFetchInput,
    SurveyStructureCreateInput,
    SurveyStructureCreateOutput,
    SurveyStructureFetchOutput,
    SurveyUserActions,
    SurveyUserDeleteAction,
)
from src.api.models.users.user import User
from src.db.base import get_session

router = APIRouter()


@router.post(
    "/count", response_description="Number of surveys of a user", response_model=int
)
async def count_surveys(user_input: User, session: Session = Depends(get_session)):
    return service.count_surveys(user_input, session)


@router.post(
    "/all/{page}",
    response_description="Get all survey headers of a user",
    response_model=list[SurveyHeadersOutput],
)
async def get_surveys_for_user(
    page: int, user_input: User, session: Session = Depends(get_session)
):
    return service.get_surveys_for_user(page, user_input, session)


@router.post(
    "/fetch",
    response_description="Fetch a survey to fill it out",
    response_model=SurveyStructureFetchOutput,
)
async def get_survey_by_code(
    survey_fetch: SurveyInfoFetchInput,
    session: Session = Depends(get_session),
):
    return service.get_survey_by_code(survey_fetch, session)


@router.post(
    "/respondents-count",
    response_description="Number of possible respondents for a surveys",
    response_model=int,
)
async def count_survey_respondents(
    respondents_fetch: SurveyInfoFetchInput, session: Session = Depends(get_session)
):
    return service.count_survey_respondents(respondents_fetch, session)


@router.post(
    "/respondents/{page}",
    response_description="Get emails of respondents",
    response_model=list[str],
)
async def get_respondents_by_code(
    page: int,
    respondents_fetch: SurveyInfoFetchInput,
    session: Session = Depends(get_session),
):
    return service.get_respondents_by_code(page, respondents_fetch, session)


@router.post("/delete", response_description="Delete a survey", response_model=dict)
async def delete_surveys(
    survey_delete: SurveyUserDeleteAction, session: Session = Depends(get_session)
):
    service.delete_surveys(survey_delete, session)
    return {"message": "survey deleted successfully"}


@router.post(
    "/create",
    response_description="Create a new survey",
    response_model=SurveyStructureCreateOutput,
)
async def create_survey(
    survey_create: SurveyStructureCreateInput,
    session: Session = Depends(get_session),
):
    return service.create_survey(survey_create, session)


@router.post(
    "/give-access",
    response_description="Give access to a survey to other users",
    response_model=dict,
)
async def give_access_to_surveys(
    share_surveys_input: ShareSurveyActions, session: Session = Depends(get_session)
):
    service.give_access_to_surveys(share_surveys_input, session)
    return {"message": "Survey access given successfully"}


@router.post(
    "/take-away-access",
    response_description="Take away access to a survey from another user",
    response_model=dict,
)
async def take_away_access_to_surveys(
    take_away_access_input: ShareSurveyActions,
    session: Session = Depends(get_session),
):
    service.take_away_access_to_surveys(take_away_access_input, session)
    return {"message": "Survey access taken away successfully"}


@router.post(
    "/reject-access",
    response_description="Reject access to surveys given by another user",
    response_model=dict,
)
async def reject_access_to_surveys(
    reject_access_input: SurveyUserDeleteAction,
    session: Session = Depends(get_session),
):
    service.reject_access_to_surveys(reject_access_input, session)
    return {"message": "Survey access rejected successfully"}


@router.post(
    "/all-with-access-count",
    response_description="Number of users who can view results of a survey",
    response_model=int,
)
async def get_count_of_users_with_access(
    user_input: SurveyUserActions, session: Session = Depends(get_session)
):
    return service.get_count_of_users_with_access(user_input, session)


@router.post(
    "/all-without-access",
    response_description="Users who do not have access to a survey",
    response_model=list[str],
)
async def get_all_users_without_access(
    user_input: SurveyUserActions, session: Session = Depends(get_session)
):
    return service.get_all_users_without_access(user_input, session)


@router.post(
    "/get-all-with-access/{page}",
    response_description="Check who has access to results of a given survey",
    response_model=list[str],
)
async def check_access_to_surveys(
    page: int,
    check_survey_access_input: SurveyUserActions,
    session: Session = Depends(get_session),
):
    return service.check_access_to_surveys(page, check_survey_access_input, session)


@router.post(
    "/set-enabled",
    response_description="Enable or disable a survey",
    response_model=dict,
)
async def enable_or_disable_survey(
    user_input: SurveyEnableDisableAction,
    session: Session = Depends(get_session),
):
    service.enable_or_disable_survey(user_input, session)
    return {"message": "Survey enabled status set successfully"}
