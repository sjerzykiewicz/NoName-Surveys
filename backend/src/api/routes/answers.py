from fastapi import APIRouter, Depends, HTTPException
from gmpy2 import mpz
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
from src.cryptography.ring_signature import verify_lrs
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

    survey = survey_crud.get_survey_by_code(survey_fetch.survey_code, session)
    if survey is None:
        raise HTTPException(status_code=400, detail="Survey not found")

    if not survey_crud.user_has_access_to_survey(user.id, survey.id, session):
        raise HTTPException(
            status_code=400, detail="User does not have access to this survey"
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
        SurveyAnswerBase.model_validate_json(answer.answer) for answer in answers
    ]
    is_owned_by_user = user.id == survey.creator_id
    return [
        SurveyAnswersFetchOutput(
            title=survey_title,
            questions=answer.questions,
            is_owned_by_user=is_owned_by_user,
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
        raise HTTPException(status_code=404, detail="No survey found with this code")

    if survey.uses_cryptographic_module:
        if not survey_answer.signature:
            raise HTTPException(
                status_code=400,
                detail="Survey requires cryptographic signature",
            )

        if answer_crud.signature_already_present_for_user(
            survey.id, survey_answer.signature[0], session
        ):
            raise HTTPException(
                status_code=400, detail="User already answered this survey"
            )

        public_keys = [
            mpz(ring_member.public_key)
            for ring_member in ring_member_crud.get_ring_members_for_survey(
                survey.id, session
            )
        ]
        if not verify_lrs(
            survey.survey_code,
            public_keys,
            [mpz(x) for x in survey_answer.signature],
        ):
            raise HTTPException(
                status_code=400,
                detail="Answer has not been saved because the signature was invalid.",
            )

    survey_draft = survey_draft_crud.get_survey_draft_by_id(
        survey.survey_structure_id, session
    )

    survey_structure = SurveyStructure.model_validate_json(
        survey_draft.survey_structure
    )
    questions = survey_structure.questions
    # validate answer
    if len(survey_answer.questions) != len(questions):
        raise HTTPException(
            status_code=400,
            detail="Invalid answer. Number of questions did not match.",
        )
    try:
        for q1, q2 in zip(survey_answer.questions, questions):
            q1.validate_structure_against(q2)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # save answer
    answer = Answer(
        survey_id=survey.id,
        answer=survey_answer.model_dump_json(),
        y0=survey_answer.signature[0] if survey_answer.signature else "",
    )
    answer_crud.save_answer(answer, session)

    return {"message": "Answer saved successfully"}
