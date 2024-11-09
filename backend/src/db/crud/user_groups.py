from sqlalchemy import func
from sqlmodel import select

from src.db.base import Session
from src.db.models.user_group import UserGroup, UserGroupBase
from src.db.models.user_group_member import UserGroupMember, UserGroupMemberBase


def get_count_of_user_groups_of_user(user_id: int, session: Session) -> int:
    statement = select(func.count(UserGroup.id)).where(
        (UserGroup.creator_id == user_id)
        & (UserGroup.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def get_all_user_groups_of_user(user_id: int, session: Session) -> list[UserGroup]:
    statement = select(UserGroup).where(
        (UserGroup.creator_id == user_id)
        & (UserGroup.is_deleted == False)  # noqa: E712
    )
    return [user_group for user_group in session.exec(statement).all()]


def get_user_groups(
    user_id: int, offset: int, limit: int, session: Session
) -> list[UserGroup]:
    statement = (
        select(UserGroup)
        .where(
            (UserGroup.creator_id == user_id)
            & (UserGroup.is_deleted == False)  # noqa: E712
        )
        .offset(offset)
        .limit(limit)
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


def create_user_group(creator_id: int, name: str, session: Session) -> UserGroup:
    user_group = UserGroupBase(
        creator_id=creator_id,
        name=name,
    )
    user_group = UserGroup.model_validate(user_group)
    session.add(user_group)
    session.commit()
    session.refresh(user_group)
    return user_group


def add_user_to_group(group_id: int, user_id: int, session: Session) -> UserGroupMember:
    user_group_member = UserGroupMemberBase(
        group_id=group_id,
        user_id=user_id,
    )
    user_group_member = UserGroupMember.model_validate(user_group_member)
    session.add(user_group_member)
    session.commit()
    session.refresh(user_group_member)


def delete_user_groups(
    user_id: int, names: list[str], session: Session
) -> list[UserGroup]:
    user_groups = session.exec(
        select(UserGroup).where(
            (UserGroup.creator_id == user_id)
            & (UserGroup.name.in_(names))
            & (UserGroup.is_deleted == False)  # noqa: E712
        )
    ).all()
    for user_group in user_groups:
        user_group.is_deleted = True
    session.commit()
    return user_groups


def get_user_group_members_count(user_group_id: int, session: Session) -> int:
    statement = select(func.count(UserGroupMember.id)).where(
        UserGroupMember.group_id == user_group_id
    )
    return session.exec(statement).one()


def get_user_group_members(
    user_group_id: int, session: Session
) -> list[UserGroupMember]:
    statement = select(UserGroupMember).where(UserGroupMember.group_id == user_group_id)
    return [user for user in session.exec(statement).all()]


def get_user_group_members_paginated(
    user_group_id: int, offset: int, limit: int, session: Session
) -> list[UserGroupMember]:
    statement = (
        select(UserGroupMember)
        .where(UserGroupMember.group_id == user_group_id)
        .offset(offset)
        .limit(limit)
    )
    return [user for user in session.exec(statement).all()]
