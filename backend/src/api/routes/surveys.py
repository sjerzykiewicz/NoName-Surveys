from secrets import randbelow

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.ring_member as ring_member_crud
import src.db.crud.survey as survey_crud
import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
from src.api.models.surveys.survey import (
    ShareSurveyActions,
    SurveyHeadersOutput,
    SurveyInfoFetchInput,
    SurveyStructure,
    SurveyStructureCreateInput,
    SurveyStructureCreateOutput,
    SurveyStructureFetchOutput,
    SurveyUserActions,
    SurveyUserDeleteAction,
)
from src.api.models.users.user import User
from src.db.base import get_session

router = APIRouter()


LIMIT_OF_ACTIVE_SURVEYS = 50
PAGE_SIZE = 10


@router.post(
    "/count", response_description="Number of surveys of a user", response_model=int
)
async def count_surveys(user_input: User, session: Session = Depends(get_session)):
    user = user_crud.get_user_by_email(user_input.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    return survey_crud.get_count_of_not_deleted_surveys_for_user(user.id, session)


@router.post(
    "/all/{page}",
    response_description="Get all survey headers of a user",
    response_model=list[SurveyHeadersOutput],
)
async def get_surveys_for_user(
    page: int, user: User, session: Session = Depends(get_session)
):
    if page < 0:
        raise HTTPException(status_code=400, detail="Invalid page number")

    user = user_crud.get_user_by_email(user.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    user_surveys = survey_crud.get_all_surveys_user_can_view(
        user.id, page * PAGE_SIZE, PAGE_SIZE, session
    )
    return [
        SurveyHeadersOutput(
            title=survey_draft_crud.get_survey_draft_by_id(
                survey.survey_structure_id, session
            ).title,
            survey_code=survey.survey_code,
            creation_date=survey.creation_date,
            uses_cryptographic_module=survey.uses_cryptographic_module,
            is_owned_by_user=ownership,
            group_size=ring_member_crud.get_ring_member_count_for_survey(
                survey.id, session
            ),
        )
        for survey, ownership in user_surveys
    ]


@router.post(
    "/fetch",
    response_description="Fetch a survey to fill it out",
    response_model=SurveyStructureFetchOutput,
)
async def get_survey_by_code(
    survey_fetch: SurveyInfoFetchInput,
    session: Session = Depends(get_session),
):
    survey = survey_crud.get_survey_by_code(survey_fetch.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    survey_draft = survey_draft_crud.get_survey_draft_by_id(
        survey.survey_structure_id, session
    )
    return SurveyStructureFetchOutput(
        title=survey_draft.title,
        survey_structure=SurveyStructure.model_validate_json(
            survey_draft.survey_structure
        ),
        survey_code=survey.survey_code,
        uses_cryptographic_module=survey.uses_cryptographic_module,
        public_keys=(
            [
                ring_member.public_key
                for ring_member in ring_member_crud.get_ring_members_for_survey(
                    survey.id, session
                )
            ]
            if survey.uses_cryptographic_module
            else []
        ),
    )


@router.post(
    "/respondents-count",
    response_description="Number of possible respondents for a surveys",
    response_model=int,
)
async def count_survey_respondents(
    respondents_fetch: SurveyInfoFetchInput, session: Session = Depends(get_session)
):
    survey = survey_crud.get_survey_by_code(respondents_fetch.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    return (
        ring_member_crud.get_ring_member_count_for_survey(survey.id, session)
        if survey.uses_cryptographic_module
        else 0
    )


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
    if page < 0:
        raise HTTPException(status_code=400, detail="Invalid page number")

    survey = survey_crud.get_survey_by_code(respondents_fetch.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    if survey.uses_cryptographic_module:
        return [
            ring_member.user_email
            for ring_member in ring_member_crud.get_ring_members_for_survey_paginated(
                survey.id, page * PAGE_SIZE, PAGE_SIZE, session
            )
        ]
    else:
        return []


@router.post("/delete", response_description="Delete a survey", response_model=dict)
async def delete_surveys(
    survey_delete: SurveyUserDeleteAction, session: Session = Depends(get_session)
):
    user = user_crud.get_user_by_email(survey_delete.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    deleted_surveys = survey_crud.delete_surveys(
        user.id, survey_delete.survey_codes, session
    )

    if len(deleted_surveys) != len(survey_delete.survey_codes):
        raise HTTPException(
            status_code=404,
            detail="Some survey do not exist or user does not have access to them",
        )

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
    user = user_crud.get_user_by_email(survey_create.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    if (
        survey_crud.get_count_of_active_surveys_of_user(user.id, session)
        >= LIMIT_OF_ACTIVE_SURVEYS
    ):
        raise HTTPException(
            status_code=400,
            detail="User already has too many active surveys, delete some to create more",
        )

    if (
        survey_create.uses_cryptographic_module
        and not user_crud.all_users_exist_and_have_public_keys(
            survey_create.ring_members, session
        )
    ):
        raise HTTPException(
            status_code=400,
            detail="Not all users are registered or have public keys created",
        )

    try:
        survey_create.survey_structure.validate()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    survey_draft = survey_draft_crud.create_survey_draft(
        user.id,
        survey_create.title,
        survey_create.survey_structure.model_dump_json(),
        True,
        session,
    )

    survey_code = "".join(str(randbelow(10)) for _ in range(6))
    while survey_crud.survey_code_taken(survey_code, session):
        survey_code = "".join(str(randbelow(10)) for _ in range(6))
    survey = survey_crud.create_survey(
        user.id,
        survey_create.uses_cryptographic_module,
        survey_draft.id,
        survey_code,
        session,
    )
    if survey_create.uses_cryptographic_module:
        for email in survey_create.ring_members:
            public_key = user_crud.get_user_by_email(email, session).public_key
            ring_member_crud.add_ring_member(survey.id, email, public_key, session)

    survey_crud.give_survey_access(survey.id, user.id, session)
    return SurveyStructureCreateOutput(survey_code=survey.survey_code)


@router.post(
    "/give-access",
    response_description="Give access to a survey to other users",
    response_model=dict,
)
async def give_access_to_surveys(
    share_surveys_input: ShareSurveyActions, session: Session = Depends(get_session)
):
    owner = user_crud.get_user_by_email(share_surveys_input.user_email, session)
    if owner is None:
        raise HTTPException(status_code=400, detail="User not found")

    survey = survey_crud.get_survey_by_code(share_surveys_input.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    if survey.creator_id != owner.id:
        raise HTTPException(
            status_code=403, detail="User does not have access to this survey"
        )

    if not user_crud.all_users_exist(share_surveys_input.user_emails, session):
        raise HTTPException(status_code=400, detail="Not all users are registered")

    for email in share_surveys_input.user_emails:
        user = user_crud.get_user_by_email(email, session)
        survey_crud.give_survey_access(survey.id, user.id, session)

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
    owner = user_crud.get_user_by_email(take_away_access_input.user_email, session)
    if owner is None:
        raise HTTPException(status_code=400, detail="User not found")

    survey = survey_crud.get_survey_by_code(take_away_access_input.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    if survey.creator_id != owner.id:
        raise HTTPException(
            status_code=403, detail="User does not have access to this survey"
        )

    users = [
        user.id
        for user in user_crud.get_users_by_emails(
            take_away_access_input.user_emails, session
        )
    ]
    access_taken_from = survey_crud.take_away_survey_access(
        owner.id, survey.id, users, session
    )

    if len(access_taken_from) != len(users):
        raise HTTPException(
            status_code=404, detail="Some users did not have access taken away"
        )

    return {"message": "Survey access taken away successfully"}


@router.post(
    "/all-with-access-count",
    response_description="Number of users who can view results of a survey",
    response_model=int,
)
async def get_count_of_users_with_access(
    user_input: SurveyUserActions, session: Session = Depends(get_session)
):
    owner = user_crud.get_user_by_email(user_input.user_email, session)
    if owner is None:
        raise HTTPException(status_code=400, detail="User not found")

    survey = survey_crud.get_survey_by_code(user_input.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    if survey.creator_id != owner.id:
        raise HTTPException(
            status_code=403, detail="User does not have access to this survey"
        )

    return survey_crud.get_all_users_with_access_to_survey_count(survey.id, session)


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
    if page < 0:
        raise HTTPException(status_code=400, detail="Invalid page number")

    owner = user_crud.get_user_by_email(check_survey_access_input.user_email, session)
    if owner is None:
        raise HTTPException(status_code=400, detail="User not found")

    survey = survey_crud.get_survey_by_code(
        check_survey_access_input.survey_code, session
    )
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    if survey.creator_id != owner.id:
        raise HTTPException(
            status_code=403, detail="User does not have access to this survey"
        )

    return [
        user_crud.get_user_by_id(access.user_id, session).email
        for access in survey_crud.get_all_users_with_access_to_survey(
            survey.id, page * PAGE_SIZE, PAGE_SIZE, session
        )
    ]
