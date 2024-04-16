from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    response_description="List all surveys",
)
def list_surveys():
    return {"message": "List all surveys"}
