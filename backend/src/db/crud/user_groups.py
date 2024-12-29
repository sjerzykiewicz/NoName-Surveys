from sqlalchemy import func
from sqlmodel import select

from src.db.base import Session
from src.db.models.user import User
from src.db.models.user_group import UserGroup, UserGroupBase
from src.db.models.user_group_member import UserGroupMember


def get_count_of_user_groups_of_user(user_id: int, session: Session) -> int:
    statement = (
        select(func.count(UserGroup.id))
        .where(UserGroup.creator_id == user_id)
        .where(UserGroup.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def get_all_user_groups_of_user(user_id: int, session: Session) -> list[UserGroup]:
    statement = (
        select(UserGroup)
        .where(UserGroup.creator_id == user_id)
        .where(UserGroup.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).all()


def get_user_groups(
    user_id: int, offset: int, limit: int, session: Session
) -> list[UserGroup]:
    statement = (
        select(UserGroup)
        .where(UserGroup.creator_id == user_id)
        .where(UserGroup.is_deleted == False)  # noqa: E712
        .order_by(UserGroup.name.asc())
        .offset(offset)
        .limit(limit)
    )
    return session.exec(statement).all()


def find_by_name(user_id: int, name: str, session: Session) -> UserGroup:
    statement = (
        select(UserGroup)
        .where(UserGroup.creator_id == user_id)
        .where(UserGroup.name == name)
        .where(UserGroup.is_deleted == False)  # noqa: E712
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


def add_users_to_group(
    group_id: int, user_ids: list[int], session: Session
) -> list[UserGroupMember]:
    user_group_members = []
    for user_id in user_ids:
        user_group_member = session.exec(
            select(UserGroupMember)
            .where(UserGroupMember.group_id == group_id)
            .where(UserGroupMember.user_id == user_id)
        ).first()

        if user_group_member is not None:
            user_group_member.is_deleted = False
        else:
            user_group_member = UserGroupMember(
                group_id=group_id,
                user_id=user_id,
            )

        session.add(user_group_member)
        user_group_members.append(user_group_member)

    session.commit()
    return user_group_members


def remove_users_from_group(
    group_id: int, user_ids: list[int], session: Session
) -> list[UserGroupMember]:
    user_group_members = session.exec(
        select(UserGroupMember)
        .where(UserGroupMember.group_id == group_id)
        .where(UserGroupMember.user_id.in_(user_ids))
    ).all()
    for user in user_group_members:
        user.is_deleted = True
    session.commit()
    return user_group_members


def delete_user_groups(
    user_id: int, names: list[str], session: Session
) -> list[UserGroup]:
    user_groups = session.exec(
        select(UserGroup)
        .where(UserGroup.creator_id == user_id)
        .where(UserGroup.name.in_(names))
        .where(UserGroup.is_deleted == False)  # noqa: E712
    ).all()
    for user_group in user_groups:
        user_group.is_deleted = True
    session.commit()
    return user_groups


def get_user_group_members_count(user_group_id: int, session: Session) -> int:
    statement = (
        select(func.count(UserGroupMember.id))
        .where(UserGroupMember.group_id == user_group_id)
        .where(UserGroupMember.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def get_user_group_members(user_group_id: int, session: Session) -> list[int]:
    statement = (
        select(UserGroupMember.user_id)
        .where(UserGroupMember.group_id == user_group_id)
        .where(UserGroupMember.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).all()


def get_all_users_in_user_group(user_group_id: int, session: Session) -> list[User]:
    statement = (
        select(User)
        .join(UserGroupMember, User.id == UserGroupMember.user_id)
        .where(UserGroupMember.group_id == user_group_id)
        .where(UserGroupMember.is_deleted == False)  # noqa: E712
        .order_by(User.email.asc())
    )
    return session.exec(statement).all()


def get_user_group_members_paginated(
    user_group_id: int, offset: int, limit: int, session: Session
) -> list[User]:
    statement = (
        select(User)
        .join(UserGroupMember, User.id == UserGroupMember.user_id)
        .where(UserGroupMember.group_id == user_group_id)
        .where(UserGroupMember.is_deleted == False)  # noqa: E712
        .order_by(User.email.asc())
        .offset(offset)
        .limit(limit)
    )
    return session.exec(statement).all()


def get_all_users_who_are_not_members(
    user_group_id: int, session: Session
) -> list[User]:
    statement = (
        select(User)
        .where(
            User.id.notin_(
                select(UserGroupMember.user_id)
                .where(UserGroupMember.group_id == user_group_id)
                .where(UserGroupMember.is_deleted == False)  # noqa: E712
            )
        )
        .order_by(User.email.asc())
    )
    return session.exec(statement).all()
