from fastapi import APIRouter

from src.api.routes import surveys, users

api_router = APIRouter()
api_router.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(users.router, prefix="/users", tags=["users"])


@api_router.get(
    "/",
    response_description="Get test Hello World message",
)
def root():
    return {"message": "Hello World"}
