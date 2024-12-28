from secrets import randbelow

from sqlmodel import Session

import src.db.crud.survey as survey_repository
import src.db.crud.survey_draft as survey_draft_repository
import src.db.crud.user as user_repository
import src.db.crud.user_groups as user_groups_repository
from src.db.models.survey import Survey
from src.db.models.survey_draft import SurveyDraft
from src.db.models.user import User
from src.db.models.user_group import UserGroup
from src.services.utils.exceptions import (
    InvalidPageNumberException,
    SurveyDraftNotFoundException,
    SurveyNotFoundException,
    UserAccessException,
    UserGroupNotFoundException,
    UserNotFoundException,
)

SURVEY_CODE_LENGTH = 6


def get_user_by_email(email: str, session: Session) -> User:
    user = user_repository.find_by_email(email, session)
    if user is None:
        raise UserNotFoundException("User not found")
    return user


def get_user_group_by_name(
    user_id: int, group_name: str, session: Session
) -> UserGroup:
    user_group = user_groups_repository.find_by_name(user_id, group_name, session)
    if user_group is None:
        raise UserGroupNotFoundException("User group not found for the given user")

    return user_group


def get_survey_by_code(survey_code: str, session: Session) -> Survey:
    survey = survey_repository.find_by_code(survey_code, session)
    if survey is None:
        raise SurveyNotFoundException("Survey not found")
    return survey


def get_active_survey_by_code(survey_code: str, session: Session) -> Survey:
    survey = survey_repository.find_active_by_code(survey_code, session)
    if survey is None:
        raise SurveyNotFoundException("Survey deactivated by the creator or not found")
    return survey


def get_survey_draft_by_id(survey_draft_id: int, session: Session) -> SurveyDraft:
    survey_draft = survey_draft_repository.find_by_id(survey_draft_id, session)
    if survey_draft is None:
        raise SurveyDraftNotFoundException("Survey Draft not found")
    return survey_draft


def get_not_deleted_survey_draft_by_id(
    survey_draft_id: int, session: Session
) -> SurveyDraft:
    survey_draft = survey_draft_repository.find_not_deleted_by_id(
        survey_draft_id, session
    )
    if survey_draft is None:
        raise SurveyDraftNotFoundException("Survey Draft not found")
    return survey_draft


def validate_page_for_pagination(page: int) -> None:
    if page < 0:
        raise InvalidPageNumberException("Invalid page number")


def generate_six_digit_code() -> str:
    return "".join(str(randbelow(10)) for _ in range(SURVEY_CODE_LENGTH))


def generate_survey_code(session: Session) -> str:
    survey_code = generate_six_digit_code()
    while survey_repository.is_code_taken(survey_code, session):
        survey_code = generate_six_digit_code()

    return survey_code


def check_if_user_has_access(first_user: int, second_user: int) -> None:
    if first_user != second_user:
        raise UserAccessException("User not allowed to perform this action")
