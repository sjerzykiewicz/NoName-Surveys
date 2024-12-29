import src.db.crud.user as user_repository


def test_create_user(session):
    # given & when
    user = user_repository.create("test@example.com", session)

    # then
    assert user.email == "test@example.com"
    assert user.id is not None

def test_find_by_email(session):
    # given
    user_repository.create("test@example.com", session)

    # when
    user = user_repository.find_by_email("test@example.com", session)

    # then
    assert user is not None
    assert user.email == "test@example.com"

def test_find_all(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)

    # when
    users = user_repository.find_all(session)

    # then
    assert len(users) == 2

def test_find_all_with_public_keys(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)
    user_repository.update_public_key(1, "public_key_1", session)

    # when
    users = user_repository.find_all_with_public_keys(session)

    # then
    assert len(users) == 1

def test_find_by_id(session):
    # given
    user = user_repository.create("test@example.com", session)

    # when
    found_user = user_repository.find_by_id(user.id, session)

    # then
    assert found_user is not None
    assert found_user.id == user.id

def test_find_by_emails(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)

    # when
    users = user_repository.find_by_emails(
        ["test1@example.com", "test2@example.com"], session
    )

    # then
    assert len(users) == 2

def test_find_with_public_keys_by_emails(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)
    user_repository.update_public_key(1, "public_key_1", session)

    # when
    users = user_repository.find_with_public_keys_by_emails(
        ["test1@example.com", "test2@example.com"], session
    )

    # then
    assert len(users) == 1

def test_all_exist(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)

    # when & then
    assert user_repository.all_exist(["test1@example.com", "test2@example.com"], session)
    assert not user_repository.all_exist(
        ["test1@example.com", "test3@example.com"], session
    )

def test_all_exist_and_have_public_keys(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)
    user_repository.update_public_key(1, "public_key_1", session)
    user_repository.update_public_key(2, "public_key_2", session)

    # when & then
    assert user_repository.all_exist_and_have_public_keys(
        ["test1@example.com", "test2@example.com"], session
    )
    assert not user_repository.all_exist_and_have_public_keys(
        ["test1@example.com", "test3@example.com"], session
    )

def test_all_have_public_keys(session):
    # given
    user_repository.create("test1@example.com", session)
    user_repository.create("test2@example.com", session)
    user_repository.update_public_key(1, "public_key_1", session)
    user_repository.update_public_key(2, "public_key_2", session)

    # when & then
    assert user_repository.all_have_public_keys(
        [1, 2], session
    )
    assert not user_repository.all_have_public_keys(
        [1, 3], session
    )

def test_update_public_key(session):
    # given
    user = user_repository.create("test@example.com", session)

    # when
    updated_user = user_repository.update_public_key(user.id, "new_public_key", session)

    # then
    assert updated_user.public_key == "new_public_key"
