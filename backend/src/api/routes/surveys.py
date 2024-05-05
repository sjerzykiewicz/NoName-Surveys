from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.survey as survey_crud
import src.db.crud.survey_draft as survey_draft_crud
from src.api.models.surveys.survey import (
    SurveyStructure,
    SurveyStructureCreateInput,
    SurveyStructureCreateOutput,
    SurveyStructureFetchInput,
    SurveyStructureFetchOutput,
    SurveyStructureGetForUserOutput,
)
from src.db.base import get_session
from src.db.models.survey import SurveyBase
from src.db.models.survey_draft import SurveyDraftBase

router = APIRouter()


@router.post(
    "/",
    response_description="Fetch a survey to fill it out",
    response_model=SurveyStructureFetchOutput,
)
async def get_survey_by_code(
    survey_fetch: SurveyStructureFetchInput,
    session: Session = Depends(get_session),
):
    survey = survey_crud.get_survey_by_code(survey_fetch.survey_code, session)
    if not survey:
        raise HTTPException(
            status_code=404, detail="No survey found with this code"
        )

    survey_draft = survey_draft_crud.get_survey_draft_by_id(
        survey.survey_structure_id, session
    )
    return SurveyStructureFetchOutput(
        survey_structure=SurveyStructure.model_validate_json(
            survey_draft.survey_structure
        ),
        uses_cryptographic_module=survey.uses_cryptographic_module,
        survey_code=survey.survey_code,
    )


@router.get(
    "/all/{user_id}",
    response_description="Get all surveys of a user",
    response_model=list[SurveyStructureGetForUserOutput],
)
async def get_surveys_for_user(
    user_id: int, session: Session = Depends(get_session)
):
    surveys = survey_crud.get_surveys_for_user(user_id, session)
    return [
        SurveyStructureGetForUserOutput(
            survey_structure_id=survey.survey_structure_id,
            uses_cryptographic_module=survey.uses_cryptographic_module,
            survey_code=survey.survey_code,
        )
        for survey in surveys
    ]


@router.post(
    "/create",
    response_description="Create a new survey",
    response_model=SurveyStructureCreateOutput,
)
async def create_survey(
    survey_draft_create: SurveyStructureCreateInput,
    session: Session = Depends(get_session),
):
    try:
        survey_draft_create.survey_structure.validate_for_draft()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    # create a survey draft
    survey_draft_base = SurveyDraftBase(
        creator=survey_draft_create.creator,
        survey_structure=survey_draft_create.survey_structure.model_dump_json(),
    )
    survey_draft = survey_draft_crud.create_survey_draft(
        survey_draft_base, session
    )

    # create a survey
    survey = survey_crud.create_survey_draft(
        SurveyBase(
            survey_structure_id=survey_draft.id,
            deadline=survey_draft_create.deadline,
            uses_cryptographic_module=survey_draft_create.uses_cryptographic_module,
        ),
        session,
    )

    return SurveyStructureCreateOutput(
        creator=survey_draft.creator,
        survey_structure_id=survey.survey_structure_id,
        uses_cryptographic_module=survey.uses_cryptographic_module,
        survey_code=survey.survey_code,
    )
