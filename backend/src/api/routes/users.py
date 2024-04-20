from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.db.crud.user as user_crud
from src.db.base import get_session
from src.db.models.user import User, UserBase

router = APIRouter()


@router.get("/all", response_description="Get all users", response_model=list[User])
async def get_user(session: Session = Depends(get_session)):
    return user_crud.get_users(session)


@router.post("/create", response_description="Create a new user", response_model=User)
async def create_user(user_create: UserBase, session: Session = Depends(get_session)):
    return user_crud.create_user(user_create, session)
