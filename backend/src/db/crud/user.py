from datetime import datetime

import pytz
from sqlalchemy.sql import func
from sqlmodel import select

from src.db.base import Session
from src.db.models.user import User, UserBase

tz = pytz.timezone("Europe/Warsaw")


def get_all_users(session: Session) -> list[User]:
    return session.exec(select(User)).all()


def get_all_users_with_public_keys(session: Session) -> list[User]:
    return session.exec(select(User).where(User.public_key != "")).all()


def get_users_by_id(user_id: list[int], session: Session) -> User:
    return session.exec(select(User).where(User.id.in_(user_id))).all()


def get_user_by_id(user_id: int, session: Session) -> User:
    return session.exec(select(User).where(User.id == user_id)).first()


def get_user_by_email(email: str, session: Session) -> User:
    return session.exec(select(User).where(User.email == email)).first()


def get_users_by_emails(emails: list[str], session: Session) -> list[User]:
    return session.exec(select(User).where(User.email.in_(emails))).all()


def get_users_with_public_keys_by_emails(
    emails: list[str], session: Session
) -> list[User]:
    return session.exec(
        select(User).where(User.email.in_(emails)).where(User.public_key != "")
    ).all()


def all_users_exist(users_emails: list[str], session: Session) -> bool:
    count = session.exec(select(func.count()).where(User.email.in_(users_emails))).one()
    return count == len(users_emails)


def all_users_exist_and_have_public_keys(
    users_emails: list[str], session: Session
) -> bool:
    count = session.exec(
        select(func.count())
        .where(User.email.in_(users_emails))
        .where(User.public_key != "")
    ).one()
    return count == len(users_emails)


def all_users_have_public_keys(user_ids: list[int], session: Session) -> bool:
    count = session.exec(
        select(func.count()).where(User.id.in_(user_ids)).where(User.public_key != "")
    ).one()
    return count == len(user_ids)


def create_user(email: str, session: Session) -> User:
    user_create = UserBase(email=email)
    user = User.model_validate(user_create)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_user_public_key(user_id: int, public_key: str, session: Session) -> User:
    user = session.exec(select(User).where(User.id == user_id)).one()

    user.public_key = public_key
    user.key_creation_date = datetime.now(tz)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user
