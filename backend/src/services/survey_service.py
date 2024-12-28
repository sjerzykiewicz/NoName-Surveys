from fastapi import HTTPException
from sqlmodel import Session

import src.db.crud.ring_member as ring_member_crud
import src.db.crud.survey as survey_crud
import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
import src.services.utils.helpers as helpers
from src.api.models.surveys.survey import (
    ShareSurveyActions,
    SurveyEnableDisableAction,
    SurveyHeadersOutput,
    SurveyInfoFetchInput,
    SurveyStructure,
    SurveyStructureCreateInput,
    SurveyStructureCreateOutput,
    SurveyStructureFetchOutput,
    SurveyUserActions,
    SurveyUserDeleteAction,
)
from src.db.models.user import User

LIMIT_OF_ACTIVE_SURVEYS = 50
PAGE_SIZE = 10


def count_surveys(user_input: User, session: Session) -> int:
    user = helpers.get_user_by_email(user_input.user_email, session)
    return survey_crud.get_count_of_not_deleted_surveys_for_user(user.id, session)


def get_surveys_for_user(
    page: int, user_input: User, session: Session
) -> list[SurveyHeadersOutput]:
    helpers.validate_page_for_pagination(page)
    user = helpers.get_user_by_email(user_input.user_email, session)
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
            is_enabled=survey.is_enabled,
        )
        for survey, ownership in user_surveys
    ]


def get_survey_by_code(
    survey_fetch: SurveyInfoFetchInput, session: Session
) -> SurveyStructureFetchOutput:
    survey = helpers.get_survey_by_code(survey_fetch.survey_code, session)
    survey_draft = helpers.get_survey_draft_by_id(survey.survey_structure_id, session)

    return SurveyStructureFetchOutput(
        title=survey_draft.title,
        survey_structure=SurveyStructure.model_validate_json(
            survey_draft.survey_structure
        ),
        survey_code=survey.survey_code,
        uses_cryptographic_module=survey.uses_cryptographic_module,
        public_keys=(
            ring_member_crud.get_public_keys_for_survey(survey.id, session)
            if survey.uses_cryptographic_module
            else []
        ),
    )


def count_survey_respondents(
    respondents_fetch: SurveyInfoFetchInput, session: Session
) -> int:
    survey = helpers.get_survey_by_code(respondents_fetch.survey_code, session)
    return (
        ring_member_crud.get_ring_member_count_for_survey(survey.id, session)
        if survey.uses_cryptographic_module
        else 0
    )


def get_respondents_by_code(
    page: int, respondents_fetch: SurveyInfoFetchInput, session: Session
) -> list[str]:
    helpers.validate_page_for_pagination(page)
    survey = helpers.get_survey_by_code(respondents_fetch.survey_code, session)
    return (
        ring_member_crud.get_ring_members_for_survey_paginated(
            survey.id, page * PAGE_SIZE, PAGE_SIZE, session
        )
        if survey.uses_cryptographic_module
        else []
    )


def delete_surveys(survey_delete: SurveyUserDeleteAction, session: Session) -> None:
    user = helpers.get_user_by_email(survey_delete.user_email, session)
    deleted_surveys = survey_crud.delete_surveys(
        user.id, survey_delete.survey_codes, session
    )

    if len(deleted_surveys) != len(survey_delete.survey_codes):
        raise HTTPException(
            status_code=404,
            detail="Some surveys do not exist or user does not have access to them",
        )


def create_survey(
    survey_create: SurveyStructureCreateInput, session: Session
) -> SurveyStructureCreateOutput:
    user = helpers.get_user_by_email(survey_create.user_email, session)
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

    survey_code = helpers.generate_survey_code(session)
    survey = survey_crud.create_survey(
        user.id,
        survey_create.uses_cryptographic_module,
        survey_draft.id,
        survey_code,
        session,
    )
    if survey_create.uses_cryptographic_module:
        for email in survey_create.ring_members:
            public_key = helpers.get_user_by_email(email, session).public_key
            ring_member_crud.add_ring_member(survey.id, email, public_key, session)

    survey_crud.give_survey_access(survey.id, user.id, session)
    return SurveyStructureCreateOutput(survey_code=survey.survey_code)


def give_access_to_surveys(
    share_surveys_input: ShareSurveyActions, session: Session
) -> None:
    owner = helpers.get_user_by_email(share_surveys_input.user_email, session)
    survey = helpers.get_survey_by_code(share_surveys_input.survey_code, session)
    helpers.check_if_user_has_access(owner.id, survey.creator_id)

    if not user_crud.all_users_exist(share_surveys_input.user_emails, session):
        raise HTTPException(status_code=400, detail="Not all users are registered")

    for email in share_surveys_input.user_emails:
        user = helpers.get_user_by_email(email, session)
        survey_crud.give_survey_access(survey.id, user.id, session)


def take_away_access_to_surveys(
    take_away_access_input: ShareSurveyActions, session: Session
) -> None:
    owner = helpers.get_user_by_email(take_away_access_input.user_email, session)
    survey = helpers.get_survey_by_code(take_away_access_input.survey_code, session)
    helpers.check_if_user_has_access(owner.id, survey.creator_id)

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


def reject_access_to_surveys(
    reject_access_input: SurveyUserDeleteAction, session: Session
) -> None:
    user = helpers.get_user_by_email(reject_access_input.user_email, session)
    rejected_surveys = survey_crud.reject_access_to_surveys(
        user.id, reject_access_input.survey_codes, session
    )

    if len(rejected_surveys) != len(reject_access_input.survey_codes):
        raise HTTPException(
            status_code=404,
            detail="Some surveys do not exist or user does not have access to them",
        )


def get_count_of_users_with_access(
    user_input: SurveyUserActions, session: Session
) -> int:
    owner = helpers.get_user_by_email(user_input.user_email, session)
    survey = helpers.get_survey_by_code(user_input.survey_code, session)
    helpers.check_if_user_has_access(owner.id, survey.creator_id)

    return survey_crud.get_all_users_with_access_to_survey_count(survey.id, session)


def get_all_users_without_access(
    user_input: SurveyUserActions, session: Session
) -> list[str]:
    owner = helpers.get_user_by_email(user_input.user_email, session)
    survey = helpers.get_survey_by_code(user_input.survey_code, session)
    helpers.check_if_user_has_access(owner.id, survey.creator_id)

    return survey_crud.get_all_users_with_no_access_to_survey(survey.id, session)


def check_access_to_surveys(
    page: int, check_survey_access_input: SurveyUserActions, session: Session
) -> list[str]:
    helpers.validate_page_for_pagination(page)
    owner = helpers.get_user_by_email(check_survey_access_input.user_email, session)
    survey = helpers.get_survey_by_code(check_survey_access_input.survey_code, session)
    helpers.check_if_user_has_access(owner.id, survey.creator_id)

    return [
        user_crud.get_user_by_id(access.user_id, session).email
        for access in survey_crud.get_all_users_with_access_to_survey(
            survey.id, page * PAGE_SIZE, PAGE_SIZE, session
        )
    ]


def enable_or_disable_survey(
    user_input: SurveyEnableDisableAction, session: Session
) -> None:
    owner = helpers.get_user_by_email(user_input.user_email, session)
    survey = helpers.get_survey_by_code(user_input.survey_code, session)
    helpers.check_if_user_has_access(owner.id, survey.creator_id)

    survey_crud.enable_or_disable_survey(survey.id, user_input.is_enabled, session)
