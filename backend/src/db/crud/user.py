from sqlmodel import select

from src.db.base import Session
from src.db.models.user import User, UserBase


def create_user(user_create: UserBase, session: Session) -> User:
    user = User.model_validate(user_create)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session) -> list[User] | None:
    users = session.exec(select(User)).all()
    return [user for user in users]
