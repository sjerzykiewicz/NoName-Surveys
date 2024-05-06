from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import src.db.crud.answer as answer_crud
import src.db.crud.survey as survey_crud
import src.db.crud.survey_draft as survey_draft_crud
from src.api.models.surveys.answer import (
    SurveyAnswerBase,
    SurveyAnswersFetchInput,
    SurveyAnswersFetchOutput,
)
from src.api.models.surveys.survey import SurveyStructure
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
    survey = survey_crud.get_survey_by_code(survey_fetch.survey_code, session)
    if not survey:
        raise HTTPException(
            status_code=404, detail="No survey found with this code"
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
    # fetch target survey structure
    survey = survey_crud.get_survey_by_code(survey_answer.survey_code, session)
    if not survey:
        raise HTTPException(
            status_code=404, detail="No survey found with this code"
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
        raise HTTPException(status_code=400, detail="Invalid answer")
    try:
        for q1, q2 in zip(survey_answer.questions, questions):
            q1.validate_structure_against(q2)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # save answer
    answer = Answer(
        survey_id=survey.id, answer=survey_answer.model_dump_json()
    )
    answer_crud.save_answer(answer, session)

    return {"message": "Answer saved successfully"}
