from unittest.mock import MagicMock, patch
from datetime import datetime


from src.services.survey_service import (
    count_surveys,
    get_surveys_for_user,
    get_survey_by_code,
    count_survey_respondents,
    get_respondents_by_code,
    delete_surveys,
    create_survey,
    give_access_to_surveys,
    take_away_access_to_surveys,
    reject_access_to_surveys,
    get_count_of_users_with_access,
    get_all_users_without_access,
    check_access_to_surveys,
    enable_or_disable_survey,
)


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.get_count_of_not_deleted_surveys_for_user")
def test_count_surveys(mock_get_count_of_not_deleted_surveys_for_user,
                       mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_not_deleted_surveys_for_user.return_value = 5

    # when
    count = count_surveys(MagicMock(user_email="test@example.com"), session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_count_of_not_deleted_surveys_for_user.assert_called_once_with(1, session)
    assert count == 5


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.get_all_surveys_user_can_view")
@patch("src.services.survey_service.survey_draft_repository.find_by_id")
@patch("src.services.survey_service.ring_member_repository.get_ring_member_count_for_survey")
def test_get_surveys_for_user(mock_get_ring_member_count_for_survey, mock_find_by_id,
                              mock_get_all_surveys_user_can_view, mock_get_user_by_email,
                              session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_all_surveys_user_can_view.return_value = [
        (MagicMock(id=1), True),
        (MagicMock(id=2), False)
    ]
    mock_get_all_surveys_user_can_view.return_value[0][0].survey_code = "code1"
    mock_get_all_surveys_user_can_view.return_value[1][0].survey_code = "code2"
    mock_get_all_surveys_user_can_view.return_value[0][0].creation_date = (
        datetime(2023, 1, 1)
    )
    mock_get_all_surveys_user_can_view.return_value[1][0].creation_date = (
        datetime(2023, 1, 2)
    )
    mock_get_all_surveys_user_can_view.return_value[0][0].uses_cryptographic_module = True
    mock_get_all_surveys_user_can_view.return_value[1][0].uses_cryptographic_module = (
        False
    )
    mock_get_all_surveys_user_can_view.return_value[0][0].is_enabled = True
    mock_get_all_surveys_user_can_view.return_value[1][0].is_enabled = False
    mock_find_by_id.side_effect = [
        MagicMock(title="Survey 1"),
        MagicMock(title="Survey 2")
    ]
    mock_get_ring_member_count_for_survey.side_effect = [10, 0]

    # when
    surveys = get_surveys_for_user(0, MagicMock(user_email="test@example.com"), session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_all_surveys_user_can_view.assert_called_once_with(1, 0, 10, session)
    assert len(surveys) == 2
    assert surveys[0].title == "Survey 1"
    assert surveys[0].survey_code == "code1"
    assert surveys[0].creation_date == datetime(2023, 1, 1)
    assert surveys[0].uses_cryptographic_module is True
    assert surveys[0].is_owned_by_user is True
    assert surveys[0].group_size == 10
    assert surveys[0].is_enabled is True
    assert surveys[1].title == "Survey 2"
    assert surveys[1].survey_code == "code2"
    assert surveys[1].creation_date == datetime(2023, 1, 2)
    assert surveys[1].uses_cryptographic_module is False
    assert surveys[1].is_owned_by_user is False
    assert surveys[1].group_size == 0
    assert surveys[1].is_enabled is False


@patch("src.services.survey_service.helpers.get_survey_by_code")
@patch("src.services.survey_service.helpers.get_survey_draft_by_id")
@patch("src.services.survey_service.ring_member_repository.get_public_keys_for_survey")
def test_get_survey_by_code(mock_get_public_keys_for_survey, mock_get_survey_draft_by_id,
                            mock_get_survey_by_code, session):
    # given
    mock_get_survey_by_code.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value.survey_structure_id = 1
    mock_get_survey_by_code.return_value.survey_code = "code1"
    mock_get_survey_by_code.return_value.uses_cryptographic_module = True
    mock_get_survey_draft_by_id.return_value = MagicMock(title="Survey 1")
    mock_get_survey_draft_by_id.return_value.survey_structure = (
        '{"questions": [{"question_type": "binary", "required": true, '
        '"question": "Is this a test?", '
        '"choices": ["Yes", "No"]}]}'
    )
    mock_get_public_keys_for_survey.return_value = ["key1", "key2"]

    # when
    survey = get_survey_by_code(MagicMock(survey_code="code1"), session)

    # then
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_get_survey_draft_by_id.assert_called_once_with(1, session)
    mock_get_public_keys_for_survey.assert_called_once_with(1, session)
    assert survey.title == "Survey 1"
    assert survey.survey_code == "code1"
    assert survey.uses_cryptographic_module is True
    assert survey.public_keys == ["key1", "key2"]


@patch("src.services.survey_service.helpers.get_survey_by_code")
@patch("src.services.survey_service.ring_member_repository.get_ring_member_count_for_survey")
def test_count_survey_respondents(mock_get_ring_member_count_for_survey,
                                  mock_get_survey_by_code, session):
    # given
    mock_get_survey_by_code.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value.survey_structure_id = 1
    mock_get_survey_by_code.return_value.uses_cryptographic_module = True
    mock_get_ring_member_count_for_survey.return_value = 10

    # when
    count = count_survey_respondents(MagicMock(survey_code="code1"), session)

    # then
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_get_ring_member_count_for_survey.assert_called_once_with(1, session)
    assert count == 10


@patch("src.services.survey_service.helpers.get_survey_by_code")
@patch("src.services.survey_service.ring_member_repository.get_ring_members_for_survey_paginated")
def test_get_respondents_by_code(mock_get_ring_members_for_survey_paginated,
                                 mock_get_survey_by_code, session):
    # given
    mock_get_survey_by_code.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value.survey_structure_id = 1
    mock_get_survey_by_code.return_value.uses_cryptographic_module = True
    mock_get_ring_members_for_survey_paginated.return_value = [
        "user1@example.com", "user2@example.com"
    ]

    # when
    respondents = get_respondents_by_code(0, MagicMock(survey_code="code1"), session)

    # then
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_get_ring_members_for_survey_paginated.assert_called_once_with(1, 0, 10, session)
    assert len(respondents) == 2
    assert respondents[0] == "user1@example.com"
    assert respondents[1] == "user2@example.com"


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.delete_surveys")
def test_delete_surveys(mock_delete_surveys, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_delete_surveys.return_value = [MagicMock(survey_code="code1")]

    # when
    delete_surveys(MagicMock(
        user_email="test@example.com", survey_codes=["code1"]
        ), session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_delete_surveys.assert_called_once_with(1, ["code1"], session)


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.get_count_of_active_surveys_of_user")
@patch("src.services.survey_service.survey_draft_repository.create_survey_draft")
@patch("src.services.survey_service.helpers.generate_survey_code")
@patch("src.services.survey_service.survey_repository.create_survey")
@patch("src.services.survey_service.survey_repository.give_survey_access")
def test_create_survey(mock_give_survey_access, mock_create_survey,
                       mock_generate_survey_code, mock_create_survey_draft,
                       mock_get_count_of_active_surveys_of_user,
                       mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_active_surveys_of_user.return_value = 0
    mock_create_survey_draft.return_value = MagicMock(id=1)
    mock_generate_survey_code.return_value = "code1"
    mock_create_survey.return_value = MagicMock(id=1)
    mock_create_survey.return_value.survey_code = "code1"
    mock_give_survey_access.return_value = None
    survey_create = MagicMock(user_email="test@example.com", title="Test Survey",
                              survey_structure=MagicMock(),
                              uses_cryptographic_module=False)

    # when
    survey = create_survey(survey_create, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_count_of_active_surveys_of_user.assert_called_once_with(1, session)
    mock_create_survey_draft.assert_called_once()
    mock_generate_survey_code.assert_called_once()
    mock_create_survey.assert_called_once()
    mock_give_survey_access.assert_called_once_with(1, 1, session)
    assert survey.survey_code == "code1"


@patch("src.services.user_group_service.user_repository.all_exist")
@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.give_survey_access")
@patch("src.services.survey_service.helpers.get_survey_by_code")
def test_give_access_to_surveys(mock_get_survey_by_code, mock_give_survey_access,
                                mock_get_user_by_email, mock_all_exist, session):
    # given
    mock_get_user_by_email.side_effect = [MagicMock(id=1), MagicMock(id=2)]
    mock_get_survey_by_code.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value.creator_id = 1
    mock_give_survey_access.return_value = None
    mock_all_exist.return_value = True
    share_surveys_input = MagicMock(user_email="test@example.com", survey_code="code1",
                                    user_emails=["user2@example.com"])

    # when
    give_access_to_surveys(share_surveys_input, session)

    # then
    mock_get_user_by_email.assert_any_call("test@example.com", session)
    mock_get_user_by_email.assert_any_call("user2@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_give_survey_access.assert_called()


@patch("src.services.user_group_service.user_repository.find_by_emails")
@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.take_away_survey_access")
@patch("src.services.survey_service.helpers.get_survey_by_code")
def test_take_away_access_to_surveys(mock_get_survey_by_code,
                                     mock_take_away_survey_access,
                                     mock_get_user_by_email,
                                     mock_find_by_emails, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value = MagicMock(id=1, creator_id=1)
    mock_find_by_emails.return_value = [MagicMock(id=2)]
    mock_take_away_survey_access.return_value = [MagicMock()]
    take_away_access_input = MagicMock(user_email="test@example.com", survey_code="code1",
                                       user_emails=["user2@example.com"])

    # when
    take_away_access_to_surveys(take_away_access_input, session)

    # then
    mock_get_user_by_email.assert_any_call("test@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_take_away_survey_access.assert_called_once_with(1, 1, [2], session)
    mock_take_away_survey_access.assert_called()


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.reject_access_to_surveys")
def test_reject_access_to_surveys(mock_reject_access_to_surveys,
                                  mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_reject_access_to_surveys.return_value = [MagicMock(), MagicMock()]
    reject_access_input = MagicMock(user_email="test@example.com",
                                    survey_codes=["code1", "code2"]
                                    )

    # when
    reject_access_to_surveys(reject_access_input, session)

    # then
    mock_get_user_by_email.assert_called_with("test@example.com", session)
    mock_reject_access_to_surveys.assert_called_once_with(1, ["code1", "code2"], session)


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.get_all_users_with_access_to_survey_count")
@patch("src.services.survey_service.helpers.get_survey_by_code")
def test_get_count_of_users_with_access(mock_get_survey_by_code,
                                        mock_get_all_users_with_access_to_survey_count,
                                        mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value = MagicMock(id=1, creator_id=1)
    mock_get_all_users_with_access_to_survey_count.return_value = 5
    user_input = MagicMock(user_email="test@example.com", survey_code="code1")

    # when
    count = get_count_of_users_with_access(user_input, session)

    # then
    mock_get_user_by_email.assert_called_with("test@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_get_all_users_with_access_to_survey_count.assert_called_once_with(1, session)
    assert count == 5


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.get_all_users_with_no_access_to_survey")
@patch("src.services.survey_service.helpers.get_survey_by_code")
def test_get_all_users_without_access(mock_get_survey_by_code,
                                      mock_get_all_users_with_no_access_to_survey,
                                      mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value = MagicMock(id=1, creator_id=1)
    mock_get_all_users_with_no_access_to_survey.return_value = [
        "user1@example.com", "user2@example.com"
    ]
    user_input = MagicMock(user_email="test@example.com", survey_code="code1")

    # when
    users = get_all_users_without_access(user_input, session)

    # then
    mock_get_user_by_email.assert_called_with("test@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_get_all_users_with_no_access_to_survey.assert_called_once_with(1, session)
    assert len(users) == 2
    assert users[0] == "user1@example.com"
    assert users[1] == "user2@example.com"


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.get_all_users_with_access_to_survey")
@patch("src.services.survey_service.helpers.get_survey_by_code")
@patch("src.services.survey_service.user_repository.find_by_id")
def test_check_access_to_surveys(mock_find_by_id, mock_get_survey_by_code,
                                 mock_get_all_users_with_access_to_survey,
                                 mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value = MagicMock(id=1, creator_id=1)
    mock_get_all_users_with_access_to_survey.return_value = [
        MagicMock(user_id=2), MagicMock(user_id=3)
    ]
    mock_find_by_id.side_effect = [
        MagicMock(email="user1@example.com"),
        MagicMock(email="user2@example.com")
    ]
    check_survey_access_input = MagicMock(user_email="test@example.com",
                                          survey_code="code1")

    # when
    users = check_access_to_surveys(0, check_survey_access_input, session)

    # then
    mock_get_user_by_email.assert_called_with("test@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_get_all_users_with_access_to_survey.assert_called_once_with(1, 0, 10, session)
    mock_find_by_id.assert_called()
    assert len(users) == 2
    assert users[0] == "user1@example.com"
    assert users[1] == "user2@example.com"


@patch("src.services.survey_service.helpers.get_user_by_email")
@patch("src.services.survey_service.survey_repository.enable_or_disable_survey")
@patch("src.services.survey_service.helpers.get_survey_by_code")
def test_enable_or_disable_survey(mock_get_survey_by_code, mock_enable_or_disable_survey,
                                  mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_survey_by_code.return_value = MagicMock(id=1, creator_id=1)
    mock_enable_or_disable_survey.return_value = None
    user_input = MagicMock(user_email="test@example.com", survey_code="code1",
                           is_enabled=True)

    # when
    enable_or_disable_survey(user_input, session)

    # then
    mock_get_user_by_email.assert_called_with("test@example.com", session)
    mock_get_survey_by_code.assert_called_once_with("code1", session)
    mock_enable_or_disable_survey.assert_called_once_with(1, True, session)
