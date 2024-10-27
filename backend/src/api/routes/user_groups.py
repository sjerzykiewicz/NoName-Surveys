from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.user as user_crud
import src.db.crud.user_groups as user_groups_crud
from src.api.models.user_groups.user_groups import (  # noqa
    AllUserGroupsOutput,
    UserGroupAction,
    UserGroupCreate,
    UserGroupCreator,
    UserGroupNameUpdate,
)
from src.db.base import get_session
from src.db.models.user_group import UserGroupBase
from src.db.models.user_group_member import UserGroupMemberBase

router = APIRouter()


@router.post(
    "/all",
    response_description="List of of all user groups of a given user",
    response_model=list[AllUserGroupsOutput],
)
async def get_user_groups(
    user_group_creator: UserGroupCreator,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(user_group_creator.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")
    return [
        AllUserGroupsOutput(
            user_group_name=user_group.name,
            all_members_have_public_keys=user_crud.all_users_have_public_keys(
                [
                    member.user_id
                    for member in user_groups_crud.get_user_group_members(
                        user_group.id, session
                    )
                ],
                session,
            ),
        )
        for user_group in user_groups_crud.get_user_groups(user.id, session)
    ]


@router.post(
    "/all-with-public-keys",
    response_description="List of names of all user groups of a given user which members all have public keys",
    response_model=list[str],
)
async def get_user_groups_with_members_having_public_keys(
    user_group_creator: UserGroupCreator,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(user_group_creator.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")
    return [
        user_group.name
        for user_group in user_groups_crud.get_user_groups(user.id, session)
        if user_crud.all_users_have_public_keys(
            [
                member.user_id
                for member in user_groups_crud.get_user_group_members(
                    user_group.id, session
                )
            ],
            session,
        )
    ]


@router.post(
    "/fetch",
    response_description="List of user emails in a given user group",
    response_model=list[str],
)
async def get_user_group(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(user_group_request.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")

    user_group = user_groups_crud.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    if user_group is None:
        raise HTTPException(
            status_code=400, detail="User group not found for the given user"
        )

    user_group_members = user_groups_crud.get_user_group_members(user_group.id, session)
    return [
        user_crud.get_user_by_id(user_group_member.user_id, session).email
        for user_group_member in user_group_members
    ]


@router.post("/create", response_description="Create a user group", response_model=dict)
async def create_user_group(
    user_group_creation_request: UserGroupCreate,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(user_group_creation_request.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")

    if not user_crud.all_users_exist(
        user_group_creation_request.user_group_members, session
    ):
        raise HTTPException(
            status_code=400,
            detail="Not all users are registered (or perhaps duplicate emails cause this issue)",
        )

    existing_user_group = user_groups_crud.get_user_group_by_name(
        user.id, user_group_creation_request.user_group_name, session
    )
    if existing_user_group is not None:
        raise HTTPException(
            status_code=400, detail="User group already exists for given user"
        )

    user_group = user_groups_crud.create_user_group(
        UserGroupBase(
            creator_id=user.id,
            name=user_group_creation_request.user_group_name,
        ),
        session,
    )
    for user_group_member in user_group_creation_request.user_group_members:
        user_groups_crud.add_user_to_group(
            UserGroupMemberBase(
                group_id=user_group.id,
                user_id=user_crud.get_user_by_email(user_group_member, session).id,
            ),
            session,
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
    user = user_crud.get_user_by_email(user_group_rename_request.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")

    existing_user_group_with_new_name = user_groups_crud.get_user_group_by_name(
        user.id, user_group_rename_request.new_name, session
    )
    if existing_user_group_with_new_name is not None:
        raise HTTPException(
            status_code=400, detail="User group with the new name already exists"
        )

    user_group = user_groups_crud.get_user_group_by_name(
        user.id, user_group_rename_request.name, session
    )
    if user_group is None:
        raise HTTPException(
            status_code=400, detail="User group not found for the given user"
        )

    user_groups_crud.update_user_group_name(
        user_group.id, user_group_rename_request.new_name, session
    )

    return {"message": "user group updated successfully"}


@router.post("/delete", response_description="Delete a user group", response_model=dict)
async def delete_user_group(
    user_group_request: UserGroupAction,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(user_group_request.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")

    user_group = user_groups_crud.get_user_group_by_name(
        user.id, user_group_request.name, session
    )
    if user_group is None:
        raise HTTPException(
            status_code=400, detail="User group not found for the given user"
        )

    user_groups_crud.delete_user_group(user_group.id, session)

    return {"message": "user group deleted successfully"}
