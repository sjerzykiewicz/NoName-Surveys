from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.services.user_group_service as service
from src.api.models.user_groups.user_groups import (
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
from src.services.utils.exceptions import (
    InvalidPageNumberException,
    UserAccessException,
    UserGroupExistsException,
    UserGroupLimitException,
    UserGroupMemberException,
    UserGroupNotFoundException,
    UserNotFoundException,
)

router = APIRouter()


@router.post(
    "/count",
    response_description="Number of all user groups of a given user",
    response_model=int,
)
async def get_user_groups_count(
    user_group_creator: UserGroupCreator,
    session: Session = Depends(get_session),
):
    try:
        return service.get_user_groups_count(user_group_creator.user_email, session)
    except UserNotFoundException as e:
        raise HTTPException(status_code=400, detail=str(e))


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
    try:
        return service.get_user_groups(page, user_group_creator.user_email, session)
    except (UserNotFoundException, InvalidPageNumberException) as e:
        raise HTTPException(status_code=400, detail=str(e))


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
    try:
        return service.get_user_groups_with_members_having_public_keys(
            user_group_creator.user_email, session
        )
    except UserNotFoundException as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/group-members-count",
    response_description="Number of members in a given user group",
    response_model=int,
)
async def get_user_group_members_count(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    try:
        return service.get_user_group_members_count(user_group_request, session)
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/all-who-are-not-members",
    response_description="List of users who are not members of a given user group",
    response_model=list[str],
)
async def get_users_who_are_not_members(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    try:
        return service.get_users_who_are_not_members(user_group_request, session)
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/fetch",
    response_description="List of all user emails in a given user group",
    response_model=list[UserGroupMembersOutput],
)
async def get_whole_user_group(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    try:
        return service.get_whole_user_group(user_group_request, session)
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


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
    try:
        return service.get_user_group(page, user_group_request, session)
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
        InvalidPageNumberException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create", response_description="Create a user group", response_model=dict)
async def create_user_group(
    user_group_creation_request: UserGroupCreate,
    session: Session = Depends(get_session),
):
    try:
        service.create_user_group(user_group_creation_request, session)
        return {"message": "user group created successfully"}
    except (
        UserNotFoundException,
        UserGroupExistsException,
        UserGroupLimitException,
        UserGroupMemberException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/rename",
    response_description="Rename a user group name",
    response_model=dict,
)
async def rename_user_group(
    user_group_rename_request: UserGroupNameUpdate,
    session: Session = Depends(get_session),
):
    try:
        service.rename_user_group(user_group_rename_request, session)
        return {"message": "user group updated successfully"}
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
        UserGroupExistsException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/delete", response_description="Delete user groups", response_model=dict)
async def delete_user_groups(
    user_group_request: UserGroupMultipleActions,
    session: Session = Depends(get_session),
):
    try:
        service.delete_user_groups(user_group_request, session)
        return {"message": "user group deleted successfully"}
    except (UserNotFoundException, UserGroupNotFoundException) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/add-users", response_description="Add users to a group", response_model=dict
)
async def add_users_to_group(
    user_group_request: UserGroupUsersActions,
    session: Session = Depends(get_session),
):
    try:
        service.add_users_to_group(user_group_request, session)
        return {"message": "User added to the group successfully"}
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
        UserGroupMemberException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/remove-users",
    response_description="Remove users from a group",
    response_model=dict,
)
async def remove_users_from_group(
    user_group_request: UserGroupUsersActions,
    session: Session = Depends(get_session),
):
    try:
        service.remove_users_from_group(user_group_request, session)
        return {"message": "User removed from the group successfully"}
    except (
        UserNotFoundException,
        UserGroupNotFoundException,
        UserAccessException,
        UserGroupMemberException,
    ) as e:
        raise HTTPException(status_code=400, detail=str(e))
