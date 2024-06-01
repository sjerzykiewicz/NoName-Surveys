from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.user as user_crud
from src.api.models.users.user import CreateUser, User
from src.db.base import get_session
from src.db.models.user import UserBase

router = APIRouter()


@router.get(
    "/all",
    response_description="List of all active user emails",
    response_model=list[str],
)
async def get_users(session: Session = Depends(get_session)):
    return [user.email for user in user_crud.get_all_users(session)]


@router.post(
    "/validate", response_description="Validate a user", response_model=bool
)
async def does_user_exist(
    user_create: User, session: Session = Depends(get_session)
):
    return (
        user_crud.get_user_by_email(user_create.user_email, session)
        is not None
    )


@router.post(
    "/register",
    response_description="Register a new user",
    response_model=dict,
)
async def create_user(
    user_create: CreateUser, session: Session = Depends(get_session)
):
    if (
        user_crud.get_user_by_email(user_create.user_email, session)
        is not None
    ):
        raise HTTPException(status_code=400, detail="User already registered")

    user_crud.create_user(
        UserBase(
            email=user_create.user_email, public_key=user_create.public_key
        ),
        session,
    )
    return {"message": "User registered successfully"}
