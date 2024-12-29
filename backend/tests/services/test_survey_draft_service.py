import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime

from src.services.survey_draft_service import (
    get_survey_drafts,
    get_survey_draft,
    delete_survey_drafts,
    create_survey_draft,
    count_survey_drafts,
)
from src.services.utils.exceptions import (
    InvalidSurveyStructureException,
    LimitExceededException,
)


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch("src.services.survey_draft_service.survey_draft_repository.get_not_deleted_survey_drafts_for_user")
def test_get_survey_drafts(
    mock_get_not_deleted_survey_drafts_for_user, mock_get_user_by_email, session
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_not_deleted_survey_drafts_for_user.return_value = [
        MagicMock(id=1, title="Survey 1", creation_date=datetime(2023, 1, 1)),
        MagicMock(id=2, title="Survey 2", creation_date=datetime(2023, 1, 2)),
    ]

    # when
    survey_drafts = get_survey_drafts(0, "test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_not_deleted_survey_drafts_for_user.assert_called_once_with(
        1, 0, 10, session
    )
    assert len(survey_drafts) == 2
    assert survey_drafts[0].id == 1
    assert survey_drafts[0].title == "Survey 1"
    assert survey_drafts[0].creation_date == datetime(2023, 1, 1)
    assert survey_drafts[1].id == 2
    assert survey_drafts[1].title == "Survey 2"
    assert survey_drafts[1].creation_date == datetime(2023, 1, 2)


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch("src.services.survey_draft_service.helpers.get_not_deleted_survey_draft_by_id")
@patch("src.services.survey_draft_service.helpers.check_if_user_has_access")
def test_get_survey_draft(
    mock_check_if_user_has_access,
    mock_get_not_deleted_survey_draft_by_id,
    mock_get_user_by_email,
    session,
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_not_deleted_survey_draft_by_id.return_value = MagicMock(creator_id=1)

    # when
    survey_draft = get_survey_draft(1, "test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_not_deleted_survey_draft_by_id.assert_called_once_with(1, session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    assert survey_draft is not None


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch("src.services.survey_draft_service.survey_draft_repository.delete_survey_drafts")
def test_delete_survey_drafts(
    mock_delete_survey_drafts, mock_get_user_by_email, session
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_delete_survey_drafts.return_value = [1]

    # when
    delete_survey_drafts("test@example.com", [1], session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_delete_survey_drafts.assert_called_once_with(1, [1], session)


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch("src.services.survey_draft_service.survey_draft_repository.create_survey_draft")
@patch(
    "src.services.survey_draft_service.survey_draft_repository.get_count_of_not_deleted_survey_drafts_for_user"
)
def test_create_survey_draft(
    mock_get_count_of_not_deleted_survey_drafts_for_user,
    mock_create_survey_draft,
    mock_get_user_by_email,
    session,
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_not_deleted_survey_drafts_for_user.return_value = 0
    mock_create_survey_draft.return_value = MagicMock(id=1)
    survey_draft_create = MagicMock(
        user_email="test@example.com", title="Test Survey", survey_structure=MagicMock()
    )

    # when
    survey_draft_id = create_survey_draft(survey_draft_create, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_count_of_not_deleted_survey_drafts_for_user.assert_called_once_with(
        1, session
    )
    mock_create_survey_draft.assert_called_once()
    assert survey_draft_id == 1


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch(
    "src.services.survey_draft_service.survey_draft_repository.get_count_of_not_deleted_survey_drafts_for_user"
)
def test_create_survey_draft_limit_exceeded(
    mock_get_count_of_not_deleted_survey_drafts_for_user, mock_get_user_by_email, session
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_not_deleted_survey_drafts_for_user.return_value = 50
    survey_draft_create = MagicMock(
        user_email="test@example.com", title="Test Survey", survey_structure=MagicMock()
    )

    # when & then
    with pytest.raises(LimitExceededException):
        create_survey_draft(survey_draft_create, session)


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch(
    "src.services.survey_draft_service.survey_draft_repository.get_count_of_not_deleted_survey_drafts_for_user"
)
def test_create_survey_draft_invalid_structure(
    mock_get_count_of_not_deleted_survey_drafts_for_user, mock_get_user_by_email, session
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_not_deleted_survey_drafts_for_user.return_value = 0
    survey_draft_create = MagicMock(
        user_email="test@example.com", title="Test Survey", survey_structure=MagicMock()
    )
    survey_draft_create.survey_structure.validate.side_effect = ValueError(
        "Invalid structure"
    )

    # when & then
    with pytest.raises(InvalidSurveyStructureException):
        create_survey_draft(survey_draft_create, session)


@patch("src.services.survey_draft_service.helpers.get_user_by_email")
@patch(
    "src.services.survey_draft_service.survey_draft_repository.get_count_of_not_deleted_survey_drafts_for_user"
)
def test_count_survey_drafts(
    mock_get_count_of_not_deleted_survey_drafts_for_user, mock_get_user_by_email, session
):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_not_deleted_survey_drafts_for_user.return_value = 5

    # when
    count = count_survey_drafts("test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_count_of_not_deleted_survey_drafts_for_user.assert_called_once_with(
        1, session
    )
    assert count == 5
