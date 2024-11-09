from fastapi.testclient import TestClient

from test_users import create_user, create_users, create_users_with_public_keys

TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_3 = "user3@st.amu.edu.pl"
TEST_USER_GROUP_NAME_1 = "Test Group"
TEST_USER_GROUP_NAME_2 = "Test Group 2"


def create_user_group(client: TestClient, email: str, group_name: str, members: list[str]):
    return client.post(
        "/user-groups/create",
        json={
            "user_email": email,
            "user_group_name": group_name,
            "user_group_members": members,
        },
    )


def test_create_user_group_happy_path(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)

    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "user group created successfully"


def test_create_user_group_user_not_registered(client: TestClient):
    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 400


def test_create_user_group_with_unregistered_members(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 400


def test_create_user_group_when_group_already_exists(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 400


def test_get_user_groups_count(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/count",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 1


def test_get_user_groups(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/all/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["user_group_name"] == TEST_USER_GROUP_NAME_1


def test_get_user_groups_with_members_having_public_keys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_users_with_public_keys(client, [TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_2, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/all-with-public-keys",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0] == TEST_USER_GROUP_NAME_2


def test_get_user_group_members_count(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/group-members-count",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 1


def test_get_user_group(client: TestClient):
    # given
    users = [f"user{i}@st.amu.edu.pl" for i in range(20)]
    create_users(client, users)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, users)

    # when
    response = client.post(
        "/user-groups/fetch/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10
    assert [user["email"] for user in data] == users[:10]
    assert all(user["has_public_key"] == False for user in data)


def test_get_user_group_with_public_keys(client: TestClient):
    # given
    users = [f"user{i}@st.amu.edu.pl" for i in range(20)]
    create_users_with_public_keys(client, users)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, users)

    # when
    response = client.post(
        "/user-groups/fetch/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10
    assert [user["email"] for user in data] == users[:10]
    assert all(user["has_public_key"] == True for user in data)


def test_rename_user_group(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])
    new_group_name = "New Group Name"

    # when
    response = client.post(
        "/user-groups/rename",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME_1, "new_name": new_group_name},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "user group updated successfully"


def test_rename_user_group_group_not_found(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    new_group_name = "New Group Name"

    # when
    response = client.post(
        "/user-groups/rename",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME_1, "new_name": new_group_name},
    )

    # then
    assert response.status_code == 400


def test_rename_user_group_new_group_name_already_exists(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_2, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/rename",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME_1, "new_name": TEST_USER_GROUP_NAME_2},
    )

    # then
    assert response.status_code == 400


def test_delete_user_groups(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/delete",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "names": [TEST_USER_GROUP_NAME_1]},
    )

    # then
    assert response.status_code == 200


def test_delete_user_groups_some_not_found(client: TestClient):
    # given
    create_users(client, [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2])
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME_1, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user-groups/delete",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "names": [TEST_USER_GROUP_NAME_1, "Nonexistent Group"]},
    )

    # then
    assert response.status_code == 400
