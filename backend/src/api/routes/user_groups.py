from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.api.utils.helpers as helpers
import src.db.crud.user as user_crud
import src.db.crud.user_groups as user_groups_crud
from src.api.models.user_groups.user_groups import (  # noqa
    AllUserGroupsOutput,
    UserGroupAction,
    UserGroupCreate,
    UserGroupCreator,
    UserGroupMembersOutput,
    UserGroupMultipleActions,
    UserGroupNameUpdate,
    UserGroupUsersActions,
)
from src.db.base import get_session

router = APIRouter()


LIMIT_OF_ACTIVE_USER_GROUPS = 50
PAGE_SIZE = 10


@router.post(
    "/count",
    response_description="Number of all user groups of a given user",
    response_model=int,
)
async def get_user_groups_count(
    user_group_creator: UserGroupCreator,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_creator.user_email, session)
    return user_groups_crud.get_count_of_user_groups_of_user(user.id, session)


@router.post(
    "/all/{page}",
    response_description="List of of all user groups of a given user",
    response_model=list[AllUserGroupsOutput],
)
async def get_user_groups(
    page: int,
    user_group_creator: UserGroupCreator,
    session: Session = Depends(get_session),
):
    helpers.validate_page_for_pagination(page)
    user = helpers.get_user_by_email(user_group_creator.user_email, session)
    return [
        AllUserGroupsOutput(
            user_group_name=user_group.name,
            all_members_have_public_keys=user_crud.all_users_have_public_keys(
                user_groups_crud.get_user_group_members(user_group.id, session),
                session,
            ),
        )
        for user_group in user_groups_crud.get_user_groups(
            user.id, page * PAGE_SIZE, PAGE_SIZE, session
        )
    ]


@router.post(
    "/all-with-public-keys",
    response_description=(
        "List of names of all user groups of a given user which "
        "members all have public keys"
    ),
    response_model=list[str],
)
async def get_user_groups_with_members_having_public_keys(
    user_group_creator: UserGroupCreator,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_creator.user_email, session)
    return [
        user_group.name
        for user_group in user_groups_crud.get_all_user_groups_of_user(user.id, session)
        if user_crud.all_users_have_public_keys(
            user_groups_crud.get_user_group_members(user_group.id, session),
            session,
        )
    ]


@router.post(
    "/group-members-count",
    response_description="Number of members in a given user group",
    response_model=int,
)
async def get_user_group_members_count(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_request.user_email, session)
    user_group = helpers.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    return user_groups_crud.get_user_group_members_count(user_group.id, session)


@router.post(
    "/all-who-are-not-members",
    response_description="List of users who are not members of a given user group",
    response_model=list[str],
)
async def get_users_who_are_not_members(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_request.user_email, session)
    user_group = helpers.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    return [
        user.email
        for user in user_groups_crud.get_all_users_who_are_not_members_of_user_group(
            user_group.id, session
        )
    ]


@router.post(
    "/fetch",
    response_description="List of all user emails in a given user group",
    response_model=list[UserGroupMembersOutput],
)
async def get_whole_user_group(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_request.user_email, session)
    user_group = helpers.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    return [
        UserGroupMembersOutput(
            email=member.email, has_public_key=member.public_key != ""
        )
        for member in user_groups_crud.get_all_users_in_user_group(
            user_group.id, session
        )
    ]


@router.post(
    "/fetch/{page}",
    response_description="List of user emails in a given user group",
    response_model=list[UserGroupMembersOutput],
)
async def get_user_group(
    page: int,
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    helpers.validate_page_for_pagination(page)
    user = helpers.get_user_by_email(user_group_request.user_email, session)
    user_group = helpers.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    return [
        UserGroupMembersOutput(
            email=member.email, has_public_key=member.public_key != ""
        )
        for member in user_groups_crud.get_user_group_members_paginated(
            user_group.id, page * PAGE_SIZE, PAGE_SIZE, session
        )
    ]


@router.post("/create", response_description="Create a user group", response_model=dict)
async def create_user_group(
    user_group_creation_request: UserGroupCreate,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_creation_request.user_email, session)

    user_groups_count = user_groups_crud.get_count_of_user_groups_of_user(
        user.id, session
    )
    if user_groups_count >= LIMIT_OF_ACTIVE_USER_GROUPS:
        raise HTTPException(
            status_code=400,
            detail="User has reached the limit of active user groups",
        )

    if not user_crud.all_users_exist(
        user_group_creation_request.user_group_members, session
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Not all users are registered "
                "(or perhaps duplicate emails cause this issue)"
            ),
        )

    existing_user_group = user_groups_crud.get_user_group_by_name(
        user.id, user_group_creation_request.user_group_name, session
    )
    if existing_user_group is not None:
        raise HTTPException(
            status_code=400, detail="User group already exists for given user"
        )

    user_group = user_groups_crud.create_user_group(
        user.id, user_group_creation_request.user_group_name, session
    )

    users_to_add = [
        user_to_add.id
        for user_to_add in user_crud.get_users_by_emails(
            user_group_creation_request.user_group_members, session
        )
    ]
    added_users = user_groups_crud.add_users_to_group(
        user_group.id, users_to_add, session
    )
    if len(added_users) != len(users_to_add):
        raise HTTPException(
            status_code=400, detail="Some users could not be added to the group"
        )

    return {"message": "user group created successfully"}


@router.post(
    "/rename",
    response_description="Rename a user group name",
    response_model=dict,
)
async def rename_user_group(
    user_group_rename_request: UserGroupNameUpdate,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_rename_request.user_email, session)

    if (
        user_groups_crud.get_user_group_by_name(
            user.id, user_group_rename_request.new_name, session
        )
        is not None
    ):
        raise HTTPException(
            status_code=400, detail="User group with the new name already exists"
        )

    user_group = helpers.get_user_group_by_name(
        user.id, user_group_rename_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    user_groups_crud.update_user_group_name(
        user_group.id, user_group_rename_request.new_name, session
    )

    return {"message": "user group updated successfully"}


@router.post("/delete", response_description="Delete user groups", response_model=dict)
async def delete_user_groups(
    user_group_request: UserGroupMultipleActions,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_request.user_email, session)

    deleted_user_groups = user_groups_crud.delete_user_groups(
        user.id, user_group_request.names, session
    )

    if len(deleted_user_groups) != len(user_group_request.names):
        raise HTTPException(
            status_code=400, detail="Some user groups were not found for the given user"
        )

    return {"message": "user group deleted successfully"}


@router.post(
    "/add-users", response_description="Add users to a group", response_model=dict
)
async def add_users_to_group(
    user_group_request: UserGroupUsersActions,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_request.user_email, session)
    user_group = helpers.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    users_to_add = [
        user_to_add.id
        for user_to_add in user_crud.get_users_by_emails(
            user_group_request.users, session
        )
    ]
    added_users = user_groups_crud.add_users_to_group(
        user_group.id, users_to_add, session
    )

    if len(added_users) != len(users_to_add):
        raise HTTPException(
            status_code=400, detail="Some users could not be added to the group"
        )

    return {"message": "User added to the group successfully"}


@router.post(
    "/remove-users",
    response_description="Remove users from a group",
    response_model=dict,
)
async def remove_users_from_group(
    user_group_request: UserGroupUsersActions,
    session: Session = Depends(get_session),
):
    user = helpers.get_user_by_email(user_group_request.user_email, session)
    user_group = helpers.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    helpers.check_if_user_has_access(user.id, user_group.creator_id)

    users_to_remove = [
        user_to_remove.id
        for user_to_remove in user_crud.get_users_by_emails(
            user_group_request.users, session
        )
    ]
    removed_users = user_groups_crud.remove_users_from_group(
        user_group.id, users_to_remove, session
    )

    if len(removed_users) != len(users_to_remove):
        raise HTTPException(
            status_code=400, detail="Some users could not be removed from the group"
        )

    return {"message": "User removed from the group successfully"}
