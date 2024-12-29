from unittest.mock import MagicMock, patch

from src.services.user_group_service import (
    get_user_groups_count,
    get_user_groups,
    get_user_groups_with_members_having_public_keys,
    get_user_group_members_count,
    get_users_who_are_not_members,
    get_whole_user_group,
    get_user_group,
    create_user_group,
    rename_user_group,
    delete_user_groups,
    add_users_to_group,
    remove_users_from_group,
)


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_count_of_user_groups_of_user")
def test_get_user_groups_count(mock_get_count_of_user_groups_of_user, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_user_groups_of_user.return_value = 5

    # when
    count = get_user_groups_count("test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_count_of_user_groups_of_user.assert_called_once_with(1, session)
    assert count == 5


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_user_groups")
@patch("src.services.user_group_service.user_repository.all_have_public_keys")
def test_get_user_groups(mock_all_have_public_keys, mock_get_user_groups, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_groups.return_value = [
        MagicMock(id=1),
        MagicMock(id=2)
    ]
    mock_get_user_groups.return_value[0].name = "Group 1"
    mock_get_user_groups.return_value[1].name = "Group 2"
    mock_all_have_public_keys.side_effect = [True, False]

    # when
    user_groups = get_user_groups(0, "test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_groups.assert_called_once_with(1, 0, 10, session)
    assert len(user_groups) == 2
    assert user_groups[0].user_group_name == "Group 1"
    assert user_groups[0].all_members_have_public_keys is True
    assert user_groups[1].user_group_name == "Group 2"
    assert user_groups[1].all_members_have_public_keys is False


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_all_user_groups_of_user")
@patch("src.services.user_group_service.user_repository.all_have_public_keys")
def test_get_user_groups_with_members_having_public_keys(mock_all_have_public_keys, mock_get_all_user_groups_of_user, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_all_user_groups_of_user.return_value = [
        MagicMock(id=1),
        MagicMock(id=2)
    ]
    mock_get_all_user_groups_of_user.return_value[0].name = "Group 1"
    mock_get_all_user_groups_of_user.return_value[1].name = "Group 2"
    mock_all_have_public_keys.side_effect = [True, False]

    # when
    user_groups = get_user_groups_with_members_having_public_keys("test@example.com", session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_all_user_groups_of_user.assert_called_once_with(1, session)
    assert len(user_groups) == 1
    assert user_groups[0] == "Group 1"


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_user_group_members_count")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_get_user_group_members_count(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_get_user_group_members_count, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_group_by_name.return_value = MagicMock(id=1, creator_id=1)
    mock_check_if_user_has_access.return_value = True
    mock_get_user_group_members_count.return_value = 10
    user_group_request = MagicMock(user_email="test@example.com")
    user_group_request.name = "Group 1"

    # when
    count = get_user_group_members_count(user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_get_user_group_members_count.assert_called_once_with(1, session)
    assert count == 10


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_all_users_who_are_not_members_of_user_group")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_get_users_who_are_not_members(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_get_all_users_who_are_not_members_of_user_group, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_group_by_name.return_value = MagicMock(id=1, creator_id=1)
    mock_check_if_user_has_access.return_value = True
    mock_get_all_users_who_are_not_members_of_user_group.return_value = [
        MagicMock(email="user1@example.com"),
        MagicMock(email="user2@example.com")
    ]
    mock_get_all_users_who_are_not_members_of_user_group.return_value[0].email ="user1@example.com"
    mock_get_all_users_who_are_not_members_of_user_group.return_value[1].email ="user2@example.com"
    user_group_request = MagicMock(user_email="test@example.com", name="Group 1")
    user_group_request.user_email = "test@example.com"
    user_group_request.name = "Group 1"

    # when
    users = get_users_who_are_not_members(user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_get_all_users_who_are_not_members_of_user_group.assert_called_once_with(1, session)
    assert len(users) == 2
    assert users[0] == "user1@example.com"
    assert users[1] == "user2@example.com"


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_all_users_in_user_group")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_get_whole_user_group(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_get_all_users_in_user_group, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_group_by_name.return_value = MagicMock(id=1, creator_id=1)
    mock_check_if_user_has_access.return_value = True
    mock_get_all_users_in_user_group.return_value = [
        MagicMock(email="user1@example.com"),
        MagicMock(email="user2@example.com")
    ]
    mock_get_all_users_in_user_group.return_value[0].public_key = "key1"
    mock_get_all_users_in_user_group.return_value[1].public_key = ""
    user_group_request = MagicMock(user_email="test@example.com")
    user_group_request.name = "Group 1"

    # when
    users = get_whole_user_group(user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_get_all_users_in_user_group.assert_called_once_with(1, session)
    assert len(users) == 2
    assert users[0].email == "user1@example.com"
    assert users[0].has_public_key is True
    assert users[1].email == "user2@example.com"
    assert users[1].has_public_key is False


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.get_user_group_members_paginated")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_get_user_group(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_get_user_group_members_paginated, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_group_by_name.return_value = MagicMock(id=1, creator_id=1)
    mock_check_if_user_has_access.return_value = True
    mock_get_user_group_members_paginated.return_value = [
        MagicMock(email="user1@example.com"),
        MagicMock(email="user2@example.com")
    ]
    mock_get_user_group_members_paginated.return_value[0].public_key = "key1"
    mock_get_user_group_members_paginated.return_value[1].public_key = ""
    user_group_request = MagicMock(user_email="test@example.com")
    user_group_request.name = "Group 1"

    # when
    users = get_user_group(0, user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_get_user_group_members_paginated.assert_called_once_with(1, 0, 10, session)
    assert len(users) == 2
    assert users[0].email == "user1@example.com"
    assert users[0].has_public_key is True
    assert users[1].email == "user2@example.com"
    assert users[1].has_public_key is False


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.create_user_group")
@patch("src.services.user_group_service.user_groups_repository.get_count_of_user_groups_of_user")
@patch("src.services.user_group_service.user_repository.all_exist")
@patch("src.services.user_group_service.user_groups_repository.find_by_name")
@patch("src.services.user_group_service.user_repository.find_by_emails")
@patch("src.services.user_group_service.user_groups_repository.add_users_to_group")
def test_create_user_group(mock_add_users_to_group, mock_find_by_emails, mock_find_by_name, mock_all_exist, mock_get_count_of_user_groups_of_user, mock_create_user_group, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_count_of_user_groups_of_user.return_value = 0
    mock_all_exist.return_value = True
    mock_find_by_name.return_value = None
    mock_create_user_group.return_value = MagicMock(id=1)
    mock_find_by_emails.return_value = [MagicMock(id=2), MagicMock(id=3)]
    mock_add_users_to_group.return_value = [MagicMock(id=2), MagicMock(id=3)]
    user_group_create = MagicMock(user_email="test@example.com")
    user_group_create.user_group_name = "Group 1"
    user_group_create.user_group_members = ["user1@example.com", "user2@example.com"]

    # when
    create_user_group(user_group_create, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_count_of_user_groups_of_user.assert_called_once_with(1, session)
    mock_all_exist.assert_called_once_with(["user1@example.com", "user2@example.com"], session)
    mock_find_by_name.assert_called_once_with(1, "Group 1", session)
    mock_create_user_group.assert_called_once_with(1, "Group 1", session)
    mock_find_by_emails.assert_called_once_with(["user1@example.com", "user2@example.com"], session)
    mock_add_users_to_group.assert_called_once_with(1, [2, 3], session)


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.find_by_name")
@patch("src.services.user_group_service.user_groups_repository.update_user_group_name")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_rename_user_group(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_update_user_group_name, mock_find_by_name, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_find_by_name.side_effect = [None, MagicMock(id=2)]
    mock_get_user_group_by_name.return_value = MagicMock(id=2)
    mock_get_user_group_by_name.return_value.creator_id = 1
    mock_check_if_user_has_access.return_value = True
    user_group_rename = MagicMock(user_email="test@example.com")
    user_group_rename.name = "Group 1"
    user_group_rename.new_name = "Group 2"

    # when
    rename_user_group(user_group_rename, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_find_by_name.assert_any_call(1, "Group 2", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_update_user_group_name.assert_called_once_with(2, "Group 2", session)


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.delete_user_groups")
def test_delete_user_groups(mock_delete_user_groups, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_delete_user_groups.return_value = [MagicMock(name="Group 1"), MagicMock(name="Group 2")]
    user_group_request = MagicMock(user_email="test@example.com")
    user_group_request.names = ["Group 1", "Group 2"]

    # when
    delete_user_groups(user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_delete_user_groups.assert_called_once_with(1, ["Group 1", "Group 2"], session)


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.add_users_to_group")
@patch("src.services.user_group_service.user_repository.find_by_emails")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_add_users_to_group(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_find_by_emails, mock_add_users_to_group, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_group_by_name.return_value = MagicMock(id=1, creator_id=1)
    mock_check_if_user_has_access.return_value = True
    mock_find_by_emails.return_value = [MagicMock(id=2), MagicMock(id=3)]
    mock_add_users_to_group.return_value = [MagicMock(id=2), MagicMock(id=3)]
    user_group_request = MagicMock(user_email="test@example.com")
    user_group_request.name = "Group 1"
    user_group_request.users = ["user1@example.com", "user2@example.com"]

    # when
    add_users_to_group(user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_find_by_emails.assert_called_once_with(["user1@example.com", "user2@example.com"], session)
    mock_add_users_to_group.assert_called_once_with(1, [2, 3], session)


@patch("src.services.user_group_service.helpers.get_user_by_email")
@patch("src.services.user_group_service.user_groups_repository.remove_users_from_group")
@patch("src.services.user_group_service.user_repository.find_by_emails")
@patch("src.services.user_group_service.helpers.get_user_group_by_name")
@patch("src.services.user_group_service.helpers.check_if_user_has_access")
def test_remove_users_from_group(mock_check_if_user_has_access, mock_get_user_group_by_name, mock_find_by_emails, mock_remove_users_from_group, mock_get_user_by_email, session):
    # given
    mock_get_user_by_email.return_value = MagicMock(id=1)
    mock_get_user_group_by_name.return_value = MagicMock(id=1, creator_id=1)
    mock_check_if_user_has_access.return_value = True
    mock_find_by_emails.return_value = [MagicMock(id=2), MagicMock(id=3)]
    mock_remove_users_from_group.return_value = [MagicMock(id=2), MagicMock(id=3)]
    user_group_request = MagicMock(user_email="test@example.com")
    user_group_request.name = "Group 1"
    user_group_request.users = ["user1@example.com", "user2@example.com"]

    # when
    remove_users_from_group(user_group_request, session)

    # then
    mock_get_user_by_email.assert_called_once_with("test@example.com", session)
    mock_get_user_group_by_name.assert_called_once_with(1, "Group 1", session)
    mock_check_if_user_has_access.assert_called_once_with(1, 1)
    mock_find_by_emails.assert_called_once_with(["user1@example.com", "user2@example.com"], session)
    mock_remove_users_from_group.assert_called_once_with(1, [2, 3], session)
