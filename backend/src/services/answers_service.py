from gmpy2 import mpz
from sqlmodel import Session

import src.db.crud.answer as answer_repository
import src.db.crud.ring_member as ring_member_repository
import src.db.crud.survey as survey_repository
import src.services.utils.helpers as helpers
from src.api.models.questions.question_base import Question
from src.api.models.surveys.answer import (
    SurveyAnswerBase,
    SurveyAnswersFetchInput,
    SurveyAnswersFetchOutput,
)
from src.api.models.surveys.survey import SurveyStructure
from src.cryptography.ring_signature import verify_lrs
from src.services.utils.exceptions import (
    DuplicateAnswerException,
    InvalidSignatureException,
    InvalidSurveyStructureException,
    UserAccessException,
)


def get_survey_answers_by_code(
    survey_fetch: SurveyAnswersFetchInput, session: Session
) -> list[SurveyAnswersFetchOutput]:
    user = helpers.get_user_by_email(survey_fetch.user_email, session)
    survey = helpers.get_survey_by_code(survey_fetch.survey_code, session)

    if not survey_repository.user_has_access_to_survey(user.id, survey.id, session):
        raise UserAccessException("User does not have access to this survey")

    survey_draft = helpers.get_survey_draft_by_id(survey.survey_structure_id, session)
    survey_title = survey_draft.title

    answers = answer_repository.find_by_survey_id(survey.id, session)
    answer_structures = [
        SurveyAnswerBase.model_validate_json(answer.answer) for answer in answers
    ]
    return [
        SurveyAnswersFetchOutput(
            title=survey_title,
            questions=answer.questions,
        )
        for answer in answer_structures
    ]


def save_survey_answer(survey_answer: SurveyAnswerBase, session: Session) -> dict:
    try:
        survey_answer.validate()
    except ValueError as e:
        raise InvalidSurveyStructureException(str(e))

    survey = helpers.get_active_survey_by_code(survey_answer.survey_code, session)

    if survey.uses_cryptographic_module:
        if not survey_answer.signature:
            raise InvalidSignatureException("Survey requires cryptographic signature")

        if answer_repository.is_signature_present(
            survey.id, survey_answer.signature[0], session
        ):
            raise DuplicateAnswerException("You have already answered this survey")

        question_answers = [
            question
            for question in survey_answer.questions
            if isinstance(question, Question)
        ]
        message = (
            "".join(
                question.question + question.get_answer()
                for question in question_answers
            )
            + survey_answer.survey_code
        )

        public_keys = [
            ring_member.public_key
            for ring_member in ring_member_repository.get_ring_members_for_survey(
                survey.id, session
            )
        ]

        if not verify_lrs(
            message,
            public_keys,
            [mpz(x) for x in survey_answer.signature],
        ):
            raise InvalidSignatureException("Invalid cryptographic signature")

    survey_draft = helpers.get_survey_draft_by_id(survey.survey_structure_id, session)

    survey_structure = SurveyStructure.model_validate_json(
        survey_draft.survey_structure
    )
    questions = survey_structure.questions
    # validate answer
    if len(survey_answer.questions) != len(questions):
        raise InvalidSurveyStructureException(
            "Invalid answer. Number of questions did not match."
        )
    try:
        for q1, q2 in zip(survey_answer.questions, questions):
            q1.validate_structure_against(q2)
    except ValueError as e:
        raise InvalidSurveyStructureException(str(e))

    y0 = survey_answer.signature[0] if survey_answer.signature else ""
    answer_repository.save(survey.id, survey_answer.model_dump_json(), y0, session)

    return {"message": "Answer saved successfully"}
