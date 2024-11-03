from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.user as user_crud
from src.api.models.users.user import (  # noqa
    User,
    UserFilterOthers,
    UserUpdatePublicKey,
)
from src.cryptography.fingerprint import verify
from src.db.base import get_session

router = APIRouter()


@router.get(
    "/all",
    response_description="List of all active user emails",
    response_model=list[str],
)
async def get_users(session: Session = Depends(get_session)):
    return [user.email for user in user_crud.get_all_users(session)]


@router.get(
    "/all-with-public-keys",
    response_description="List of all active user emails with public key",
    response_model=list[str],
)
async def get_users_with_keys(session: Session = Depends(get_session)):
    return [user.email for user in user_crud.get_all_users_with_public_keys(session)]


@router.post("/validate", response_description="Validate a user", response_model=bool)
async def does_user_exist(user_create: User, session: Session = Depends(get_session)):
    return user_crud.get_user_by_email(user_create.user_email, session) is not None


@router.post(
    "/has-public-key",
    response_description="Check if user has a non-empty public key",
    response_model=bool,
)
async def check_if_user_has_public_key(
    user_input: User,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(user_input.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not registered")
    return user.public_key != ""


@router.post(
    "/register",
    response_description="Register a new user",
    response_model=dict,
)
async def create_user(user_create: User, session: Session = Depends(get_session)):
    if user_crud.get_user_by_email(user_create.user_email, session) is not None:
        raise HTTPException(status_code=400, detail="User already registered")

    user_crud.create_user(user_create.user_email, session)
    return {"message": "User registered successfully"}


@router.post(
    "/update-public-key",
    response_description="Update user's public key",
    response_model=dict,
)
async def update_user_public_key(
    update_user_public_key: UserUpdatePublicKey,
    session: Session = Depends(get_session),
):
    if user_crud.get_user_by_email(update_user_public_key.user_email, session) is None:
        raise HTTPException(status_code=400, detail="User not registered")

    if not verify(
        update_user_public_key.public_key, update_user_public_key.fingerprint
    ):
        raise HTTPException(
            status_code=400, detail="Invalid fingerprint. Please try again"
        )

    user_crud.update_user_public_key(
        update_user_public_key.user_email, update_user_public_key.public_key, session
    )
    return {"message": "User's public key updated successfully"}


@router.post(
    "/filter-unregistered-users",
    response_description="Returns a list of user emails that are not registered",
    response_model=list[str],
)
async def filter_unregistered_users(
    user_input: UserFilterOthers,
    session: Session = Depends(get_session),
):
    matched_users = {
        user.email for user in user_crud.get_users_by_emails(user_input.emails, session)
    }
    return [email for email in user_input.emails if email not in matched_users]


@router.post(
    "/filter-users-with-no-public-key",
    response_description="Returns a list of user emails that have no public key",
    response_model=list[str],
)
async def filter_users_with_no_public_keys(
    user_input: UserFilterOthers,
    session: Session = Depends(get_session),
):
    matched_users = {
        user.email
        for user in user_crud.get_users_with_public_keys_by_emails(
            user_input.emails, session
        )
    }
    return [email for email in user_input.emails if email not in matched_users]
