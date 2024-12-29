
import src.db.crud.answer as answer_repository
import src.db.crud.survey as survey_repository
import src.db.crud.user as user_repository


def test_find_by_survey_id(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    answer_repository.save(survey.id, "answer1", "y0_1", session)

    # when
    answers = answer_repository.find_by_survey_id(survey.id, session)

    # then
    assert len(answers) == 1
    assert answers[0].answer == "answer1"


def test_is_signature_present(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    answer_repository.save(survey.id, "answer1", "y0_1", session)

    # when
    is_present = answer_repository.is_signature_present(survey.id, "y0_1", session)

    # then
    assert is_present


def test_save(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when & then
    assert answer_repository.save(survey.id, "answer1", "y0_1", session) is None
