import Crypto.PublicKey.RSA as RSA
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.answer as answer_crud
import src.db.crud.ring_member as ring_member_crud
import src.db.crud.survey as survey_crud
import src.db.crud.survey_draft as survey_draft_crud
import src.db.crud.user as user_crud
from src.api.models.surveys.answer import (
    SurveyAnswerBase,
    SurveyAnswersFetchInput,
    SurveyAnswersFetchOutput,
)
from src.api.models.surveys.survey import SurveyStructure
from src.cryptography.ring_signature import Ring
from src.db.base import get_session
from src.db.models.answer import Answer

router = APIRouter()


@router.post(
    "/fetch",
    response_description="Fetch answers to a given survey",
    response_model=list[SurveyAnswersFetchOutput],
)
async def get_survey_answers_by_code(
    survey_fetch: SurveyAnswersFetchInput,
    session: Session = Depends(get_session),
):
    user = user_crud.get_user_by_email(survey_fetch.user_email, session)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    user_id = user.id

    survey = survey_crud.get_survey_by_code(survey_fetch.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=400, detail="Survey not found")

    if survey.creator_id != user_id:
        raise HTTPException(
            status_code=403, detail="User not authorized to access this survey"
        )

    survey_draft = survey_draft_crud.get_survey_draft_by_id(
        survey.survey_structure_id, session
    )
    survey_structure = SurveyStructure.model_validate_json(
        survey_draft.survey_structure
    )
    survey_title = survey_structure.title

    answers = answer_crud.get_answers_by_survey_id(survey.id, session)
    answer_structures = [
        SurveyAnswerBase.model_validate_json(answer.answer)
        for answer in answers
    ]
    return [
        SurveyAnswersFetchOutput(
            title=survey_title, questions=answer.questions
        )
        for answer in answer_structures
    ]


@router.post(
    "/fill",
    response_description="Fill out a survey",
    response_model=dict,
)
async def save_survey_answer(
    survey_answer: SurveyAnswerBase,
    session: Session = Depends(get_session),
):
    try:
        survey_answer.validate()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # fetch target survey structure
    survey = survey_crud.get_survey_by_code(survey_answer.survey_code, session)
    if not survey:
        raise HTTPException(
            status_code=404, detail="No survey found with this code"
        )

    if survey.uses_cryptographic_module:
        if not survey_answer.signature or not survey_answer.y0:
            raise HTTPException(
                status_code=400,
                detail="Survey requires cryptographic signature and y0",
            )

        if answer_crud.user_already_answered_survey(
            survey.id, survey_answer.y0, session
        ):
            raise HTTPException(
                status_code=400, detail="User already answered this survey"
            )

        public_keys = [
            RSA.import_key(ring_member.public_key)
            for ring_member in ring_member_crud.get_ring_members_for_survey(
                survey.id, session
            )
        ]
        ring = Ring(public_keys)
        if not ring.verify(survey_answer.questions, survey_answer.signature):
            raise HTTPException(status_code=400, detail="Invalid signature")

    survey_draft = survey_draft_crud.get_survey_draft_by_id(
        survey.survey_structure_id, session
    )

    survey_structure = SurveyStructure.model_validate_json(
        survey_draft.survey_structure
    )
    questions = survey_structure.questions
    # validate answer
    if len(survey_answer.questions) != len(questions):
        raise HTTPException(status_code=400, detail="Invalid answer")
    try:
        for q1, q2 in zip(survey_answer.questions, questions):
            q1.validate_structure_against(q2)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # save answer
    answer = Answer(
        survey_id=survey.id,
        answer=survey_answer.model_dump_json(),
        y0=survey_answer.y0,
    )
    answer_crud.save_answer(answer, session)

    return {"message": "Answer saved successfully"}
