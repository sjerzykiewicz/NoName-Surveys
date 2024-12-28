from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
import src.services.utils.helpers as helpers
from src.api.models.surveys.survey_draft import (
    SurveyDraftCreate,
    SurveyDraftHeadersOutput,
)
from src.db.models.survey_draft import SurveyDraft
from src.services.utils.exceptions import (
    InvalidSurveyStructureException,
    LimitExceededException,
    SurveyDraftNotFoundException,
)

LIMIT_OF_ACTIVE_SURVEY_DRAFTS = 50
PAGE_SIZE = 10


def get_survey_drafts(
    page: int, user_email: str, session: Session
) -> list[SurveyDraftHeadersOutput]:
    helpers.validate_page_for_pagination(page)
    user = helpers.get_user_by_email(user_email, session)

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


def get_survey_draft(
    survey_draft_id: int, user_email: str, session: Session
) -> SurveyDraft:
    user = helpers.get_user_by_email(user_email, session)
    survey_draft = helpers.get_not_deleted_survey_draft_by_id(survey_draft_id, session)
    helpers.check_if_user_has_access(survey_draft.creator_id, user.id)
    return survey_draft


def delete_survey_drafts(
    user_email: str, survey_draft_ids: list[int], session: Session
) -> None:
    user = helpers.get_user_by_email(user_email, session)
    deleted_survey_drafts = survey_draft_crud.delete_survey_drafts(
        user.id, survey_draft_ids, session
    )

    if len(deleted_survey_drafts) != len(survey_draft_ids):
        raise SurveyDraftNotFoundException(
            "Some of the survey drafts do not exist or are already deleted"
        )


def create_survey_draft(
    survey_draft_create: SurveyDraftCreate, session: Session
) -> int:
    user = helpers.get_user_by_email(survey_draft_create.user_email, session)

    survey_drafts_count = (
        survey_draft_crud.get_count_of_not_deleted_survey_drafts_for_user(
            user.id, session
        )
    )
    if survey_drafts_count >= LIMIT_OF_ACTIVE_SURVEY_DRAFTS:
        raise LimitExceededException(
            f"User cannot have more than {LIMIT_OF_ACTIVE_SURVEY_DRAFTS} active survey drafts"
        )

    try:
        survey_draft_create.survey_structure.validate()
    except ValueError as e:
        raise InvalidSurveyStructureException(str(e))

    created_survey_draft = survey_draft_crud.create_survey_draft(
        user.id,
        survey_draft_create.title,
        survey_draft_create.survey_structure.model_dump_json(),
        False,
        session,
    )

    return created_survey_draft.id


def count_survey_drafts(user_email: str, session: Session) -> int:
    user = helpers.get_user_by_email(user_email, session)
    return survey_draft_crud.get_count_of_not_deleted_survey_drafts_for_user(
        user.id, session
    )
