import pytest
from unittest.mock import MagicMock, patch

from src.services.user_service import (
    create_user,
    update_user_public_key,
    get_all_users,
    get_all_users_with_public_keys,
    get_user_by_email,
    get_users_by_emails,
    get_users_with_public_keys_by_emails,
    get_user_by_email_helper,
)
from src.services.utils.exceptions import DuplicateUserException


@patch("src.services.user_service.user_repository.create")
@patch("src.services.user_service.get_user_by_email")
def test_create_user_happy_path(mock_get_user_by_email, mock_create, session):
    # given
    mock_get_user_by_email.return_value = None
    mock_create.return_value = MagicMock()

    # when
    user = create_user("test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_create.assert_called_once_with("test@example.com", session)
    assert user is not None


@patch("src.services.user_service.get_user_by_email")
def test_create_user_duplicate(mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock()

    # when
    with pytest.raises(DuplicateUserException):
        create_user("test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)


@patch("src.services.user_service.fingerprint_verification.verify")
@patch("src.services.user_service.user_repository.update_public_key")
@patch("src.services.user_service.helpers.get_user_by_email")
def test_update_user_public_key(mock_get_user_by_email, mock_update_public_key,
                                mock_verify, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_verify.return_value = True
    mock_update_public_key.return_value = MagicMock()

    # when
    user = update_user_public_key("test@example.com", "new_public_key", "12345", session)

    # then
    mock_update_public_key.assert_called_once_with(1, "new_public_key", session)
    assert user is not None


@patch("src.services.user_service.user_repository.find_all")
def test_get_all_users(mock_find_all, session):
    # given
    mock_find_all.return_value = [MagicMock(), MagicMock()]

    # when
    users = get_all_users(session)

    # then
    mock_find_all.assert_called_once_with(session)
    assert len(users) == 2


@patch("src.services.user_service.user_repository.find_all_with_public_keys")
def test_get_all_users_with_public_keys(mock_find_all_with_public_keys, session):
    # given
    mock_find_all_with_public_keys.return_value = [MagicMock(), MagicMock()]

    # when
    users = get_all_users_with_public_keys(session)

    # then
    mock_find_all_with_public_keys.assert_called_once_with(session)
    assert len(users) == 2


@patch("src.services.user_service.user_repository.find_by_email")
def test_get_user_by_email(mock_find_by_email, session):
    # given
    mock_find_by_email.return_value = MagicMock()

    # when
    user = get_user_by_email("test@example.com", session)

    # then
    mock_find_by_email.assert_called_once_with("test@example.com", session)
    assert user is not None


@patch("src.services.user_service.user_repository.find_by_emails")
def test_get_users_by_emails(mock_find_by_emails, session):
    # given
    mock_find_by_emails.return_value = [MagicMock(), MagicMock()]

    # when
    users = get_users_by_emails(["test1@example.com", "test2@example.com"], session)

    # then
    mock_find_by_emails.assert_called_once_with(
        ["test1@example.com", "test2@example.com"], session
    )
    assert len(users) == 2


@patch("src.services.user_service.user_repository.find_with_public_keys_by_emails")
def test_get_users_with_public_keys_by_emails(mock_find_with_public_keys_by_emails,
                                              session):
    # given
    mock_find_with_public_keys_by_emails.return_value = [MagicMock(), MagicMock()]

    # when
    users = get_users_with_public_keys_by_emails(
        ["test1@example.com", "test2@example.com"], session
    )

    # then
    mock_find_with_public_keys_by_emails.assert_called_once_with(
        ["test1@example.com", "test2@example.com"], session
    )
    assert len(users) == 2


@patch("src.services.user_service.helpers.get_user_by_email")
def test_get_user_by_email_helper(mock_helpers_get_user_by_email, session):
    # given
    mock_helpers_get_user_by_email.return_value = MagicMock()

    # when
    user = get_user_by_email_helper("test@example.com", session)

    # then
    mock_helpers_get_user_by_email.assert_called_once_with("test@example.com", session)
    assert user is not None
