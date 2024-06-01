from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.ring_member as ring_member_crud
import src.db.crud.survey as survey_crud
import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
from src.api.models.surveys.survey import (
    SurveyHeadersOutput,
    SurveyStructure,
    SurveyStructureCreateInput,
    SurveyStructureCreateOutput,
    SurveyStructureFetchInput,
    SurveyStructureFetchOutput,
)
from src.api.models.users.user import User
from src.db.base import get_session
from src.db.models.survey import SurveyBase
from src.db.models.survey_draft import SurveyDraftBase

router = APIRouter()


@router.post(
    "/all",
    response_description="Get all survey headers of a user",
    response_model=list[SurveyHeadersOutput],
)
async def get_surveys_for_user(
    user: User, session: Session = Depends(get_session)
):
    if user_crud.get_user_by_email(user.user_email, session) is None:
        raise HTTPException(status_code=400, detail="User not found")

    user_id = user_crud.get_user_by_email(user.user_email, session).id
    user_surveys = survey_crud.get_all_surveys_for_user(user_id, session)
    return [
        SurveyHeadersOutput(
            title=SurveyStructure.model_validate_json(
                survey_draft_crud.get_survey_draft_by_id(
                    survey.id, session
                ).survey_structure
            ).title,
            survey_code=survey.survey_code,
            creation_date=survey.creation_date,
            uses_cryptographic_module=survey.uses_cryptographic_module,
        )
        for survey in user_surveys
    ]


@router.post(
    "/fetch",
    response_description="Fetch a survey to fill it out",
    response_model=SurveyStructureFetchOutput,
)
async def get_survey_by_code(
    survey_fetch: SurveyStructureFetchInput,
    session: Session = Depends(get_session),
):
    survey = survey_crud.get_survey_by_code(survey_fetch.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey does not exist")

    return SurveyStructureFetchOutput(
        survey_structure=SurveyStructure.model_validate_json(
            survey_draft_crud.get_survey_draft_by_id(
                survey.id, session
            ).survey_structure
        ),
        survey_code=survey.survey_code,
        uses_cryptographic_module=survey.uses_cryptographic_module,
        public_keys=[
            ring_member.public_key
            for ring_member in ring_member_crud.get_ring_members_for_survey(
                survey.id, session
            )
        ]
        if survey.uses_cryptographic_module
        else [],
    )


@router.post(
    "/create",
    response_description="Create a new survey",
    response_model=SurveyStructureCreateOutput,
)
async def create_survey(
    survey_create: SurveyStructureCreateInput,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_create.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    user_id = user.id

    if survey_create.uses_cryptographic_module:
        not_found_emails = [
            email
            for email in survey_create.ring_members
            if user_crud.get_user_by_email(email, session) is None
        ]
        if len(not_found_emails) > 0:
            raise HTTPException(
                status_code=400,
                detail=f"Users not found: {', '.join(not_found_emails)}",
            )

    try:
        survey_create.survey_structure.validate()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    survey_draft = survey_draft_crud.create_survey_draft(
        SurveyDraftBase(
            creator_id=user_id,
            survey_structure=survey_create.survey_structure.model_dump_json(),
        ),
        session,
    )

    survey = survey_crud.create_survey(
        SurveyBase(
            creator_id=user_id,
            uses_cryptographic_module=survey_create.uses_cryptographic_module,
            survey_structure_id=survey_draft.id,
        ),
        session,
    )

    if survey_create.uses_cryptographic_module:
        for email in survey_create.ring_members:
            public_key = user_crud.get_user_by_email(email, session).public_key
            ring_member_crud.add_ring_member(survey.id, public_key, session)

    return SurveyStructureCreateOutput(survey_code=survey.survey_code)
