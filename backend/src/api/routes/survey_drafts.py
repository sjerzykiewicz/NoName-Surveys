from fastapi import APIRouter, Depends
from sqlmodel import Session

import src.db.crud.survey_draft as survey_draft_crud
from src.api.models.surveys.survey import Survey
from src.api.models.surveys.survey_draft import SurveyDraftCreate
from src.db.base import get_session
from src.db.models.survey_draft import SurveyDraftBase

router = APIRouter()


@router.get(
    "/all",
    response_description="Get all Survey Drafts",
    response_model=list[SurveyDraftCreate],
)
async def get_survey_drafts(session: Session = Depends(get_session)):
    return [
        SurveyDraftCreate(
            creator=draft.creator,
            title=draft.title,
            creation_date=draft.creation_date,
            survey_structure=Survey.parse_raw(draft.survey_structure),
        )
        for draft in survey_draft_crud.get_survey_drafts(session)
    ]


@router.post(
    "/create",
    response_description="Create a new Survey Draft",
    response_model=SurveyDraftBase,
)
async def create_survey_draft(
    survey_draft_create: SurveyDraftCreate,
    session: Session = Depends(get_session),
):
    survey_draft = SurveyDraftBase(
        creator=survey_draft_create.creator,
        title=survey_draft_create.title,
        survey_structure=survey_draft_create.survey_structure.model_dump_json(),
        creation_date=survey_draft_create.creation_date,
    )
    return survey_draft_crud.create_survey_draft(survey_draft, session)
