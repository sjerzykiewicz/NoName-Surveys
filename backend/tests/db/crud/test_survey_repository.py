
import src.db.crud.survey as survey_repository
import src.db.crud.user as user_repository


def test_get_count_of_not_deleted_surveys_for_user(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    count = survey_repository.get_count_of_not_deleted_surveys_for_user(user.id, session)

    # then
    assert count == 1


def test_find_by_code(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    survey = survey_repository.find_by_code("survey1", session)

    # then
    assert survey is not None


def test_find_active_by_code(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.enable_or_disable_survey(survey.id, True, session)

    # when
    active_survey = survey_repository.find_active_by_code("survey1", session)

    # then
    assert active_survey is not None


def test_delete_surveys(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    surveys = survey_repository.delete_surveys(user.id, ["survey1"], session)

    # then
    assert len(surveys) == 1
    assert surveys[0].is_deleted


def test_get_all_surveys_user_has_ownership_over(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    surveys = survey_repository.get_all_surveys_user_has_ownership_over(user.id, session)

    # then
    assert len(surveys) == 1


def test_get_count_of_active_surveys_of_user(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.enable_or_disable_survey(survey.id, True, session)

    # when
    count = survey_repository.get_count_of_active_surveys_of_user(user.id, session)

    # then
    assert count == 1


def test_is_code_taken(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    is_taken = survey_repository.is_code_taken("survey1", session)

    # then
    assert is_taken


def test_create_survey(session):
    # given
    user = user_repository.create("test@example.com", session)

    # when
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # then
    assert survey.survey_code == "survey1"


def test_give_survey_access(session):
    # given
    user = user_repository.create("test@example.com", session)
    other_user = user_repository.create("test2@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    survey_repository.give_survey_access(survey.id, other_user.id, session)
    surveys = survey_repository.get_all_surveys_user_can_view(other_user.id, 0, 10, session)

    # then
    assert len(surveys) == 1


def test_take_away_survey_access(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.give_survey_access(survey.id, user.id, session)

    # when
    survey_repository.take_away_survey_access(user.id, survey.id, [user.id], session)
    surveys = survey_repository.get_all_surveys_user_can_view(user.id, 0, 10, session)

    # then
    assert len(surveys) == 1


def test_reject_access_to_surveys(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.give_survey_access(survey.id, user.id, session)

    # when
    survey_repository.reject_access_to_surveys(user.id, ["survey1"], session)
    surveys = survey_repository.get_all_surveys_user_can_view(user.id, 0, 10, session)

    # then
    assert len(surveys) == 1


def test_get_all_surveys_user_can_view(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.give_survey_access(survey.id, user.id, session)

    # when
    surveys = survey_repository.get_all_surveys_user_can_view(user.id, 0, 10, session)

    # then
    assert len(surveys) == 1


def test_get_all_users_with_access_to_survey_count(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.give_survey_access(survey.id, user.id, session)

    # when
    count = survey_repository.get_all_users_with_access_to_survey_count(survey.id, session)

    # then
    assert count == 1


def test_get_all_users_with_no_access_to_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    users = survey_repository.get_all_users_with_no_access_to_survey(survey.id, session)

    # then
    assert len(users) == 1
    assert users[0] == "test@example.com"


def test_get_all_users_with_access_to_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.give_survey_access(survey.id, user.id, session)

    # when
    accesses = survey_repository.get_all_users_with_access_to_survey(survey.id, 0, 10, session)

    # then
    assert len(accesses) == 1


def test_user_has_access_to_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    survey_repository.give_survey_access(survey.id, user.id, session)

    # when
    has_access = survey_repository.user_has_access_to_survey(user.id, survey.id, session)

    # then
    assert has_access


def test_enable_or_disable_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    survey_repository.enable_or_disable_survey(survey.id, True, session)

    # then
    assert survey.is_enabled
