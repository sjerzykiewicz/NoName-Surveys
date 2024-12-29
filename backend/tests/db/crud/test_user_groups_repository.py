import src.db.crud.user as user_repository
import src.db.crud.user_groups as user_groups_repository


def test_get_count_of_user_groups_of_user(session):
    # given
    user_id = 1
    user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    count = user_groups_repository.get_count_of_user_groups_of_user(user_id, session)

    # then
    assert count == 1


def test_get_all_user_groups_of_user(session):
    # given
    user_id = 1
    user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    groups = user_groups_repository.get_all_user_groups_of_user(user_id, session)

    # then
    assert len(groups) == 1


def test_get_user_groups(session):
    # given
    user_id = 1
    user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    groups = user_groups_repository.get_user_groups(user_id, 0, 10, session)

    # then
    assert len(groups) == 1


def test_find_by_name(session):
    # given
    user_id = 1
    user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    group = user_groups_repository.find_by_name(user_id, "Group 1", session)

    # then
    assert group is not None


def test_update_user_group_name(session):
    # given
    user_id = 1
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    updated_group = user_groups_repository.update_user_group_name(
        group.id, "New Group Name", session
    )

    # then
    assert updated_group.name == "New Group Name"


def test_create_user_group(session):
    # given
    user_id = 1

    # when
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)

    # then
    assert group.name == "Group 1"


def test_add_users_to_group(session):
    # given
    user_id = 1
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    members = user_groups_repository.add_users_to_group(group.id, [user_id], session)

    # then
    assert len(members) == 1


def test_remove_users_from_group(session):
    # given
    user_id = 1
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)
    user_groups_repository.add_users_to_group(group.id, [user_id], session)

    # when
    members = user_groups_repository.remove_users_from_group(group.id, [user_id], session)

    # then
    assert len(members) == 1
    assert members[0].is_deleted


def test_delete_user_groups(session):
    # given
    user_id = 1
    user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    groups = user_groups_repository.delete_user_groups(user_id, ["Group 1"], session)

    # then
    assert len(groups) == 1
    assert groups[0].is_deleted


def test_get_user_group_members_count(session):
    # given
    user_id = 1
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)
    user_groups_repository.add_users_to_group(group.id, [user_id], session)

    # when
    count = user_groups_repository.get_user_group_members_count(group.id, session)

    # then
    assert count == 1


def test_get_user_group_members(session):
    # given
    user_id = 1
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)
    user_groups_repository.add_users_to_group(group.id, [user_id], session)

    # when
    members = user_groups_repository.get_user_group_members(group.id, session)

    # then
    assert len(members) == 1


def test_get_all_users_in_user_group(session):
    # given
    user = user_repository.create("test@example.com", session)
    group = user_groups_repository.create_user_group(user.id, "Group 1", session)
    user_groups_repository.add_users_to_group(group.id, [user.id], session)

    # when
    users = user_groups_repository.get_all_users_in_user_group(group.id, session)

    # then
    assert len(users) == 1
    assert users[0].email == "test@example.com"


def test_get_user_group_members_paginated(session):
    # given
    user = user_repository.create("test@example.com", session)
    group = user_groups_repository.create_user_group(user.id, "Group 1", session)
    user_groups_repository.add_users_to_group(group.id, [user.id], session)

    # when
    users = user_groups_repository.get_user_group_members_paginated(
        group.id, 0, 10, session
    )

    # then
    assert len(users) == 1


def test_get_all_users_who_are_not_members_of_user_group(session):
    # given
    user_id = 1
    group = user_groups_repository.create_user_group(user_id, "Group 1", session)

    # when
    users = user_groups_repository.get_all_users_who_are_not_members(
        group.id, session
    )

    # then
    assert len(users) == 0
