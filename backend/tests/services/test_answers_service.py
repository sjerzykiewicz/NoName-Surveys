from unittest.mock import MagicMock, patch
from src.services.answers_service import (
    get_survey_answers_by_code,
    save_survey_answer,
)
from src.api.models.surveys.answer import SurveyAnswersFetchInput, SurveyAnswerBase
from src.api.models.questions.binary_question import BinaryQuestion


@patch("src.services.answers_service.survey_repository.user_has_access_to_survey")
@patch("src.services.answers_service.helpers.get_user_by_email")
@patch("src.services.answers_service.helpers.get_survey_by_code")
@patch("src.services.answers_service.answer_repository.find_by_survey_id")
@patch("src.services.answers_service.helpers.get_survey_draft_by_id")
def test_get_survey_answers_by_code(
    mock_get_survey_draft_by_id,
    mock_find_by_survey_id,
    mock_get_survey_by_code,
    mock_get_user_by_email,
    mock_user_has_access_to_survey,
    session,
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value = MagicMock(id=1, survey_structure_id=1)
    mock_user_has_access_to_survey.return_value = True
    mock_get_survey_draft_by_id.return_value = MagicMock(title="Survey 1")
    mock_find_by_survey_id.return_value = [
        MagicMock(answer='{"survey_code": "123456", "questions": '
                  '[{"question_type": "binary", '
                  '"required": true, "answer": "Yes", "question": "Is this a test?", '
                  '"choices": ["Yes", "No"]}]}')
    ]
    survey_fetch = SurveyAnswersFetchInput(
        user_email="test@example.com", survey_code="123456"
    )

    # when
    answers = get_survey_answers_by_code(survey_fetch, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("123456", session)
    mock_find_by_survey_id.assert_called_once_with(1, session)
    mock_get_survey_draft_by_id.assert_called_once_with(1, session)
    assert len(answers) == 1
    assert answers[0].title == "Survey 1"
    assert answers[0].questions[0].question_type == "binary"
    assert answers[0].questions[0].question == "Is this a test?"
    assert answers[0].questions[0].answer == "Yes"


@patch("src.services.answers_service.helpers.get_active_survey_by_code")
@patch("src.services.answers_service.answer_repository.is_signature_present")
@patch("src.services.answers_service.answer_repository.save")
@patch("src.services.answers_service.ring_member_repository.get_ring_members_for_survey")
@patch("src.services.answers_service.verify_lrs")
@patch("src.services.answers_service.helpers.get_survey_draft_by_id")
def test_save_survey_answer(
    mock_get_survey_draft_by_id,
    mock_verify_lrs,
    mock_get_ring_members_for_survey,
    mock_save,
    mock_is_signature_present,
    mock_get_active_survey_by_code,
    session,
):
    # given
    mock_get_active_survey_by_code.return_value = MagicMock(
        id=1, uses_cryptographic_module=True, survey_structure_id=1
    )
    mock_is_signature_present.return_value = False
    mock_get_ring_members_for_survey.return_value = [MagicMock(public_key="key1")]
    mock_verify_lrs.return_value = True
    mock_get_survey_draft_by_id.return_value = MagicMock(
        survey_structure='{"questions": [{"question_type": "binary", "required": true, '
                         '"question": "Is this a test?", "choices": ["Yes", "No"]}]}'
    )
    survey_answer = SurveyAnswerBase(
        survey_code="123456",
        questions=[BinaryQuestion(
            question="Is this a test?", required=True, choices=["Yes", "No"], answer="Yes"
            )
        ],
        signature=["1234"],
    )

    # when
    result = save_survey_answer(survey_answer, session)

    # then
    mock_get_active_survey_by_code.assert_called_once_with("123456", session)
    mock_is_signature_present.assert_called_once_with(1, "1234", session)
    mock_get_ring_members_for_survey.assert_called_once_with(1, session)
    mock_verify_lrs.assert_called_once()
    mock_get_survey_draft_by_id.assert_called_once_with(1, session)
    mock_save.assert_called_once()
    assert result == {"message": "Answer saved successfully"}
