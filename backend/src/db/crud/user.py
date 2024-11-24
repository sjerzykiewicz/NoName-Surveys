from datetime import datetime

import pytz
from sqlmodel import select

from src.db.base import Session
from src.db.models.user import User, UserBase, UserWithKey

tz = pytz.timezone("Europe/Warsaw")


def get_all_users(session: Session) -> list[User]:
    users = session.exec(select(User)).all()
    return [user for user in users]


def get_all_users_with_public_keys(session: Session) -> list[User]:
    users = session.exec(select(User).filter(User.public_key != "")).all()
    return [user for user in users]


def get_users_by_id(user_id: list[int], session: Session) -> User:
    users = session.exec(select(User).filter(User.id.in_(user_id))).all()
    return [user for user in users]


def get_user_by_id(user_id: int, session: Session) -> User:
    user = session.exec(select(User).filter(User.id == user_id)).first()
    return user


def get_user_by_email(email: str, session: Session) -> User:
    user = session.exec(select(User).filter(User.email == email)).first()
    return user


def get_users_by_emails(emails: list[str], session: Session) -> list[User]:
    users = session.exec(select(User).filter(User.email.in_(emails))).all()
    return [user for user in users]


def get_users_with_public_keys_by_emails(
    emails: list[str], session: Session
) -> list[User]:
    users = session.exec(
        select(User).filter(User.email.in_(emails), User.public_key != "")
    ).all()
    return [user for user in users]


def all_users_exist(users_emails: list[str], session: Session) -> bool:
    users = session.exec(select(User).filter(User.email.in_(users_emails))).all()
    return len(users) == len(users_emails)


def all_users_exist_and_have_public_keys(
    users_emails: list[str], session: Session
) -> bool:
    users = session.exec(
        select(User).filter(User.email.in_(users_emails), User.public_key != "")
    ).all()

    return len(users) == len(users_emails)


def all_users_have_public_keys(user_ids: list[int], session: Session) -> bool:
    users = session.exec(
        select(User).filter(User.id.in_(user_ids), User.public_key != "")
    ).all()

    return len(users) == len(user_ids)


def create_user(email: str, session: Session) -> User:
    user_create = UserBase(email=email)
    user = User.model_validate(user_create)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_user_public_key(email: str, public_key: str, session: Session) -> User:
    user_update_key = UserWithKey(
        email=email, public_key=public_key, key_creation_date=datetime.now(tz)
    )
    user = session.exec(
        select(User).filter(User.email == user_update_key.email)
    ).first()
    user.public_key = user_update_key.public_key
    user.key_creation_date = user_update_key.key_creation_date
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
