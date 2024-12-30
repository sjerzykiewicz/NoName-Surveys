import pytz
from sqlmodel import Session

import src.cryptography.fingerprint as fingerprint_verification
import src.db.crud.user as user_repository
import src.services.utils.helpers as helpers
from src.db.models.user import User
from src.services.utils.exceptions import (
    DuplicateUserException,
    InvalidFingerprintException,
)

tz = pytz.timezone("Europe/Warsaw")


def create_user(email: str, session: Session) -> User:
    if get_user_by_email(email, session) is not None:
        raise DuplicateUserException("User is already registered")
    return user_repository.create(email, session)


def update_user_public_key(
    user_email: str, public_key: str, fingerprint: str, session: Session
) -> User:
    user = helpers.get_user_by_email(user_email, session)
    if not fingerprint_verification.verify(public_key, fingerprint):
        raise InvalidFingerprintException("Invalid fingerprint. Please try again")
    return user_repository.update_public_key(user.id, public_key, session)


def get_all_users(session: Session) -> list[User]:
    return user_repository.find_all(session)


def get_all_users_with_public_keys(session: Session) -> list[User]:
    return user_repository.find_all_with_public_keys(session)


def get_user_by_email(email: str, session: Session) -> User:
    return user_repository.find_by_email(email, session)


def get_users_by_emails(emails: list[str], session: Session) -> list[User]:
    return user_repository.find_by_emails(emails, session)


def get_users_with_public_keys_by_emails(
    emails: list[str], session: Session
) -> list[User]:
    return user_repository.find_with_public_keys_by_emails(emails, session)


def get_user_by_email_helper(email: str, session: Session) -> User:
    return helpers.get_user_by_email(email, session)
