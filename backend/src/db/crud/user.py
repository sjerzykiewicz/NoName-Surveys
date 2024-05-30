from sqlmodel import select

from src.db.base import Session
from src.db.models.user import User, UserBase


def get_all_users(session: Session) -> list[User]:
    users = session.exec(select(User)).all()
    return [user for user in users]


def get_user_by_email(email: str, session: Session) -> User:
    user = session.exec(select(User).filter(User.email == email)).first()
    return user


def create_user(user_create: UserBase, session: Session) -> User:
    user = User.model_validate(user_create)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
