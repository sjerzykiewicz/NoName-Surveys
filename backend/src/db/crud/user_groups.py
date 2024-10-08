from sqlmodel import select

from src.db.base import Session
from src.db.models.user_group import UserGroup, UserGroupBase
from src.db.models.user_group_member import UserGroupMember, UserGroupMemberBase


def get_user_groups(user_id: int, session: Session) -> list[UserGroup]:
    statement = select(UserGroup).where(
        (UserGroup.creator_id == user_id)
        & (UserGroup.is_deleted == False)  # noqa: E712
    )
    return [user_group for user_group in session.exec(statement).all()]


def get_user_group_by_name(user_id: int, name: str, session: Session) -> UserGroup:
    statement = select(UserGroup).where(
        (UserGroup.creator_id == user_id)
        & (UserGroup.name == name)
        & (UserGroup.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first()


def update_user_group_name(
    user_group_id: int, new_name: str, session: Session
) -> UserGroup:
    user_group = session.exec(
        select(UserGroup).where(UserGroup.id == user_group_id)
    ).first()
    user_group.name = new_name
    session.add(user_group)
    session.commit()
    session.refresh(user_group)
    return user_group


def create_user_group(user_group: UserGroupBase, session: Session) -> UserGroup:
    user_group = UserGroup.model_validate(user_group)
    session.add(user_group)
    session.commit()
    session.refresh(user_group)
    return user_group


def add_user_to_group(
    user_group_member: UserGroupMemberBase, session: Session
) -> UserGroupMember:
    user_group_member = UserGroupMember.model_validate(user_group_member)
    session.add(user_group_member)
    session.commit()
    session.refresh(user_group_member)


def delete_user_group(user_group_id: int, session: Session) -> UserGroup:
    user_group = session.exec(
        select(UserGroup).where(UserGroup.id == user_group_id)
    ).first()
    user_group.is_deleted = True
    session.commit()
    return user_group


def get_user_group_members(
    user_group_id: int, session: Session
) -> list[UserGroupMember]:
    statement = select(UserGroupMember).where(UserGroupMember.group_id == user_group_id)
    return [user for user in session.exec(statement).all()]
